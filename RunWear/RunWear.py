import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta


def hour_rounder(t):
    # Rounds to nearest hour by adding a timedelta hour if minute >= 30
    return (t.replace(second=0, microsecond=0, minute=0, hour=t.hour)
               +timedelta(hours=t.minute//30))


def runwearnow():
    x = 0
    clothes_list = []
    phrs = ''

    now = datetime.now()
    current_round_time = hour_rounder(now).strftime("%H")
    req_hour = current_round_time

    url = 'https://dressmyrun.com/place/59.32944,18.06861?hour=' + req_hour + '&date=' \
          + datetime.today().strftime('%Y-%m-%d')
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    clothes = soup.find_all('h3', class_='sc-AxgMl sc-fzoJMP sc-fzpkqZ sc-fznYue bkzNQG')

    for piece in clothes:
        if piece.text != 'ID':
            clothes_list.append(piece.text)

    for y in clothes_list:
        x += 1
        if x < len(clothes_list):
            phrs += y + ', '
        else:
            phrs += 'and ' + y

    runwearnow.phrase = phrs


def runwearlater(req_day,req_hour):
    x = 0
    clothes_list = []
    phrs = ''

    url = 'https://dressmyrun.com/place/59.32944,18.06861?hour=' + req_hour + '&date=' \
          + req_day
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    clothes = soup.find_all('h3', class_='sc-AxgMl sc-fzoJMP sc-fzpkqZ sc-fznYue bkzNQG')

    for piece in clothes:
        if piece.text != 'ID':
            clothes_list.append(piece.text)

    for y in clothes_list:
        x += 1
        if x < len(clothes_list):
            phrs += y + ', '
        else:
            phrs += 'and ' + y

    runwearlater.phrase = phrs
