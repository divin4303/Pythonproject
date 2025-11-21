sudo service mysql status \
hostname -I\
sudo mysql - enter to mysql interface\
--SQL--\
CREATE USER 'root'@'%' IDENTIFIED BY 'Oct@2019';\
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION;\
FLUSH PRIVILEGES;\
--\
sudo netstat -tlnp | grep 3306\
sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf

---
Raspberry Pi
---
SSH (Industry SSH, TCP/IP etc...)
* connection through ETHERNET cable
OPC UA vs WinCC
