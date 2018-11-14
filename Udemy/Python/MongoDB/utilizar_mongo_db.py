import pymongo
from pymongo import MongoClient
import datetime

myClient = MongoClient() #instancia a inicialização do MongoDB
db = myClient.mydb #instancia o banco
user = db.users #cria a Collection do banco
user1 = {"username": "Paulo", "password": "mysecurepassword", "favorite_number": 445, "hobbies": ["python", "games"]} #Variavel que armazena o que sera inserido no banco
user_id = users.insert_one(user1).inserted_id #Insere o conteudo de user1 no banco
user1 = [{"username": "Joao", "password": "12345"}, {"username": "Maria", "password": "abcd"}]
user_id = users.insert_many(user1) #Caso a variavel usada para armazenar o que sera inserido no banco seja uma lista, insere varios usarios de uma vez só

user.find({}).count() #Conta quantos documentos existem na coleção -> output -> 3

current_date = datetime.datetime.now()
datetime.datetime(2018, 11, 14, 14, 17, 39, 596264)
old_date = datetime.datetime(2009, 8, 11)
uid = Users.insert_one({"username": "ffie", "date": current_date})
Users.find({"date": {"$gte": old_date}}).count() # output -> 1, GTE = Greater Than, LTE = Less Than, NE = Not Equal

db.users.create_index([("username", pymongo.ASCENDING)]) #Cria um index para o campo Username e o ordena de forma crescente
