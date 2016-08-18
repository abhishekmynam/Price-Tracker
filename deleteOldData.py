import pymongo
import datetime as dt
import exceptionHandling

DBClient = pymongo.MongoClient()
DB = DBClient.priceTrackerDB

def deleteOldData():
    try:

        activeSearchDate = dt.datetime.now() - dt.timedelta(days=90)
        prodsDel= DB.productSearch.find({"dailySearch.searchDate": {"$gt": activeSearchDate}},{"_id": 0, "prodName": 1})

        prodsList=[]
        for prods in prodsDel:
            names = prods["prodName"]
            DB.productSearch.remove({"prodName":names})

    except Exception as e:
        errorHandle = exceptionHandling.exceptionHandler(e, "deleteOldData")
        errorHandle.logErrorInDB()