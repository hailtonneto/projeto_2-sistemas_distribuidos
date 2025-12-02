## 📄 README.md – Desafio 1

# Desafio 1 - Containers em Rede

## 📌 Descrição
Este projeto demonstra a comunicação entre dois containers Docker conectados a uma rede customizada:
- **Servidor Web** (Flask) rodando na porta 8080.
- **Cliente** que realiza requisições HTTP periódicas ao servidor usando `curl`.

O objetivo é mostrar como containers podem se comunicar entre si através de uma rede interna Docker.

---

## 🏗️ Arquitetura
- Rede Docker criada automaticamente pelo `docker compose`.
- Container **server**:
  - Imagem baseada em `python:3.9-slim`.
  - Executa um servidor Flask na porta 8080.
- Container **client**:
  - Imagem baseada em `curlimages/curl`.
  - Executa um script em loop que faz requisições HTTP para o servidor.

Fluxo de comunicação:

```markdown
client ----HTTP----> server
```

---

## ⚙️ Passo a Passo de Execução

1. Clone o repositório e entre na pasta do desafio:
   ```bash
   git clone <seu-repositorio>
   cd desafio1
   ```

2. Suba os containers com Docker Compose:
   ```bash
   docker compose up --build
   ```

3. O servidor Flask estará acessível em:
   ```
   http://localhost:8080
   ```

4. O cliente enviará requisições periódicas e exibirá as respostas no log.

---

## 📜 Exemplos de Logs

### Server
```
 * Running on http://0.0.0.0:8080
172.18.0.3 - - [02/Dec/2025 02:04:40] "GET / HTTP/1.1" 200 -
```

### Client
```
Connecting to server...
Hello from Server
Connecting to server...
Hello from Server
```

---

## ✅ Critérios atendidos
- [x] Rede Docker configurada corretamente  
- [x] Comunicação funcional entre containers  
- [x] Explicação clara no README  
- [x] Organização do projeto e scripts de execução  

---

## 📂 Estrutura de Pastas
```
/desafio1
   ├── docker-compose.yml
   ├── server/
   │   ├── Dockerfile
   │   └── app.py
   └── client/
       ├── Dockerfile
       └── script.sh
```