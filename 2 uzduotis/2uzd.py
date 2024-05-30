from pymongo import MongoClient

def connect():
    client = MongoClient("mongodb+srv://luksasaurelijus1:Auriuks@aurelijus.kuy6knr.mongodb.net/")
    return client

def getData(): # 2nd task
    client = connect()
    db = client['Restaurants']
    collection = db['Data']
    data = collection.find()
    for restaurant in data:
        for key, value in restaurant.items():
            print(f"{key}: {value}")
        print()
    return collection.find()

def fourthTask():
    client = connect()
    db = client['Restaurants']
    collection = db['Data']
    data = collection.find({}, {"restaurant_id": 1, "name": 1, "borough": 1, "cuisine": 1, "_id": 0})
    for restaurant in data:
        for key, value in restaurant.items():
            print(f"{key}: {value}")
        print()
    return collection.find({}, {"restaurant_id": 1, "name": 1, "borough": 1, "cuisine": 1, "_id": 0})

def thirdTask():
    client = connect()
    db = client['Restaurants']
    collection = db['Data']
    data = collection.find({}, {"restaurant_id": 1, "name": 1, "borough": 1, "cuisine": 1, "_id": 1})
    for restaurant in data:
        for key, value in restaurant.items():
            print(f"{key}: {value}")
        print()
    return collection.find({}, {"restaurant_id": 1, "name": 1, "borough": 1, "cuisine": 1, "_id": 1})

def fifthTask():
    client = connect()
    db = client['Restaurants']
    collection = db['Data']
    data = collection.find({"borough": "Bronx"})
    for restaurant in data:
        for key, value in restaurant.items():
            print(f"{key}: {value}")
        print()
    return collection.find({"borough": "Bronx"})


def sixthTask():
    client = connect()
    db = client['Restaurants']
    collection = db['Data']
    pipeline = [
        {"$unwind": "$grades"},
        {"$match": {"grades.score": {"$gte": 80, "$lte": 100}}}
    ]
    data = collection.aggregate(pipeline)
    for restaurant in data:
        for key, value in restaurant.items():
            print(f"{key}: {value}")
        print()
    return collection.aggregate(pipeline)

def seventhTask():
    client = connect()
    db = client['Restaurants']
    collection = db['Data']
    pipeline = [
        {"$project": {"cuisine": 1, "borough": 1, "_id": 0}},
        {"$sort": {"cuisine": 1, "borough": -1}}
    ]
    data = collection.aggregate(pipeline)
    for restaurant in data:
        for key, value in restaurant.items():
            print(f"{key}: {value}")
        print()
    return collection.aggregate(pipeline)

# thirdTask()
# fourthTask()
# fifthTask()
# sixthTask()
# seventhTask()
