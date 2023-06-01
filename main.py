from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

import json
import secrets



api = FastAPI(
    title='My exam_API'
)

security = HTTPBasic()

# just for testing, it's unsafe !!!
users_db = [
    {
       
        'username': 'Alice',
        'password' : 'wonderland',
        'v1'       : 1,
        'v2'       : 1
        
    },
    {
        
        'username': 'Bob',
        'password' : 'builder',
        'v1'       :  1,
        'v2'       :  0
    },
    {
        
        'username': 'Clementine',
        'password' : 'machine',
        'v1'       :  0,
        'v2'       :  1
    }
]



@api.get("/status")        
async def test():
    return 1

@api.get('/permissions')
async def permissions(credentials: HTTPBasicCredentials = Depends(security)):
   # parcours du fichier data.json
    for user in users_db:
       # vérification de l'username et du password
       if secrets.compare_digest(credentials.username, user['username']) == True and secrets.compare_digest(credentials.password, user['password']) == True:
            # si l'username et le mot de passe sont corrects la liste des
            # permissions est renvoyée
            return user
                
   # dans le cas où le user n'est pas trouvé
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect email or password",
        headers={"WWW-Authenticate": "Basic"},
    )  

#création du dictionnaire des scores des modeles entraînés et testés
tf = open("app/Modele/Perf/score_ML.json", "r")
score_dic = json.load(tf)

# création de vue des clés du dictionnaire des scores
list_model=score_dic.keys() 

# création d'une route pour obtenir la liste des modeles
@api.get('/modele')
async def get_modele_list():
    """Return list of models
    """
    return list(list_model)

# création d'une route pour obtenir le score d'un modele
@api.get('/score/{modele:str}')
async def get_score_ML(modele):
    """Return score of the selected model
    """
    try:
        return {modele : score_dic[modele]}
    except  KeyError:
        return {}


from typing import Optional
from pydantic import BaseModel
import pandas as pd
from joblib import load


class predict(BaseModel):
     """A predict has to respect this pattern.
       The champs purchase_value, age, source_Ads
       source_Direct, source_SEO, browser_Chrome,
       browser_FireFox, browser_IE,
       browser_Opera, browser_Safari,
       sex_F, sex_M,
     """
     purchase_value        : int
     age                   : int
     hour                  : int
     day                   : int
     month                 : int
     source_Ads            : int
     source_Direct         : int
     source_SEO            : int
     browser_Chrome        : int
     browser_FireFox       : int
     browser_IE            : int
     browser_Opera         : int
     browser_Safari        : int
     sex_F                 : int
     sex_M                 : int
     

# chargement des modèles entraînés
LogReg = load('app/Modele/LogReg.pckl')
KNN = load('app/Modele/KNN.pckl')
SVC = load('app/Modele/SVC.pckl')
DTC = load('app/Modele/DTC_2.pckl')
RFC = load('app/Modele/RFC_2.pckl')
BC = load('app/Modele/BC_2.pckl')
GBC = load('app/Modele/GBC.pckl')
scaler_2 = load('app/Modele/scaler_2.pckl')

# création d'une route pour prédiction
@api.post('/v1/predict/modele')
async def prediction(test_pred : predict, credentials: HTTPBasicCredentials = Depends(security) ):
# parcours du fichier data.json
    for user in users_db:
       # vérification de l'username et du password
       if secrets.compare_digest(credentials.username, user['username']) == True and secrets.compare_digest(credentials.password, user['password']) == True:
            # si l'username et le mot de passe sont corrects
            #  et si le user a accès au modèle v1  
            if user['v1'] == 1 :
 
                 try:
                    dic = {"purchase_value"                             : [test_pred.purchase_value],
                            "age"                                       : [test_pred.age],
                            "hour"                                      : [test_pred.hour],
                            "day"                                       : [test_pred.day],
                            "month"                                     : [test_pred.month],
                            "source_Ads"                                : [test_pred.source_Ads],
                            "source_Direct"                             : [test_pred.source_Direct],
                            "source_SEO"                                : [test_pred.source_SEO],
                            "browser_Chrome"                            : [test_pred.browser_Chrome],
                            "browser_FireFox"                           : [test_pred.browser_FireFox],
                            "browser_IE"                                : [test_pred.browser_IE],
                            "browser_Opera"                             : [test_pred.browser_Opera],
                            "browser_Safari"                            : [test_pred.browser_Safari],
                            "sex_F"                                     : [test_pred.sex_F],
                            "sex_M"                                     : [test_pred.sex_M]
                        }
                  
                       
                    db = pd.DataFrame([test_pred.dict()])
                    X_norm = scaler_2.transform(db) 
                    y_res = int(BC.predict(X_norm))
                    return{"resultats":y_res}
                 except:
                    error = "calcul impossible"
                    return error
                
    # dans le cas où le user n'est pas trouvé
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect email or password",
        headers={"WWW-Authenticate": "Basic"},
        )  
   

# création d'une route pour prédiction
@api.post('/v2/predict/modele')
async def prediction(test_pred : predict, credentials: HTTPBasicCredentials = Depends(security) ):
# parcours du fichier data.json
    for user in users_db:
       # vérification de l'username et du password
       if secrets.compare_digest(credentials.username, user['username']) == True and secrets.compare_digest(credentials.password, user['password']) == True:
            # si l'username et le mot de passe sont corrects la liste des
            # et si le user a accès au modèle v2 
            if user['v2'] == 1 :
   
                 try:
                    dic = {"purchase_value"                             : [test_pred.purchase_value],
                            "age"                                       : [test_pred.age],
                            "hour"                                      : [test_pred.hour],
                            "day"                                       : [test_pred.day],
                            "month"                                     : [test_pred.month],
                            "source_Ads"                                : [test_pred.source_Ads],
                            "source_Direct"                             : [test_pred.source_Direct],
                            "source_SEO"                                : [test_pred.source_SEO],
                            "browser_Chrome"                            : [test_pred.browser_Chrome],
                            "browser_FireFox"                           : [test_pred.browser_FireFox],
                            "browser_IE"                                : [test_pred.browser_IE],
                            "browser_Opera"                             : [test_pred.browser_Opera],
                            "browser_Safari"                            : [test_pred.browser_Safari],
                            "sex_F"                                     : [test_pred.sex_F],
                            "sex_M"                                     : [test_pred.sex_M]
                        }
                  
                       
                    db = pd.DataFrame([test_pred.dict()])
                    X_norm = scaler_2.transform(db) 
                    y_res = int(RFC.predict(X_norm))
                    return{"resultats":y_res}
                 except:
                    error = "calcul impossible"
                    return error
                
    # dans le cas où le user n'est pas trouvé
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect email or password",
        headers={"WWW-Authenticate": "Basic"},
        )  

