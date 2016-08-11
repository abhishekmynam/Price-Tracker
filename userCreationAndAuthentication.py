'''creation of users in the system and password is encoded'''

import pymongo
import datetime as dt
import exceptionHandling

DBClient = pymongo.MongoClient()
DB = DBClient.priceTrackerDB

class createAndAuthUser(object):

    def __init__(self, users):
        self.firstName = users["firstName"]
        self.lastName = users["lastName"]
        self.DOB = users["DOB"]
        self.email = users["email"]
        self.password = users["password"]

    def createUser(self):

        try:
            isExistingUser = DB.userInfo.find({"email": self.email}).count()
            if isExistingUser==0:
                curUserId = DB.userInfo.find_one(sort=[("userId", -1)])+1
                DB.userInfo.insert_one({"userId":curUserId,"firstName":self.firstName,"lastName":self.lastName,"DOB":self.DOB,"email":self.email,
                                "password":self.password})
                message = "user created"
                return message
            else:
                message = "user exists"
                return message

        except Exception as e:
            errorHandle = exceptionHandling.exceptionHandler(e, "createUser")
            errorHandle.logErrorInDB()

    def authUser(self):

        try:
            isExistingUser = DB.userInfo.find({"email": self.email}).count()
            if isExistingUser == 0:
                message="no user exists"
                return message
            else:
                passowrd= DB.userInfo.find_one({"email":self.email},{"password":1})
                if passowrd==self.password:
                    return 1
                else:
                    return 0
        except Exception as e:
            errorHandle = exceptionHandling.exceptionHandler(e, "createUser")
            errorHandle.logErrorInDB()

