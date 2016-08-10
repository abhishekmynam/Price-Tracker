'''search the internet for the product'''
import urllib.request
import json
from insertUpdateProd import insertUpdateProds
from trackUserSearch import updateUserSearch


'''from amazon.api import AmazonAPI

amazon = AmazonAPI(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG)
products = amazon.search(Keywords='kindle', SearchIndex='All')
for i, product in enumerate(products):
    print("{0}. '{1}'".format(i, product.title))
    ("https://api.bestbuy.com/v1/products((search=iphone))?apiKey=dwg5j4bky4vpvcpsvqt7nbuc&sort=salePrice.asc&show=salePrice,url&pageSize=1&callback=JSON_CALLBACK&format=json")

    for bill in data['bills']:
    for organization in bill['organizations']:
        print (organization.get('name'))`

'''


class internetSearch(object):
   def __init__(self,productName,userId):
       self.productName = productName
       self.userId=userId

   def bestBuyData (self):
       bestBuyApiKey="dwg5j4bky4vpvcpsvqt7nbuc"
       user =123
       self.productName="xbox"
       urlString = "https://api.bestbuy.com/v1/products((search="+self.productName+"))?apiKey="+bestBuyApiKey+"&sort=salePrice.asc&show=salePrice,url&pageSize=1&callback=JSON_CALLBACK&format=json"
       response= urllib.request.urlopen(urlString)
       response_string=response.read().decode("utf-8")
       response_string =response_string.replace("JSON_CALLBACK({","{")
       response_string= response_string.replace("})","}")
       response_json = json.loads(response_string)
       prodPrice = response_json["products"][0]["salePrice"]
       produrl = response_json["products"][0]["url"]
       product ={"name":self.productName,"price":prodPrice,"url":produrl}
       writeToDB = insertUpdateProds(product)
       writeToDB.prodManipulations()
       userSearch = updateUserSearch(product,user)
       userSearch.insertUpdateUserSearch()

'''classes = getPrevSearch(user)
dicts=classes.prevSearch()'''



