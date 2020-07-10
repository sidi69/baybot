import concurrent.futures, random, requests, colorama
from colorama import Fore, init

init()

def check(url):
    useragent = random.choice(list(open('useragents.txt')))
    headers={
            "authority" : "www.ebay.com",
            "method" : "GET",
            "scheme" : "https",
            "accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-encoding" : "gzip, deflate, br",
            "accept-language" : "en-US,en;q=0.9,sq;q=0.8",
            "cache-control" : "max-age=0",
            "sec-fetch-dest" : "document",
            "sec-fetch-mode" : "navigate",
            "sec-fetch-site" : "same-origin",
            "sec-fetch-user" : "1",
            "upgrade-insecure-requests" : "1",
            "user-agent" : "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
        }

    src = requests.get(url, headers = headers)

splash = f"""

    {Fore.BLUE},--.   {Fore.YELLOW}        {Fore.GREEN}         {Fore.RED},-----.   ,-----. ,--------. 
    {Fore.BLUE}|  |-. {Fore.YELLOW} ,--,--.{Fore.GREEN},--. ,--.{Fore.RED}|  |) /_ '  .-.  ''--.  .--' 
    {Fore.BLUE}| .-. '{Fore.YELLOW}' ,-.  |{Fore.GREEN} \  '  / {Fore.RED}|  .-.  \|  | |  |   |  |    
    {Fore.BLUE}| `-' |{Fore.YELLOW}\ '-'  |{Fore.GREEN}  \   '  {Fore.RED}|  '--' /'  '-'  '   |  |    
    {Fore.BLUE} `---' {Fore.YELLOW} `--`--'{Fore.GREEN}.-'  /   {Fore.RED}`------'  `-----'    `--'    
    {Fore.BLUE}       {Fore.YELLOW}        {Fore.GREEN}`---'    {Fore.RED}                             
               {Fore.WHITE}Made by sidi {Fore.RED}| {Fore.WHITE}Version: {Fore.RED}1.0                 
"""
print(splash)
print(f"{Fore.RED}[{Fore.WHITE}!{Fore.RED}]{Fore.WHITE} Threads: ", end = '')
threads = input()
print(f"{Fore.RED}[{Fore.WHITE}!{Fore.RED}]{Fore.WHITE} Listing URL: ", end = '')
url = input()
print(f"{Fore.RED}[{Fore.WHITE}!{Fore.RED}]{Fore.WHITE} Sending views...")

with concurrent.futures.ThreadPoolExecutor(max_workers = int(threads)) as executor:
    while True:
        executor.submit(check, url)
