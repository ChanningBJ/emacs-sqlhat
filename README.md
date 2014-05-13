emacs-sqlhat
============

emacs-sqlhat is an emacs extension to enhance sql-mode. When using sql-mode, user need to select the product before start SQLi session, emacs-sqlhat let the user to define the product (only support mysql currently) and connection information (user, password, hostname, database)on the head of sql file.

## setup
```
python setup.py install 
```

After that, add following lines in .emacs file:
```
(add-to-list 'load-path  "/path/to/emacs-sqlhat")
(require 'sqlhat)
```
## usage
You should put following information in you XXX.sql file:
```
--! product: mysql
--! hostname: 127.0.0.1
--! user: mysqluser
--! password: mysqlpassword
--! database: databasename
```
use command sqlhat-connect to create SQLi session.
