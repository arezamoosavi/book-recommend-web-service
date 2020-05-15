from cassandra.cqlengine import management

def sync_db(db):

    keyspaces = ['book_keyspace',]
    conns = ['node_0', 'node_1']

    # registers your connections
    # ...

    # create all keyspaces on all connections
    for ks in keyspaces:
        management.create_keyspace_simple(name=ks,
         replication_factor=2, durable_writes=True, connections=conns)

    # define your Automobile model
    # ...

    # sync your models
    management.sync_table(db, keyspaces=keyspaces, connections=conns)