## Python scripts 

```python
# -----------------------------------------------------------------------------
# USING ALCHEMY
import sqlalchemy as sa
url_str = "mssql+pyodbc://usr:pass@server:port/db?driver=FreeTDS"
eng = sa.create_engine(url_str)
query = 'SELECT * FROM db WHERE field = 2'
eng.execute(query).fetchall()

# -----------------------------------------------------------------------------
# From url to pyodbc params
from sqlalchemy.engine.url import make_url
from sqlalchemy.connectors.pyodbc import PyODBCConnector
import pyodbc

query = 'SELECT * FROM db WHERE field = 2'
url_str = "mssql+pyodbc://usr:pass@server:port/db?driver=FreeTDS&TDS_Version=7.2"
url_str = "mssql+pyodbc://usr:pass@server:port/db?driver=FreeTDS"
connector =  PyODBCConnector()
url = make_url(url_str)
ops = connector.create_connect_args(url)
c = pyodbc.connect(*ops)

# -----------------------------------------------------------------------------
# USING PYODBC
import pyodbc
ops = 'DRIVER={FreeTDS};Server=server,port;Database=db;UID=user;PWD=pass'
ops = 'DRIVER={FreeTDS};Server=server,port;Database=db;UID=user;PWD=pass&TDS_Version=7.2'
c = pyodbc.connect(ops)
query = 'SELECT * FROM db WHERE field = 2'
c.execute(query).fetchall()

import pandas as pd
pd.read_sql(query, c).dtypes

# -----------------------------------------------------------------------------
# Get table info
query = "SELECT COLUMN_NAME, DATA_TYPE FROM information_schema.columns WHERE table_name = 'tbname'"
eng.execute(query).fetchall()
```

## Another issue:

If server is passed throught connection string then config files are ignored,
see: https://stackoverflow.com/a/16219721/3124367

## Useful files and commands

```bash
$SERVER=server
$USER=user
$PASS=password
$PORT=1433
$DBNAME=dbname

cat /etc/odbc.ini
cat /etc/odbcinst.ini
cat /etc/freetds/freetds.conf

tsql -C
tsql -S $SERVER -U $USER -P $PASS -p $PORT -D $DBNAME
osql -S $SERVER -U $USER -P $PASS
```

## References

* https://www.freetds.org/userguide/freetdsconf.htm#FREETDSCONFPURPOSE
* https://www.freetds.org/userguide/choosingtdsprotocol.htm
* https://www.freetds.org/userguide/odbcconnattr.htm
* https://www.freetds.org/userguide/confirminstall.htm
* https://github.com/mkleehammer/pyodbc/wiki/Connecting-to-SQL-Server-from-Windows
* https://stackoverflow.com/a/16219721/3124367

