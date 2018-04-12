'''
Project: PayU Turkey Token v2 Services - Create Token with Ref No Python3 Sample Code
Author: Göktürk Enez
'''
from datetime import datetime
import hmac
import hashlib
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import time
import collections

url = 'https://secure.payu.com.tr/order/token/v2/merchantToken/'

merchant = 'OPU_TEST'
secret = 'SECRET_KEY'
refNo = 57039798
TimeStamp = str(time.time()).split('.')[0]

array = collections.OrderedDict()
array['merchant'] = merchant
array['refNo'] = refNo
array['timestamp'] = TimeStamp

hashstring = ''

for k, v in array.items():
    hashstring += str(v)
print(hashstring)
signature = hmac.new(secret.encode('utf-8'), hashstring.encode('utf-8'), hashlib.sha256).hexdigest()

array['signature'] = signature

print(signature)

request = Request(url, urlencode(array).encode())
response = urlopen(request).read().decode()

print(response)

