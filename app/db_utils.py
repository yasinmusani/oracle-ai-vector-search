import oracledb
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

def get_connection():
    return oracledb.connect(
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        dsn=os.getenv("DB_TNS_ALIAS")
    )

