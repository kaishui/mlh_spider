from py_mlh_scrapy.helper.mongo_util import MongoSupport

categorys = [
    {
        "category": "住宅",
        "mlh": "住宅",
        "quantity": 2149.0
    },
    {
        "category": "独立住宅",
        "mlh": "住宅",
        "quantity": 800.0
    },
    {
        "category": "公寓",
        "mlh": "住宅",
        "quantity": 375.0
    },
    {
        "category": "办公建筑",
        "mlh": "办公建筑",
        "quantity": 269.0
    },
    {
        "category": "酒店",
        "mlh": "旅游建筑",
        "quantity": 181.0
    },
    {
        "category": "博物馆",
        "mlh": "文化建筑",
        "quantity": 175.0
    },
    {
        "category": "办公室室内",
        "mlh": "办公建筑",
        "quantity": 149.0
    },
    {
        "category": "大学",
        "mlh": "教育建筑",
        "quantity": 141.0
    },
    {
        "category": "混合用途建筑",
        "mlh": "住宅",
        "quantity": 138.0
    },
    {
        "category": "餐厅",
        "mlh": "商业建筑",
        "quantity": 138.0
    },
    {
        "category": "图书馆",
        "mlh": "文化建筑",
        "quantity": 128.0
    },
    {
        "category": "公共机构建筑",
        "mlh": "公共职能建筑",
        "quantity": 116.0
    },
    {
        "category": "学校",
        "mlh": "教育建筑",
        "quantity": 110.0
    },
    {
        "category": "展馆",
        "mlh": "文化建筑",
        "quantity": 101.0
    },
    {
        "category": "办公室",
        "mlh": "办公建筑",
        "quantity": 91.0
    },
    {
        "category": "办公设施",
        "mlh": "办公建筑",
        "quantity": 91.0
    },
    {
        "category": "幼儿园",
        "mlh": "教育建筑",
        "quantity": 85.0
    },
    {
        "category": "文化建筑",
        "mlh": "文化建筑",
        "quantity": 82.0
    },
    {
        "category": "教育建筑",
        "mlh": "教育建筑",
        "quantity": 72.0
    },
    {
        "category": "安装与结构",
        "quantity": 70.0
    },
    {
        "category": "社区中心",
        "mlh": "公共职能建筑",
        "quantity": 66.0
    },
    {
        "category": "展览中心",
        "mlh": "文化建筑",
        "quantity": 62.0
    },
    {
        "category": "温泉",
        "mlh": "旅游建筑",
        "quantity": 60.0
    },
    {
        "category": "画廊",
        "mlh": "文化建筑",
        "quantity": 59.0
    },
    {
        "category": "公共机构设施",
        "mlh": "公共职能建筑",
        "quantity": 58.0
    },
    {
        "category": "集合住宅",
        "mlh": "住宅",
        "quantity": 56.0
    },
    {
        "category": "装修",
        "quantity": 55.0
    },
    {
        "category": "商业建筑",
        "mlh": "商业建筑",
        "quantity": 55.0
    },
    {
        "category": "医院",
        "mlh": "医疗保健建筑",
        "quantity": 53.0
    },
    {
        "category": "娱乐与训练",
        "mlh": "体育建筑",
        "quantity": 52.0
    },
    {
        "category": "公寓室内",
        "mlh": "住宅",
        "quantity": 51.0
    },
    {
        "category": "游客中心",
        "mlh": "文化建筑",
        "quantity": 50.0
    },
    {
        "category": "公园",
        "mlh": "文化建筑",
        "quantity": 50.0
    },
    {
        "category": "咖啡馆",
        "mlh": "商业建筑",
        "quantity": 48.0
    },
    {
        "category": "教堂",
        "mlh": "宗教建筑",
        "quantity": 46.0
    },
    {
        "category": "工业建筑",
        "mlh": "工业建筑",
        "quantity": 43.0
    },
    {
        "category": "居住建筑",
        "mlh": "住宅",
        "quantity": 41.0
    },
    {
        "category": "文化中心",
        "mlh": "文化建筑",
        "quantity": 41.0
    },
    {
        "category": "中小学校",
        "mlh": "教育建筑",
        "quantity": 40.0
    },
    {
        "category": "博物馆与展览",
        "mlh": "文化建筑",
        "quantity": 39.0
    },
    {
        "category": "商店",
        "mlh": "商业建筑",
        "quantity": 38.0
    },
    {
        "category": "体育馆",
        "mlh": "体育建筑",
        "quantity": 38.0
    },
    {
        "category": "社会住宅",
        "mlh": "住宅",
        "quantity": 36.0
    },
    {
        "category": "景观建筑",
        "quantity": 35.0
    },
    {
        "category": "剧院",
        "mlh": "文化建筑",
        "quantity": 35.0
    },
    {
        "category": "购物中心",
        "mlh": "商业建筑",
        "quantity": 34.0
    },
    {
        "category": "诊所",
        "mlh": "医疗保健建筑",
        "quantity": 34.0
    },
    {
        "category": "其他设施",
        "mlh": "公共职能建筑",
        "quantity": 33.0
    },
    {
        "category": "高等教育",
        "mlh": "教育建筑",
        "quantity": 33.0
    },
    {
        "category": "研究中心",
        "mlh": "办公建筑",
        "quantity": 32.0
    },
    {
        "category": "体育建筑",
        "mlh": "体育建筑",
        "quantity": 30.0
    },
    {
        "category": "小学和中学",
        "mlh": "教育建筑",
        "quantity": 30.0
    },
    {
        "category": "卫生保健",
        "mlh": "医疗保健建筑",
        "quantity": 29.0
    },
    {
        "category": "公寓室内设计",
        "mlh": "住宅",
        "quantity": 29.0
    },
    {
        "category": "零售",
        "mlh": "商业建筑",
        "quantity": 28.0
    },
    {
        "category": "临时装置",
        "mlh": "文化建筑",
        "quantity": 27.0
    },
    {
        "category": "视觉艺术中心",
        "mlh": "文化建筑",
        "quantity": 27.0
    },
    {
        "category": "餐饮建筑",
        "mlh": "商业建筑",
        "quantity": 27.0
    },
    {
        "category": "景观装置",
        "mlh": "文化建筑",
        "quantity": 26.0
    },
    {
        "category": "适应性再利用",
        "mlh": "体育建筑",
        "quantity": 26.0
    },
    {
        "category": "餐厅与吧",
        "mlh": "商业建筑",
        "quantity": 25.0
    },
    {
        "category": "游泳池",
        "mlh": "体育建筑",
        "quantity": 25.0
    },
    {
        "category": "更新项目",
        "mlh": "更新改造",
        "quantity": 25.0
    },
    {
        "category": "展陈建筑",
        "mlh": "文化建筑",
        "quantity": 24.0
    },
    {
        "category": "酒厂",
        "mlh": "工业建筑",
        "quantity": 24.0
    },
    {
        "category": "阁楼",
        "mlh": "住宅",
        "quantity": 24.0
    },
    {
        "category": "陈列室",
        "mlh": "文化建筑",
        "quantity": 24.0
    },
    {
        "category": "教会",
        "mlh": "宗教建筑",
        "quantity": 24.0
    },
    {
        "category": "高中",
        "mlh": "教育建筑",
        "quantity": 24.0
    },
    {
        "category": "工作室",
        "mlh": "办公建筑",
        "quantity": 23.0
    },
    {
        "category": "宗教建筑",
        "mlh": "宗教建筑",
        "quantity": 22.0
    },
    {
        "category": "学习",
        "mlh": "教育建筑",
        "quantity": 22.0
    },
    {
        "category": "店",
        "mlh": "商业建筑",
        "quantity": 22.0
    },
    {
        "category": "机场",
        "mlh": "工业建筑",
        "quantity": 21.0
    },
    {
        "category": "公共空间",
        "mlh": "文化建筑",
        "quantity": 21.0
    },
    {
        "category": "室内建筑",
        "quantity": 21.0
    },
    {
        "category": "广场",
        "mlh": "文化建筑",
        "quantity": 20.0
    },
    {
        "category": "公共建筑",
        "mlh": "公共职能建筑",
        "quantity": 20.0
    },
    {
        "category": "度假小屋",
        "mlh": "旅游建筑",
        "quantity": 20.0
    },
    {
        "category": "房子室内",
        "mlh": "住宅",
        "quantity": 20.0
    },
    {
        "category": "基础结构",
        "quantity": 19.0
    },
    {
        "category": "零售建筑",
        "mlh": "商业建筑",
        "quantity": 19.0
    },
    {
        "category": "服务",
        "mlh": "公共职能建筑",
        "quantity": 19.0
    },
    {
        "category": "实验室",
        "mlh": "办公建筑",
        "quantity": 19.0
    },
    {
        "category": "翻修",
        "mlh": "更新改造",
        "quantity": 19.0
    },
    {
        "category": "美术馆",
        "mlh": "文化建筑",
        "quantity": 18.0
    },
    {
        "category": "礼堂",
        "mlh": "宗教建筑",
        "quantity": 18.0
    },
    {
        "category": "人行天桥",
        "mlh": "工业建筑",
        "quantity": 17.0
    },
    {
        "category": "停车",
        "mlh": "工业建筑",
        "quantity": 17.0
    },
    {
        "category": "学院",
        "mlh": "教育建筑",
        "quantity": 17.0
    },
    {
        "category": "火车站",
        "mlh": "工业建筑",
        "quantity": 17.0
    },
    {
        "category": "安装",
        "mlh": "工业建筑",
        "quantity": 17.0
    },
    {
        "category": "健身房",
        "mlh": "体育建筑",
        "quantity": 16.0
    },
    {
        "category": "娱乐训练场馆",
        "mlh": "体育建筑",
        "quantity": 16.0
    },
    {
        "category": "工厂",
        "mlh": "工业建筑",
        "quantity": 16.0
    },
    {
        "category": "展陈装置",
        "mlh": "文化建筑",
        "quantity": 16.0
    },
    {
        "category": "展厅",
        "mlh": "文化建筑",
        "quantity": 15.0
    },
    {
        "category": "住宅室内",
        "mlh": "住宅",
        "quantity": 15.0
    },
    {
        "category": "适应性利用",
        "mlh": "更新改造",
        "quantity": 15.0
    },
    {
        "category": "公交站",
        "mlh": "工业建筑",
        "quantity": 15.0
    },
    {
        "category": "研究所",
        "mlh": "办公建筑",
        "quantity": 15.0
    },
    {
        "category": "中学",
        "mlh": "教育建筑",
        "quantity": 15.0
    },
    {
        "category": "保健中心",
        "mlh": "医疗保健建筑",
        "quantity": 14.0
    },
    {
        "category": "吧",
        "mlh": "商业建筑",
        "quantity": 13.0
    },
    {
        "category": "医疗建筑",
        "mlh": "医疗保健建筑",
        "quantity": 13.0
    },
    {
        "category": "社区",
        "mlh": "公共职能建筑",
        "quantity": 13.0
    },
    {
        "category": "酒店建筑",
        "mlh": "旅游建筑",
        "quantity": 13.0
    },
    {
        "category": "咖啡厅",
        "mlh": "商业建筑",
        "quantity": 13.0
    },
    {
        "category": "宿舍",
        "mlh": "住宅",
        "quantity": 13.0
    },
    {
        "category": "音乐厅",
        "mlh": "文化建筑",
        "quantity": 13.0
    },
    {
        "category": "市政厅",
        "mlh": "公共职能建筑",
        "quantity": 12.0
    },
    {
        "category": "旅游业",
        "mlh": "旅游建筑",
        "quantity": 12.0
    },
    {
        "category": "剧院与表演",
        "mlh": "文化建筑",
        "quantity": 12.0
    },
    {
        "category": "牙医诊所",
        "mlh": "医疗保健建筑",
        "quantity": 12.0
    },
    {
        "category": "寺庙",
        "mlh": "宗教建筑",
        "quantity": 12.0
    },
    {
        "category": "音乐会场",
        "mlh": "文化建筑",
        "quantity": 12.0
    },
    {
        "category": "演艺中心",
        "mlh": "文化建筑",
        "quantity": 12.0
    },
    {
        "category": "旅社",
        "mlh": "旅游建筑",
        "quantity": 12.0
    },
    {
        "category": "医疗设施",
        "mlh": "医疗保健建筑",
        "quantity": 11.0
    },
    {
        "category": "能源工厂",
        "mlh": "工业建筑",
        "quantity": 11.0
    },
    {
        "category": "摩天大楼",
        "mlh": "商业建筑",
        "quantity": 11.0
    },
    {
        "category": "小教堂",
        "mlh": "宗教建筑",
        "quantity": 11.0
    },
    {
        "category": "演艺建筑",
        "mlh": "文化建筑",
        "quantity": 11.0
    },
    {
        "category": "小学及初中",
        "mlh": "教育建筑",
        "quantity": 11.0
    },
    {
        "category": "消防站",
        "mlh": "工业建筑",
        "quantity": 11.0
    },
    {
        "category": "停车场",
        "mlh": "工业建筑",
        "quantity": 11.0
    },
    {
        "category": "总体规划",
        "quantity": 11.0
    },
    {
        "category": "运动场地",
        "mlh": "体育建筑",
        "quantity": 11.0
    },
    {
        "category": "康复中心",
        "mlh": "医疗保健建筑",
        "quantity": 10.0
    },
    {
        "category": "其他结构",
        "quantity": 10.0
    },
    {
        "category": "酒吧",
        "mlh": "商业建筑",
        "quantity": 10.0
    },
    {
        "category": "科学中心",
        "mlh": "文化建筑",
        "quantity": 10.0
    },
    {
        "category": "小学与中学",
        "mlh": "教育建筑",
        "quantity": 10.0
    },
    {
        "category": "桥梁",
        "mlh": "工业建筑",
        "quantity": 10.0
    },
    {
        "category": "小礼拜堂",
        "mlh": "宗教建筑",
        "quantity": 10.0
    },
    {
        "category": "园",
        "mlh": "文化建筑",
        "quantity": 9.0
    },
    {
        "category": "青年活动中心",
        "mlh": "文化建筑",
        "quantity": 9.0
    },
    {
        "category": "电影院",
        "mlh": "文化建筑",
        "quantity": 8.0
    },
    {
        "category": "高等教育设施",
        "mlh": "教育建筑",
        "quantity": 8.0
    },
    {
        "category": "城市设计",
        "mlh": "文化建筑",
        "quantity": 8.0
    },
    {
        "category": "市政建设",
        "mlh": "公共职能建筑",
        "quantity": 8.0
    },
    {
        "category": "百货商店",
        "mlh": "商业建筑",
        "quantity": 8.0
    },
    {
        "category": "运输",
        "mlh": "工业建筑",
        "quantity": 8.0
    },
    {
        "category": "人行桥",
        "mlh": "工业建筑",
        "quantity": 8.0
    },
    {
        "category": "其他公共建筑管理",
        "mlh": "公共职能建筑",
        "quantity": 8.0
    },
    {
        "category": "市场",
        "mlh": "商业建筑",
        "quantity": 8.0
    },
    {
        "category": "火葬场",
        "mlh": "公共职能建筑",
        "quantity": 7.0
    },
    {
        "category": "纪念中心",
        "mlh": "文化建筑",
        "quantity": 7.0
    },
    {
        "category": "行政建筑",
        "mlh": "公共职能建筑",
        "quantity": 7.0
    },
    {
        "category": "其他建筑",
        "mlh": "文化建筑",
        "quantity": 7.0
    },
    {
        "category": "学生大厅",
        "mlh": "教育建筑",
        "quantity": 7.0
    },
    {
        "category": "其他教育设施",
        "mlh": "教育建筑",
        "quantity": 7.0
    },
    {
        "category": "社会住房",
        "mlh": "住宅",
        "quantity": 7.0
    },
    {
        "category": "健身俱乐部",
        "mlh": "体育建筑",
        "quantity": 7.0
    },
    {
        "category": "医学实验室",
        "mlh": "医疗保健建筑",
        "quantity": 7.0
    },
    {
        "category": "酒庄",
        "mlh": "工业建筑",
        "quantity": 7.0
    },
    {
        "category": "社区建筑",
        "mlh": "公共职能建筑",
        "quantity": 7.0
    },
    {
        "category": "交通",
        "mlh": "工业建筑",
        "quantity": 6.0
    },
    {
        "category": "修复",
        "mlh": "更新改造",
        "quantity": 6.0
    },
    {
        "category": "退休",
        "mlh": "医疗保健建筑",
        "quantity": 6.0
    },
    {
        "category": "保健",
        "mlh": "医疗保健建筑",
        "quantity": 6.0
    },
    {
        "category": "体育场馆",
        "mlh": "体育建筑",
        "quantity": 6.0
    },
    {
        "category": "室内设计",
        "quantity": 6.0
    },
    {
        "category": "小尺度",
        "quantity": 6.0
    },
    {
        "category": "水疗",
        "mlh": "医疗保健建筑",
        "quantity": 6.0
    },
    {
        "category": "小尺度项目",
        "quantity": 6.0
    },
    {
        "category": "足球场馆",
        "mlh": "体育建筑",
        "quantity": 5.0
    },
    {
        "category": "福利",
        "mlh": "医疗保健建筑",
        "quantity": 5.0
    },
    {
        "category": "消防局",
        "mlh": "公共职能建筑",
        "quantity": 5.0
    },
    {
        "category": "日托中心",
        "mlh": "教育建筑",
        "quantity": 5.0
    },
    {
        "category": "快餐",
        "mlh": "商业建筑",
        "quantity": 5.0
    },
    {
        "category": "地铁站",
        "mlh": "工业建筑",
        "quantity": 5.0
    },
    {
        "category": "药疗设施",
        "mlh": "医疗保健建筑",
        "quantity": 5.0
    },
    {
        "category": "食堂",
        "mlh": "公共职能建筑",
        "quantity": 5.0
    },
    {
        "category": "建筑",
        "quantity": 5.0
    },
    {
        "category": "旅游景点",
        "mlh": "旅游建筑",
        "quantity": 5.0
    },
    {
        "category": "警察局",
        "mlh": "公共职能建筑",
        "quantity": 5.0
    },
    {
        "category": "派出所",
        "mlh": "公共职能建筑",
        "quantity": 5.0
    },
    {
        "category": "法院",
        "mlh": "公共职能建筑",
        "quantity": 5.0
    },
    {
        "category": "城市与市政厅",
        "mlh": "公共职能建筑",
        "quantity": 5.0
    },
    {
        "category": "青年旅舍",
        "mlh": "旅游建筑",
        "quantity": 5.0
    },
    {
        "category": "改造项目",
        "mlh": "更新改造",
        "quantity": 5.0
    },
    {
        "category": "动物园",
        "mlh": "文化建筑",
        "quantity": 5.0
    },
    {
        "category": "葬礼",
        "mlh": "宗教建筑",
        "quantity": 5.0
    },
    {
        "category": "水族馆",
        "mlh": "文化建筑",
        "quantity": 4.0
    },
    {
        "category": "学生活动中心",
        "mlh": "教育建筑",
        "quantity": 4.0
    },
    {
        "category": "桥",
        "mlh": "工业建筑",
        "quantity": 4.0
    },
    {
        "category": "水疗设施",
        "mlh": "医疗保健建筑",
        "quantity": 4.0
    },
    {
        "category": "修道院",
        "mlh": "宗教建筑",
        "quantity": 4.0
    },
    {
        "category": "纪念碑",
        "mlh": "文化建筑",
        "quantity": 4.0
    },
    {
        "category": "修复项目",
        "mlh": "更新改造",
        "quantity": 4.0
    },
    {
        "category": "其他公共管理建筑",
        "mlh": "公共职能建筑",
        "quantity": 4.0
    },
    {
        "category": "桑拿",
        "mlh": "医疗保健建筑",
        "quantity": 4.0
    },
    {
        "category": "歌剧院",
        "mlh": "文化建筑",
        "quantity": 4.0
    },
    {
        "category": "码头",
        "mlh": "工业建筑",
        "quantity": 4.0
    },
    {
        "category": "墓地",
        "mlh": "宗教建筑",
        "quantity": 4.0
    },
    {
        "category": "谷仓",
        "mlh": "工业建筑",
        "quantity": 4.0
    },
    {
        "category": "服务建筑",
        "mlh": "公共职能建筑",
        "quantity": 4.0
    },
    {
        "category": "足球场",
        "mlh": "体育建筑",
        "quantity": 4.0
    },
    {
        "category": "仓房",
        "mlh": "工业建筑",
        "quantity": 4.0
    },
    {
        "category": "港口",
        "mlh": "工业建筑",
        "quantity": 4.0
    },
    {
        "category": "学生会馆",
        "mlh": "教育建筑",
        "quantity": 4.0
    },
    {
        "category": "其他",
        "quantity": 4.0
    },
    {
        "category": "日间护理",
        "quantity": 4.0
    },
    {
        "category": "游船码头",
        "mlh": "工业建筑",
        "quantity": 4.0
    },
    {
        "category": "城市规划",
        "quantity": 4.0
    },
    {
        "category": "别墅室内",
        "mlh": "住宅",
        "quantity": 4.0
    },
    {
        "category": "半圆形剧场",
        "mlh": "文化建筑",
        "quantity": 4.0
    },
    {
        "category": "大使馆",
        "mlh": "公共职能建筑",
        "quantity": 4.0
    },
    {
        "category": "科教建筑",
        "mlh": "教育建筑",
        "quantity": 4.0
    },
    {
        "category": "养老院",
        "mlh": "医疗保健建筑",
        "quantity": 4.0
    },
    {
        "category": "清真寺",
        "mlh": "宗教建筑",
        "quantity": 4.0
    },
    {
        "category": "加油站",
        "mlh": "工业建筑",
        "quantity": 4.0
    },
    {
        "category": "景观设计",
        "quantity": 3.0
    },
    {
        "category": "旅馆",
        "mlh": "旅游建筑",
        "quantity": 3.0
    },
    {
        "category": "药店",
        "mlh": "医疗保健建筑",
        "quantity": 3.0
    },
    {
        "category": "照明",
        "quantity": 3.0
    },
    {
        "category": "仪式建筑",
        "mlh": "宗教建筑",
        "quantity": 3.0
    },
    {
        "category": "桑拿房",
        "mlh": "医疗保健建筑",
        "quantity": 3.0
    },
    {
        "category": "市政建筑",
        "mlh": "公共职能建筑",
        "quantity": 3.0
    },
    {
        "category": "政府",
        "mlh": "公共职能建筑",
        "quantity": 3.0
    },
    {
        "category": "扩展",
        "quantity": 3.0
    },
    {
        "category": "大教堂",
        "mlh": "宗教建筑",
        "quantity": 3.0
    },
    {
        "category": "温室",
        "quantity": 3.0
    },
    {
        "category": "舞厅",
        "mlh": "商业建筑",
        "quantity": 3.0
    },
    {
        "category": "耳房",
        "quantity": 3.0
    },
    {
        "category": "土窖与陵墓",
        "mlh": "宗教建筑",
        "quantity": 3.0
    },
    {
        "category": "银行",
        "mlh": "公共职能建筑",
        "quantity": 3.0
    },
    {
        "category": "澡堂",
        "mlh": "医疗保健建筑",
        "quantity": 3.0
    },
    {
        "category": "崇拜",
        "mlh": "宗教建筑",
        "quantity": 3.0
    },
    {
        "category": "马厩",
        "mlh": "工业建筑",
        "quantity": 3.0
    },
    {
        "category": "军事总部",
        "mlh": "工业建筑",
        "quantity": 3.0
    },
    {
        "category": "加建项目",
        "mlh": "更新改造",
        "quantity": 3.0
    },
    {
        "category": "会堂",
        "mlh": "文化建筑",
        "quantity": 2.0
    },
    {
        "category": "教室",
        "mlh": "教育建筑",
        "quantity": 2.0
    },
    {
        "category": "保留基地",
        "mlh": "更新改造",
        "quantity": 2.0
    },
    {
        "category": "公路桥",
        "mlh": "工业建筑",
        "quantity": 2.0
    },
    {
        "category": "灯光设计",
        "quantity": 2.0
    },
    {
        "category": "其他公共行政建筑",
        "mlh": "公共职能建筑",
        "quantity": 2.0
    },
    {
        "category": "总统套房",
        "mlh": "商业建筑",
        "quantity": 2.0
    },
    {
        "category": "夜店",
        "mlh": "商业建筑",
        "quantity": 2.0
    },
    {
        "category": "船坞",
        "mlh": "工业建筑",
        "quantity": 2.0
    },
    {
        "category": "历史保护",
        "mlh": "更新改造",
        "quantity": 2.0
    },
    {
        "category": "遗址保护",
        "mlh": "更新改造",
        "quantity": 2.0
    },
    {
        "category": "赌场",
        "mlh": "商业建筑",
        "quantity": 2.0
    },
    {
        "category": "控制中心",
        "mlh": "工业建筑",
        "quantity": 2.0
    },
    {
        "category": "礼拜",
        "mlh": "宗教建筑",
        "quantity": 2.0
    },
    {
        "category": "康乐设施",
        "mlh": "工业建筑",
        "quantity": 2.0
    },
    {
        "category": "基础设施",
        "mlh": "工业建筑",
        "quantity": 2.0
    },
    {
        "category": "精神病院",
        "mlh": "医疗保健建筑",
        "quantity": 2.0
    },
    {
        "category": "祈祷室",
        "mlh": "宗教建筑",
        "quantity": 2.0
    },
    {
        "category": "寄宿",
        "mlh": "旅游建筑",
        "quantity": 2.0
    },
    {
        "category": "部门建筑",
        "mlh": "公共职能建筑",
        "quantity": 2.0
    },
    {
        "category": "露天剧场",
        "mlh": "文化建筑",
        "quantity": 2.0
    },
    {
        "category": "使馆",
        "mlh": "公共职能建筑",
        "quantity": 2.0
    },
    {
        "category": "夜生活",
        "mlh": "商业建筑",
        "quantity": 2.0
    },
    {
        "category": "主题公园",
        "mlh": "文化建筑",
        "quantity": 2.0
    },
    {
        "category": "配送中心",
        "mlh": "工业建筑",
        "quantity": 2.0
    },
    {
        "category": "库房",
        "mlh": "工业建筑",
        "quantity": 2.0
    },
    {
        "category": "EMBT在巴塞罗那建造开创性癌症中心",
        "quantity": 1.0
    },
    {
        "category": "重庆长嘉汇购物公园 / 伍兹贝格",
        "quantity": 1.0
    },
    {
        "category": "卜石 · 新天地馆 / Archi-Union Architects",
        "quantity": 1.0
    },
    {
        "category": "Sordo Madaleno Arquitectos事务所公布在墨西哥的酒店和公寓项目",
        "quantity": 1.0
    },
    {
        "category": "香港铁路海洋公园及黄竹坑站 / Aedas",
        "quantity": 1.0
    },
    {
        "category": "欢易小面 / 众舍空间设计",
        "quantity": 1.0
    },
    {
        "category": "MVRDV新作H-O-M-E——将曼海姆前军营改造成综合区",
        "quantity": 1.0
    },
    {
        "category": "赋乐旅居 / 三石建筑事务所",
        "quantity": 1.0
    },
    {
        "category": "BIG新作-哥本哈根动物园阴阳熊猫馆",
        "quantity": 1.0
    },
    {
        "category": "DROR事务所为伊斯坦布尔Parkorman公园设计能让游客跃上树顶观光的方案",
        "quantity": 1.0
    },
    {
        "category": "GZ广场 / Studio Cáceres Lazo",
        "quantity": 1.0
    },
    {
        "category": "保利商务中心 / Aedas",
        "quantity": 1.0
    },
    {
        "category": "华东院与 CAAU 设计联合体赢得深圳宝安公共文化艺术中心国际竞赛",
        "quantity": 1.0
    },
    {
        "category": "Impressive auto salon  / 峻佳设计",
        "quantity": 1.0
    },
    {
        "category": "生命的光 / 谭淑静与禾筑设计团队",
        "quantity": 1.0
    },
    {
        "category": "蚌埠市博物馆和规划馆 / 本原设计",
        "quantity": 1.0
    },
    {
        "category": "杭州新天地商务中心开发项目E地块 / 浙江大学建筑设计研究院有限公司(第七建筑设计院）",
        "quantity": 1.0
    },
    {
        "category": "Aedas设计为“一带一路”打开门户",
        "quantity": 1.0
    },
    {
        "category": "山东师范大学长清校区图书馆 / 浙江大学建筑设计研究院有限公司(第七建筑设计院）",
        "quantity": 1.0
    },
    {
        "category": "2030年的地拉那 - 看自然和都市生活如何在阿尔巴尼亚首都和谐共存",
        "quantity": 1.0
    },
    {
        "category": "3XN建筑师事务所赢得瑞典水上中心竞赛",
        "quantity": 1.0
    },
    {
        "category": "香港终审法院大楼 / 香港特别行政区政府建筑署",
        "quantity": 1.0
    },
    {
        "category": "动物健康设施",
        "quantity": 1.0
    },
    {
        "category": "LAVA宣布关于马来西亚森林城市竞赛的候选方案",
        "quantity": 1.0
    },
    {
        "category": "网络办公空间 / MDDM STUDIO",
        "quantity": 1.0
    },
    {
        "category": "重庆两江新区人民小学 / 上海天华建筑设计有限公司",
        "quantity": 1.0
    },
    {
        "category": "AGi建筑事务所赢得了将加利西亚的罗马遗址改造为感官博物馆的竞赛",
        "quantity": 1.0
    },
    {
        "category": "Ateliers 2/3/4/建筑事务所公布了法国巴黎花园大楼的设计方案",
        "quantity": 1.0
    },
    {
        "category": "上海公寓改造 / ZHU HAO Studio",
        "quantity": 1.0
    },
    {
        "category": "兄弟住宅 / 5X Studio",
        "quantity": 1.0
    },
    {
        "category": "岱山小学 / 南京大学建筑与城市规划学院-周凌工作室",
        "quantity": 1.0
    },
    {
        "category": "黄土上的院子 / hyperSity Architects",
        "quantity": 1.0
    },
    {
        "category": "合风苍飞 / Soar Design Studio",
        "quantity": 1.0
    },
    {
        "category": "林茂森 / 开物设计",
        "quantity": 1.0
    },
    {
        "category": "Schmidt Hammer Lassen 主持设计耗资8800万美元的墨尔本维多利亚国家图书馆改建项目",
        "quantity": 1.0
    },
    {
        "category": "ANS OFFICE / 开物设计",
        "quantity": 1.0
    },
    {
        "category": "湖南城陵矶综合保税区通关服务中心 /上海建筑设计研究院有限公司，第一原创工作室",
        "quantity": 1.0
    },
    {
        "category": "Aedas赢得三亚新建旅游枢纽的设计竞赛",
        "quantity": 1.0
    },
    {
        "category": "壹舍设计办公室 / 方磊作品",
        "quantity": 1.0
    },
    {
        "category": "理性与感性 / Robot 3 工作室",
        "quantity": 1.0
    },
    {
        "category": "光明村灾后重建示范项目 / 香港中文大学＋昆明理工大学",
        "quantity": 1.0
    },
    {
        "category": "医学研究机构",
        "quantity": 1.0
    },
    {
        "category": "OMA 城市更新项目：上海哥伦比亚公园",
        "quantity": 1.0
    },
    {
        "category": "Meepark智能型会展场地／ Lattitute",
        "quantity": 1.0
    },
    {
        "category": "城市客栈宽窄巷/朱志康空间规划",
        "quantity": 1.0
    },
    {
        "category": "神秘游戏餐厅 / Feel Design",
        "quantity": 1.0
    },
    {
        "category": "香港Kornville住宅 / EMCS",
        "quantity": 1.0
    },
    {
        "category": "Vincent Callebaut Architectures 台湾双螺旋结构生态塔",
        "quantity": 1.0
    },
    {
        "category": "青山村小学图书室 / SLOW Architects",
        "quantity": 1.0
    },
    {
        "category": "桥沟教学点图书室 / SLOW 建筑事务所",
        "quantity": 1.0
    },
    {
        "category": "灯市口住宅改造 / B.L.U.E. 建筑设计事务所",
        "quantity": 1.0
    },
    {
        "category": "原麦山丘北京华贸店 / B.L.U.E. 建筑设计事务所",
        "quantity": 1.0
    },
    {
        "category": "蓝月影视办公设计——一条切割时间的线",
        "quantity": 1.0
    },
    {
        "category": "四件异尺度家具 – LANDER电竞公司办公室 / 里建筑事务所",
        "quantity": 1.0
    },
    {
        "category": "Chao酒店灯光设计 / GD-Lighting Design",
        "quantity": 1.0
    },
    {
        "category": "从自然而来——北京ROSEMOO创意空间环境设计/寸-DESIGN",
        "quantity": 1.0
    },
    {
        "category": "BYA住宅 / BUDIC",
        "quantity": 1.0
    },
    {
        "category": "交通建筑",
        "quantity": 1.0
    },
    {
        "category": "KT 公寓 / Marty Chou Architects",
        "quantity": 1.0
    },
    {
        "category": "KWK Promes 建筑事务所对波兰当代艺术馆的扩建方案",
        "quantity": 1.0
    },
    {
        "category": "天津蓟县地质博物馆 / 天津大学建筑设计研究院",
        "quantity": 1.0
    },
    {
        "category": "理查德·迈耶及合伙人事务所公布了其里程碑式的纽约黑玻璃住宅大楼",
        "quantity": 1.0
    },
    {
        "category": "比利时历史区的新建泳池与健身中心",
        "quantity": 1.0
    },
    {
        "category": "AD经典：伽利略天文馆 / Enrique Jan",
        "quantity": 1.0
    },
    {
        "category": "Aedas公布了深圳罗湖区友谊交易中心的动态设计",
        "quantity": 1.0
    },
    {
        "category": "Schmidt Hammer Lassen 赢得了挪威斯塔万格的城市规划与多功能大楼的竞赛",
        "quantity": 1.0
    },
    {
        "category": "Petras Architecture建筑事务所在塞浦路斯“文化村”设计竞赛中获奖",
        "quantity": 1.0
    },
    {
        "category": "Transborder工作室赢得挪威奥斯陆乳品厂新型农业区改造竞赛",
        "quantity": 1.0
    },
    {
        "category": "斯德哥尔摩的转型始于此宝石般的建筑",
        "quantity": 1.0
    },
    {
        "category": "城堡",
        "quantity": 1.0
    },
    {
        "category": "KOSMOS建筑事务所为HelloWood 2016设计了一面更注重联合性的墙",
        "quantity": 1.0
    },
    {
        "category": "由一系列圆顶和起伏波浪组成的莫斯科马戏学校方案",
        "quantity": 1.0
    },
    {
        "category": "Casa Graham y Angus  / DTR 建筑事务所",
        "quantity": 1.0
    },
    {
        "category": "奥巴马总统图书馆在“第二故乡” 设计大奖赛中的非官方获奖者",
        "quantity": 1.0
    },
    {
        "category": "啤酒厂",
        "quantity": 1.0
    },
    {
        "category": "临时商店",
        "quantity": 1.0
    },
    {
        "category": "荷兰阿尔梅勒市创新型自可持续发展村落模型可成为半城市生活的未来",
        "quantity": 1.0
    },
    {
        "category": "HI-POP茶饮概念店 / 肯斯尼恩设计",
        "quantity": 1.0
    },
    {
        "category": "朱锫建筑设计事务所 日前公布了大理杨丽萍表演艺术中心设计方案",
        "quantity": 1.0
    },
    {
        "category": "深圳猫树里咖啡厅 / 间外建筑工作室",
        "quantity": 1.0
    },
    {
        "category": "Vo Trong Nghia Architects 建筑事务所设计的特色水疗中心",
        "quantity": 1.0
    },
    {
        "category": "好玩的 \"泰线\" 给曼谷带来的无价绿空间",
        "quantity": 1.0
    },
    {
        "category": "MMK+ & Taehyung Park 把首尔的废弃岛屿打造成了新文化中心",
        "quantity": 1.0
    },
    {
        "category": "跑马场",
        "quantity": 1.0
    },
    {
        "category": "Iosa Ghini Associati 建筑事务所设计的迈阿密新摩天大楼充满了意大利式的奢华",
        "quantity": 1.0
    },
    {
        "category": "伊斯坦布尔人工岛码头上的“伊斯坦布尔明珠”",
        "quantity": 1.0
    },
    {
        "category": "受到印度阶梯井和水迷宫启发设计的新景观",
        "quantity": 1.0
    },
    {
        "category": "cnYES 办公室设计 / 水相设计",
        "quantity": 1.0
    },
    {
        "category": "Nartarchitects在曾经的煤矿上设计了戏剧性的博物馆",
        "quantity": 1.0
    },
    {
        "category": "英飞特科技园 / gad",
        "quantity": 1.0
    },
    {
        "category": "AD综述：第四部经典",
        "quantity": 1.0
    },
    {
        "category": "Jewell / Kavellaris Urban Design",
        "quantity": 1.0
    },
    {
        "category": "哥本哈根糖尿病中心：一个让患者与自然产生对话的地方",
        "quantity": 1.0
    },
    {
        "category": "三维运动跑道 / Subarquitectura",
        "quantity": 1.0
    },
    {
        "category": "S.Misagh Architecture & Planning用前卫的设计向陈旧的教室告别",
        "quantity": 1.0
    },
    {
        "category": "Café Del Volcán 烘焙创意坊 / gDS 和 Birdhouse 联袂设计",
        "quantity": 1.0
    },
    {
        "category": "MISA工作室 / 万境设计",
        "quantity": 1.0
    },
    {
        "category": "阿拉伯最大的碗状体育场/ Perkins+Will",
        "quantity": 1.0
    },
    {
        "category": "折纸屋: 灾害到来时桌子变成避难所",
        "quantity": 1.0
    },
    {
        "category": "Las Palmas de Leyda Spa / Cristobal Valenzuela",
        "quantity": 1.0
    },
    {
        "category": "殡葬建筑",
        "quantity": 1.0
    },
    {
        "category": "Lead 8 建筑事务所在香港港口设计人行天桥环路",
        "quantity": 1.0
    },
    {
        "category": "颠覆性的手法让 Michael Ryan Charters 和 Ranjit John Korah 设计的摩天楼“原形毕露”",
        "quantity": 1.0
    },
    {
        "category": "高脚屋 / Wang Hsiao-Kuei Architecture Studio",
        "quantity": 1.0
    },
    {
        "category": "阿联酋生物气候学的医疗健康设施",
        "quantity": 1.0
    },
    {
        "category": "BIG与BARCODE赢得阿姆斯特丹住宅竞赛",
        "quantity": 1.0
    },
    {
        "category": "特纳利夫岛南部会展中心 / AMP arquitectos",
        "quantity": 1.0
    },
    {
        "category": "MVRDV设计的台湾Y形屋顶泳池住宅",
        "quantity": 1.0
    },
    {
        "category": "MAD的首个欧洲项目UNIC即将开工",
        "quantity": 1.0
    },
    {
        "category": "CEBRA 为格陵兰岛和北极地区设计了新博物馆",
        "quantity": 1.0
    },
    {
        "category": "Architects of Invention建筑事务所在塞舌尔群岛上利用生物仿生技术设计出来的珊瑚酒店",
        "quantity": 1.0
    },
    {
        "category": "港北区小住宅 / Torafu",
        "quantity": 1.0
    },
    {
        "category": "想不想参与设计一座投资1000亿美元的未来城市？",
        "quantity": 1.0
    },
    {
        "category": "Vila Velha 博物馆 / Belém Lima Arquitectos",
        "quantity": 1.0
    },
    {
        "category": "历史街区空间再生－隐居江南精品酒店 / gad 杰地设计",
        "quantity": 1.0
    },
    {
        "category": "Diagonal 80",
        "quantity": 1.0
    },
    {
        "category": "兰家山公园 / 門口建筑合作社&epos architects",
        "quantity": 1.0
    },
    {
        "category": "Georges Batzios Architects事务所提出完全由干草建成的文化中心",
        "quantity": 1.0
    },
    {
        "category": "动物收容所",
        "quantity": 1.0
    },
    {
        "category": "RDH 建筑事务所将把加拿大历史知名的邮局改造成数字图书馆",
        "quantity": 1.0
    },
    {
        "category": "新景观规划将减少哥本哈根城市的洪水",
        "quantity": 1.0
    },
    {
        "category": "Nabil Gholam以银行总部项目获得2016世界建筑节",
        "quantity": 1.0
    },
    {
        "category": "未来东京 2045 / Kohn Pederson Fox Associates + Leslie E. Robertsobn Associates",
        "quantity": 1.0
    },
    {
        "category": "隈研吾事务所将在土耳其以“堆叠木盒”建造博物馆",
        "quantity": 1.0
    },
    {
        "category": "Snøhetta 设计的费城天普大学图书馆动工建设",
        "quantity": 1.0
    },
    {
        "category": "药房",
        "quantity": 1.0
    },
    {
        "category": "观光塔",
        "quantity": 1.0
    },
    {
        "category": "McGee Art Pavilion / ikon.5 architects",
        "quantity": 1.0
    },
    {
        "category": "AD经典: 古尔本金安基金会 / Ruy Jervis d’Athouguia, Pedro Cid and Alberto Pessoa",
        "quantity": 1.0
    },
    {
        "category": "工业艺术中心竞赛 / Stefano Corbo Studio",
        "quantity": 1.0
    },
    {
        "category": "Lake Iosco House / RES4",
        "quantity": 1.0
    },
    {
        "category": "艺术和建筑",
        "quantity": 1.0
    },
    {
        "category": "日常中心 / FLEXO Arquitectura",
        "quantity": 1.0
    },
    {
        "category": "DLRG救生船站 / Kunze Seeholzer",
        "quantity": 1.0
    },
    {
        "category": "小园 / 阮晓舟设计工作室",
        "quantity": 1.0
    },
    {
        "category": "千卡",
        "quantity": 1.0
    },
    {
        "category": "捷克的市政厅和社区中心设计/Plukk",
        "quantity": 1.0
    },
    {
        "category": "klee klee 品牌首发零售店 / AIM Architecture",
        "quantity": 1.0
    },
    {
        "category": "BIG 公布了洛杉矶艺术区的多功能混凝土上层建筑",
        "quantity": 1.0
    },
    {
        "category": "漂浮的房子 / NRJA",
        "quantity": 1.0
    },
    {
        "category": "Hamonic+Masson & Associés 展望为卡萨布兰卡重新设计金融区",
        "quantity": 1.0
    },
    {
        "category": "香港戏曲中心/ Bing Thom Architects",
        "quantity": 1.0
    },
    {
        "category": "SOM公布了瑞典哥德堡设计的 Karlatornet 港口新图片",
        "quantity": 1.0
    },
    {
        "category": "诺曼·福斯特事务所在纽约布鲁克林水滨设计综合体",
        "quantity": 1.0
    },
    {
        "category": "Agence d’Architecture A. Bechu 与 Associés赢得了摩洛哥海边城市新校园的设计竞赛",
        "quantity": 1.0
    },
    {
        "category": "伦敦设计双年展提出了美国和墨西哥之间“边界城市”的新议题",
        "quantity": 1.0
    },
    {
        "category": "南京垂直森林 / 博埃里建筑设计事务所",
        "quantity": 1.0
    },
    {
        "category": "田园归梦：鄕根•东林渡民宿设计与艺术装置 /  + 艾松,，李豪",
        "quantity": 1.0
    },
    {
        "category": "Topio7建筑事务所的杰作——将煤矿改造成生态走廊",
        "quantity": 1.0
    },
    {
        "category": "新的城市规划将催化美国密尔沃基市中心的动态变革",
        "quantity": 1.0
    },
    {
        "category": "杂货店",
        "quantity": 1.0
    },
    {
        "category": "MVRDV 赢得了汉堡创新港口总体规划竞赛",
        "quantity": 1.0
    },
    {
        "category": "废弃了27年，开始重建的黑山项目",
        "quantity": 1.0
    },
    {
        "category": "MVRDV将首尔废弃高速路改造为奢华空中花园",
        "quantity": 1.0
    },
    {
        "category": "Ennead Architects 建筑事务所宣布中国南京麒麟科技创新园项目计划",
        "quantity": 1.0
    },
    {
        "category": "北欧事务所赢得温州肯恩大学新学生中心和图书馆设计竞赛",
        "quantity": 1.0
    },
    {
        "category": "丽京花园公寓 / 安东红坊",
        "quantity": 1.0
    },
    {
        "category": "Richard Meier & Partners将设计在德国汉堡的河岸综合应用大楼",
        "quantity": 1.0
    },
    {
        "category": "FR-EE 公布了墨西哥马萨特兰市博物馆设计方案",
        "quantity": 1.0
    },
    {
        "category": "临时仓储",
        "quantity": 1.0
    },
    {
        "category": "中国设想了具有技术创新高速公路的未来碳中和城市",
        "quantity": 1.0
    },
    {
        "category": "船屋",
        "quantity": 1.0
    },
    {
        "category": "纸桌 / 建筑营设计工作室",
        "quantity": 1.0
    },
    {
        "category": "原麦山丘 北京三里屯店 / B.L.U.E. Architecture Studio",
        "quantity": 1.0
    },
    {
        "category": "维也纳军营院内设计的新办公楼",
        "quantity": 1.0
    },
    {
        "category": "AD经典：博尼范登博物馆 / 阿尔多·罗西",
        "quantity": 1.0
    },
    {
        "category": "TA.R.I 建筑事务所赢得了韩国首尔的女性与家庭设施综合体竞赛二等奖",
        "quantity": 1.0
    },
    {
        "category": "扎哈·哈迪德建筑事务所将在卡塔尔设计高层酒店住宅",
        "quantity": 1.0
    },
    {
        "category": "Trahan 建筑师事务所改造亚特兰大联合剧院",
        "quantity": 1.0
    },
    {
        "category": "White Arkitekter的砖结构住房项目赢得斯德哥尔摩皇家港口区竞赛",
        "quantity": 1.0
    },
    {
        "category": "HENN Architects建筑事务所赢得了在柏林的新西兰总部大楼设计竞赛",
        "quantity": 1.0
    },
    {
        "category": "RSAA建筑事务所的Kunstsilo方案对挪威历史谷仓进行保护，改建和重现",
        "quantity": 1.0
    },
    {
        "category": "Schiattarella Associati 设计公司日前公布了利雅得体育场设计方案",
        "quantity": 1.0
    },
    {
        "category": "Kimmel Eshkolot 建筑事务所赢得了以色列特拉维夫市总规划建筑竞赛",
        "quantity": 1.0
    },
    {
        "category": "经开智汇园新媒体展示中心 / hyperSity 工作室",
        "quantity": 1.0
    },
    {
        "category": "动物栖息地",
        "quantity": 1.0
    },
    {
        "category": "表演艺术中心",
        "quantity": 1.0
    },
    {
        "category": "AD经典系列: 哥伦布大厦骑士  / Kevin Roche & John Dinkeloo",
        "quantity": 1.0
    },
    {
        "category": "部门大楼",
        "quantity": 1.0
    },
    {
        "category": "Kéré 建筑事务所将设计苏丹 Meroe 皇家浴场保护棚",
        "quantity": 1.0
    },
    {
        "category": "城市规划设计",
        "quantity": 1.0
    },
    {
        "category": "AD 摘要： 经典第 II 部分",
        "quantity": 1.0
    },
    {
        "category": "经典的第三部分",
        "quantity": 1.0
    },
    {
        "category": "常绿砖头工厂的推广亭 / Levitt Goodman Architects",
        "quantity": 1.0
    },
    {
        "category": "自然科学中心 / NORD Arkitekter",
        "quantity": 1.0
    },
    {
        "category": "AD经典：马拉帕特别墅 / Adalberto Libera",
        "quantity": 1.0
    },
    {
        "category": "公墓",
        "quantity": 1.0
    },
    {
        "category": "MX快餐店  / Craft Design",
        "quantity": 1.0
    },
    {
        "category": "旧金山的私人住宅 / Garcia Tamjidi Architecture Design",
        "quantity": 1.0
    },
    {
        "category": "魔方小屋 / AR Arquitetos",
        "quantity": 1.0
    },
    {
        "category": "螺旋走廊Spiral Arches/ 筑梦社",
        "quantity": 1.0
    },
    {
        "category": "希堤微旅 / 张景尧建筑师事务所+大埕设计股份有限公司",
        "quantity": 1.0
    },
    {
        "category": "AD Round Up: Classics Part V",
        "quantity": 1.0
    },
    {
        "category": "摩天楼",
        "quantity": 1.0
    },
    {
        "category": "UNStudio 和 Heerim 赢得首尔住宅开发区设计竞赛",
        "quantity": 1.0
    },
    {
        "category": "無同 / WOOTON",
        "quantity": 1.0
    },
    {
        "category": "中国长沙建造中的多彩购物街“ Joytown”",
        "quantity": 1.0
    },
    {
        "category": "椿吉大理古城精品酒店 / 共向设计",
        "quantity": 1.0
    },
    {
        "category": "着眼于未来：Mecanoo 建筑事务所为曼彻斯特大学设计的工程校区",
        "quantity": 1.0
    },
    {
        "category": "扎哈哈迪德建筑事务所公布了墨尔本花瓶大楼的新图片及视频",
        "quantity": 1.0
    },
    {
        "category": "滑板公园",
        "quantity": 1.0
    },
    {
        "category": "OostCampus 改造项目 / Carlos Arroyo",
        "quantity": 1.0
    },
    {
        "category": "种植灵感：杭州安道新总部建筑设计解读 / 安道集团",
        "quantity": 1.0
    },
    {
        "category": "Loft",
        "quantity": 1.0
    },
    {
        "category": "竞赛报名：伊斯坦布尔 Gülsuyu Cemevi 文化中心",
        "quantity": 1.0
    },
    {
        "category": "朴隐居 / EF design studio",
        "quantity": 1.0
    },
    {
        "category": "o2a 建筑事务所为特拉维夫大学的可持续性发展所设计的自然光和风的控制系统",
        "quantity": 1.0
    },
    {
        "category": "悉尼林间将出现一座没有墓碑的公墓",
        "quantity": 1.0
    },
    {
        "category": "TEN Arquitectos 设计的布鲁克林高层建筑即将完工",
        "quantity": 1.0
    },
    {
        "category": "残疾人中心 / g.bang architecture",
        "quantity": 1.0
    },
    {
        "category": "Hollwich Kushner 公布慕尼黑综合商业体设计方案",
        "quantity": 1.0
    },
    {
        "category": "OMA 发布了其设计的卢卡斯博物馆替代方案",
        "quantity": 1.0
    },
    {
        "category": "Blob vB3 移动泡泡屋 / dmvA",
        "quantity": 1.0
    },
    {
        "category": "Schmidt Hammer Lassen 建筑事务所设计上海黄浦江畔“云展馆”",
        "quantity": 1.0
    },
    {
        "category": "灰.容器 LP AUTO GALLERY / C.DD Design",
        "quantity": 1.0
    },
    {
        "category": "Chapultepec空间 / at103",
        "quantity": 1.0
    },
    {
        "category": "吴宅 / 是合设计研究室",
        "quantity": 1.0
    },
    {
        "category": "原型住宅 I / Collective Studio",
        "quantity": 1.0
    },
    {
        "category": "CEBRA事务所为迪拜可持续发展城设计学校",
        "quantity": 1.0
    },
    {
        "category": "阳光的颂词 / 游雅清空间设计",
        "quantity": 1.0
    },
    {
        "category": "解说中心",
        "quantity": 1.0
    },
    {
        "category": "Aedas的“无限”北京新浪总部设计正式开工",
        "quantity": 1.0
    },
    {
        "category": "URBAN AGENCY 设计的法国豪华公寓",
        "quantity": 1.0
    },
    {
        "category": "司令部",
        "quantity": 1.0
    },
    {
        "category": "Matteo Cainer Architects 为韩国顺天艺术平台竞赛的方案 \"Open Gate\"",
        "quantity": 1.0
    },
    {
        "category": "功能灵活的包豪斯博物馆",
        "quantity": 1.0
    },
    {
        "category": "2016里约奥运手球场馆 / Lopes Santos e Ferreira Gomes Arquitetos + OA | Oficina de Arquitetos",
        "quantity": 1.0
    },
    {
        "category": "Ennead 建筑事务所在设计了位于中国武汉的华为研究中心",
        "quantity": 1.0
    },
    {
        "category": "西班牙 F&A 住宅  / Colectivo Du Arquitectura",
        "quantity": 1.0
    },
    {
        "category": "3rd Skin 建筑事务所的折叠跨过伊朗高速公路的Haghani人行天桥项目",
        "quantity": 1.0
    },
    {
        "category": "中国中铁售楼中心和社区图书馆 ／ Van Wang Architects",
        "quantity": 1.0
    },
    {
        "category": "aLL Design 公布了南伦敦居住区塔楼的计划",
        "quantity": 1.0
    },
    {
        "category": "GRAFT开始在德国设计水疗酒店",
        "quantity": 1.0
    },
    {
        "category": "RSAA／庄子玉工作室在中国的现代教堂重构了巴西利卡式建筑",
        "quantity": 1.0
    },
    {
        "category": "城区规划",
        "quantity": 1.0
    },
    {
        "category": "餐厅& 酒吧",
        "quantity": 1.0
    },
    {
        "category": "Vincent Callebaut Architectures设计的布鲁塞尔生态社区",
        "quantity": 1.0
    },
    {
        "category": "瓦尔纳地区图书馆 / Stewart Hollenstein",
        "quantity": 1.0
    },
    {
        "category": "橄榄球场",
        "quantity": 1.0
    },
    {
        "category": "加气站",
        "quantity": 1.0
    },
    {
        "category": "HENN 赢得竞赛将设计中国金蝶大厦",
        "quantity": 1.0
    },
    {
        "category": "就试 试衣间 / 唯想国际",
        "quantity": 1.0
    },
    {
        "category": "十年、十条媒体线索与一百名杰出的中国建筑师 —— UED2015北京国际设计周展览 / WAY Studio",
        "quantity": 1.0
    },
    {
        "category": "SOM 建筑事务所展示的曼哈顿西区大开发计划",
        "quantity": 1.0
    },
    {
        "category": "飞机库",
        "quantity": 1.0
    },
    {
        "category": "里斯本沙丘形状的艺术建筑和技术博物馆将于10月开放",
        "quantity": 1.0
    },
    {
        "category": "交通中心",
        "quantity": 1.0
    },
    {
        "category": "扎哈·哈迪德建筑事务所开始纽伦堡3C大厅工程建设",
        "quantity": 1.0
    },
    {
        "category": "哥本哈根的全新岛屿将成为两个街区之间的“垫脚石”",
        "quantity": 1.0
    },
    {
        "category": "滑雪中心",
        "quantity": 1.0
    },
    {
        "category": "Ennead Architects 建筑事务所公开了天津美术学院的扩建方案",
        "quantity": 1.0
    },
    {
        "category": "Aedas建筑事务所设计的吉达阿卜杜勒·拉蒂夫·贾米尔公司总部",
        "quantity": 1.0
    },
    {
        "category": "架景叠园 / 出品建筑事务所",
        "quantity": 1.0
    },
    {
        "category": "安保",
        "quantity": 1.0
    },
    {
        "category": "来自MIT的张永和优秀毕业生冯菲菲作品，让济南平庸的住房焕然一新",
        "quantity": 1.0
    },
    {
        "category": "风语空中别墅 / Penda",
        "quantity": 1.0
    },
    {
        "category": "受折纸启发的墨尔本大楼",
        "quantity": 1.0
    },
    {
        "category": "英良石材档案馆 / Atelier Alter",
        "quantity": 1.0
    },
    {
        "category": "Gang 建筑工作室为芝加哥全球公民学院设计的可持续性发展健康项目",
        "quantity": 1.0
    },
    {
        "category": "Napur Architect 建筑事务所为布达佩斯民族志博物馆设计的弓形建筑",
        "quantity": 1.0
    },
    {
        "category": "豪华度假村方案 / Make建筑事务所",
        "quantity": 1.0
    },
    {
        "category": "大卫·奇普菲尔德事务所公布了瑞典诺贝尔中心新效果图片",
        "quantity": 1.0
    },
    {
        "category": "虚幻作品第1号 / 天津大学建筑学院-非标准建筑工作室",
        "quantity": 1.0
    },
    {
        "category": "青云里居住艺术馆 / TEAM_BLDG",
        "quantity": 1.0
    },
    {
        "category": "可持续的梦幻岛启发 Group8asia 在首尔的梦之岛项目",
        "quantity": 1.0
    },
    {
        "category": "园区",
        "quantity": 1.0
    },
    {
        "category": "KAAN 以“开放的渗透”概念赢得阿姆斯特丹法院设计竞赛",
        "quantity": 1.0
    },
    {
        "category": "EFFEKT 和 karres+brands团队赢得竞赛，将丹麦罗斯基勒市工业废弃用地改造成充满活力的城市街区",
        "quantity": 1.0
    },
    {
        "category": "芜湖苏宁广场 / MG2",
        "quantity": 1.0
    },
    {
        "category": "White Arkitekter 设计谢莱夫特奥文化中心大楼，将成为北欧地区最高的木结构建筑",
        "quantity": 1.0
    },
    {
        "category": "C.F. Møller 设计的厄勒布鲁小木镇将城市融于自然",
        "quantity": 1.0
    },
    {
        "category": "Sabri Pasayigit设计工作室为土耳其开塞利市新区规划",
        "quantity": 1.0
    },
    {
        "category": "Pliskin Architecture 公布了以色列的音乐学校方案",
        "quantity": 1.0
    },
    {
        "category": "济州全球教育城布兰克森霍尔亚洲学校 / / Samoo Architects & Engineers建筑工程事务所",
        "quantity": 1.0
    },
    {
        "category": "WE Architecture 在奥尔胡斯结合了绿色空间与社会保障房的方案获奖",
        "quantity": 1.0
    },
    {
        "category": "Arquitectonica 在迈阿密设计了三段的住宅塔楼",
        "quantity": 1.0
    },
    {
        "category": "Mecanoo 事务所公布了台湾高雄绿色车站总体设计规划",
        "quantity": 1.0
    },
    {
        "category": "印度火葬场的神圣风景或“禁忌空间”",
        "quantity": 1.0
    },
    {
        "category": "城市 & 土地利用规划",
        "quantity": 1.0
    },
    {
        "category": "B’大厦 / Wiel Arets Architects",
        "quantity": 1.0
    },
    {
        "category": "瞭望塔",
        "quantity": 1.0
    },
    {
        "category": "Ennead Architects 设计了厦门的大型新音乐中心",
        "quantity": 1.0
    },
    {
        "category": "龙卷风造型的韩国流行音乐厅设计在首尔奥林匹克运动场改造竞赛中获胜",
        "quantity": 1.0
    },
    {
        "category": "流动的美感 / 游雅清空间设计",
        "quantity": 1.0
    },
    {
        "category": "COBE为科隆新港区设计的大型公共水池及瀑布",
        "quantity": 1.0
    },
    {
        "category": "位于中国温州的建筑设计学院获奖设计展示",
        "quantity": 1.0
    },
    {
        "category": "Architects for Urbanity建筑事务所在韩国首尔为新女性和家庭设计了新的综合设施 '城市子宫'",
        "quantity": 1.0
    },
    {
        "category": "Nabil Gholam Architects在沙特阿拉伯设计了特别的\"艺术绿洲\"",
        "quantity": 1.0
    },
    {
        "category": "The Martians Have Landed / LAVA",
        "quantity": 1.0
    },
    {
        "category": "意大利的峭崖中嵌入了一个自然圆形露天剧场",
        "quantity": 1.0
    }
];

def deleteNoContainMlhFieldItem():
    mongoclient = MongoSupport()
    mongoclient.db["scrapy_categorys"].insert_many(categorys)

if __name__ == '__main__':
    deleteNoContainMlhFieldItem()