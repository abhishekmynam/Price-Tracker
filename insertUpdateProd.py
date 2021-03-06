'''class to insert data into productSearch collection when the current search is first time
    else updates the already existing record with new set of values'''

import pymongo
import datetime as dt
import exceptionHandling

DBClient = pymongo.MongoClient()
DB = DBClient.priceTrackerDB

class insertUpdateProds(object):

    def __init__(self,prod):

        self.product=prod

    def checkRecords(self):

        try:
            colData = DB.productSearch.find({"prodName": self.product["name"]}).count()
            return colData

        except Exception as e:
            errorHandle = exceptionHandling.exceptionHandler(e, "checkRecords")
            errorHandle.logErrorInDB()

    def prodManipulations(self):

        try:
            colData = insertUpdateProds.checkRecords(self)

            if colData == 0:
                maxProdId = DB.productSearch.find_one(sort=[("prodId", -1)])
                nextProdId=maxProdId["prodId"] +1
                DB.productSearch.insert_one({"prodId": nextProdId,"prodName":self.product["name"],"firstSearchDate":dt.datetime.now(),
                                    "dailySearch":[{"searchDate":dt.datetime.now(),"url":self.product["url"],"minPrice":self.product["price"]}]})
            else:
                prodName = DB.productSearch.update_one({"prodName":self.product["name"]},
                                                       {"$addToSet":{"dailySearch":{"searchDate":dt.datetime.now(),"url":self.product["url"],"minPrice":self.product["price"]}}})

        except Exception as e:
            errorHandle = exceptionHandling.exceptionHandler(e, "prodManipulations")
            errorHandle.logErrorInDB()