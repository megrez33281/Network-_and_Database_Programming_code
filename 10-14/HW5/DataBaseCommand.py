from pymongo import MongoClient
import pymongo
import pprint
import re

client = MongoClient(host="localhost", port=27017)
db = client.HW5


def getTable(dest):
    if re.match('[sS][tT][uU][dD][eE][nN][tT]', dest):
        return db.STUDENT
    elif re.match('[cC][oO][uU][rR][sS][eE]', dest):
        return db.COURSE
    elif re.match('[eE][nN][rR][oO][lL][lL][mM][eE][nN][tT]', dest):
        return db.Enrollment
    elif re.match('[iI][mM][aA][gG][eE]', dest):
        return db.image
    else:
        print("No such Table!")
        return NULL

def renewTable(table):
    #觸發更新
    for data in table.find():
        break
    
def InsertData(dest,  field):
    table = getTable(dest)
    field_id = table.insert_one(field).inserted_id
    renewTable(table)
    return field_id
    
def UpdateData(dest, target, newContent):
    table = getTable(dest)
    table.update_one(target, { '$set': newContent })
    renewTable(table)

def QueryData(dest, condition):
    table = getTable(dest)
    data_list = []
    for data in table.find(condition):
        data_list.append(data)
    return data_list
        

def DeleteData(dest):
    table = getTable(dest)
    table.delete_many({})
    renewTable(table)
    
def MakeIndex(dest, indexs=[], unique_indexs=[]):
    table = getTable(dest)
    if len(indexs) > 0:
        for index in indexs:
            table.create_index([(index, pymongo.ASCENDING)])

    if len(unique_indexs) > 0:
        unique_tuples = []
        for index in unique_indexs:
            unique_tuples.append((index, pymongo.ASCENDING))
        table.create_index(unique_tuples, unique=True)
    renewTable(table)

def getIndex(dest):
    table = getTable(dest)
    indexs = table.list_indexes()
    lists = []
    for index in indexs:
        lists.append(lists)
    if len(lists) > 0:
        return 1
    return 0
if __name__ == '__main__':
    DeleteData("STUDENT")
    