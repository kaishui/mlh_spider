#!/bin/bash
##curl http://192.168.10.11:6800/delproject.json -d project=py_mlh_scrapy

curl http://192.168.10.11:6800/schedule.json -d project=py_mlh_scrapy -d spider=scrapy_urls

curl http://192.168.10.11:6800/schedule.json -d project=py_mlh_scrapy -d spider=scrapy_detail

#curl http://192.168.10.11:6800/cancel.json -d project=py_mlh_scrapy -d job=5b38c9fcd03711e79fb902420aff0007

