# Desafio 2 - Volumes e Persistência

## 📌 Descrição
Este projeto demonstra como usar volumes Docker para garantir persistência de dados em containers.  
O banco de dados escolhido foi **PostgreSQL**.

---

## 🏗️ Arquitetura
- Serviço `db` rodando PostgreSQL.
- Volume `db_data` mapeado para `/var/lib/postgresql/data`.
- Mesmo após remover o container, os dados continuam disponíveis.

---

## ⚙️ Passo a Passo de Execução

1. Subir o container:
   ```bash
   docker compose up -d
   ```

2. Acessar o banco de dados:
   ```bash
   docker exec -it desafio2-db psql -U user -d mydb
   ```

3. Criar uma tabela e inserir dados:
   ```sql
   CREATE TABLE usuarios (id SERIAL PRIMARY KEY, nome VARCHAR(50));
   INSERT INTO usuarios (nome) VALUES ('Hailton');
   SELECT * FROM usuarios;
   ```

4. Remover o container:
   ```bash
   docker compose down
   ```

5. Subir novamente:
   ```bash
   docker compose up -d
   docker exec -it desafio2-db psql -U user -d mydb
   SELECT * FROM usuarios;
   ```

✅ Você verá que os dados continuam lá, provando a persistência.

---

## 📜 Logs/Resultados
Exemplo de saída:
```
 id |  nome
----+---------
  1 | Hailton
```

---

## ✅ Critérios atendidos
- [x] Uso correto de volumes  
- [x] Persistência comprovada após recriação do container  
- [x] README com explicação e prints/resultados  
- [x] Clareza e organização do código  

---

## 🎯 Resultado esperado
- Você cria dados no banco.  
- Remove o container.  
- Sobe de novo e os dados ainda estão lá.  