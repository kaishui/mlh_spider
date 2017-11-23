//news index
db.getCollection('b_news').createIndex({sourceUrl:1},{unique:1});

//archdaily content
db.getCollection('scrapy_archdaily_contents').createIndex({url:1},{unique:1});