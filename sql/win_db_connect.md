## Connecting

Resumen de cómo conectarse en Window:


```python
# Using the drivers we have installed in Windows
# with logged user credentials
drivers = ['ODBC Driver 11 for SQL Server', 'SQL Server', 'SQL Server Native Client 11.0']
connection_string = r'DRIVER={{{}}};SERVER=SERVERNAME;Trusted_Connection=Yes;'.format(drivers[1])

# with custom credentials
drivers = ['ODBC Driver 11 for SQL Server', 'SQL Server', 'SQL Server Native Client 11.0']
connection_string = r'DRIVER={{{}}};SERVER=SERVERNAME;UID=etsreader;PWD=etsreader;'.format(drivers[2])

qry = "SELECT @@servername"
c = pyodbc.connect(connection_string)

info = {
                'server': c.getinfo(pyodbc.SQL_SERVER_NAME),
                'dbms_name': c.getinfo(pyodbc.SQL_DBMS_NAME),
                'dbms_ver': c.getinfo(pyodbc.SQL_DBMS_VER),
                'user_name': c.getinfo(pyodbc.SQL_USER_NAME),
                'database_name': c.getinfo(pyodbc.SQL_DATABASE_NAME)
            }

import pprint
pprint.pprint(info)
```


Referencias:

- https://github.com/mkleehammer/pyodbc/wiki/Connection#getinfo
- https://docs.microsoft.com/en-us/sql/odbc/reference/syntax/sqlgetinfo-function?redirectedfrom=MSDN&view=sql-server-ver15

## Information

Es posible obtener información sobre el driver:

```python
import pyodbc
ops = 'DRIVER={FreeTDS};Server=SERVERNAME,1433;Database=DB;UID=user;PWD=pass'
c = pyodbc.connect(ops)
c.getinfo(pyodbc.SQL_DRIVER_AWARE_POOLING_SUPPORTED)
c.getinfo(pyodbc.SQL_DRIVER_HDBC)
c.getinfo(pyodbc.SQL_DRIVER_HDESC)
c.getinfo(pyodbc.SQL_DRIVER_HENV)
c.getinfo(pyodbc.SQL_DRIVER_HLIB)
c.getinfo(pyodbc.SQL_DRIVER_HSTMT)
c.getinfo(pyodbc.SQL_DRIVER_NAME)
c.getinfo(pyodbc.SQL_DRIVER_ODBC_VER)
c.getinfo(pyodbc.SQL_DRIVER_VER)
c.getinfo(pyodbc.SQL_DYNAMIC_CURSOR_ATTRIBUTES1)
c.getinfo(pyodbc.SQL_DYNAMIC_CURSOR_ATTRIBUTES2)
c.getinfo(pyodbc.SQL_FORWARD_ONLY_CURSOR_ATTRIBUTES1)
c.getinfo(pyodbc.SQL_ACTIVE_ENVIRONMENTS)
```



Referencias

- https://github.com/mkleehammer/pyodbc/wiki/Connection#getinfo
- https://docs.microsoft.com/en-us/sql/odbc/reference/syntax/sqlgetinfo-function?redirectedfrom=MSDN&view=sql-server-ver15#driver-information

## Version

Para ver la versión del protocolo tds que se usa:

```bash
pip install python-tds
```
En python: 

```python
import pytds
conn = pytds.connect('sever', 'db', 'user', 'pass')
hex(conn.tds_version)
```

Referenias

- https://python-tds.readthedocs.io/en/latest/pytds.html#pytds.Connection
- https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-tds/135d0ebe-5c4c-4a94-99bf-1811eccb9f4a#Appendix_A_17
- https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-tds/773a62b6-ee89-4c02-9e5e-344882630aac (Ver sección "Stream 
Parameter Details" )
