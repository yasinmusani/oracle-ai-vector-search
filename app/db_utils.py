import oracledb
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Set TNS_ADMIN to point to wallet path before using Oracle DB
os.environ["TNS_ADMIN"] = os.getenv("DB_WALLET_PATH")

# Initialize Oracle client for thick mode (required for wallet)
oracledb.init_oracle_client(lib_dir="C:\\instantclient_23_8")

def get_connection():
    return oracledb.connect(
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        dsn=os.getenv("DB_TNS_ALIAS")
    )
