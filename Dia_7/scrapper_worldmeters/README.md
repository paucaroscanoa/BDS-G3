scrapy
scrapy bench
pip freeze #verificar la versión scrapy

## Star Project
scrapy startproject scraper_meters
## Iniciando
scrapy genspider woldmeters https://www.worldometers.info/world-population/population-by-country/
## Revisión resultado - terminal
scrapy shell
r=scrapy.Request(url='https://www.worldometers.info/world-population/population-by-country')
response.body
## probar xpath
response.xpath('//h1/text()').get()
## salir del shell
quit()

## Ejecutando un proyecto scrapy
scrapy crawl woldmeters

## Para ubicar el xpath 
"F12","Cntr+f"
