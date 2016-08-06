'''fetch the data from DB to display on the previous search window'''
import pymongo
import datetime as dt

DBClient = pymongo.MongoClient()
DB = DBClient.priceTrackerDB

class getPrevSearch(object):

    def __init__(self, userId, rows = 1000):
        self.userId =userId
        self.rows = rows

    def userProdList (self):
        prods=DB.userSearch.find_one({"userId":self.userId},{"_id":0,"prods":1})["prods"]
        return prods

    def prevSearch(self):
        prodList = getPrevSearch.userProdList(self)
        #activeSearchDate= dt.datetime.today() - dt.timedelta(days=90)
        prevProds=[]
        for prod in prodList:
            prevProds.append(DB.productSearch.find_one
                             ({"prodId":prod["prodId"],"dailySearch.searchDate":{"$gt":prod["searchDate"] }},{"_id":0,"prodName":1,"dailySearch.minPrice":1,"dailySearch.url":1,"dailySearch.searchDate":1}))


        prevProdstemp=prevProds

