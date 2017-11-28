#!/bin/bash

# execute it each 30mins
##curl http://192.168.10.11:6800/delproject.json -d project=py_mlh_scrapy_test

#scrapy projects list
curl http://192.168.10.11:6800/schedule.json -d project=py_mlh_scrapy_test -d spider=arch_projects_list -d duplicate=True

# scrapy news list
curl http://192.168.10.11:6800/schedule.json -d project=py_mlh_scrapy_test -d spider=arch_news_list

###set archdaily project detail urls into redis
#curl http://192.168.10.11:6800/schedule.json -d project=py_mlh_scrapy_test -d spider=scrapy_news_detail_start_urls_spider -d site=archdaily -d detail_spider=arch_project_detail
###set archdaily news start urls into redis
#curl http://192.168.10.11:6800/schedule.json -d project=py_mlh_scrapy_test -d spider=scrapy_news_detail_start_urls_spider -d site=archdaily_news -d detail_spider=arch_news_detail_page

##scrapy project detail
#curl http://192.168.10.11:6800/schedule.json -d project=py_mlh_scrapy_test -d spider=arch_project_detail
#
##scrapy news detail
#curl http://192.168.10.11:6800/schedule.json -d project=py_mlh_scrapy_test -d spider=arch_news_detail_page

# delete spider
#curl http://192.168.10.11:6800/cancel.json -d project=py_mlh_scrapy_test -d job=5b38c9fcd03711e79fb902420aff0007

