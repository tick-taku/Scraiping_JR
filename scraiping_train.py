import requests
from bs4 import BeautifulSoup
import sys
import slackweb

TARGET_URL_JR = "https://trafficinfo.westjr.co.jp/sp/kinki.html"

def scraiping_jr():
    req = requests.get(TARGET_URL_JR)
    soup = BeautifulSoup(req.text, 'lxml')

    parent = soup.find('article', {'id' : 'chiku_unkolist'})

    infoElement = parent.find('ul', {'class' : 'clearfix'})
    information = infoElement.find('li').find('span', {'class':'unko_status'}).find(text=True, recursive=False)

    if information != "遅れの情報はありません。":
        time = parent.find('h1').find(text=True, recursive=False)

        text = [time, information, TARGET_URL_JR]
        message = "\n".join(text)

        slack = slackweb.Slack("")
        slack.notify(text=message, unfurl_links='true')


if __name__ == '__main__':
    scraiping_jr()
