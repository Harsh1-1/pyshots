import requests
import re
from datetime import date

headers = {
"User-Agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0",
"Accept-Language" : "en-US,en;q=0.5",
"Connection" : "keep-alive"}

BASE_URL="https://www1.nseindia.com/products/dynaContent/equities/indices/historical_pepb.jsp?indexName=NIFTY%2050&fromDate="
TAIL_URL="&yield1=pe&yield2=undefined&yield3=undefined&yield4=undefined"

def get_nifty_pe():
    date_string = date.today().strftime("%d-%m-%Y")
    data = requests.get(BASE_URL + date_string + "&toDate=" + date_string + TAIL_URL, headers=headers).text
    # print(BASE_URL + date_string + "&toDate=" + TAIL_URL)
    # print(data)
    regex_string = "\d+\.\d+"
    match_list = re.findall(regex_string, data)
    # print(match_list)
    return match_list[0]

if __name__ == "__main__":
    print(get_nifty_pe()) # This thing can be mailed somewhere as well
