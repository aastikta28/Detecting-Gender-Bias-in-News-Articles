# python crawler.py YYYY MM <path to store docs>

import calendar
import datetime
import json
import os
import sys
import urllib2

if len(sys.argv) < 3:
	print 'Please use this format: python crawler.py MM YYYY'
	sys.exit()

crawl_year = int(sys.argv[1])
#crawl_month = int(sys.argv[2])
destination = sys.argv[2]

for crawl_month in range(1,13):
    
    api_key = '4ddd8c6844a146499178cb66172cdb5a:18:74308147'
    url = 'http://api.nytimes.com/svc/search/v2/articlesearch.json?fq=news_desk:("Sports")'

    date_range = calendar.monthrange(crawl_year, crawl_month)

    start_date = datetime.datetime(
    year = crawl_year,
    month = crawl_month,
    day = 1
    )

    publish_start_date = start_date.strftime('%Y%m%d')

    end_date = datetime.datetime(
    year = crawl_year,
    month = crawl_month,
    day = date_range[1]
    )

    publish_end_date = end_date.strftime('%Y%m%d')

    url += '&begin_date=' + publish_start_date + '&end_date=' + publish_end_date

    url += '&api-key=' + api_key

    docs = ['default']

    page_number = 0
    doc_number = 1

    path_prefix = str(crawl_year) + '_' + str(crawl_month)
    os.chdir(destination)
    if not os.path.exists(path_prefix):
        os.makedirs(path_prefix)
        
    os.chdir(path_prefix)

    show_hits = True
    while len(docs) > 0:
        url_object = urllib2.urlopen(url + '&page=' + str(page_number))
        response = json.load(url_object)
        if show_hits:
            hits = response['response']['meta']['hits']
            print 'Number of docs: ' + str(response['response']['meta']['hits'])
            show_hits = False
        docs = response['response']['docs']
        page_number += 1
        for doc in docs:
            fil = open(str(crawl_year) + '_' + str(crawl_month) + '_' + str(doc_number), 'w+')
            json.dump(doc, fil)
            fil.close()
            print 'Writing file number ' + str(doc_number)
            doc_number += 1

    if hits <= doc_number:
        print "All docs received."
        
    else:
        print "Error occured during ", crawl_month
        sys.exit()

