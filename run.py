#!/usr/bin/env python3
"""
Priorizze - Sistema de Gerenciamento de Tarefas
Desenvolvido com Amazon Q
"""

from app import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)