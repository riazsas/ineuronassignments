import pymongo

client = pymongo.MongoClient("mongodb+srv://riazsadique96:<Inf29nity!>@cluster0.gnzto.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)


d = {
    "name":"sudanshu",
      "email" :"sudhanshu@ineuron.ai",
      "surname" : "kumar"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)


