//mlh 分类
var categoryArr = [
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

/**
 * 转换成马良行的类型
 * @param type 类型
 * @return 分类数据，格式：{
        "id": "residential",
        "name": "住宅"
    }
 */
function getCategory(type) {
    var category = {};
    for (var index in categoryArr) {
        if (type == categoryArr[index].name) {
            category = categoryArr[index];
            break;
        }
    }
    return category;
}

/**
 * 转换成马良行维度信息
 *
 * @param key 传入维度中的中文名
 * @param value 爬虫中的值
 * @return 处理过的值
 * **/
function changToMlhContentDimension(key, value) {
    // print("key = " + key + " value = " + value);
    var returnVal = {};
    switch (key) {
        case "项目地址":
            returnVal = {
                "address": {
                    "detail": {
                        "name": value
                    }
                }
            };
            break;
        case "建筑面积":
            returnVal = {
                "buildingArea": value //TODO 转化成字符串 数字
            };
            break;
        case "容积率":
            returnVal = {
                "volumeRate": value //TODO 转化成字符串 数字
            };
            break;
        case "占地面积":
            returnVal = {
                "coverPlace": value //TODO 转化成字符串 数字
            };
            break;
        case "绿化率":
            returnVal = {
                "greeningRate": value //TODO 转化成字符串 数字
            };
            break;
        case "投资方":
            returnVal = {
                "investor": [
                    {
                        "name": value
                    }
                ]
            };
            break;

        case "投资总额":
            returnVal = {
                "totalInvestment": {
                    "money": value //TODO 转化成字符串 数字
                }
            };
            break;
        case "设计时间":
            returnVal = {
                "designTime": NumberLong(1485820800000)//TODO 转化成时间
            };
            break;
        case "建成时间":
            returnVal = {
                "buildEndTime": NumberLong(1485820800000)//TODO 转化成时间
            };
            break;
        case "建筑设计单位":
            returnVal = {
                "buildingDesign": [
                    {
                        "name": value
                    }
                ]
            };
            break;
        case "景观设计单位":
            returnVal = {
                "sceneryDesignCompany": [
                    {
                        "name": value
                    }
                ]
            };
            break;
        case "室内设计单位":
            returnVal = {
                "planningDesign": [
                    {
                        "name": "规划设计单位"
                    }
                ]
            };
            break;

        case "建筑主创设计师":
            returnVal = {
                "buildingMainDesigner": [
                    {
                        "name": value
                    }
                ]
            };
            break;
        case "景观主创设计师":
            returnVal = {
                "sceneryDesignMainDesigner": [
                    {
                        "name": value
                    }
                ]
            };
            break;
        case "室内主创设计师":
            returnVal = {
                "indoorMainDesigner": [
                    {
                        "name": value
                    }
                ]
            };
            break;
        case "施工图设计":
            returnVal = {
                "drawingDesign": [
                    {
                        "name": value
                    }
                ]
            };
            break;
        case "结构设计单位":
            returnVal = {
                "structureDesign": [
                    {
                        "name": value
                    }
                ]
            };
            break;
        case "结构工程师":
            returnVal = {
                "structuralEngineer": [
                    {
                        "name": value
                    }
                ]
            };
            break;
        case "给排水工程师":
            returnVal = {
                "waterSupplyEngineer": [
                    {
                        "name": value
                    }
                ]
            };
            break;
        case "暖通设计单位":
            returnVal = {
                "HVACDesign": [
                    {
                        "name": value
                    }
                ]
            };
            break;
        case "暖通工程师":
            returnVal = {
                "HVACEngineer": [
                    {
                        "name": value
                    }
                ]
            };
            break;

        case "电气设计单位":
            returnVal = {
                "electricalDesign": [
                    {
                        "name": value
                    }
                ]
            };
            break;

        case "电气工程师":
            returnVal = {
                "electricalEngineer": [
                    {
                        "name": value
                    }
                ]
            };
            break;

        case "开发建设方":
            returnVal = {
                "devBuilder": [
                    {
                        "name": value
                    }
                ]
            };
            break;

        case "工程总承包":
            returnVal = {
                "projectContract": [
                    {
                        "name": value
                    }
                ]
            };
            break;

        case "施工单位":
            returnVal = {
                "buildTeam": [
                    {
                        "name": value
                    }
                ],
            };
            break;

        case "监理单位":
            returnVal = {
                "superviseCompany": [
                    {
                        "name": value
                    }
                ]
            };
            break;

        case "工程造价单位":
            returnVal = {
                "engineeringCostCompany": [
                    {
                        "name": value
                    }
                ]
            };
            break;

        case "物业管理":
            returnVal = {
                "propertyCompany": [
                    {
                        "name": value
                    }
                ]
            };
            break;

        case "获奖情况":
            returnVal = {
                "awards": [
                    {
                        "name": value
                    }
                ]
            };
        case "摄影":
            returnVal = {
                "takePhoto": [
                    {
                        "name": value
                    }
                ]
            };
            break;
        default: //没有找到时，默认加入tag
            returnVal = {
                "others": {
                    "name": value
                }
            }
    }

    return returnVal;
}

/**
 * 设置封面图/标题图
 * @param project
 * @param sdetail
 */
function setImgToContent(project, sdetail) {
    //封面图
    var firstImgObject = {};
    for (var i in sdetail.originImgs) {
        //oss 上的image id
        var ossUrl = sdetail.originImgs[i].ossImgUrl;
        if (undefined != ossUrl && "" != ossUrl) {
            firstImgObject = sdetail.originImgs[i];
            break;
        }
    }
    //标题图
    project["titleImage"] = [
        {
            "id": firstImgObject.ossImgUrl,
            "name": firstImgObject.copyright
        }
    ];
    //封面图
    project["poster"] = [
        {
            "id": firstImgObject.ossImgUrl,
            "name": firstImgObject.copyright
        }
    ];
    //默认图片
    project["imgurl"] = firstImgObject.ossImgUrl;
    //增加tag
    project["tag"].push({
        "id": firstImgObject.ossImgUrl,
        "name": firstImgObject.copyright
    });

    return project;
}

/**
 * 设置维度
 * @param project 构造项目的数据
 * @param sdetail 爬虫数据
 * @return project 返回构造数据
 */
function setDimensions(project, sdetail) {
    //获取爬虫详情数据中的维度数组
    var dimension = sdetail.category;
    for (var index in dimension) {
        // print("index: " + index);
        var dItem = sdetail.category[index];
        //通过爬虫数据维度找到对应马良行的维度
        var item = db.getCollection('scrapy_dimensions').findOne({item: dItem.attr, mlh: {$exists: 1}}, {
            mlh: 1,
            _id: 0
        });

        if (undefined != item && null != item) {
            var mlhAttr = item.mlh;
            //转化成为马良行的维度数据
            var mlhItem = changToMlhContentDimension(mlhAttr, dItem.text);
            project = Object.assign(project, mlhItem);
            //设置标签
            project["tag"].push({
                "name": dItem.text
            });
        }
    }
    return project;
}

/**
 * 设置项目中category
 * @param sdetail 爬虫数据
 * @param project 项目详情数据
 * @return project
 */
function setCategorys(sdetail, project) {
    //类别
    var mlhTypeItem = db.getCollection('scrapy_categorys').findOne({"category": sdetail.type, "mlh": {$exists: 1}}, {
        mlh: 1,
        _id: 0
    });
    if (undefined != mlhTypeItem && null != mlhTypeItem && "" != mlhTypeItem) {
        var mType = mlhTypeItem.mlh;
        //转化成为马良行的分类
        var mlhCategoryItem = getCategory(mType);
        //设置标签
        project["tag"].push(mlhCategoryItem);
        project["category"].push(mlhCategoryItem);
    }
    return project;
}

/**
 * 初始项目结构数据
 * @return {{op: string, createTime: *, status: string, source: string, sourceWebsite: string, createUser: {userId: string, realName: string}, type: string, hasOwner: string, ownerTime: *, updateTime: *, updateUser: {userId: string, realName: string}, opening: string, author: {id: string, name: string}, tag: Array, category: Array}}
 */
function initProject() {
    //创建时间
    var createTime = NumberLong(new Date().getTime());
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
}


/**
 * 运行
 */
function start() {
    // var count = db.getCollection('scrapy_detail').count({"isDeal": {"$exists": 0}});
    // print(count);
    // for (var step = 0; step < count; step = step + 50) {
        // 获取爬虫详情数据数据
        db.getCollection('scrapy_detail').aggregate(
            [
                {$match: {"isDeal": {"$exists": 0}}},
                {
                    $project: {
                        category: 1,
                        url: 1,
                        title: 1,
                        originImgs: 1,
                        location: 1,
                        tags: 1,
                        createTime: 1,
                        type: 1
                    }
                },
                {$sort: {_id: -1}},
                {"$skip": 0},
                {"$limit": 50}
            ]
        ).forEach(function (sdetail) {
            //b_content项目
            var project = initProject();

            //项目ID
            var projectId = new ObjectId().str;
            project["_id"] = projectId;
            //访问uri
            project["resurl"] = "/detail/" + projectId;
            //标题
            project["title"] = [
                {
                    "name": sdetail.title
                }
            ];

            //经维度
            if (undefined != sdetail.location && null != sdetail.location.latitude
                && "null" != sdetail.location.latitude) {
                project['lbs'] = sdetail.location.latitude + "," + sdetail.location.longitude
            }

            //设置内容图片
            project = setImgToContent(project, sdetail);
            //设置维度信息
            project = setDimensions(project, sdetail);
            //设置类型
            project = setCategorys(sdetail, project);

            // print(project);
            //保存项目信息
            db.getCollection('b_content').save(project);

            //标志这条爬虫数据已经处理过
            db.getCollection('scrapy_detail').update({"_id": sdetail["_id"]}, {"$set": {"isDeal": "Y"}});

            //设置图片
            setPictures(projectId, sdetail.originImgs);

        });
    // }
}

/**
 * 设置图片信息
 * @param projectId 项目ID
 * @param originImgs 爬虫图片列表数据
 */
function setPictures(projectId, originImgs) {
    //图片信息为空时
    if (undefined == originImgs || null == originImgs || originImgs.length <= 0) {
        return;
    }
    //图片ID
    var pictureId = new ObjectId().str;
    //图片类型内容
    var picture = {
        "_id": pictureId,
        "parentType": "product",
        "op": "ACT",
        "createTime": NumberLong(new Date().getTime()),
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
            projectId //项目ID
        ],
        "tag": [
            {
                "name": pictureId
            }
        ],
        "picture": []
    };
    //设置图片信息
    for (var i in originImgs) {
        //oss 上的image id
        var ossUrl = originImgs[i].ossImgUrl;
        if (undefined != ossUrl && "" != ossUrl) {
            picture["picture"].push({
                "id": ossUrl,
                "watermark": originImgs[i].copyright
            });
        }
    }

    //print(picture);
    //保存图片信息
    db.getCollection('b_content').save(picture);
}


start();