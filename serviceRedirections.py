'''this receives all services'''

import exceptionHandling
import insertUpdateProd
import prevSearch
import searchIntenet
import trackUserSearch
import userCreationAndAuthentication

class serviceUsage(object):
    def __init__(self, servObject):
        self.servObj = servObject

    def createUserService(self):
        callServ = userCreationAndAuthentication.createAndAuthUser(self.servObj)
        isUserAdded = callServ.createUser()

    def authUserService(self):
        callServ = userCreationAndAuthentication.createAndAuthUser(self)