import requests
import bs4
import youtube_dl
from CConection import Conection
from CJsonFile import JsonFile
import io


class DownloaderXHamster:

    def __init__(self, _output_dir, _search, _first_page, _last_page):
        self.output_dir = _output_dir
        self.search = _search
        self.first_page = _first_page
        self.last_page = _last_page
        self.i = 1
        self.j = 1
        self.Conection = Conection()
        self.jsonfile = JsonFile("data")
        self.list_link = []

    def download(self):
        self.list_link = self.get_list_link()
        if self.list_link != 0:
            for j in range(0, len(self.get_list_link())):
                self.jsonfile.json_details_write(len(self.list_link), j, self.list_link[j])
                self.ydl_opts = {'outtmpl': self.output_dir + '\%(title)s.%(ext)s'}
                with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
                    ydl.download([self.list_link[j]])

    def get_list_link(self):
        self.list_link = []
        if self.Conection.get_status():
            for self.i in range(self.first_page, self.last_page):
                response = requests.get(str('https://pt.xhamster.com/search?q=' + self.search + '&p=' + str(self.i)))
                soup = bs4.BeautifulSoup(response.text, "html.parser")
                for div in soup.find_all(class_='video-thumb-info'):  # video-thumb-info é a classe de div que contem os links
                    link = str(div.find('a')['href'])
                    self.list_link.append(link)
            return self.list_link
        else:
            print("No conection... ")
            return 0
