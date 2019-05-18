import scrapy
import csv
import os
import re

RENDER_HTML_URL = "http://192.168.99.100:8050/render.html"

x = {"Host": "www.soccerstats.com",
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'pl,en-US;q=0.7,en;q=0.3',
'Accept-Encoding': 'gzip, deflate, br',
'Referer': 'https://www.soccerstats.com/results.asp?league=england',
'Connection': 'keep-alive',
'Cookie': '_ga=GA1.2.113516786.1498762300; cookiesok=yes; __gads=ID=c16e3dab13f60a8c:T=1556550150:S=ALNI_MYKR8tsOmfFOE-_qD4qzmYsdtexjw; euconsent=BOfxrQuOfxrQuABABAPLB7-AAAAix7_______9______9uz_Gv_v_f__33e8__9v_l_7_-___u_-33d4-_1vf99yfm1-7ftr3tp_87ues2_Xur_959__3z3_NIA; cto_lwid=57f0dac1-4d57-4f88-b010-231bf5a52c0c; cto_idcpy=20baafa8-f81a-47ef-b19a-c3cd9ca08897; ASPSESSIONIDAUABQTCD=JOJCLJLAEKIBAEMAEFCDHKCD; tz=60; cdisp=yes; myhtmlticker=89; sc_is_visitor_unique=rx2749989.1557249559.4F83131F29B14FAFD789038BB13AF603.153.141.128.123.111.108.73.49.24',
'Upgrade-Insecure-Requests': '1',
'Cache-Control': 'max-age=0'}

class MySpider(scrapy.Spider):
    start_urls = ["https://www.soccerstats.com/team_results.asp?league={}&pmtype=bydate".format(i)
                  for i in ["netherlands", "netherlands_2018", "netherlands_2017", "netherlands_2016", "netherlands_2015"]]
    name="soccerstats"

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, method='GET', body='{"filters": []}', headers=x,
                                 callback=self.parse)

    def parse(self, response):
        ht = list(map(lambda z: z[2:-2],
                 filter(lambda k: (k[:2] == "\r\n" and k[2:-2] != '' and len(k[2:-2]) == 5),
                        response.css("tr.odd").css("td[align='center']::text").getall())))
        if ht == []:
            ht = list(map(lambda z: z[2:-2],
                 filter(lambda k: (k[:2] == "\r\n" and k[2:-2] != '' and len(k[2:-2]) == 5),
                        response.css("tr.odd").css("td[align='center']").css("font::text").getall())))


        yield {"AAAAAAAAA": len(list(filter(lambda y: (y[:2] != "\r\n"),
                                        response.css("table#btable")[0].css("tr.odd").css("td::text").getall()))),
               "BBBBBBBBBB": len(response.css("font[color='black']").css("b::text").getall()),
               "CCCCCCCCC": len(ht),
               "DDDDDDDD": len(response.css("tr.odd").css("td[height='20']").css("font[size='1']::text").getall()),
               "EEEEEEEEE": (response.url[52:-19],response.url[-18:-14])
               }
        ft = response.css("font[color='black']").css("b::text").getall()
        teams = list(filter(lambda y: (y[:2] != "\r\n"),
                                        response.css("table#btable")[0].css("tr.odd").css("td::text").getall()))
        league = re.findall(r'[a-z]+[1-9]?', response.url[52:-14])
        season = re.findall(r'\d{4}', response.url[52:-14])
        if re.findall(r'\d{4}', response.url[52:-14]) == []:
            season = "['2019']"
        MySpider.csv_file_writer(teams, ft, ht, league, season)
        

    @staticmethod
    def csv_file_writer(teams, ft, ht, league, season):
        table = zip(teams, ft, ht)
        if not os.path.exists(os.path.dirname('{}/{}.csv'.format(league, season))):
            os.makedirs(os.path.dirname('{}/{}.csv'.format(league, season)))
        with open('{}/{}.csv'.format(league, season), 'a') as csvFile:
            writer = csv.writer(csvFile)
            for a, b, c in table:
                writer.writerow((a, int(b[0]), int(b[-1]), int(c[1]), int(c[-2])))
        csvFile.close()
