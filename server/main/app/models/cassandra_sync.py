from cassandra.cqlengine import management

def sync_db(db):

    keyspaces = ['book_keyspace',]
    conns = ['book_cluster',]

    # registers your connections
    # ...

    # create all keyspaces on all connections
    for ks in keyspaces:
        management.create_simple_keyspace(ks, connections=conns)

    # define your Automobile model
    # ...

    # sync your models
    management.sync_table(db, keyspaces=keyspaces, connections=conns)