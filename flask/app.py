from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import base64

app = Flask(__name__)
DATABASE = 'redesocial'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_db() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL,
                foto_base64 TEXT
            )
        ''')

@app.route('/')
def index():
    conn = get_db()
    usuarios = conn.execute('SELECT * FROM usuarios').fetchall()
    return render_template('index.html', usuarios=usuarios)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        foto = request.files['foto']

        if foto:
            foto_bytes = foto.read()
            foto_base64 = base64.b64encode(foto_bytes).decode('utf-8')
        else:
            foto_base64 = None

        with get_db() as conn:
            conn.execute(
                'INSERT INTO usuarios (nome, email, foto_base64) VALUES (?, ?, ?)',
                (nome, email, foto_base64)
            )
        return redirect(url_for('index'))

    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    conn = get_db()
    usuario = conn.execute('SELECT * FROM usuarios WHERE id = ?', (id,)).fetchone()

    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        foto = request.files['foto']

        if foto:
            foto_bytes = foto.read()
            foto_base64 = base64.b64encode(foto_bytes).decode('utf-8')
        else:
            foto_base64 = usuario['foto_base64']

        conn.execute(
            'UPDATE usuarios SET nome = ?, email = ?, foto_base64 = ? WHERE id = ?',
            (nome, email, foto_base64, id)
        )
        return redirect(url_for('index'))

    return render_template('edit.html', usuario=usuario)

@app.route('/delete/<int:id>')
def delete(id):
    with get_db() as conn:
        conn.execute('DELETE FROM usuarios WHERE id = ?', (id,))
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
