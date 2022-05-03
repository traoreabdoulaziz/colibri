from fireorm.Models import Model
from fireorm.Fields import TextField

class User(Model):
    username = TextField()
    password_hash = TextField()