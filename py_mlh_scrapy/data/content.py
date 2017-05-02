import logging
import re
from sqlite3 import time, datetime

from bson import ObjectId
from bson.int64 import long

from py_mlh_scrapy.helper.mongo_util import MongoSupport


class SynContent(object):
    logger = logging.getLogger("SynContent")
    logger.setLevel(logging.DEBUG)

    mongoclient = MongoSupport()

    categoryArr = [
        {
            "id": "culture",
            "name": "文化建筑"
        },
        {
            "id": "business",
            "name": "商业建筑"
        },
        {
            "id": "education",
            "name": "教育建筑"
        },
        {
            "id": "office",
            "name": "办公建筑"
        },
        {
            "id": "physical",
            "name": "体育建筑"
        },
        {
            "id": "public",
            "name": "公共职能建筑"
        },
        {
            "id": "medical",
            "name": "医疗保健建筑"
        },
        {
            "id": "renovation",
            "name": "更新改造"
        },
        {
            "id": "tourism",
            "name": "旅游建筑"
        },
        {
            "id": "religion",
            "name": "宗教建筑"
        },
        {
            "id": "industry",
            "name": "工业建筑及基础设施"
        },
        {
            "id": "residential",
            "name": "住宅"
        }
    ];


    # /**
    #  * 转换成马良行的类型
    #  * @param type 类型
    #  * @return 分类数据，格式：{
    #         "id": "residential",
    #         "name": "住宅"
    #     }
    #  */
    def getCategory(self, type):
        category = {};
        for ctg in self.categoryArr:
            if type == ctg["name"]:
                category = ctg;
                break;
        return category;

    """
        @:param key 关键词
        @:param year 年份
        @:return ms
    """
    def yearToTimestamp(self, key, year):
        if "建成时间" == key or "设计时间" == key:
            y = self.stringExtractFirstNumber(year)
            self.logger.debug("year = ", y)
            if int(float(y)) > 0 :
                if len(y) > 4:
                    y = y[0:4]
                return long(time.mktime(datetime.datetime(year=int(float(y)), month=1, day=1).timetuple()) * 1000)
            else:
                return 0
        else:
            return 0

    """
        提取第一个数字
        @:param text 需要提取的文本
        @:return 返回找到的第一个数字
    """
    def stringExtractFirstNumber(self, text):
        if text is None:
            return 0
        numberArr = re.findall(r"[-+]?\d*\.\d+|\d+",text)
        if numberArr is not None and len(numberArr):
            return numberArr[0]
        else:
            return 0

    # /**
    #  * 转换成马良行维度信息
    #  *
    #  * @param key 传入维度中的中文名
    #  * @param value 爬虫中的值
    #  * @return 处理过的值
    #  * **/
    def changToMlhContentDimension(self, key, value):
        # print("key = " + key + " value = " + value);
        dimensions = {
            "项目地址": {
                "address": {
                    "detail": {
                        "name": value
                    }
                }
            },
            "建筑面积": {
                "buildingArea": str(self.stringExtractFirstNumber(value))
            },
            "容积率": {
                "volumeRate": str(self.stringExtractFirstNumber(value)) # 转化成字符串 数字
            },
            "占地面积": {
                "coverPlace": str(self.stringExtractFirstNumber(value))  # 转化成字符串 数字
            },
            "绿化率": {
                "greeningRate": str(self.stringExtractFirstNumber(value))  # 转化成字符串 数字
            },
            "投资方": {
                "investor": [
                    {
                        "name": value
                    }
                ]
            },
            "投资总额": {
                "totalInvestment": {
                    "money": value
                }
            },
            "设计时间": {
                "designTime": self.yearToTimestamp(key, value)
            },
            "建成时间": {
                "buildEndTime": self.yearToTimestamp(key, value)
            },
            "建筑设计单位": {
                "buildingDesign": [
                    {
                        "name": value
                    }
                ]
            },
            "景观设计单位": {
                "sceneryDesignCompany": [
                    {
                        "name": value
                    }
                ]
            },
            "室内设计单位": {
                "planningDesign": [
                    {
                        "name": value
                    }
                ]
            },
            "建筑主创设计师": {
                "buildingMainDesigner": [
                    {
                        "name": value
                    }
                ]
            },
            "景观主创设计师": {
                "sceneryDesignMainDesigner": [
                    {
                        "name": value
                    }
                ]
            },
            "室内主创设计师": {
                "indoorMainDesigner": [
                    {
                        "name": value
                    }
                ]
            },
            "施工图设计": {
                "drawingDesign": [
                    {
                        "name": value
                    }
                ]
            },
            "结构设计单位": {
                "structureDesign": [
                    {
                        "name": value
                    }
                ]
            },
            "结构工程师": {
                "structuralEngineer": [
                    {
                        "name": value
                    }
                ]
            },
            "给排水工程师": {
                "waterSupplyEngineer": [
                    {
                        "name": value
                    }
                ]
            },
            "暖通设计单位": {
                "HVACDesign": [
                    {
                        "name": value
                    }
                ]
            },
            "暖通工程师": {
                "HVACEngineer": [
                    {
                        "name": value
                    }
                ]
            },
            "电气设计单位": {
                "electricalDesign": [
                    {
                        "name": value
                    }
                ]
            },
            "电气工程师": {
                "electricalEngineer": [
                    {
                        "name": value
                    }
                ]
            },
            "开发建设方": {
                "devBuilder": [
                    {
                        "name": value
                    }
                ]
            },
            "工程总承包": {
                "projectContract": [
                    {
                        "name": value
                    }
                ]
            },
            "施工单位": {
                "buildTeam": [
                    {
                        "name": value
                    }
                ],
            },
            "监理单位": {
                "superviseCompany": [
                    {
                        "name": value
                    }
                ]
            },
            "工程造价单位": {
                "engineeringCostCompany": [
                    {
                        "name": value
                    }
                ]
            },
            "物业管理": {
                "propertyCompany": [
                    {
                        "name": value
                    }
                ]
            },
            "获奖情况": {
                "awards": [
                    {
                        "name": value
                    }
                ]
            },
            "摄影": {
                "takePhoto": [
                    {
                        "name": value
                    }
                ]
            }
        }

        if key in dimensions:
            return dimensions[key]
        else:
            return None


    # /**
    #  * 设置封面图/标题图
    #  * @param project
    #  * @param sdetail
    #  */
    def setImgToContent(self, project, sdetail):
        if len(sdetail["originImgs"]) == 0 :
            return project;
        # 封面图
        for img in sdetail["originImgs"]:
            # oss 上的image id
            if "ossImgUrl" in img and img["ossImgUrl"] is not None:
                # 标题图
                project["titleImage"] = [
                    {
                        "id": img["ossImgUrl"],
                        "name": img["copyright"]
                    }
                ];
                # 封面图
                project["poster"] = [
                    {
                        "id": img["ossImgUrl"],
                        "name": img["copyright"]
                    }
                ];
                # 默认图片
                project["imgurl"] = img["ossImgUrl"]
                # 增加tag
                project["tag"].append({
                    "id": img["ossImgUrl"],
                    "name": img["copyright"]
                });
                break;
        return project;


    # /**
    #  * 设置维度
    #  * @param project 构造项目的数据
    #  * @param sdetail 爬虫数据
    #  * @return project 返回构造数据
    #  */
    def setDimensions(self,project, sdetail):
        # 获取爬虫详情数据中的维度数组
        dimension = sdetail["category"]
        for dItem in dimension:
            # print("index: " + index);
            # 通过爬虫数据维度找到对应马良行的维度
            item = self.mongoclient.db['scrapy_dimensions'].find_one({"item": dItem["attr"], "mlh": {"$exists": 1}}, {
                "mlh": 1,
                "_id": 0
            });

            if item is not None:
                mlhAttr = item["mlh"];
                # 转化成为马良行的维度数据
                mlhItem = self.changToMlhContentDimension(mlhAttr, dItem["text"]);
                if mlhItem is not None:
                    project.update(mlhItem);
                    # 设置标签
                    project["tag"].append({
                        "name": dItem["text"]
                    });
        return project;


    # /**
    #  * 设置项目中category
    #  * @param sdetail 爬虫数据
    #  * @param project 项目详情数据
    #  * @return project
    #  */
    def setCategorys(self, sdetail, project):
        # 类别
        mlhTypeItem = self.mongoclient.db['scrapy_categorys'].find_one({"category": sdetail["type"], "mlh": {"$exists": 1}}, {
            "mlh": 1,
            "_id": 0
        });
        if mlhTypeItem is not None:
            mType = mlhTypeItem["mlh"];
            # 转化成为马良行的分类
            mlhCategoryItem = self.getCategory(mType);
            # 设置标签
            project["tag"].append(mlhCategoryItem);
            project["category"].append(mlhCategoryItem);
        return project;


    # /**
    #  * 初始项目结构数据
    #  * @return {{op: string, createTime: *, status: string, source: string, sourceWebsite: string, createUser: {userId: string, realName: string}, type: string, hasOwner: string, ownerTime: *, updateTime: *, updateUser: {userId: string, realName: string}, opening: string, author: {id: string, name: string}, tag: Array, category: Array}}
    #  */
    def initProject(self):
        # 创建时间
        createTime = long(time.time()*1000);
        return {
            "op": "ACT",
            "createTime": createTime,
            "status": "draft",
            "source": "spider",
            "sourceWebsite": "archdaily",
            "createUser": {
                "userId": "57f5bb5eafd1196165f255d0",
                "realName": "马小良"
            },
            "type": "product",
            "hasOwner": "Y",
            "ownerTime": createTime,
            "updateTime": createTime,
            "updateUser": {
                "userId": "57f5bb5eafd1196165f255d0",
                "realName": "马小良"
            },
            "opening": "N",
            "author": {
                "id": "57f5bb5eafd1196165f255d0",
                "name": "马小良"
            },
            "tag": [],
            "category": []
        };


    # /**
    #  * 运行
    #  */
    def start(self):
        count = self.mongoclient.db['scrapy_detail'].count({"isDeal": {"$exists": 0}});
        self.logger.debug("count =", count);

        skip = 0;
        while skip < count:
            skip += 500;
            # 获取爬虫详情数据数据
            details = self.mongoclient.db['scrapy_detail'].aggregate(
                [
                    {"$match": {"isDeal": {"$exists": 0}}},
                    {
                        "$project": {
                            "category": 1,
                            "url": 1,
                            "title": 1,
                            "originImgs": 1,
                            "location": 1,
                            "tags": 1,
                            "createTime": 1,
                            "type": 1
                        }
                    },
                    {"$sort": {"_id": -1}},
                    {"$skip": 0},
                    {"$limit": 500}
                ]
            )
            for sdetail in details:
                self.logger.debug("scrapy detail : %s", str(sdetail))
                # b_content项目
                project = self.initProject();

                # 项目ID
                projectId = str(ObjectId());
                project["_id"] = projectId;
                # 访问uri
                project["resurl"] = "/detail/" + projectId;
                # 标题
                project["title"] = [
                    {
                        "name": sdetail["title"]
                    }
                ];

                project["tag"].append({
                        "name": sdetail["title"]
                    });

                # 经维度
                # if (undefined != sdetail.location && null != sdetail.location.latitude
                #     && "null" != sdetail.location.latitude) {
                if "location" in sdetail:
                    project['lbs'] = sdetail["location"]["latitude"] + "," + sdetail["location"]["longitude"]

                # 设置内容图片
                project = self.setImgToContent(project, sdetail);
                # 设置维度信息
                project = self.setDimensions(project, sdetail);
                # 设置类型
                project = self.setCategorys(sdetail, project);

                self.logger.debug("project: ", str(project));
                # 不存在封面图就放弃这个项目
                if "imgurl" in project:
                    # 保存项目信息
                    self.mongoclient.db['b_content_spider'].save(project);

                    # 标志这条爬虫数据已经处理过
                    self.mongoclient.db['scrapy_detail'].update({"_id": sdetail["_id"]}, {"$set": {"isDeal": "Y"}});

                    # 设置图片
                    self.setPictures(projectId, sdetail["originImgs"]);


    # /**
    #  * 设置图片信息
    #  * @param projectId 项目ID
    #  * @param originImgs 爬虫图片列表数据
    #  */
    def setPictures(self, projectId, originImgs):
        # 图片信息为空时
        # if (undefined == originImgs || null == originImgs || originImgs.length <= 0) {
        if originImgs is None:
            return;
        # 图片ID
        pictureId = str(ObjectId());
        # 图片类型内容
        picture = {
            "_id": pictureId,
            "parentType": "product",
            "op": "ACT",
            "createTime": long(time.time()*1000),
            "status": "released",
            "source": "spider",
            "sourceWebsite": "archdaily",
            "createUser": {
                "userId": "57f5bb5eafd1196165f255d0",
                "realName": "马小良"
            },
            "author": {
                "id": "57f5bb5eafd1196165f255d0",
                "name": "马小良"
            },
            "type": "picture",
            "fkTag": [
                projectId  # 项目ID
            ],
            "tag": [
                {
                    "name": pictureId
                }
            ],
            "picture": []
        };
        # 设置图片信息
        for img in originImgs:
            # oss 上的image id
            if "ossImgUrl"in img and img["ossImgUrl"] is not None:
                picture["picture"].append({
                    "id": img["ossImgUrl"],
                    "watermark": img["copyright"]
                });

        self.logger.debug("picture: %s", str(picture))
        # 保存图片信息
        self.mongoclient.db['b_content_spider'].save(picture);


if __name__ == '__main__':
    # item = changToMlhContentDimension("绿化率", "fengzt")
    # print(item)
    SynContent().start()
    # date = time.mktime(datetime.datetime.strptime("2015", "%Y").date().timetuple()) * 1000
    # print(date)
    #
    # number = SynContent().stringExtractFirstNumber("400.0 m2")
    # print(number)
    # pass
