'''sets alert message for the user for a particular product'''

import pymongo
import searchIntenet
import datetime as dt
import exceptionHandling

DBClient = pymongo.MongoClient()
DB = DBClient.priceTrackerDB

class emailAlertForProducts(object):
    def __init__(self, product, userId):
        self.product = product
        self.userId = userId

    def createAlert (self):

        try:
            getProductDetails = searchIntenet.internetSearch(self.product,self.userId)
            searchedData = getProductDetails.bestBuyData()
            userExists = DB.alerts.find({"userId": self.userId}).count()
            if (userExists !=0):
                if (DB.alerts.find({"userId": self.userId, "prods.prodName":self.product}).count() >0):
                    prices= DB.alerts.find_one({"userId": self.userId, "prods": {"$elemMatch": {"prodName": self.product}}},{"_id":0,"prods.minPrice":1})["prods"]
                    lowestPrice= min([price["minPrice"] for price in prices])
                    if (lowestPrice > searchedData["price"]):
                        DB.alerts.update_one({"userId": self.userId,"prods":{"$elemMatch":{"prodName": self.product}}},{"$set": {"prods.$.minPrice":searchedData["price"],"prods.$.date":dt.datetime.now()}})

                else:
                    DB.alerts.update_one({"userId": self.userId},{"$addToSet":{"prods":{"prodName":self.product,"minPrice":searchedData["price"],"date":dt.datetime.now()}}})
            else:
                DB.alerts.insert_one({"userId": self.userId, "prods":[{"prodName":self.product,"minPrice":searchedData["price"],"date":dt.datetime.now()}]})

        except Exception as e:
            errorHandle = exceptionHandling.exceptionHandler(e, "createAlert")
            errorHandle.logErrorInDB()

