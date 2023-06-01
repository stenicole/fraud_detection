import os
import requests
import time

# définition de l'adresse de l'API
api_address = 'fastapi'
# port de l'API
api_port = 8000

# attente pour donner le temps au container fastapi de se lancer
#time.sleep(5)
# requête
r1 = requests.get(url='http://{address}:{port}/permissions'.format(address=api_address, port=api_port), auth=('Alice', 'wonderland'))


output1 = '''
============================
    Authentication test
============================

request done at "/permissions"
| username="Alice"
| password="wonderland"


expected result = 200
actual restult = {status_code}

==>  {test_status}

==> {response}

'''


# statut de la requête
status_code1 = r1.status_code
response1 = r1.text

# affichage des résultats
if status_code1 == 200:
    test_status1 = 'SUCCESS'
else:
    test_status1 = 'FAILURE'
print(output1.format(status_code=status_code1, test_status=test_status1,
                     response=response1))



# impression dans un fichier
if os.environ.get('LOG') == '1': 
    filepath = os.path.join('data','api_test.log')
    with open(filepath, 'a') as file:
        file.write(output1)
       

r2 = requests.get(url='http://{address}:{port}/permissions'.format(address=api_address, port=api_port), auth=('Bob', 'builder'))


output2 = '''
============================
    Authentication test
============================

request done at "/permissions"
| username="Bob"
| password="builder"

expected result = 200
actual restult = {status_code}

==>  {test_status}

==>{response}

'''


# statut de la requête
status_code2 = r2.status_code
response2 = r2.text

# affichage des résultats
if status_code2 == 200:
    test_status2 = 'SUCCESS'
else:
    test_status2 = 'FAILURE'
print(output2.format(status_code=status_code2, test_status=test_status2,
                     response=response2))


# impression dans un fichier
if os.environ.get('LOG') == '1': 
    filepath = os.path.join('data','api_test.log')
    with open(filepath, 'a') as file:
        file.write(output2)
        

r3 = requests.get(url='http://{address}:{port}/permissions'.format(address=api_address, port=api_port), auth=('Alice', 'clementine'))


output3 = '''
============================
    Authentication test
============================

request done at "/permissions"
| username="Alice"
| password="clementine"

expected result = 401
actual restult = {status_code}

==>  {test_status}

'''


# statut de la requête
status_code3 = r3.status_code


# affichage des résultats
if status_code3 == 200:
    test_status3 = 'SUCCESS'
else:
    test_status3 = 'FAILURE'
print(output3.format(status_code=status_code3, test_status=test_status3))

# impression dans un fichier
if os.environ.get('LOG') == '1': 
    filepath = os.path.join('data','api_test.log')
    with open(filepath, 'a') as file:
        file.write(output3)
        
r4 = requests.get(url='http://{address}:{port}/permissions'.format(address=api_address, port=api_port), auth=('Bob', 'mandarine'))


output4 = '''
============================
    Authentication test
============================

request done at "/permissions"
| username="Bob"
| password="mandarine"

expected result = 401
actual restult = {status_code}

==>  {test_status}

'''

# statut de la requête
status_code4 = r4.status_code

# affichage des résultats
if status_code4 == 200:
    test_status4 = 'SUCCESS'
else:
    test_status4 = 'FAILURE'
print(output4.format(status_code=status_code4, test_status=test_status4))

# impression dans un fichier
if os.environ.get('LOG') == '1': 
    filepath = os.path.join('data','api_test.log')
    with open(filepath, 'a') as file:
        file.write(output4)



