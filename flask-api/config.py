SECRET_KEY = "log_parser"

MYSQL_ROOT_PASSWORD: "devpasswordlogparser"
MYSQL_HOST = "database"
MYSQL_USER = "flask"
MYSQL_PASSWORD = "devpasswordlogparser"
MYSQL_DB = "log_parser"
MYSQL_PORT = 3306

SQLALCHEMY_DATABASE_URI = (
    f"mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}"
)
