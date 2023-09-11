import json
import psycopg2


# read JSON data from file
with open('properties.json') as f:
   moredata = json.load(f)
    
# connect to the database
conn = psycopg2.connect(host="localhost", database="testi2", user="postgres", password="Arwe1981")

# create a cursor and table

cur = conn.cursor()
cur.execute("CREATE TABLE data_table3 ( id SERIAL PRIMARY KEY, location varchar, name varchar, code varchar);")

# execute the INSERT statement

sql = "INSERT INTO data_table3 (location, name, code) VALUES "
vals = []
for data in moredata:
    vals.append("('%s', '%s', '%s')" %
                (data['locationName'], data['propertyName'], data['propertyCode']))
cur.execute(sql + ",".join(vals))

# commit the changes to the database
conn.commit()

# close the cursor and connection
cur.close()
conn.close()
