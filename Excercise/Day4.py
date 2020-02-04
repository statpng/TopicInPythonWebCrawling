from fileTostr import fileTostr
from datetime import datetime
from urlTostr import png_urlopen
from bs4 import BeautifulSoup
import re

url = "https://movie.naver.com/movie/point/af/list.nhn"
url = "https://movie.naver.com/"
url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn" # ranking
data = png_urlopen(url)
# data = fileTostr("./html.html")
bs = BeautifulSoup(data, "html.parser")

meta = bs.meta
print(meta)

bs.div
bs.a
bs.p
bs.find("li")

res_findall = bs.find_all("td")
len(res_findall)
for i in res_findall:
    print(i.text)
    print("-"*30)



res_findall

bs.find("li", {"class":"c1"})
#review1 > div > a > div > span.score

bs.select_one("p")
bs.select("p")

bs.select(".list_netizen_score")

[ print(i.text) for i in bs.select(".tit3")]


bs.find_all("tr")
bs.find_all("thead")

bs.select("tbody > tr > .ac")


i=0
for i in bs.select("tbody > tr"):
    if( len(i.find_all("td")) == 4 ):
        j = i.select("td")
        if( str( j[0].img ) == "None" ):
            ranking = ""
        else:
            ranking = j[0].img.get("alt")
            # ranking = re.search( "alt=\"([0-9]+)\"", str( j[0].img ) ).group(1).replace("\n", "")
        print(
            ranking,
            j[1].text.replace("\n", ""),
            j[3].text
            )



len( [i.get("alt") for i in bs.select("tbody > tr > .ac> img")] )
len( [i.text for i in bs.select("tbody > tr > .title")] )
len( [i.text for i in bs.select("tbody > tr > .range")] )

re.findall(bs.select("tbody > tr"), )
[ i.select("td").text for i in bs.select("tbody > tr") ]







url_daum = "https://movie.daum.net/boxoffice/yearly"
url_daum = "https://movie.daum.net/boxoffice/yearly?year=2020"
data = png_urlopen(url_daum)
bs = BeautifulSoup(data, "html.parser")
bs.select("#mArticle ul li .desc_boxthumb strong")
bs.select("#mArticle ul li .desc_boxthumb dd")


nrank = 10;
bs.select("#mArticle ul li span")
res_li = bs.select("#mArticle ul li .desc_boxthumb")
for i in res_li[:nrank]:
    print( i.find("strong").text.replace("\n", ""), "//", i.find("dd").text )



".desc_boxthumb dd"
#mArticle > ul > li:nth-child(21) > div.wrap_movie > div > a







npage = 10
for i in 1:npage:
    url = "https://movie.naver.com/movie/point/af/list.nhn?&page=" + str(i)
    data = png_urlopen(url)
    bs = BeautifulSoup(data, "html.parser")
    bs.select(".report")



# --------------------------------------------------

import requests
url = "https://www.google.com/search?q=%ED%8C%8C%EC%9D%B4%EC%8D%AC&source=lnms&tbm=isch&sa=X&ved=2ahUKEwigjuGPy7TnAhXSc94KHdk-AlgQ_AUoAXoECBIQAw&cshid=1580705647473485&biw=958&bih=910"
data = requests.get(url)
soup = BeautifulSoup(data.text, 'html.parser')
bars = soup.find("div")
bar_names=bars.find_all("h3")
print(bar_names)


bar_list = []
for b in bar_names[0:]:
    result = b.text.strip()
    bar_list.append(result)

bar_list = bar_list[:-9]
len(bar_list)

bar_address = bars.find_all("em")


address_list = []
for a in bar_address[0:]:
    result2 = a.text.strip()
    address_list.append(result2)
print(address_list)

address_list = address_list[:-1]


len(address_list)


minn_bars = pd.DataFrame({'Bars': bar_list,'Address & Contact': address_list})

print(minn_bars)

minn_bars.to_excel("Best Bars in Minneapolis.xlsx", index=False)





for( )