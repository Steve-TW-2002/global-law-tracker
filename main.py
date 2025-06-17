from tw_bills import fetch_tw_bills
from translate import translate_laws
from google_sheets import write_to_google_sheets

import os

def write_creds_from_secret():
    creds = os.environ.get("CREDS_JSON")
    if creds:
        with open("creds.json", "w", encoding="utf-8") as f:
            f.write(creds)
    else:
        raise ValueError("CREDS_JSON not found in environment variables")

def main():
    write_creds_from_secret()
    data = fetch_tw_bills()
    data = translate_laws(data)
    write_to_google_sheets("global-law-tracker", data)

if __name__ == "__main__":
    main()
