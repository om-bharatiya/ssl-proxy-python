import requests
from bs4 import BeautifulSoup
from random import choice


def get_proxy():
    url = 'https://www.sslproxies.org/'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')
    return {
        'https': choice(list(
            map(
                lambda x: x[0]+":"+x[1],
                list(
                    zip(
                        map(
                            lambda x: x.text,
                            soup.findAll('td')[::8]
                        ),
                        map(
                            lambda x: x.text,
                            soup.findAll('td')[1::8]
                        )
                    )
                )
            )
        ))
    }


def get_proxy2():
    url = 'https://www.sslproxies.org/'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')
    prox = choice(list(
        map(
            lambda x: x[0]+":"+x[1],
            list(
                zip(
                    map(
                        lambda x: x.text,
                        soup.findAll('td')[::8]
                    ),
                    map(
                        lambda x: x.text,
                        soup.findAll('td')[1::8]
                    )
                )
            )
        )
    ))
    return {
        'https': prox,
        'http': prox
    }


def proxy_request(request_type, url, **kwargs):
    while 1:
        try:
            proxy = get_proxy()
            print("Using proxy: {}".format(proxy))
            r = requests.request(
                request_type, url, proxies=proxy, timeout=5, **kwargs)
            break
        except:
            pass
    return r


def proxy_request2(request_type, url, **kwargs):
    while 1:
        try:
            proxy = get_proxy2()
            print("Using proxy: {}".format(proxy))
            r = requests.request(
                request_type, url, proxies=proxy, timeout=5, **kwargs)
            break
        except:
            pass
    return r


def without_proxy_request(request_type, url, **kwargs):
    while 1:
        try:
            r = requests.request(
                request_type, url, timeout=5, **kwargs)
            break
        except:
            pass
    return r


url2 = 'http://httpbin.org/ip'

r = proxy_request('get', url2)
# r = proxy_request2('get', url2)
# r = without_proxy_request('get', url2)
r.json()




