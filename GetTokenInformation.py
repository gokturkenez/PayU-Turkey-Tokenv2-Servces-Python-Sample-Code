'''
Project: PayU Turkey Token v2 Services - Get Token Information  Python3 Sample Code
Author: Göktürk Enez
'''
# Importing required libraries.
import hmac
import hashlib
from urllib.request import Request, urlopen
import time


merchant = 'OPU_TEST'
secretKey = "SECRET_KEY"
token = "ae7200bf363a8ae7059e25fcf714e9b0"
timestamp = str(time.time()).split('.')[0]

hashstring =  merchant +timestamp

signature = hmac.new(secretKey.encode('utf-8'), hashstring.encode('utf-8'), hashlib.sha256).hexdigest()
# https://secure.payu.com.tr/order/token/v2/merchantToken/'+Token+"?merchant="+Merchant+"&timestamp="+TimeStamp+"&signature="+Signature+"&cancelReason="+cancelReason
url = 'https://secure.payu.com.tr/order/token/v2/merchantToken/'+ token +'?merchant='+ merchant +'&timestamp='+ timestamp +'&signature='+signature
print(url)

request = Request(url, method='GET')
response = urlopen(request).read().decode()

print(response)

