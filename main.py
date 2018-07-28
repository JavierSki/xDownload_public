import sys
from CDownloaderXvideos import DownloaderXvideos
from CDownloaderYouPorn import DownloaderYouPorn
from CDownloaderRedTube import DownloaderRedTube
from CDownloaderPornHub import DownloaderPornHub
from CDownloaderBeeg import DownloaderBeeg
from CDownloaderXHamster import DownloaderXHamster
from CDownloaderEporner import DownloaderEporner
from CDownloaderPorn import DownloaderPorn
from CDownloaderPornHD import DownloaderPornHD
from CDownloaderGotPorn import DownloaderGotPorn

# ordem: servidor, pesquisa, pagina inicial, pagina final, pasta de saida


if len(sys.argv) == 6:
    server = str(sys.argv[1]).lower()
    search = str(sys.argv[2]).lower()
    first_page = int(sys.argv[3])
    last_page = int(sys.argv[4])
    output_dir = str(sys.argv[5])
    server_downloaders = {"xvideos": DownloaderXvideos, "youporn": DownloaderYouPorn, "redtube": DownloaderRedTube,
                        "pornhub": DownloaderPornHub, "beeg": DownloaderBeeg, "xhamster": DownloaderXHamster,
                        "eporner": DownloaderEporner, "porn": DownloaderPorn, "pornhd": DownloaderPornHD,
                        "gotporn": DownloaderGotPorn}

    if server in server_downloaders.keys():
        print("-----------------------------------------------------------")
        print(f"server: {server}")
        print("search: " + search)
        print("page " + str(first_page) + " to " + str(last_page))
        print("-----------------------------------------------------------")
        downloader = server_downloaders[server](output_dir, search, first_page, last_page)
        downloader.download()
    else:
        print('Server not found.')
else:
    print('ERROR: Waiting arguments...')
