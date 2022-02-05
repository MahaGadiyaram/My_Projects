import requests
from sqlalchemy import create_engine


## POSTGRES
USERNAME_PG = 'postgres'
PASSWORD_PG = 'postgres'
HOST_PG = 'psqltweet' 
PORT_PG = 5432
DATABASE_NAME_PG = 'sentiment_db'

# Connection string
conn_string_pg = f"postgresql://{USERNAME_PG}:{PASSWORD_PG}@{HOST_PG}:{PORT_PG}/{DATABASE_NAME_PG}" 
pg = create_engine(conn_string_pg)


webhook_url = "https://hooks.slack.com/services/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"

data = {'text': joke}
requests.post(url=webhook_url, json = data)