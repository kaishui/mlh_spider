#!/bin/bash
##curl http://192.168.10.11:6800/delproject.json -d project=py_mlh_scrapy

#scrapy projects list
curl http://192.168.10.11:6800/schedule.json -d project=py_mlh_scrapy -d spider=arch_projects_list -d duplicate=True

# scrapy news list
curl http://192.168.10.11:6800/schedule.json -d project=py_mlh_scrapy -d spider=arch_news_list

##set archdaily project detail urls into redis
curl http://192.168.10.11:6800/schedule.json -d project=py_mlh_scrapy -d spider=scrapy_news_detail_start_urls_spider -d site=archdaily -d detail_spider=arch_project_detail

##set archdaily news start urls into redis
curl http://192.168.10.11:6800/schedule.json -d project=py_mlh_scrapy -d spider=scrapy_news_detail_start_urls_spider -d site=archdaily_news -d detail_spider=arch_news_detail_page

#scrapy project detail
curl http://192.168.10.11:6800/schedule.json -d project=py_mlh_scrapy -d spider=arch_project_detail

#scrapy news detail
curl http://192.168.10.11:6800/schedule.json -d project=py_mlh_scrapy -d spider=arch_news_detail_page

# delete spider
#curl http://192.168.10.11:6800/cancel.json -d project=py_mlh_scrapy -d job=b3366ad4d35b11e7be8002420aff0005

