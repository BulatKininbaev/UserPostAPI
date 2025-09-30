from os import getenv


db_url_async="postgresql+asyncpg://up_user:up_pass@localhost:5432/users_posts_db"
db_url="postgresql://up_user:up_pass@localhost:5432/users_posts_db"

sqla_max_overflow = 0
sqla_pool_size = 50

# вывод алхимичных скриптов во время исполнения
db_echo = False

# включаем только в переменной среды
if getenv("DB_ECHO") == "1":
    db_echo = True