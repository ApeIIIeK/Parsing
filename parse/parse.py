import requests
from bs4 import BeautifulSoup
class MyDownload:
    def __init__(self, urls):
        self.urls = urls
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.urls) <= self.current_index:
            raise StopIteration
        else:
            url = self.urls[self.current_index]
            data = requests.get(url)

            filename = f"data_{self.current_index}" + url.split('/')[2] + ".txt"

            if data.status_code == 200:
                with open("data/" + filename, 'w', encoding='utf-8') as file:
                    file.write(data.text)
            self.current_index += 1
            return self.current_index

# urls = ["https://ru.wikipedia.org/wiki/%D0%93%D1%80%D0%B0%D0%B2%D0%B8%D1%86%D0%B0%D0%BF%D0%BF%D0%B0","https://ru.wikipedia.org/wiki/%D0%9B%D0%B5%D1%82%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9_%D0%B0%D0%BF%D0%BF%D0%B0%D1%80%D0%B0%D1%82","https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%BA%D0%BE%D0%BD_%D0%A5%D0%B0%D0%B1%D0%B1%D0%BB%D0%B0"]
# list_page = MyDownload(urls)
# for i in list_page:
#     print(f"Download.. {i}")

def my_parse(filename):
    with open(filename, 'r', encoding= 'utf=8') as file:
        data = file.read() 
    data = BeautifulSoup(data, 'html.parser')
    title = data.find("h1", id = "firstHeading")
    print("Заголовок страницы: ", title.text)

my_parse("datadata_0ru.wikipedia.org.txt")
my_parse("datadata_1ru.wikipedia.org.txt")
my_parse("datadata_2ru.wikipedia.org.txt")