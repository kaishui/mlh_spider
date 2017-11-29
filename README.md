# python scrapy 从零开始使用

新手上路python

## 1.1 安装Python环境

```

apt-get install -y  python3 python-dev python3-dev libxml2-dev libxslt-dev python3-pip

```

### 1.1.1 下载压缩包安装

```

https://www.python.org/ftp/python/3.6.1/Python-3.6.1.tar.xz

```

### 1.1.2 解压

```

xz -d ./Python-3.6.1.tar.xz

tar -xvf ./Python-3.6.1.tar

```

### 1.1.3 编译安装

```

cd $Python_path

./configure

make & make install

rm /usr/bin/python

ln -r /usr/local/bin/python3.5 /usr/bin/python

```

### 1.1.4 安装

```

apt install python3-pip

```

### 1.1.5 安装 virtualenv

```
 pip install virtualenv
```
### 1.1.6 创建激活相应python环境

```
virtualenv  -p /usr/bin/python3.6 ~/virtualenv/3.6

#open virtual environment dir
cd ~/virtualenv/3.6/bin

##active python3.6

source active

```

## 1.1.7 requirements.txt

使用插件：

```

pip install pipreqs

```

生成 requirements.txt

```

pipreqs ./

```

安装：

```

 pip install -r requirements.txt

```

更新：

```

 pip install --upgrade -r requirements.txt

```

## 1.2 scrapy

```

pip install Scrapy==1.3.3

```

## 1.3 scrapyd

```

pip install scrapyd==1.2.*

```

配置：

sudo vim /etc/scrapyd/scrapyd.conf

```

[scrapyd]
eggs_dir    = eggs
logs_dir    = logs
items_dir   =
jobs_to_keep = 5
dbs_dir     = dbs
max_proc    = 0
max_proc_per_cpu = 4
finished_to_keep = 100
poll_interval = 5.0
bind_address = 127.0.0.1
http_port   = 6800
debug       = off
runner      = scrapyd.runner
application = scrapyd.app.application
launcher    = scrapyd.launcher.Launcher
webroot     = scrapyd.website.Root

[services]
schedule.json     = scrapyd.webservice.Schedule
cancel.json       = scrapyd.webservice.Cancel
addversion.json   = scrapyd.webservice.AddVersion
listprojects.json = scrapyd.webservice.ListProjects
listversions.json = scrapyd.webservice.ListVersions
listspiders.json  = scrapyd.webservice.ListSpiders
delproject.json   = scrapyd.webservice.DeleteProject
delversion.json   = scrapyd.webservice.DeleteVersion
listjobs.json     = scrapyd.webservice.ListJobs
daemonstatus.json = scrapyd.webservice.DaemonStatus
```

## 1.4 scrapy-client

```

pip install scrapyd-client

```



## 1.5 打包

```

python setup.py install

```

## 1.6 向scrapyd中推送

```

scrapyd-deploy -p py_mlh_scrapy --egg=/software/workspace/python/py_mlh_scrapy/dist/py_mlh_scrapy-0.1-py3.5.egg

```

## 1.7启动一个spider

参考API：

```

http://scrapyd.readthedocs.io/en/latest/api.html

```

```

curl http://localhost:6801/schedule.json -d project=py_mlh_scrapy -d spider=scrapy_urls

```

## 1.8 取消一个spider

```

curl http://localhost:6801/cancel.json -d project=py_mlh_scrapy -d job=2f8bf77a258d11e7b3c1b46d8338db7d

```

## 1.9 其他API

```

curl http://localhost:6801/listprojects.json



curl http://localhost:6801/listspiders.json?project=py_mlh_scrapy



curl http://localhost:6801/listjobs.json?project=py_mlh_scrapy



curl http://localhost:6801/delversion.json -d project=py_mlh_scrapy -d version=r99



curl http://localhost:6800/delproject.json -d project=py_mlh_scrapy

```

## 2. sslv3 alert handshake failure

```

 can you try with cryptography<2? (e.g. pip install --upgrade 'cryptography<2')

```

## 3. scrapyd docker-compose.yml
```
version: "3"
services:
  scrapyd:
    image: registry.cn-hangzhou.aliyuncs.com/malianghang/scrapyd-python3.6:latest
    ports:
      - "6800:6800"
    volumes:
      - /tmp:/scrapyd
    deploy:
      replicas: 1
      restart_policy:
        condition: on-failure
    networks:
      - webnet

networks:
  webnet:
```

