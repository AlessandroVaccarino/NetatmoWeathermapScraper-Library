import requests
import numpy


class Error(Exception):
    pass


class ParamType(Error):
    pass


class ParamValue(Error):
    pass


def scrape_data(lat_ne,lon_ne,lat_sw,lon_sw,search_type):
    url = "https://app.netatmo.net/api/getpublicmeasures"
    extraction_area_step = 0.1

    if type(lat_ne) not in (int,float):
        raise ParamType('3rd parameter (NorthEast Latitude) must be float')
    if type(lon_ne) not in (int,float):
        raise ParamType('4th parameter (NorthEast Longitude) must be float')
    if type(lat_sw) not in (int,float):
        raise ParamType('1st parameter (SouthOvest Latitude) must be float')
    if type(lon_sw) not in (int,float):
        raise ParamType('2nd parameter (SouthOvest Longitude) must be float')

    if lon_ne < lon_sw:
        raise ParamValue('lon_ne (' + str(lon_ne) + ') < lon_sw (' + str(lon_sw) + ')')
    if lat_ne < lat_sw:
        raise ParamValue('lat_sw (' + str(lat_sw) + ') < lat_ne (' + str(lat_ne) + ')')

    if type(search_type) is not str:
        raise ParamType('4th parameter (sensor type) must be str')
    else:
        if search_type.lower() not in ["temperature","rain","wind"]:
            raise ParamValue('4th parameter (sensor type) value undefined. Must be "temperature", "rain" or "wind"')

    scraper_return = []
    for lat in numpy.arange(lat_sw, lat_ne, extraction_area_step):
        for lon in numpy.arange(lon_sw, lon_ne, extraction_area_step):
            headers = {
                'Accept': "application/json, text/plain, */*",
                'Referer': "https://weathermap.netatmo.com/",
                'Origin': "https://weathermap.netatmo.com",
                'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
                'Authorization': "Bearer 52d42f05177759882c8b456a|753293ecafa4f4b1a9604611adc998e9",
                'Cache-Control': "no-cache",
                'Host': "app.netatmo.net",
                'accept-encoding': "gzip, deflate",
                'Connection': "keep-alive",
                'cache-control': "no-cache"
            }

            payload = {
                "date_end": "last",
                "divider": "3",
                "lat_ne": lat + extraction_area_step,
                "lat_sw": lat,
                "limit": "2",
                "lon_ne": lon + extraction_area_step,
                "lon_sw": lon,
                "quality": "7",
                "type": search_type,
                "zoom": "9"
            }

            response = requests.get(url, headers=headers, params=payload)

            if response.status_code == 200:
                if response not in scraper_return:
                    scraper_return.append(response.json())
            else:
                pass

    return scraper_return
