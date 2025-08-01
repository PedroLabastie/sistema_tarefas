# 🚀 PRIORIZZE

> Sistema elegante de gerenciamento de tarefas com interface moderna e animações suaves

[![Powered by AWS](https://d0.awsstatic.com/logos/powered-by-aws.png)](https://aws.amazon.com/)

**Desenvolvido com Amazon Q** - Demonstração das capacidades de desenvolvimento full-stack com IA.

## 🎯 Sobre o Projeto

Priorizze é um MVP de sistema de gerenciamento de tarefas que combina funcionalidade robusta com design moderno. Criado para demonstrar o poder do Amazon Q no desenvolvimento de aplicações web completas.

## ✨ Preview

- **Design**: Interface dark com gradientes azul/roxo
- **Animações**: Transições suaves e efeitos interativos
- **Responsivo**: Funciona perfeitamente em desktop e mobile
- **Logo**: Tipografia única com efeito "breathing"

## 🎨 Funcionalidades

### 📊 Dashboard Interativo
- Estatísticas em tempo real
- Cards animados com hover effects
- Atualização automática a cada 30s
- Visualização clara de métricas

### ✏️ Gerenciamento Completo (CRUD)
- ➕ **Criar** tarefas com descrição e prioridade
- 📋 **Listar** todas as tarefas com filtros visuais
- ✅ **Marcar** tarefas como concluídas
- 🗑️ **Deletar** tarefas com confirmação

### 🎯 Sistema de Prioridades
- 🔴 **Alta** - Borda vermelha, urgente
- 🟠 **Média** - Borda laranja, importante
- 🟢 **Baixa** - Borda verde, quando possível

### 🔌 API REST
- `GET /api/stats` - Estatísticas em JSON
- Pronto para integrações externas

### 🎭 UX/UI Moderna
- Animações CSS3 suaves
- Efeitos de hover interativos
- Transições com cubic-bezier
- Logo com efeito "breathing"
- Gradientes animados

## 🚀 Instalação e Execução

### Pré-requisitos
- Python 3.7+
- pip

### Instalação

1. **Clone o repositório**
```bash
git clone https://github.com/seu-usuario/priorizze.git
cd priorizze
```

2. **Instale as dependências**
```bash
pip install -r requirements.txt
```

3. **Execute a aplicação**
```bash
# Desenvolvimento
python app.py

# Produção
python run.py
```

4. **Acesse no navegador**
```
http://localhost:5000
```

## 🛠️ Stack Tecnológica

| Categoria | Tecnologia | Versão |
|-----------|------------|--------|
| **Backend** | Python | 3.7+ |
| **Framework** | Flask | 2.3.3 |
| **Database** | SQLite | Built-in |
| **Frontend** | HTML5 + CSS3 + JS | - |
| **Styling** | CSS Grid + Flexbox | - |
| **Animations** | CSS3 Transitions | - |
| **Icons** | Unicode Symbols | - |
| **AI Assistant** | Amazon Q | Latest |

## 📁 Estrutura do Projeto

```
priorizze/
├── 📄 app.py                 # Aplicação Flask principal
├── 📄 run.py                 # Script de produção
├── 📄 requirements.txt       # Dependências Python
├── 📄 .gitignore            # Arquivos ignorados pelo Git
├── 📄 README.md             # Esta documentação
├── 📁 templates/            # Templates Jinja2
│   ├── 📄 base.html         # Template base com styling
│   ├── 📄 dashboard.html    # Página inicial com stats
│   ├── 📄 tarefas.html      # Lista de tarefas
│   └── 📄 nova_tarefa.html  # Formulário de criação
└── 📄 tarefas.db           # Banco SQLite (auto-criado)
```

## 🎯 O que este MVP Demonstra

### 💻 Desenvolvimento Full-Stack
- Backend robusto com Flask
- Frontend responsivo e moderno
- Integração completa entre camadas

### 🎨 Design e UX
- Interface moderna com gradientes
- Animações CSS3 profissionais
- Experiência do usuário fluida
- Design system consistente

### 🔧 Arquitetura
- Padrão MVC bem estruturado
- Separação clara de responsabilidades
- Código limpo e documentado
- Pronto para escalar

### 🚀 Deploy Ready
- Configuração de produção
- Estrutura preparada para cloud
- Fácil containerização
- CI/CD friendly

## 🤖 Desenvolvido com Amazon Q

Este projeto foi criado inteiramente com a assistência do Amazon Q, demonstrando:
- Capacidade de desenvolvimento full-stack
- Criação de interfaces modernas
- Implementação de animações CSS
- Estruturação de projetos profissionais
- Documentação completa

## 📝 Licença

MIT License - Sinta-se livre para usar este projeto como base para seus próprios desenvolvimentos.

---

**Criado com ❤️ e Amazon Q**