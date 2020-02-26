import requests
import json
apikey={'api_key':'keyFt0iUCIPncgJA6'}
url='https://api.airtable.com/v0/appIap7xPyOplHI7c/NursaDbAvalogics'
test_data={
    'fields': {
                        'Nurse Full Name': 'Francisco Mendoza',
                        'Phone': '(208) 734-0000',
                        'Email': 'francisco@gmail.com',
                        'Profession License (1)': [
                            'RN'
                        ],
                        'First Name': 'Francisco',
                        'Last Name': 'Mendoza',
                        'Nursa Status': '2 | Outreach',
                        'Source': 'NurseFly'
                },
        }
try:
    r = requests.post(url,params=apikey,json=test_data)
    print(r.json())
except :
    print("Error")