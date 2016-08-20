'''search the internet for the product'''
import urllib.request
import json
import exceptionHandling
from insertUpdateProd import insertUpdateProds
from trackUserSearch import updateUserSearch

class internetSearch(object):

   def __init__(self,productName,userId):
       self.productName = productName
       self.userId=userId

   def bestBuyData (self):

       try:
           bestBuyApiKey="dwg5j4bky4vpvcpsvqt7nbuc"
           #self.userId =123
           #self.productName="xbox"
           urlString = "https://api.bestbuy.com/v1/products((search="+self.productName+"))?apiKey="+bestBuyApiKey+"&sort=salePrice.asc&show=salePrice,url&pageSize=1&callback=JSON_CALLBACK&format=json"
           response= urllib.request.urlopen(urlString)
           response_string=response.read().decode("utf-8")
           response_string =response_string.replace("JSON_CALLBACK({","{")
           response_string= response_string.replace("})","}")
           response_json = json.loads(response_string)
           prodPrice = response_json["products"][0]["salePrice"] if (len(response_json["products"]) >0) else 0
           produrl = response_json["products"][0]["url"] if (len(response_json["products"]) >0) else "no data found on internet"
           product ={"name":self.productName,"price":prodPrice,"url":produrl}
           writeToDB = insertUpdateProds(product)
           writeToDB.prodManipulations()
           if (self.userId !=999):
               userSearch = updateUserSearch(product,self.userId)
               userSearch.insertUpdateUserSearch()
           return product

       except Exception as e:
           errorHandle = exceptionHandling.exceptionHandler(e,"bestBuyData")
           errorHandle.logErrorInDB()



