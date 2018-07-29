import requests
import bs4
from CConection import Conection
from CJsonFile import JsonFile
import youtube_dl
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import time


class Downloader:

    def __init__(self, _server, _output_dir, _search, _first_page, _last_page):
        self.server = _server
        self.output_dir = _output_dir
        self.search = _search
        self.first_page = _first_page
        self.last_page = _last_page
        self.i = 1
        self.j = 1
        self.Conection = Conection()
        self.jsonfile = JsonFile("data")
        self.list_link = []
        self.ydl_opts = {}

    def download(self):
        self.list_link = self.get_list_link()
        if self.list_link != 0:
            for j in range(0, len(self.list_link)):
                self.jsonfile.json_details_write(len(self.list_link), j, self.list_link[j])
                self.ydl_opts = {'outtmpl': + self.output_dir + '\%(title)s.%(ext)s'}
                with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
                    ydl.download([self.list_link[j]])

    def get_list_link(self):
        self.list_link = []
        if self.Conection.get_status():
            # Test witch server will scan
            if self.server == 'xvideos':
                for self.i in range(self.first_page, self.last_page):
                    response = requests.get(str('https://www.xvideos.com/?k=' + self.search + '&p=' + str(self.i)))
                    soup = bs4.BeautifulSoup(response.text, "html.parser")
                    for div in soup.find_all(class_='thumb'):  # thumb é a classe de div que contem os links
                        link = "https://www.xvideos.com" + str(div.find('a')['href'])
                        self.list_link.append(link)
            elif self.server == 'eporner':
                for self.i in range(self.first_page, self.last_page):
                    response = requests.get(
                        str('https://www.eporner.com/search/' + self.search + '/' + str(self.i)) + '/')
                    soup = bs4.BeautifulSoup(response.text, "html.parser")
                    for div in soup.find_all(class_='mb'):  # mb é a classe de div que contem os links
                        link = "https://www.eporner.com" + str(div.find('a')['href'])
                        self.list_link.append(link)
            elif self.server == 'gotporn':
                for self.i in range(self.first_page, self.last_page):
                    response = requests.get(
                        str('https://www.gotporn.com/results?search_query=' + self.search + '&page=' + str(self.i)))
                    soup = bs4.BeautifulSoup(response.text, "html.parser")
                    for li in soup.find_all(class_='video-item'):  # thumb é a classe de div que contem os links
                        link = str(li.find('a')['href'])
                        self.list_link.append(link)
            elif self.server == 'porn':
                for self.i in range(self.first_page, self.last_page):
                    response = requests.get(
                        str('https://www.porn.com/videos/search?q=' + self.search + '&p=' + str(self.i)))
                    soup = bs4.BeautifulSoup(response.text, "html.parser")
                    for div in soup.find_all(class_='thumb'):  # thumb é a classe de div que contem os links
                        link = "https://www.porn.com/videos" + str(div.find('a')['href'])
                        self.list_link.append(link)
            elif self.server == 'pornhd':
                for self.i in range(self.first_page, self.last_page):
                    response = requests.get(
                        str('https://www.pornhd.com/popular/' + self.search + '?page=' + str(self.i)))
                    soup = bs4.BeautifulSoup(response.text, "html.parser")
                    for div in soup.find_all(
                            class_='thumb videoThumb popTrigger'):  # thumb videoThumb popTrigger é a classe de div que contem os links
                        link = "https://www.pornhd.com" + str(div['href'])
                        self.list_link.append(link)
            elif self.server == 'pornhub':
                for self.i in range(self.first_page, self.last_page):
                    response = requests.get(
                        str('https://pt.pornhub.com/video/search?search=' + self.search + '&page=' + str(self.i)))
                    soup = bs4.BeautifulSoup(response.text, "html.parser")
                    for div in soup.find_all(
                            class_='img fade fadeUp videoPreviewBg'):  # img fade videoPreviewBg fadeUp é a classe de div que contem os links
                        link = "https://pt.pornhub.com" + str(div.find('a')['href'])
                        self.list_link.append(link)
            elif self.server == 'redtube':
                for self.i in range(self.first_page, self.last_page):
                    response = requests.get(
                        str('https://www.redtube.com/?search=' + self.search + '&page=' + str(self.i)))
                    soup = bs4.BeautifulSoup(response.text, "html.parser")
                    for span in soup.find_all(
                            class_='video_thumb_wrap'):  # video-box four-column video_block_wrapper é a classe de div que contem os links
                        link = "https://www.redtube.com" + str(span.find('a')['href'])
                        self.list_link.append(link)
            elif self.server == 'spankbang':
                for self.i in range(self.first_page, self.last_page):
                    response = requests.get(str('https://br.spankbang.com/s/' + self.search + '/' + str(self.i)) + "/")
                    soup = bs4.BeautifulSoup(response.text, "html.parser")
                    for div in soup.find_all(class_='video-item'):  # video-item é a classe de div que contém os links
                        link = "https://br.spankbang.com" + str(div.find('a')['href'])
                        self.list_link.append(link)
            elif self.server == 'xhamster':
                for self.i in range(self.first_page, self.last_page):
                    response = requests.get(
                        str('https://pt.xhamster.com/search?q=' + self.search + '&p=' + str(self.i)))
                    soup = bs4.BeautifulSoup(response.text, "html.parser")
                    for div in soup.find_all(
                            class_='video-thumb-info'):  # video-thumb-info é a classe de div que contem os links
                        link = str(div.find('a')['href'])
                        self.list_link.append(link)
            elif self.server == 'youporn':
                for self.i in range(self.first_page, self.last_page):
                    response = requests.get(
                        str('https://www.youporn.com/search/?query=' + self.search + '&page=' + str(self.i)))
                    soup = bs4.BeautifulSoup(response.text, "html.parser")
                    for div in soup.find_all(
                            class_='video-box four-column video_block_wrapper'):  # video-box four-column video_block_wrapper é a classe de div que contem os links
                        link = "https://www.youporn.com" + str(div.find('a')['href'])
                        self.list_link.append(link)
                return self.list_link
            elif self.server == 'xnxx':
                for self.i in range(self.first_page, self.last_page):
                    response = requests.get(
                        str('https://www.xnxx.com/search/' + self.search + '/' + str(self.i)) + '/')
                    soup = bs4.BeautifulSoup(response.text, "html.parser")
                    for div in soup.find_all(class_='thumb'):  # thumb é a classe de div que contem os links
                        link = "https://www.xnxx.com" + str(div.find('a')['href'])
                        self.list_link.append(link)
                return self.list_link
            elif self.server == 'beeg':
                url = str('https://www.beeg.com/tag/' + self.search)
                options = webdriver.ChromeOptions()
                options.add_argument('--ignore-certificate-errors')
                options.add_argument("--test-type")
                options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                driver = webdriver.Chrome(chrome_options=options)
                try:
                    driver.get(url)
                    print("Aguardando carregamento em 20s ...")
                    time.sleep(20)
                    html = driver.page_source
                    soup = bs4.BeautifulSoup(html, "html.parser")
                    for div in soup.find_all(class_='thumb-unit'):  # thumb-unit é a classe de div que contem os links
                        link = "https://beeg.com" + str(div.find('a')['href'])
                        self.list_link.append(link)
                    return self.list_link
                except TimeoutException:
                    print("Tempo de carregamento esgotado!")
                except:
                    os.system("cls")
                    print("Tempo limite para o carregamento da página esgotado.")
                    print("Tente novamente!")
            else:
                print("Server not found.")
                self.list_link = []
            return self.list_link
        else:
            print("No conection... ")
            return 0
