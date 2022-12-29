import requests
from decouple import config

# set the custom headers
header_data = {'T1':'Add_First_Header', 'T2':'Add_Second_Header', 'T3':'Add_Third_Header', 'T4':'Add_Fourth_Header', 'T6':'Add_Sixth_Header'}
# get the custom header data
response = requests.get(config('DOMAIN') + "/students", headers=header_data)
# display the response headers
print("Display headers", response.request.headers)
