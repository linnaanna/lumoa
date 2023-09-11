import requests
import psycopg2
import json

def insert_data(propertyCode):
#connect to API and fetch data
    response_API = requests.get('https://helsinki-openapi.nuuka.cloud/api/v1/EnergyData/Daily/ListByProperty?Record=PropertyCode&SearchString=' + propertyCode + '&ReportingGroup=Electricity&StartTime=2022-01-01&EndTime=2022-01-14')

#convert data to list
    response = response_API.text
    data = json.loads(response)

    
# connect to the database
    conn = psycopg2.connect(host="localhost", database="testi2", user="postgres", password="Arwe1981")

# create a cursor

    cur = conn.cursor()


# execute the INSERT statement

    sql = "INSERT INTO table10 (id, tammi1, tammi2, tammi3, tammi4, tammi5, tammi6, tammi7, tammi8, tammi9, tammi10, tammi11, tammi12, tammi13, tammi14) VALUES"
    vals = []

    vals.append("('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" %
                ( propertyCode, data[0]['value'], data[1]['value'], data[2]['value'], data[3]['value'], data[4]['value'], data[5]['value'], data[6]['value'], data[7]['value'], data[8]['value'], data[9]['value'], data[10]['value'], data[11]['value'], data[12]['value'], data[13]['value']))
    cur.execute(sql + "," .join(vals))

# commit the changes to the database
    conn.commit()

# close the cursor and connection
    cur.close()
    conn.close()

insert_data("091-029-0006-0004")
insert_data("091-041-0200-0010")
insert_data("091-003-0049-0006")
insert_data("091-022-0530-0018")
insert_data("091-011-0333-0012")    