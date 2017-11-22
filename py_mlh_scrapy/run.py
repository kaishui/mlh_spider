from scrapy.cmdline import execute
import sys
import os

# 打断点调试py文件
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
print(os.path.dirname(os.path.abspath(__file__)))
execute(['scrapy', 'crawl', 'scrapy_mlhang'])