from dotenv import load_dotenv
import os

load_dotenv(".env")

MEDIA_PATH = os.getenv("media_path")
DB_NAME = os.getenv("db_name")
DB_PORT = os.getenv("db_port")
DB_PASSWORD = os.getenv("db_password")
DB_HOST = os.getenv("db_host")
DB_USER= os.getenv("db_user")
LLM_API_KEY = os.getenv("api_key")

print("db_name in configh--",DB_NAME,DB_HOST,DB_PORT)