def urlCharset(data1024):
    import re
    encoding = re.search("charset=([\w\-\d]+)\"", str(data1024))

    if encoding :
        encoding = encoding.group(1)
    else:
        encoding = "utf-8"
    
    return encoding


def png_urlopen(url):
    from urllib.request import urlopen
    # url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn"
    res_urlopen = urlopen(url)
    data = res_urlopen.read()
    encoding = urlCharset(data[:1024].decode("ascii", errors="replace"))
    
    data = data.decode(encoding)
    print(data)
    return data

if __name__ == "__main__":
    from urllib.request import urlopen
    url = input("Enter the url that you want to get.")
    res_urlopen = urlopen(url)
    data = res_urlopen.read()
    print(data)