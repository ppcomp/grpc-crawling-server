import sys, os
import json
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

def get_secret(setting):
    try:
        with open('secret.json', 'r') as f:
            secret = json.loads(f.read())
    except:
        with open('secret_dev.json', 'r') as f:
            secret = json.loads(f.read())
    return secret[setting]

# Scheme: "postgres+psycopg2://<USERNAME>:<PASSWORD>@<IP_ADDRESS>:<PORT>/<DATABASE_NAME>"
DATABASE_URI = f"postgres+psycopg2://postgres:{get_secret('DB_PASSWORD')}@db:5432/postgres"