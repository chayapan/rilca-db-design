FROM mysql/mysql-server:5.7
# CMD mysql -uroot -pexample < /dbconf/setup_db_users.sql

ADD conf/setup_db_users.sql /docker-entrypoint-initdb.d/
