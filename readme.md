
```bash
sudo service mysql status
hostname -I
sudo mysql - enter to mysql interface\
```
--
```sql
CREATE USER 'root'@'%' IDENTIFIED BY '*******';
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;
```
--
```bash
sudo netstat -tlnp | grep 3306
sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf
```
---
Raspberry Pi
---
SSH (Industry SSH, TCP/IP etc...)
* connection through ETHERNET cable or WiFi

Connected through WiFi

Project Directory
```bash
mkdir building_automation\
cd building_automation
```
---
TON, TP, TOF
---

implimented this in python\
(Add some diagrams)
---
establishing MODBUS connection
---
```bash
netstat -ano | findstr :502
tasklist | findstr 10800
```
