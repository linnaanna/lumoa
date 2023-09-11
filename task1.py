import json
import psycopg2


# read JSON data from file
with open('properties.json') as f:
   
    moredata = json.load(f)
    data = moredata[0]["propertyCode"]
   
    print(type(moredata))
    print(type(data))
    print(data)

    length = len(moredata)

    #for i in range (length): 
       # moredata[i]["propertyCode"]

# connect to the database
conn = psycopg2.connect(host="localhost", database="testi2", user="postgres", password="Arwe1981")

# create a cursor
cur = conn.cursor()


cur.execute("CREATE TABLE data_table2 ( id SERIAL PRIMARY KEY, propertyCode varchar, propertyName varchar);")




# execute the INSERT statement

sql = "INSERT INTO data_table2 (propertyCode, propertyName) VALUES "
vals = []
for word in moredata:
    vals.append("('%s', '%s')" %
                (word['propertyCode'], word['propertyName']))
cur.execute(sql + ",".join(vals))



# commit the changes to the database
conn.commit()

# close the cursor and connection
cur.close()
conn.close()

