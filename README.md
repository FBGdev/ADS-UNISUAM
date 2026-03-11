# Sistema de Gerenciamento de Alunos (Use Case 1)

## 📚 Sobre o projeto

Este projeto foi desenvolvido como **primeiro trabalho de Use Case do curso de Análise e Desenvolvimento de Sistemas (ADS)**.

O objetivo do sistema é simular um **pequeno sistema acadêmico**, permitindo o gerenciamento básico de alunos através de uma **API**.

O sistema permite:

* cadastrar alunos
* listar alunos
* atualizar informações
* remover alunos
* visualizar notas e presença

O projeto foi desenvolvido utilizando **Python**, com **Flask** para criação da API e **JSON** como forma simples de armazenamento de dados.

Este projeto tem caráter **educacional**, com o objetivo de praticar conceitos básicos de desenvolvimento backend.

---

# 🧠 Conceitos utilizados

## API (Application Programming Interface)

A API é responsável por **gerenciar os dados dos alunos**.

Ela recebe requisições HTTP e responde com informações em **JSON**.

Exemplo de requisição:

```
GET /alunos
```

Essa requisição retorna a lista de alunos cadastrados.

---

## JSON como banco de dados

Neste projeto não foi utilizado banco de dados tradicional.
Os dados são armazenados em um **arquivo JSON**.

Exemplo:

```json
{
  "alunos": [
    {
      "id": 1,
      "nome": "Fabiano",
      "n1": 10,
      "n2": 10,
      "presenca": 400
    }
  ]
}
```

Cada aluno possui:

| Campo    | Descrição                    |
| -------- | ---------------------------- |
| id       | identificador único do aluno |
| nome     | nome do aluno                |
| n1       | nota da primeira prova       |
| n2       | nota da segunda prova        |
| presenca | quantidade de presenças      |

---

# 🔁 Operações CRUD

O sistema segue o padrão **CRUD**, muito comum em sistemas backend.

| Operação | Significado |
| -------- | ----------- |
| Create   | Criar       |
| Read     | Ler         |
| Update   | Atualizar   |
| Delete   | Deletar     |

No sistema isso corresponde a:

| Método HTTP | Função          |
| ----------- | --------------- |
| GET         | listar alunos   |
| GET /id     | buscar aluno    |
| POST        | adicionar aluno |
| PUT         | atualizar aluno |
| DELETE      | remover aluno   |

---

# ⚙️ Tecnologias utilizadas

* Python
* Flask
* JSON
* Requests
* Git
* GitHub

---

# 📂 Estrutura do projeto

Exemplo simplificado da estrutura do projeto:

```
projeto/
│
├── api.py
├── main.py
├── alunos.json
├── requirements.txt
└── README.md
```

Descrição dos arquivos:

**api.py**
Contém a API criada com Flask responsável por manipular os dados.

**main.py**
Interface de terminal utilizada para interagir com a API.

**alunos.json**
Arquivo que armazena os dados dos alunos.

**README.md**
Documentação do projeto.

---

# 🚀 Como executar o projeto

## 1️⃣ Clonar o repositório

```
git clone https://github.com/seu-repositorio
```

---

## 2️⃣ Criar ambiente virtual (opcional)

```
python -m venv venv
```

Ativar ambiente virtual no Windows:

```
venv\Scripts\activate
```

---

## 3️⃣ Instalar dependências

```
pip install flask requests
```

---

## 4️⃣ Iniciar a API

Execute:

```
python api.py
```

A API será iniciada em:

```
http://127.0.0.1:5000
```

---

## 5️⃣ Executar o sistema

Abra outro terminal e execute:

```
python main.py
```

O sistema será executado no terminal com um **menu de opções** para interação.

---

# 📋 Funcionalidades

O sistema permite:

* listar alunos
* adicionar novos alunos
* atualizar notas
* atualizar presença
* remover alunos

Todas as operações são feitas através de **requisições para a API**.

---

# 📖 Objetivo acadêmico

Este projeto foi desenvolvido com o objetivo de praticar:

* lógica de programação
* manipulação de JSON
* criação de APIs
* consumo de APIs
* organização de projetos em Python

Também ajuda a entender o funcionamento da arquitetura **cliente-servidor**, muito utilizada em aplicações web.

---

# 👨‍💻 Autor

Fabiano
Estudante de **Análise e Desenvolvimento de Sistemas**

---

# 📌 Observação

Este projeto foi desenvolvido para fins educacionais e pode ser expandido futuramente com:

* banco de dados real (PostgreSQL ou MySQL)
* autenticação de usuários
* interface web
* validação de dados
* testes automatizados

