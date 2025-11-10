## Homework 3
Aplikace využívá csv z prvního domácího úkolu, aby se nějak zaplnilo mongodb.

Aplikace je složena tak, že stačí zavolat:
```docker
docker compose up -d
```
Compose file je přizpůsoben, že si zavolá jednotlivé docker file a provede build.
Celé prostředí se skládá ze 3 container aplikací.
1. MongoDB
2. db_populate_app (aplikace, která jednorázově zaplní mongodb daty)
3. db_rest_api_server (api pro komunikaci s DB)

### Příkazy v REST API
Volání se provádí přes port <b>7878</b>
```
# základní volání
localhost:7878/

# vrácení OK response pro ověření běhu serveru
localhost:7878/status

# vrácení info o db
localhost:7878/status/db

Zatím nefunguje dobře query... vše vrací 404
# vrácení dat ze zvoleného řádku
localhost:7878/robot_data/row=<id>

# vrátí veškerá data z db
localhost:7878/robot_data/all

```