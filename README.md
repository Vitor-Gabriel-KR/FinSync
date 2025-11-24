# Zenkai – Guia de Instalação e Execução

Bem-vindo ao **Zenkai**, um sistema desenvolvido para gerenciamento financeiro inteligente. Este guia explica passo a passo como instalar e rodar o projeto localmente.

---

## 🚀 Pré-requisitos

Para executar o Zenkai, você precisa ter instalado:

* **PostgreSQL** (necessário para o banco de dados)

## 🛠️ Passo a Passo de Instalação

### **1️⃣ Instalar dependências (requirements.txt)**

Na pasta **root** do projeto, execute:

```
pip install -r requirements.txt
```

---

### **2️⃣ Rodar o setup do banco de dados**

O sistema possui um script de configuração em:

```
database/main.py
```

Execute-o para criar o banco de dados e gerar um usuário padrão:

```
python database/main.py
```

---

## ⚠️ Possíveis Erros e Solução

### Erro: *"Permission denied"* ou *"não foi possível criar usuário"*

Isso ocorre quando o PostgreSQL não possui um usuário com permissões adequadas.

Crie o usuário manualmente utilizando os seguintes dados:

```ini
DB_NAME=FinSync
DB_USER=FinSyncAdm
DB_PASSWORD=12345678
DB_HOST=localhost
DB_PORT=5432
```

Em seguida, conceda as permissões necessárias conforme mostrado na imagem abaixo:

*<img width="687" height="547" alt="image" src="https://github.com/user-attachments/assets/e17f9aa5-512a-4278-93a1-90c046583d41" />*

---

## ✔️ Pronto!

Após concluir esses passos, o sistema Zenkai estará pronto para uso. basta rodar o app.py!
```
python app.py
```
