from cassandra.cluster import Cluster

keyspace = 'translations'

cluster = Cluster()

session = cluster.connect(keyspace)

rows = session.execute('SELECT * FROM pl_fr')
for row in rows:
    print(row)