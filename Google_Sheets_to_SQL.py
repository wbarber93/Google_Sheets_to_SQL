user = "*******"
password = "******"
#host = hostname
#database = database_schema

import gspread
import mysql.connector
from oauth2client.service_account import ServiceAccountCredentials


# initialize variables for gspread

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
         
creds = ServiceAccountCredentials.from_json_keyfile_name("leafy-metrics-300714-9548969a14cf.json", scope)
         
client = gspread.authorize(creds)


# define method to pull data from spreadsheet

def GetSpreadsheetData(sheetName, worksheetIndex):
    sheet = client.open(sheetName).get_worksheet(worksheetIndex)
    return sheet.get_all_values()[1:]