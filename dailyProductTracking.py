''' this is a scheduled job that gathers information from internet on a daily basis'''

import searchIntenet
import datetime
import pymongo
import exceptionHandling


DBClient = pymongo.MongoClient()
DB = DBClient.priceTrackerDB

def dailyProdSearch():
    try:
        prodData = DB.productSearch.find()
        prodsList=[]

        for prods in prodData:
            names = prods["prodName"]
            prodsList.append(names)

        for prods in prodsList:
            search=searchIntenet.internetSearch(prods,999)
            searchedData = search.bestBuyData()

    except Exception as e:
        errorHandle = exceptionHandling.exceptionHandler(e, "dailyProdSearch")
        errorHandle.logErrorInDB()