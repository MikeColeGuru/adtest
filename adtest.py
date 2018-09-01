from ldap3 import Server, Connection, ALL

server = Server('prdc1b.dms.local')
conn = Connection(server)
print(conn.bind())
