# 🥪🍹 Lojinha Sucos & Sanduíches — Chat Assistente Virtual

---

## ✨ Sobre o Projeto

Este é um chatbot interativo feito com **Streamlit** que responde perguntas sobre o cardápio da sua lojinha de sucos e sanduíches. Ele usa um agente LLM da OpenAI integrado a um banco de dados **PostgreSQL remoto** para respostas dinâmicas e naturais.

---

## 🚀 Tecnologias Utilizadas

- Python 3.8+
- Streamlit (Interface Web)
- LangChain (Agente LLM)
- OpenAI API
- PostgreSQL (Render.com)
- psycopg2 (Driver PostgreSQL)
- python-dotenv (Variáveis de ambiente)
- Pillow (Manipulação de imagens)

---

## 📋 Pré-requisitos

- Python 3.8 ou superior instalado
- Conta na OpenAI com chave API válida
- Banco PostgreSQL remoto configurado (ex: Render.com)
- Git instalado (opcional, para clonar o projeto)

---

## ⚙️ Configuração do Ambiente

### 1. Clonar repositório

```bash
git clone https://github.com/JessicaDSL/lojinha-juice-agent-llm-mcp.git
cd lojinha-juice-agent-llm-mcp
```

### 2. Criar e ativar ambiente virtual

macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows (PowerShell)

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Windows (CMD)

```bash
python -m venv .venv
.\.venv\Scripts\activate.bat
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Criar arquivo .env

Na raiz do projeto, crie um arquivo .env com o conteúdo:

```bash
POSTGRES_URL=postgresql://usuario:senha@endereco:porta/banco
OPENAI_API_KEY=sua_chave_openai_aqui
```

---

▶️ Como Rodar o Projeto

```bash
streamlit run app.py
```

Abra o navegador no endereço que o Streamlit indicar (normalmente http://localhost:8501).

---

🛠 Funcionalidades
Chat com histórico visual

Respostas naturais usando modelo OpenAI

Consulta dinâmica no banco PostgreSQL remoto

Interface responsiva e estilizada com Streamlit

Botão para limpar conversa

📝 Estrutura do Projeto

.
├── app.py # Aplicação Streamlit (UI e lógica do chat)
├── agent.py # Agente LLM e funções de consulta
├── assets/
│ └── img/
│ └── design-logo-juice-store.png # Logo do projeto
├── requirements.txt # Dependências Python
├── .env # Variáveis de ambiente (não versionar)
└── README.md # Documentação do projeto

💡 Dicas e Observações
Proteja sua chave API, não compartilhe o .env

Você pode alterar o banco de dados ajustando a variável POSTGRES_URL

Expanda o agente LLM adicionando novas ferramentas em agent.py

Para atualizar dependências: pip install --upgrade -r requirements.txt

⚠️ Problemas Comuns
Erro de conexão com banco: confira string de conexão e status do banco

Erro de autenticação OpenAI: verifique chave API e limite da conta

Streamlit não inicia: atualize com pip install --upgrade streamlit

📜 Licença
Projeto licenciado sob a MIT License.

🤝 Contato
Quer sugerir melhorias ou tirar dúvidas? Abra uma issue no GitHub ou entre em contato!
