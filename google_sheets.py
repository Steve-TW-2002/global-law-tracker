import pygsheets
import pandas as pd

def write_to_google_sheets(sheet_name, data, creds_path='creds.json'):
    gc = pygsheets.authorize(service_file=creds_path)
    sh = gc.open(sheet_name)
    wks = sh.sheet1
    df = pd.DataFrame(data)
    wks.set_dataframe(df, (1, 1))
