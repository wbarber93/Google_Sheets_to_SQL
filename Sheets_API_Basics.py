import gspread
import mysql.connector
from oauth2client.service_account import ServiceAccountCredentials

# initialize variables for gspread

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
         
creds = ServiceAccountCredentials.from_json_keyfile_name("leafy-metrics-300714-9548969a14cf.json", scope)
         
client = gspread.authorize(creds)
ss = client.open("Total Sales Sheet")

ws = ss.worksheet('Sheet1')

print(ws.get()) 


#Isolates film table data

datalist = []

for x in ws.get():
    for val in x:
        data = (val.strip())
        if data == '': continue
        datalist.append(data)

#print(datalist)

y = 12

order_date=[]
name_of_client=[]
film_type=[]
gbp_price=[]
usd_price=[]
salesperson=[]


order_date.append(datalist[y])
name_of_client.append(datalist[y+1])
film_type.append(datalist[y+3])
gbp_price.append(datalist[y+4])
usd_price.append(datalist[y+5])
salesperson.append(datalist [y+6])
y+11

print(name_of_client) 
print(datalist[1])