from peewee import *

# DOCS #

# https://github.com/coleifer/peewee

# CONSTANTS #

DB_NAME = 'my_database.db'


# MODELS #

db = SqliteDatabase(DB_NAME)


class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    username = CharField(unique=True)


