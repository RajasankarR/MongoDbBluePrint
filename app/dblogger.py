from app import mongo


def insert(user):    
    print(mongo)
    db=mongo.db
    dbResponse=db.users.insert_one(user)
    x=dbResponse.inserted_id
    print(dbResponse)
    return x