from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3
from datetime import datetime
import os

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('tarefas.db')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT,
            status TEXT DEFAULT 'pendente',
            prioridade TEXT DEFAULT 'media',
            data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            data_conclusao TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def dashboard():
    conn = sqlite3.connect('tarefas.db')
    cursor = conn.cursor()
    
    # Estatísticas
    stats = {}
    stats['total'] = cursor.execute('SELECT COUNT(*) FROM tarefas').fetchone()[0]
    stats['pendentes'] = cursor.execute('SELECT COUNT(*) FROM tarefas WHERE status = "pendente"').fetchone()[0]
    stats['concluidas'] = cursor.execute('SELECT COUNT(*) FROM tarefas WHERE status = "concluida"').fetchone()[0]
    
    # Tarefas recentes
    tarefas = cursor.execute('''
        SELECT * FROM tarefas 
        ORDER BY data_criacao DESC 
        LIMIT 10
    ''').fetchall()
    
    conn.close()
    return render_template('dashboard.html', stats=stats, tarefas=tarefas)

@app.route('/tarefas')
def listar_tarefas():
    conn = sqlite3.connect('tarefas.db')
    cursor = conn.cursor()
    tarefas = cursor.execute('SELECT * FROM tarefas ORDER BY data_criacao DESC').fetchall()
    conn.close()
    return render_template('tarefas.html', tarefas=tarefas)

@app.route('/nova_tarefa', methods=['GET', 'POST'])
def nova_tarefa():
    if request.method == 'POST':
        titulo = request.form['titulo']
        descricao = request.form['descricao']
        prioridade = request.form['prioridade']
        
        conn = sqlite3.connect('tarefas.db')
        conn.execute('''
            INSERT INTO tarefas (titulo, descricao, prioridade)
            VALUES (?, ?, ?)
        ''', (titulo, descricao, prioridade))
        conn.commit()
        conn.close()
        
        return redirect(url_for('listar_tarefas'))
    
    return render_template('nova_tarefa.html')

@app.route('/concluir/<int:id>')
def concluir_tarefa(id):
    conn = sqlite3.connect('tarefas.db')
    conn.execute('''
        UPDATE tarefas 
        SET status = 'concluida', data_conclusao = CURRENT_TIMESTAMP
        WHERE id = ?
    ''', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('listar_tarefas'))

@app.route('/deletar/<int:id>')
def deletar_tarefa(id):
    conn = sqlite3.connect('tarefas.db')
    conn.execute('DELETE FROM tarefas WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('listar_tarefas'))

@app.route('/api/stats')
def api_stats():
    conn = sqlite3.connect('tarefas.db')
    cursor = conn.cursor()
    
    stats = {
        'total': cursor.execute('SELECT COUNT(*) FROM tarefas').fetchone()[0],
        'pendentes': cursor.execute('SELECT COUNT(*) FROM tarefas WHERE status = "pendente"').fetchone()[0],
        'concluidas': cursor.execute('SELECT COUNT(*) FROM tarefas WHERE status = "concluida"').fetchone()[0]
    }
    
    conn.close()
    return jsonify(stats)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)