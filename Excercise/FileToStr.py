def FileToStr(filename):
    f = open(filename, "r", encoding="utf-8")
    data = f.read()
    f.close()
    return(data)

if __name__ == "__main__" :
    filename = input("Enter your filename.")
    data = fileToStr(filename)
    print(data)