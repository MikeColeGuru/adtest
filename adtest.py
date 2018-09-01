from ldap3 import Server, Connection, ALL, NTLM

server = Server('prdc1b.dms.local',  get_info=ALL)
conn = Connection(server, user="DMS\\user", password="", authentication=NTLM)
# conn.bind()
# print(server.info)
conn.extend.standard.who_am_i()
