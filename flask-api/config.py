SECRET_KEY = "log_parser"

MYSQL_ROOT_PASSWORD: "devpasswordlogparser"
MYSQL_HOST = "localhost"
MYSQL_USER = "flask"
MYSQL_PASSWORD = "devpasswordlogparser"
MYSQL_DB = "log_parser"
MYSQL_PORT = 5432

SQLALCHEMY_DATABASE_URI = (
    f"mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}"
)
