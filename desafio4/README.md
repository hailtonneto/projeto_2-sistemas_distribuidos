# Desafio 4 - Microsserviços Independentes

## 📌 Descrição
Este projeto demonstra a criação de dois microsserviços independentes que se comunicam via HTTP:
- **Service A**: retorna lista de usuários em JSON.
- **Service B**: consome o Service A e exibe informações combinadas.

---

## 🏗️ Arquitetura
- Cada microsserviço possui seu próprio Dockerfile.
- Comunicação via HTTP usando `requests`.
- Orquestração feita com `docker-compose`.

Fluxo:
```
serviceB ----HTTP----> serviceA
```

---

## ⚙️ Passo a Passo de Execução

1. Subir os serviços:
   ```bash
   docker compose up --build
   ```

2. Testar o Service A:
   ```
   http://localhost:5000/users
   ```

   Saída esperada:
   ```json
   [
     {"id": 1, "nome": "Hailton", "ativo_desde": "2023"},
     {"id": 2, "nome": "Maria", "ativo_desde": "2024"}
   ]
   ```

3. Testar o Service B:
   ```
   http://localhost:6000/info
   ```

   Saída esperada:
   ```json
   {
     "informacoes": [
       "Usuário Hailton ativo desde 2023",
       "Usuário Maria ativo desde 2024"
     ]
   }
   ```

---

## ✅ Critérios atendidos
- [x] Comunicação entre microsserviços funcionando  
- [x] Dockerfiles e isolamento corretos  
- [x] Explicação clara da arquitetura e endpoints  
- [x] Clareza e originalidade da implementação  