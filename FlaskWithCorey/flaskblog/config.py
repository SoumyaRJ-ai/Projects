import os


class Config:
    # SECRET_KEY = os.environ.get('SECRET_KEY') # This should be used as this is not working now, so skipping
    SECRET_KEY = '3bdc196612fea2306661dd0399a39618'  # Passing manually as the above environment key is not working
    # for now
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')