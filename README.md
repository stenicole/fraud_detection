# fraud_detection
Deployment project of a Machine Learning (ML) models to detect fraud payments
1. API 
1.a Unzip the directory p2_snicole_2 
You should now have a directory structure like:
.
├── app
│   ├── __init__.py
│   └── main.py
├── Dockerfile
└── requirements.txt

1.b checking the "main.py" file
The identifiers and the passwords you can use to see the authorizations and make prediction are listed
You can also see the roads. The documentation can be viewed thanks this link :  http://localhost:8000/redoc

1.b Lauching the API :
uvicorn app.main:api

1.c Open this endpoint in your navigator :
http://localhost:8000/docs


2.Docker
2.a Copy and paste the file "script.sh"
2.b In linux type : chmod +x script.sh
2.c Launch this file with linux in order to build all the containers, so type : ./sript.sh
2.d In order do launch theses container you use docker-compose, type : docker-compose up
