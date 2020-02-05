
if FALSE:
    1. C:\Program Files\MariaDB 10.4\data디렉토리에서 my.ini를 메모장으로 열기
    2. my.ini 수정하기
    [mysqld]
    datadir=C:/Program Files/MariaDB 10.4/data
    port=3306
    innodb_buffer_pool_size=497M
    character-set-server=utf8
    collation-server=utf8_general_ci
    init_connect=SET collation_connection=utf8_general_ci
    init_connect=SET NAMES utf8
    [client]
    port=3306
    plugin-dir=C:/Program Files/MariaDB 10.4/lib/plugin
    default-character-set=utf8
    3. maria db의 서비스를 종료하기
    -윈도우 검색에서 서비스를 찾아서 서비스창을 열어서 MariaDB 서비스를 중지->시작



# Reference
if FALSE:
    https://www.adams.ai/



from fileTostr import fileTostr
import json

data = fileTostr("./cdg.json")
dataj = json.loads(data)
print(data)
print(dataj)



for key in dataj.keys():
    print(key)
    print("-"*50)



for key, value in dataj.items():
    print(key, value)
    print("-"*50)

print( dataj.get("item")[0].get("LWCR_ICD_SUMRY") )













import re
import datetime
from urlTostr import png_urlopen
from bs4 import BeautifulSoup


def get_date_range(StartDate, EndDate):

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

    return Date_list

Date_list = get_date_range(20200204, 20200204)
Date = Date_list[0]
Out_daily = []
for Date in Date_list:
    url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=430156241533f1d058c603178cc3ca0e&targetDt=" + str(Date).replace("-", "")
    source = png_urlopen(url)
    js = json.loads(str(source))
    # bs = BeautifulSoup(source, "json.parser")
    # bs = BeautifulSoup(source, "html.parser") # slower
    
    res_dailyBoxOffice = js.get("boxOfficeResult").get("dailyBoxOfficeList")

    for j in res_dailyBoxOffice:
        rank = j.get("rank")
        name = j.get("movieNm")
        openDate = j.get("openDt")
        audienceCount = j.get("audiCnt")
        rank_up_and_down = int( j.get("rankInten") )
        if( rank_up_and_down > 0 ):
            rank_up_and_down2 = "▲" + str(rank_up_and_down)
        elif( rank_up_and_down < 0 ):
            rank_up_and_down2 = "▼" + str(rank_up_and_down)
        elif( rank_up_and_down == 0 ):
            rank_up_and_down2 = "-"
        print( rank + "(" + rank_up_and_down2 + ")" , name , audienceCount , openDate )
        print("-"*50)
        


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
