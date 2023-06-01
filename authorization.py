import os
import requests
import json
import time


# définition de l'adresse de l'API
api_address = 'fastapi'
# port de l'API
api_port = 8000

payload = {
        "purchase_value": 0,
        "age": 0,
        "hour": 0,
        "day": 0,
        "month": 0,
        "source_Ads": 0,
        "source_Direct": 0,
        "source_SEO": 0,
        "browser_Chrome": 0,
        "browser_FireFox": 0,
        "browser_IE": 0,
        "browser_Opera": 0,
        "browser_Safari": 0,
        "sex_F": 0,
        "sex_M": 0
    }
# attente pour donner le temps au container fastapi de se lancer
#time.sleep(5)
# requête au endpoint /v1/predict/modele pour Bob
r5 = requests.post(url='http://{address}:{port}/v1/predict/modele'.format(address=api_address, port=api_port), auth=('Bob', 'builder'), data = json.dumps(payload))

output5 = '''
============================
    Authorization test
============================

request done at "/v1/predict/modele"
| username="Bob"
| password="builder"
| features =
        "purchase_value": 0,
        "age": 0,
        "hour": 0,
        "day": 0,
        "month": 0,
        "source_Ads": 0,
        "source_Direct": 0,
        "source_SEO": 0,
        "browser_Chrome": 0,
        "browser_FireFox": 0,
        "browser_IE": 0,
        "browser_Opera": 0,
        "browser_Safari": 0,
        "sex_F": 0,
        "sex_M": 0

expected result = 200
actual restult = {status_code}

==>  {test_status}
==> {response}

'''


# statut de la requête
status_code5 = r5.status_code
response5 = r5.text

# affichage des résultats
if status_code5 == 200:
    test_status5 = 'SUCCESS'
else:
    test_status5 = 'FAILURE'
print(output5.format(status_code=status_code5, test_status=test_status5,
                     response=response5))



# impression dans un fichier
if os.environ.get('LOG') == '1': 
    filepath = os.path.join('data','api_test.log')
    with open(filepath, 'a') as file:
    	file.write(output5)

# requête au endpoint /v2/predict/modele pour Bob
r6 = requests.post(url='http://{address}:{port}/v2/predict/modele'.format(address=api_address, port=api_port), auth=('Bob', 'builder'), data = json.dumps(payload))
        
    
output6 = '''
============================
   Authorization test
============================

request done at "/v2/predict/modele"
| username="Bob"
| password="builder"
| features =
        "purchase_value": 15,
        "age": 53,
        "hour": 18,
        "day": 3,
        "month": 1,
        "source_Ads": 0,
        "source_Direct": 0,
        "source_SEO": 1,
        "browser_Chrome": 0,
        "browser_FireFox": 0,
        "browser_IE": 0,
        "browser_Opera": 1,
        "browser_Safari": 0,
        "sex_F": 0,
        "sex_M": 1

expected result = 401
actual restult = {status_code}

==>  {test_status}
==> {response}

'''


# statut de la requête
status_code6 = r6.status_code
response6 = r6.text

# affichage des résultats
if status_code6 == 200:
    test_status6 = 'SUCCESS'
else:
    test_status6 = 'FAILURE'
print(output6.format(status_code=status_code6, test_status=test_status6,
                     response=response6))

# impression dans un fichier
if os.environ.get('LOG') == '1': 
    filepath = os.path.join('data','api_test.log')
    with open(filepath, 'a') as file:
        file.write(output6)

# requête au endpoint /v1/predict/modele pour Alice
r7 = requests.post(url='http://{address}:{port}/v1/predict/modele'.format(address=api_address, port=api_port), auth=('Alice', 'wonderland'), data = json.dumps(payload))

output7 = '''
============================
    Authorization test
============================

request done at "/v1/predict/modele"
| username="Alice"
| password="wonderland"
| features =
        "purchase_value": 15,
        "age": 53,
        "hour": 18,
        "day": 3,
        "month": 1,
        "source_Ads": 0,
        "source_Direct": 0,
        "source_SEO": 1,
        "browser_Chrome": 0,
        "browser_FireFox": 0,
        "browser_IE": 0,
        "browser_Opera": 1,
        "browser_Safari": 0,
        "sex_F": 0,
        "sex_M": 1

expected result = 200
actual restult = {status_code}

==>  {test_status}
==> {response}

'''


# statut de la requête
status_code7 = r7.status_code
response7 = r7.text

# affichage des résultats
if status_code7 == 200:
    test_status7 = 'SUCCESS'
else:
    test_status7 = 'FAILURE'
print(output7.format(status_code=status_code7, test_status=test_status7,
                     response=response7))

# impression dans un fichier
if os.environ.get('LOG') == '1': 
    filepath = os.path.join('data','api_test.log')
    with open(filepath, 'a') as file:
        file.write(output7)      

# requête au endpoint /v2/predict/modele pour Alice
r8 = requests.post(url='http://{address}:{port}/v2/predict/modele'.format(address=api_address, port=api_port), auth=('Alice', 'wonderland'), data = json.dumps(payload))
   


output8 = '''
============================
    Authorization test
============================

request done at "/v2/predict/modele"
| username="Alice"
| password="wonderland"
| features =
        "purchase_value": 15,
        "age": 53,
        "hour": 18,
        "day": 3,
        "month": 1,
        "source_Ads": 0,
        "source_Direct": 0,
        "source_SEO": 1,
        "browser_Chrome": 0,
        "browser_FireFox": 0,
        "browser_IE": 0,
        "browser_Opera": 1,
        "browser_Safari": 0,
        "sex_F": 0,
        "sex_M": 1

expected result = 200
actual restult = {status_code}

==>  {test_status}
==> {response}

'''


# statut de la requête
status_code8 = r8.status_code
response8 = r8.text

# affichage des résultats
if status_code8 == 200:
    test_status8 = 'SUCCESS'
else:
    test_status8 = 'FAILURE'
print(output8.format(status_code=status_code8, test_status=test_status8,
                     response=response8))


# impression dans un fichier
if os.environ.get('LOG') == '1': 
    filepath = os.path.join('data','api_test.log')
    with open(filepath, 'a') as file:
        file.write(output8)   
