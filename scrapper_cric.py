import requests
from bs4 import BeautifulSoup

result=requests.get("https://www.cricbuzz.com/cricket-match/live-scores")
soup = BeautifulSoup(result.content,'html.parser')
seriesList = soup.find_all("div","cb-lv-main")

for series in seriesList:
    seriesTitle = series.find("h2","cb-lv-scr-mtch-hdr")
    if seriesTitle!=None:
        print("\n> "+seriesTitle.string+"\n")
    seriesTeam =  series.find("h3","cb-lv-scr-mtch-hdr")
    seriesType = series.find_all("span","text-gray")
    print("\t "+seriesTeam.string+seriesType[0].string+seriesType[1].string)
    liveTst = series.find("div","cb-scr-wll-chvrn")
    if liveTst==None:
        print("\t Match not started yet.")
    else:
        print("\t"+liveTst.get_text())
    print("\n")
        



