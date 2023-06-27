import pymongo
client = pymongo.MongoClient("mongodb+srv://shikharg20:shikhar12345@cluster0.m3ba7wm.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d = {
    "name" : "shikhar",
    "email" : "shikhar@gmail.com",
    "surname" : "gupta"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)