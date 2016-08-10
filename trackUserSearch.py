'''updates the user searches with the current date of search if it was already searched by the user
    else update the document with a new field with prod id and current date'''
import pymongo
import datetime as dt

DBClient = pymongo.MongoClient()
DB = DBClient.priceTrackerDB
import exceptionHandling

class updateUserSearch(object):

    def __init__(self,prod,userId):

        self.product=prod
        self.user=userId

    def isOldUserSearch(self):

        try:
            prodIds=DB.productSearch.find_one({"prodName": self.product["name"]},{"prodId":1,"_id":0})
            prodExist= DB.userSearch.find_one({"userId":self.user},{"prods":{"$elemMatch":{"prodId":prodIds["prodId"]}}})
            oldYes = len(prodExist) - 1
            return oldYes

        except Exception as e:
            errorHandle = exceptionHandling.exceptionHandler(e, "isOldUserSearch")
            errorHandle.logErrorInDB()

    def insertUpdateUserSearch(self):

        try:
            oldYes = updateUserSearch.isOldUserSearch(self)

            if oldYes==1:
                prodIds = DB.productSearch.find_one({"prodName": self.product["name"]}, {"prodId": 1, "_id": 0})
                DB.userSearch.update_one({"userId": self.user, "prods": {"$elemMatch": {"prodId": prodIds["prodId"]}}},
                                         {"$set":{"prods.$.searchDate": dt.datetime.now()}})


            else:
                prodIds = DB.productSearch.find_one({"prodName": self.product["name"]}, {"prodId": 1, "_id": 0})
                DB.userSearch.update_one({"userId": self.user},
                                         {"$addToSet": {"prods": {"prodId": prodIds["prodId"], "searchDate": dt.datetime.now()}}})

        except Exception as e:
            errorHandle = exceptionHandling.exceptionHandler(e, "insertUpdateUserSearch")
            errorHandle.logErrorInDB()