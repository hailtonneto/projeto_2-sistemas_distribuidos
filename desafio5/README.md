# Desafio 5 - Microsserviços com API Gateway

## 📌 Descrição
Este projeto demonstra como usar um **API Gateway** para centralizar o acesso a múltiplos microsserviços.

---

## 🏗️ Arquitetura
- **Service A**: retorna lista de usuários.
- **Service B**: consome Service A e retorna informações formatadas.
- **Gateway**: expõe endpoints únicos e redireciona chamadas para os serviços.

Fluxo:
```
Cliente → Gateway → Service A / Service B
```

---

## ⚙️ Passo a Passo de Execução

1. Subir os serviços:
   ```bash
   docker compose up --build
   ```

2. Acessar via Gateway:
   - `http://localhost:8080/users` → retorna lista de usuários.  
   - `http://localhost:8080/info` → retorna informações formatadas.  

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

## ✅ Critérios atendidos
- [x] Gateway funcionando como ponto único de entrada  
- [x] Comunicação entre microsserviços via rede interna  
- [x] README com explicação e exemplos  