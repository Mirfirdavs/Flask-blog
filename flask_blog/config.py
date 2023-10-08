import os
from dotenv import load_dotenv, find_dotenv


class Config():
    load_dotenv(find_dotenv())
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.yandex.ru'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_ASCII_ATTACHMENTS = True
    MAIL_USERNAME = os.getenv('YANDEX-EMAIL-USERNAME')
    MAIL_PASSWORD = os.getenv('YANDEX-PASSWORD')