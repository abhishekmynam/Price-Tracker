from insertUpdateProd import insertUpdateProds
from trackUserSearch import updateUserSearch
from prevSearch import getPrevSearch
''''
prod={"name":"iphone11","url":"www.google.com","price":123}
classes = insertUpdateProds(prod)
classes.prodManipulations()
user =123
class2 = updateUserSearch(prod,user)
class2.insertUpdateUserSearch()'''
userId=123
classes = getPrevSearch(userId)
classes.prevSearch()


'''
import pymongo

DBClient = pymongo.MongoClient()

DB=DBClient.practiceDB

result = DB.post.update_one(
    {
        "title":"insert from python"},{ "$set":{
        "description":"first row updating from python",
        "learntBy":"Abhishek Mynam",
        "operations":[{"find":"done","insert":"done","update":"to be learnt"}]
    }}

)
colData=DB.post.find({"title":"insert from python"})
if colData is not None:
    for colData1 in colData:
        print(colData1)
else:
    print("no data")'''