import os
from uuid import uuid4
from datetime import datetime
from cassandra.cqlengine.models import Model
from cassandra.cqlengine import columns
from werkzeug.security import generate_password_hash, check_password_hash


class UserModel(Model):
    __keyspace__ = os.getenv('CASSANDRA_KEY_SPACE')
    __table_name__ = 'users'

    id = columns.UUID(primary_key=True, default=uuid4)
    username = columns.Text(partition_key=True, default=None)
    password_hash = columns.Text(default=None)
    is_admin = columns.Boolean(default=False)

    created = columns.DateTime(default=datetime.utcnow)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


    @classmethod
    def find_username(cls, _username: str):
        return cls.objects(username=_username)


    @classmethod
    def find_id(cls, _id: int):
        return cls.objects(id=_id)

    @classmethod
    def create_admin(cls, username: str, password: str):
        u = cls(username=username, is_admin=True)
        u.set_password(password)
        u.save()
        return u

    @classmethod
    def create_user(cls, username: str, password: str):
        u = cls(username=username)
        u.set_password(password)
        u.save()
        return u
    