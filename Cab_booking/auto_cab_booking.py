import requests
from getpass import getpass
from bs4 import BeautifulSoup

USERNAME = 'Ad username' # like harsh.s
PASSWORD = getpass('Enter Password:')
COMPANY = 'directi' 
REQUEST_TYPE = "drop"
EMP_ID = "****" # your emp id
SEX = "M"
MOBILE = "**********" #your phone number
LOCATION = "MUNNEKOLALA-SPICE GARDEN"
def select_a_slot(html):
    soup = BeautifulSoup(html,"html.parser")
    option_list = list()
    for item in soup.find_all('option'):
        option_list.append(item.get_text())

    print("Available Slots:")
    for i in range(1,5):
        print(str(i) + ". " + option_list[i])
    choice = int(input("Select a slot:"))
    if choice > 4:
        print("don't mess with me, I am here to help you")
    return option_list[choice]


URL= 'https://blrdrops.internal.directi.com/'

url = "https://blrdrops.internal.directi.com/login/"
client = requests.session()
csrf_token = client.get(url).cookies['csrftoken']
login_data = dict(username=USERNAME,password=PASSWORD,csrfmiddlewaretoken=csrf_token, company=COMPANY)

with client as s:
    p = s.post(url, data = login_data, headers=dict(Referer=url))
    r = s.get(URL)
    slot = select_a_slot(r.text)
    token = s.get(url).cookies['csrftoken']
    payload = {
    "csrfmiddlewaretoken" : token,
    "request" : REQUEST_TYPE,
    "empid" : EMP_ID,
    "sex" : SEX,
    "mobile" : MOBILE,
    "slot" : slot,
    "location" : LOCATION
    }

    book = s.post(URL, data = payload, headers=dict(Referer=URL))
    # print(book.headers,"\n\n\n")
    # print(book.text)
    # print(p.text,"\n\n\n")
    # r = s.get(URL)
    # print(r.text,"\n")

# r = client.post(URL, data=login_data, headers=dict(Referer=url))
# print(r.status_code)
# print(r.text)
