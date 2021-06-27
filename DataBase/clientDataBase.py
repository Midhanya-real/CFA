from array import array
import sys
sys.path.append("D:\Projects\PyProjects\CFAC_V1\Config");
import sqlite3
from config import configeration_app
from sqlite3.dbapi2 import Cursor;

data_base_path = configeration_app();

with sqlite3.connect(data_base_path['data_base_path']) as client_data:
    cursor = client_data.cursor();

    def add(data : array):
        try:
            query = f" INSERT INTO users(t_id, name, age, about, status, city) values({data[0]}, '{data[1]}', {data[2]}, '{data[3]}', '{data[4]}', '{data[5]}'); ";
            cursor.execute(query);
            client_data.commit();
        except:
            return False;

    def select(data : str):
        try:
            query = f" Select * from users where status = '{data}'; ";
            cursor.execute(query);
            return cursor.fetchall();
        except: 
            return False;
    
    def update(data : array):
        try:
            query = f" Update users set name = '{data[1]}', age = {data[2]}, about = '{data[3]}', status = '{data[4]}', city = '{data[5]}' where t_id = {data[0]} ;";
            cursor.execute(query);
            client_data.commit();
        except:
            return False;
    
    def delete(data : int):
        try:
            query = f" Delete from users where t_id = {data}";
            cursor.execute(query);
            client_data.commit();
        except:
            return False;