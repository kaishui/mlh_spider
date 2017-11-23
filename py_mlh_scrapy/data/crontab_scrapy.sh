#!/bin/bash
##curl http://192.168.10.11:6800/delproject.json -d project=py_mlh_scrapy

curl http://192.168.10.11:6800/schedule.json -d project=py_mlh_scrapy -d spider=scrapy_urls -d duplicate=True

curl http://192.168.10.11:6800/schedule.json -d project=py_mlh_scrapy -d spider=scrapy_detail

