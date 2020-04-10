import requests
import time


def url_ok(url):
    try:
        r = requests.head(url)
        return r.status_code == 200
    except:
        return False


if __name__ == "__main__":
    url_list = [
        ["https://github.com/mmngreco/scio", True],
        ["https://github.com/mmngreco/sio", False],
        ["https://github.com/mmngreco/io", False],
        ["https://github.com/mmngreco/ineqpy", True],
        ["http://example.com", False],
        ["https://github.com/mmngreco/scio", True],
        ]

    for url, exp in url_list:
        obt = url_ok(url)
        assert obt == exp
        print(obt, url, sep="\t")
