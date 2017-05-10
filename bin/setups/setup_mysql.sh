# -*- coding: utf-8 -*-


#echo "create user 'alladmin'@'localhost'"
#sudo mysql -p -e "\
#create user 'alladmin'@'localhost' identified by 'admin';\
#flush privileges;"

echo "drop database country_graph"
sudo mysql -p -e "\
drop database country_graph;\
create database country_graph;\
grant ALL on country_graph.* to 'alladmin'@'localhost';\
flush privileges;"

echo "create table country_graph.countries"
sudo mysql -p -e "\
create table country_graph.countries (\
id int, \
name tinytext, \
contents_path tinytext, \
flag_path tinytext);\
alter table country_graph.countries default character set "utf8";\
flush privileges;"

echo "create table country_graph.tf_parameters"
sudo mysql -p -e "\
create table country_graph.tf_parameters (\
id int, \
result int, \
v0 float, \
v1 float, \
v2 float, \
v3 float, \
v4 float, \
v5 float, \
v6 float, \
v7 float, \
v8 float, \
v9 float);\
flush privileges;"

echo "create table country_graph.edges"
sudo mysql -p -e "\
create table country_graph.edges (\
id int, \
start int, \
end int, \
relevancy float);\
flush privileges;"

