import requests


tax_url = 'http://127.0.0.1:19863/TaxCardHttps/tax_openCard'
tax_headers = {"Content-type":"application/json",'token':'839mkHas0we093s262Wfmsa+fds23ia13dfkRidMNo92Ul01266qasfDn636OoZ99xzZ5550ToMyHoo396332LxvIEbs520CxZ0109wLf'}
tax_data = 'inputJson={\'certPassWord\':\'12345678\',\'uploadInvoiceAuto\':0}'
tax_result = requests.post(url= tax_url,headers = tax_headers,data=tax_data)

print(tax_result.text)
