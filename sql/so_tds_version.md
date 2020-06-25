# How can I obtain the TDS protocol version agreed between client and server in linux?

I found an unexpected behaviuor when I make a query to a SQL Server from linux.

What I know:

* The `/etc/odbcinst.ini` has the main settings.
* I can configure DSN in `/etc/odbc.ini` or `~/odbc.ini` (Is not my case)
* The configuration can be showed with `tsql -C`


My `/etc/odbcinst.ini`:

```zsh
base ❯ cat /etc/odbcinst.ini
[ODBC Driver 17 for SQL Server]
Description=Microsoft ODBC Driver 17 for SQL Server
Driver=/opt/microsoft/msodbcsql17/lib64/libmsodbcsql-17.5.so.2.1
UsageCount=1

[FreeTDS]
Description = TDS driver (Sybase/MS SQL)
Driver = /usr/lib/x86_64-linux-gnu/odbc/libtdsodbc.so
Setup = /usr/lib/x86_64-linux-gnu/odbc/libtdsS.so
CPTimeout =
CPReuse =
FileUsage = 1
```

My `/etc/odbc.ini`

```zsh
base ❯ cat /etc/odbc.ini

```

My configuration:

```zsh
dev ❯ tsql -C
Compile-time settings (established with the "configure" script)
                            Version: freetds v1.1.6
             freetds.conf directory: /etc/freetds
     MS db-lib source compatibility: no
        Sybase binary compatibility: yes
                      Thread safety: yes
                      iconv library: yes
                        TDS version: auto
                              iODBC: no
                           unixodbc: yes
              SSPI "trusted" logins: no
                           Kerberos: yes
                            OpenSSL: no
                             GnuTLS: yes
                               MARS: yes


```

As it showed I can't see which version of TDS protocol I'm using. Of course, if
I check my freetds version (v1.1.6) on the freetds documentation I can see that 
the highest
[TDS Version supported](https://www.freetds.org/userguide/choosingtdsprotocol.htm)
is the v7.4.

The question is still open, which version of TDS I'm using? Thats should be
defined by an agreement between server and client, isn't it?

What I tried:

Because I'm working on python, I found that pyodbc has the method
[`getinfo`](https://github.com/mkleehammer/pyodbc/wiki/Connection#getinfo)
which retrieves relevant information:



```

```
