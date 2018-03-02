from json import loads
from json import dumps

import requests
from pandas import DataFrame, read_csv

#G_SHEET_TEMPLATE = 'https://spreadsheets.google.com/feeds/cells/%s/%s/public/values?range=%s&alt=json'
G_SHEET_TEMPLATE = 'https://docs.google.com/spreadsheets/d/%s/gviz/tq?headers=2&sheet=%s&range=%s&tqx=out:csv;'
def get_sheet_url(sp_id, ws, cell_range):
    s = G_SHEET_TEMPLATE % (sp_id, ws, cell_range)
    print(s)
    return (s)

NACAC_SPREADSHEET = {
        'sp_id': '1M6BuL3BQQ2KufJYfpIUjDrnJSSK7zOAY4aNs0dPdKbs',
        'ws': 'Data',
        'cell_range':'A3:G500'
        }

r = requests.get( get_sheet_url(**NACAC_SPREADSHEET) )

df = read_csv(r.text)
print(df)
