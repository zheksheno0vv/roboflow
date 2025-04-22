import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    MONGO_DB = os.getenv('MONGO_DB')
    DB_NAME = os.getenv('DB_NAME')
    ROBOFLOW_URL = os.getenv('ROBOFLOW_URL')


config = Config()