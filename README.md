# 🚀 Projeto Docker e Microsserviços

## 📌 Descrição
Este repositório reúne uma série de desafios práticos para aprender e aplicar conceitos de **Docker**, **Docker Compose** e **Microsserviços**.  
Cada desafio evolui a arquitetura, começando com um container simples e chegando até a orquestração com **API Gateway**.

---

## 🏗️ Estrutura dos Desafios

- **Desafio 1 – Container Básico**  
  Criar e rodar um container simples com uma aplicação Flask.

- **Desafio 2 – Persistência de Dados**  
  Usar volumes para persistir dados em containers.

- **Desafio 3 – Compose Orquestrando Serviços**  
  Orquestrar múltiplos serviços (Web, DB, Cache) com Docker Compose.

- **Desafio 4 – Microsserviços Independentes**  
  Criar dois microsserviços que se comunicam via HTTP.

- **Desafio 5 – API Gateway**  
  Centralizar o acesso aos microsserviços através de um Gateway.

---

## ⚙️ Como Executar

1. Clone o repositório:
   ```bash
   git clone <url-do-repo>
   cd projeto-docker
   ```

2. Entre na pasta do desafio desejado:
   ```bash
   cd desafio3
   ```

3. Suba os serviços:
   ```bash
   docker compose up --build
   ```

4. Acesse os endpoints conforme descrito em cada desafio.

---

## 🌐 Endpoints Principais

- **Desafio 3**
  - `http://localhost:8080/` → aplicação web conectada ao PostgreSQL e Redis.

- **Desafio 4**
  - `http://localhost:5000/users` → retorna lista de usuários (Service A).  
  - `http://localhost:6000/info` → retorna informações formatadas (Service B).

- **Desafio 5**
  - `http://localhost:8080/users` → acessa Service A via Gateway.  
  - `http://localhost:8080/info` → acessa Service B via Gateway.  

---

## 📜 Exemplos de Saída

### `/users`
```json
[
  {"id": 1, "nome": "Hailton", "ativo_desde": "2023"},
  {"id": 2, "nome": "Maria", "ativo_desde": "2024"}
]
```

### `/info`
```json
{
  "informacoes": [
    "Usuário Hailton ativo desde 2023",
    "Usuário Maria ativo desde 2024"
  ]
}
```

---

## ✅ Aprendizados

- Criar e rodar containers básicos.  
- Persistir dados com volumes.  
- Orquestrar múltiplos serviços com Docker Compose.  
- Construir microsserviços independentes que se comunicam via HTTP.  
- Implementar um API Gateway para centralizar o acesso.  
