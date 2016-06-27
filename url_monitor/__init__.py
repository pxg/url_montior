import requests
from time import sleep


def url_monitor():
    interval_seconds = 0.5
    # url = 'http://staging.livebetterwith.com/'
    url = 'https://livebetterwith.com/'
    down_time = 0
    print('Monitoring URL {0}'.format(url))

    while True:
        response = requests.get(url)
        if response.status_code != 200:
            # Not entirely acurate, doesn't take into account time for request
            down_time += interval_seconds
            print('Downtime {0}'.format(down_time))
        else:
            if down_time > 0:
                print('Site back online')
            down_time = 0
        sleep(interval_seconds)
