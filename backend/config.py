class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'  # Cambiar a PostgreSQL o MySQL si es necesario
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'tu_clave_secreta_aqui'