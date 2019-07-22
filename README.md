# NetatmoWeathermapScraper
A simple library aimed to scrape data from Netatmo [Weathermap portal](https://weathermap.netatmo.com/)

## 1. Dependency
```
pip install numpy
pip install requests
```

## 2. Installation
1. Download NetatmoWeathermapScraper.py and put it in the same folder of your py script
2. On your py script
```
import NetatmoWeathermapScraper
```

## 3. Usage

### 3.1 Input parameter
Parameter     | Description
------------- | -------------
lat_ne        | Latitude of the north-east vertex of the desired shape
lon_ne        | Longitude of the north-east vertex of the desired shape
lat_sw        | Latitude of the south-west vertex of the desired shape
lon_sw        | Longitude of the south-west vertex of the desired shape
search_type   | Type of sensor desired (accepted values: "temperature", "rain", "wind")

### 3.2 Output
An array of Jsons structured as provided by Netatmo

## 4. Example
```
import NetatmoWeathermapScraper

jsonArray = NetatmoWeathermapScraper.scrape_data(45.6, 9.6, 45, 8.70, 'temperature')

for jsonElement in jsonArray:
    print(jsonElement)
```
