'''search the internet for the product'''
import urllib.request
import json
from insertUpdateProd import insertUpdateProds
from trackUserSearch import updateUserSearch
from prevSearch import getPrevSearch



'''from amazon.api import AmazonAPI
AMAZON_ACCESS_KEY="AKIAIWOIGWKW3HFXWP2Q"
AMAZON_SECRET_KEY="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"
AMAZON_ASSOC_TAG= "abhiassocaws-20"
amazon = AmazonAPI(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG)
products = amazon.search(Keywords='kindle', SearchIndex='All')
for i, product in enumerate(products):
    print("{0}. '{1}'".format(i, product.title))
    ("https://api.bestbuy.com/v1/products((search=iphone))?apiKey=dwg5j4bky4vpvcpsvqt7nbuc&sort=salePrice.asc&show=salePrice,url&pageSize=1&callback=JSON_CALLBACK&format=json")

    for bill in data['bills']:
    for organization in bill['organizations']:
        print (organization.get('name'))`

'''



bestBuyApiKey="dwg5j4bky4vpvcpsvqt7nbuc"
productName="iphone"
urlString = "https://api.bestbuy.com/v1/products((search="+productName+"))?apiKey="+bestBuyApiKey+"&sort=salePrice.asc&show=salePrice,url&pageSize=1&callback=JSON_CALLBACK&format=json"
response= urllib.request.urlopen(urlString)
response_string=response.read().decode("utf-8")
response_string =response_string.replace("JSON_CALLBACK({","{")
response_string= response_string.replace("})","}")
response_json = json.loads(response_string)
prodPrice = response_json["products"][0]["salePrice"]
produrl = response_json["products"][0]["url"]
product ={"name":productName,"price":prodPrice,"url":produrl}


user =123
writeToDB = insertUpdateProds(product)
writeToDB.prodManipulations()
class2 = updateUserSearch(product,user)
class2.insertUpdateUserSearch()
classes = getPrevSearch(user)
classes.prevSearch()


