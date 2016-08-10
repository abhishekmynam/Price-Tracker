'''exceptions are handled in all functions/methods and methods in this file are being called
    methonds in this file will show a default error message and store the time and error message in the DB table exceptionsLogged'''

import pymongo
import datetime as dt

DBClient = pymongo.MongoClient()
DB = DBClient.priceTrackerDB

class exceptionHandler(object):

    def __init__(self, exceptions, method):

        self.excep = exceptions
        self.method=method

    def logErrorInDB (self):

        DB.exceptionsLogged.insert_one({"loggedDate":dt.datetime.now(),"exception":self.excep,"methodName":self.method})
