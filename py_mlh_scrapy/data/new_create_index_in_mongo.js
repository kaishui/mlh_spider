//news index
db.getCollection('b_news').createIndex({sourceUrl:1},{unique:1});

//content
db.getCollection('scrapy_archdaily_contents').createIndex({url:1},{unique:1});

//start list urls
db.getCollection('scrapy_archdaily_content_urls').createIndex({uri:1},{unique:1});