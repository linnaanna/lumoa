import requests
import json
response_API = requests.get('https://helsinki-openapi.nuuka.cloud/api/v1/EnergyData/Hourly/ListByProperty?Record=PropertyCode&SearchString=091-011-9902-0101&ReportingGroup=Electricity&StartTime=2019-09-08&EndTime=2019-09-09')
#print(response_API.status_code)

data = response_API.text

print(data)