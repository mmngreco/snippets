Problema 

Conectarse a base de datos mssqlserver. Se hace un casting automatico de
time a datetime al coger un valor de una table con type time.

Posibles motivos:

* Distinta version del driver FreeTDS
* Distinta version del protoclo TDS_Version (<7.3)


## Comprobar version del driver

```bash
snippets ❯ tsql -C
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

## Protocolo de conexión

```bash
snippets ❯ cat /etc/freetds/freetds.conf
#
# This file is installed by FreeTDS if no file by the same
# name is found in the installation directory.
#
# For information about the layout of this file and its settings,
# see the freetds.conf manpage "man freetds.conf".

# Global settings are overridden by those in a database
# server specific section
[global]
        # TDS protocol version
        tds version = auto

        # Whether to write a TDSDUMP file for diagnostic purposes
        # (setting this to /tmp is insecure on a multi-user system)
;       dump file = /tmp/freetds.log
;       debug flags = 0xffff

        # Command and connection timeouts
;       timeout = 10
;       connect timeout = 10

        # To reduce data sent from server for BLOBs (like TEXT or
        # IMAGE) try setting 'text size' to a reasonable limit
;       text size = 64512

        # If you experience TLS handshake errors and are using openssl,
        # try adjusting the cipher list (don't surround in double or single quotes)
        # openssl ciphers = HIGH:!SSLv2:!aNULL:-DH

# A typical Sybase server
[egServer50]
        host = symachine.domain.com
        port = 5000
        tds version = 5.0

# A typical Microsoft server
[egServer73]
        host = ntmachine.domain.com
        port = 1433
        tds version = 7.3

```

## Referencias

* https://www.freetds.org/userguide/freetdsconf.htm#FREETDSCONFPURPOSE
* https://www.freetds.org/userguide/choosingtdsprotocol.htm
* https://www.freetds.org/userguide/odbcconnattr.htm
* https://www.freetds.org/userguide/confirminstall.htm
