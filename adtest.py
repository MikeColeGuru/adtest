from ldap3 import Server, Connection, ALL

server = Server('prdc1b.dms.local',  get_info=ALL)
conn = Connection(server)
print(server.info)
