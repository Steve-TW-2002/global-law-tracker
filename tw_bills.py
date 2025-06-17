import requests
from bs4 import BeautifulSoup

def fetch_tw_bills():
    url = "https://lis.ly.gov.tw/lghtml/lawstat"
    res = requests.get(url)
    res.encoding = "utf-8"
    soup = BeautifulSoup(res.text, "html.parser")

    rows = soup.select("table tr")[1:]  # 略過表頭
    data = []

    for r in rows:
        cols = r.find_all("td")
        if len(cols) >= 3:
            title = cols[1].text.strip()
            date = cols[2].text.strip()
            data.append({
                "國家": "台灣",
                "法案名稱": title,
                "日期": date
            })

    return data
