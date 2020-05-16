import os
from uuid import uuid4
from datetime import datetime
from cassandra.cqlengine.models import Model
from cassandra.cqlengine import columns


class BooksModel(Model):
    __keyspace__ = os.getenv('CASSANDRA_KEY_SPACE')
    __table_name__ = 'book'

    id = columns.UUID(primary_key=True, default=uuid4)
    ip = columns.Text(index=True, default=None)
    time = columns.DateTime(default=datetime.utcnow)
    book = columns.Text(index=True, required=True, default=None)
    authors = columns.Text(required=True, default=None)
    rec_books = columns.List(value_type=columns.Text)
    state = columns.Boolean(default=False)
    agent = columns.Text(default=None)

    @classmethod
    def find_by_ip(cls, ip: str):
        return cls.objects(ip=ip)

    @classmethod
    def find_all(cls):
        return cls.objects.all()
    
    @classmethod
    def find_by_book(cls, book: str):
        return cls.objects(book=book)

"""class address(UserType):
    street = columns.Text()
    zipcode = columns.Integer()

class users(Model):
    __keyspace__ = 'cqlengine'
    name = columns.Text(primary_key=True)
    addr = columns.UserDefinedType(address)"""