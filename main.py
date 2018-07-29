import sys
from CDownloader import Downloader

# ordem: servidor, pesquisa, pagina inicial, pagina final, pasta de saida


if len(sys.argv) == 6:
    server = str(sys.argv[1]).lower()
    search = str(sys.argv[2]).lower()
    first_page = int(sys.argv[3])
    last_page = int(sys.argv[4])
    output_dir = str(sys.argv[5])
    print("-----------------------------------------------------------")
    print("server:" + server)
    print("search: " + search)
    print("page " + str(first_page) + " to " + str(last_page))
    print("-----------------------------------------------------------")
    downloader = Downloader(server, output_dir, search, first_page, last_page)
    downloader.download()
else:
    print('ERROR: Waiting arguments...')
