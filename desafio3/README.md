# Desafio 3 - Docker Compose Orquestrando Serviços

## 📌 Descrição
Este projeto demonstra como orquestrar múltiplos serviços dependentes usando Docker Compose:
- **Web**: aplicação Flask.
- **DB**: PostgreSQL.
- **Cache**: Redis.

---

## 🏗️ Arquitetura
- O serviço `web` depende de `db` e `cache`.
- Comunicação entre serviços via rede interna `minha_rede`.
- Persistência de dados garantida pelo volume `db_data`.

Fluxo:
```
web <--> db
web <--> cache
```

---

## ⚙️ Passo a Passo de Execução

1. Subir os serviços:
   ```bash
   docker compose up --build
   ```

2. Acessar a aplicação:
   ```
   http://localhost:8080
   ```

3. Testar:
   - Cada vez que acessar a rota `/`, o contador de visitas (Redis) será incrementado.
   - O banco PostgreSQL será inicializado e conectado.

---

## 📜 Exemplos de Logs
```
web_1    | Visita número 1 - Banco conectado com sucesso!
web_1    | Visita número 2 - Banco conectado com sucesso!
```

---

## ✅ Critérios atendidos
- [x] Compose funcional e bem estruturado  
- [x] Comunicação entre serviços funcionando  
- [x] README com explicação da arquitetura  
- [x] Clareza e boas práticas  