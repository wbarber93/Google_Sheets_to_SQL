import sqlite3

# connecting to the database  
connection = sqlite3.connect("Film_Database.db") 
 
# cursor  
crsr = connection.cursor() 
  
# SQL command to create a table in the database 
sql_create_film_table = """
DROP TABLE IF EXISTS Films
CREATE TABLE IF NOT EXISTS Films (
    
col_id INTEGER PRIMARY KEY,

order_date DATE,
client VARCHAR(500),
film_type VARCHAR(50),
gbp_value VARCHAR (50),
usd_value VARCHAR (50),
salespeople VARCHAR(30),
);
"""

# execute the statement 
crsr.execute(sql_create_film_table)