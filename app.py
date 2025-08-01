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
            cor TEXT DEFAULT 'azul',
            data_vencimento DATE,
            hora_vencimento TIME,
            data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            data_conclusao TIMESTAMP
        )
    ''')
    
    conn.execute('''
        CREATE TABLE IF NOT EXISTS configuracoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tema_dinamico INTEGER DEFAULT 1,
            tema_fixo TEXT DEFAULT 'escuro'
        )
    ''')
    
    # Inserir configuração padrão se não existir
    if conn.execute('SELECT COUNT(*) FROM configuracoes').fetchone()[0] == 0:
        conn.execute('INSERT INTO configuracoes (tema_dinamico, tema_fixo) VALUES (1, "escuro")')
    
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
    tema_atual = get_tema_atual()
    return render_template('dashboard.html', stats=stats, tarefas=tarefas, tema=tema_atual)

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
        cor = request.form['cor']
        data_vencimento = request.form['data_vencimento'] if request.form['data_vencimento'] else None
        hora_vencimento = request.form['hora_vencimento'] if request.form['hora_vencimento'] else None
        
        conn = sqlite3.connect('tarefas.db')
        conn.execute('''
            INSERT INTO tarefas (titulo, descricao, prioridade, cor, data_vencimento, hora_vencimento)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (titulo, descricao, prioridade, cor, data_vencimento, hora_vencimento))
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

@app.route('/configuracoes', methods=['GET', 'POST'])
def configuracoes():
    conn = sqlite3.connect('tarefas.db')
    
    if request.method == 'POST':
        tema_dinamico = 1 if request.form.get('tema_dinamico') else 0
        tema_fixo = request.form['tema_fixo']
        
        conn.execute('''
            UPDATE configuracoes 
            SET tema_dinamico = ?, tema_fixo = ?
            WHERE id = 1
        ''', (tema_dinamico, tema_fixo))
        conn.commit()
        conn.close()
        return redirect(url_for('configuracoes'))
    
    config = conn.execute('SELECT * FROM configuracoes WHERE id = 1').fetchone()
    conn.close()
    return render_template('configuracoes.html', config=config)

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

@app.route('/api/tema')
def api_tema():
    conn = sqlite3.connect('tarefas.db')
    config = conn.execute('SELECT * FROM configuracoes WHERE id = 1').fetchone()
    conn.close()
    
    if config and config[1]:  # tema_dinamico ativo
        from datetime import datetime
        hora = datetime.now().hour
        
        if 6 <= hora < 12:
            tema = 'manha'
        elif 12 <= hora < 18:
            tema = 'tarde'
        elif 18 <= hora < 22:
            tema = 'noite'
        else:
            tema = 'madrugada'
    else:
        tema = config[2] if config else 'escuro'
    
    return jsonify({'tema': tema})

def get_tema_atual():
    conn = sqlite3.connect('tarefas.db')
    config = conn.execute('SELECT * FROM configuracoes WHERE id = 1').fetchone()
    conn.close()
    
    if config and config[1]:  # tema_dinamico ativo
        from datetime import datetime
        hora = datetime.now().hour
        
        if 6 <= hora < 12:
            return 'manha'
        elif 12 <= hora < 18:
            return 'tarde'
        elif 18 <= hora < 22:
            return 'noite'
        else:
            return 'madrugada'
    else:
        return config[2] if config else 'escuro'

if __name__ == '__main__':
    init_db()
    app.run(debug=True)