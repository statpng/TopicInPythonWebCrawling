from fileTostr import fileTostr
from datetime import datetime
from urlTostr import png_urlopen
from bs4 import BeautifulSoup
import re

start_year = 2017
end_year = 2019

if( start_year > end_year ):
    tmp = end_year
    end_year = start_year
    start_year = tmp

rank = []
name = []
for input_year in range(start_year, end_year+1):
    url = "https://movie.daum.net/boxoffice/yearly?year=" + str(input_year)
    print(url)
    
    source = png_urlopen(url)
    bs = BeautifulSoup(source, "html.parser")





    res_li = bs.select("#mArticle ul > li")
    rank_year = []
    name_year = []
    for li_j in res_li:
        tags = li_j.select_one(".desc_boxthumb")
        # if tags:
        try :
            rank_year.append(float(tags.select_one(".emph_grade").text))
        except :
            rank_year.append("ERROR")

        tags = li_j.select_one("strong")
        # if tags:
        try :
            name_year.append(tags.text)
        except :
            name_year.append("ERROR")
        
        
        # tags = li_j.select_one("wrap_link")
        # # if tags:
        # try :
        #     name_year.append(tags.text)
        # except :
        #     name_year.append("ERROR")
            
        # https://movie.daum.net/
        
        #mArticle > ul > li:nth-child(3) > div.info_movie.\#poster > div > span > a.link_desc.\#info

    rank.append(rank_year)
    name.append(name_year)
    print("-"*50)



import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname = "c:/Windows/Fonts/malgun.ttf").get_name()
rc("font", family=font_name)

plt.bar(name[0][3:], rank[0][3:])
plt.show()







---------------------------------------------------------------------------------

import datetime
import re

StartDate = 20120101
EndDate = 20120228

if( StartDate > EndDate ):
    tmp = 0
    tmp = EndDate
    EndDate = StartDate
    StartDate = tmp

# str(StartDate)[0:4]
# re.search("[0-9]{4}", str(StartDate))[0]
res_re_start = re.search("([0-9]{4})([0-9]{2})([0-9]{2})", str(StartDate))
Start_year = int( res_re_start.group(1) )
Start_month = int( res_re_start.group(2) )
Start_day = int( res_re_start.group(3) )
StartDate_date = datetime.date(Start_year, Start_month, Start_day)
StartDate_date = datetime.date(Start_year, Start_month, Start_day)
StartDate_date.strftime("Year: %Y, Month: %m, Day: %d")

res_re_end = re.search("([0-9]{4})([0-9]{2})([0-9]{2})", str(EndDate))
End_year = int( res_re_end.group(1) )
End_month = int( res_re_end.group(2) )
End_day = int( res_re_end.group(3) )
EndDate_date = datetime.date(End_year, End_month, End_day)

Diff_date = EndDate_date - StartDate_date
Date_list = [StartDate_date + datetime.timedelta(days=x) for x in range(Diff_date.days+1)]


Date = Date_list[0]

Out_daily = []
for Date in Date_list:
    url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml?key=430156241533f1d058c603178cc3ca0e&targetDt=" + str(Date).replace("-", "")
    source = png_urlopen(url)
    bs = BeautifulSoup(source, "lxml-xml")
    # bs = BeautifulSoup(source, "html.parser") # slower
    
    res_dayily = bs.select("dailyBoxOffice")
    MovieName_dayily = []
    Rank_dayily = []
    Audience_dayily = []
    for j in res_dayily:
        MovieName_dayily.append( j.select_one("movieNm").text )
        Rank_dayily.append( j.select_one("rank").text )
        Audience_dayily.append( int( j.select_one("audiCnt").text ) )

    Out_daily.append( [MovieName_dayily, Rank_dayily, Audience_dayily] )
    
    
len( Out_daily )
Diff_date.days
    
Out_daily

import pandas as pd
Out_daily[0]

pd.DataFrame({ 
    [i[0] for i in Out_daily],
    [i[0] for i in Out_daily],
    [i[0] for i in Out_daily]
})








url = "http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=2641061000"
source = png_urlopen(url)
bs = BeautifulSoup(source, "lxml-xml")
# bs = BeautifulSoup(source, "html.parser") # slower
print(bs)


CurrentDate_String = bs.select_one("pubDate").text
res_re = re.search("([0-9]{4})년 ([0-9]{2})월 ([0-9]{2})일", CurrentDate_String)
BaseDate_Date = datetime.date( int( res_re.group(1) ), int( res_re.group(2) ), int( res_re.group(3) ) )


for data in bs.select("body data"):
    CurrentDate = BaseDate_Date + datetime.timedelta( int( data.select_one("day").text ) )

    CurrentHour = data.select_one("hour").text
    CurrentTemp = data.select_one("temp").text
    CurrentWeather = data.select_one("wfKor").text
    
    
    print(
        bs.select_one("pubDate").text, 
        CurrentDate.strftime("%Y-%m-%d") + " " +
        CurrentHour + "시 " +
        CurrentTemp + "도 " +
        "(" + CurrentWeather + ")"
    )

bs.select_one("pubDate").text