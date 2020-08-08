import sys, os
import json

def get_secret(setting):
    try:
        with open(os.path.dirname(os.path.abspath(__file__)) + '/secret.json', 'r') as f:
            secret = json.loads(f.read())
    except:
        with open(os.path.dirname(os.path.abspath(__file__)) + '/secret_dev.json', 'r') as f:
            secret = json.loads(f.read())
    return secret[setting]

# Scheme: "postgres+psycopg2://<USERNAME>:<PASSWORD>@<IP_ADDRESS>:<PORT>/<DATABASE_NAME>"
DATABASE_URI = f"postgres+psycopg2://postgres:{get_secret('DB_PASSWORD')}@localhost:5432/postgres"