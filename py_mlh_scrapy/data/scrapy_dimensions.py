from py_mlh_scrapy.helper.mongo_util import MongoSupport

dimensions = [
    {
        "item": "建筑师",
        "mlh": "建筑设计单位",
        "quantity": 9019.0
    },
    {
        "item": "地址",
        "mlh": "项目地址",
        "quantity": 8729.0
    },
    {
        "item": "摄影师",
        "mlh": "摄影",
        "quantity": 8260.0
    },
    {
        "item": "项目年份",
        "mlh": "建成时间",
        "quantity": 8059.0
    },
    {
        "item": "建筑面积",
        "mlh": "建筑面积",
        "quantity": 6876.0
    },
    {
        "item": "设计团队",
        "quantity": 1565.0
    },
    {
        "item": "厂家",
        "quantity": 1463.0
    },
    {
        "item": "客户",
        "mlh": "开发建设方",
        "quantity": 1285.0
    },
    {
        "item": "结构工程师",
        "mlh": "结构设计单位",
        "quantity": 1265.0
    },
    {
        "item": "项目团队",
        "quantity": 1021.0
    },
    {
        "item": "承包商",
        "mlh": "工程总承包",
        "quantity": 781.0
    },
    {
        "item": "合作者",
        "quantity": 729.0
    },
    {
        "item": "业主",
        "mlh": "开发建设方",
        "quantity": 584.0
    },
    {
        "item": "项目建筑师",
        "mlh": "建筑主创设计师",
        "quantity": 432.0
    },
    {
        "item": "总承包商",
        "mlh": "工程总承包",
        "quantity": 382.0
    },
    {
        "item": "项目经理",
        "quantity": 342.0
    },
    {
        "item": "结构",
        "mlh": "结构设计单位",
        "quantity": 329.0
    },
    {
        "item": "室内设计",
        "mlh": "室内设计单位",
        "quantity": 315.0
    },
    {
        "item": "工程师",
        "quantity": 311.0
    },
    {
        "item": "主持建筑师",
        "mlh": "建筑主创设计师",
        "quantity": 306.0
    },
    {
        "item": "首席建筑师",
        "mlh": "建筑主创设计师",
        "quantity": 305.0
    },
    {
        "item": "景观设计",
        "mlh": "景观设计单位",
        "quantity": 302.0
    },
    {
        "item": "预算",
        "mlh": "投资总额",
        "quantity": 296.0
    },
    {
        "item": "结构工程",
        "mlh": "结构设计单位",
        "quantity": 287.0
    },
    {
        "item": "主任建筑师",
        "mlh": "建筑主创设计师",
        "quantity": 268.0
    },
    {
        "item": "场地面积",
        "mlh": "占地面积",
        "quantity": 263.0
    },
    {
        "item": "景观设计师",
        "mlh": "景观主创设计师",
        "quantity": 238.0
    },
    {
        "item": "景观建筑师",
        "mlh": "景观主创设计师",
        "quantity": 235.0
    },
    {
        "item": "面积",
        "mlh": "建筑面积",
        "quantity": 221.0
    },
    {
        "item": "null",
        "quantity": 215.0
    },
    {
        "item": "结构设计",
        "mlh": "结构设计单位",
        "quantity": 208.0
    },
    {
        "item": "主创建筑师",
        "mlh": "建筑主创设计师",
        "quantity": 189.0
    },
    {
        "item": "建筑商",
        "mlh": "施工单位",
        "quantity": 186.0
    },
    {
        "item": "施工",
        "mlh": "施工单位",
        "quantity": 186.0
    },
    {
        "item": "摄影",
        "mlh": "摄影",
        "quantity": 179.0
    },
    {
        "item": "总建筑师",
        "mlh": "建筑主创设计师",
        "quantity": 159.0
    },
    {
        "item": "景观",
        "mlh": "景观设计单位",
        "quantity": 138.0
    },
    {
        "item": "团队",
        "quantity": 133.0
    },
    {
        "item": "机械工程师",
        "quantity": 130.0
    },
    {
        "item": "项目管理",
        "quantity": 129.0
    },
    {
        "item": "照明设计",
        "quantity": 126.0
    },
    {
        "item": "土木工程师",
        "quantity": 123.0
    },
    {
        "item": "室内设计师",
        "mlh": "室内主创设计师",
        "quantity": 122.0
    },
    {
        "item": "顾问",
        "quantity": 121.0
    },
    {
        "item": "设计师",
        "quantity": 115.0
    },
    {
        "item": "电气工程师",
        "mlh": "电气工程师",
        "quantity": 113.0
    },
    {
        "item": "开发商",
        "mlh": "开发建设方",
        "quantity": 111.0
    },
    {
        "item": "灯光设计",
        "quantity": 107.0
    },
    {
        "item": "建筑师负责人",
        "quantity": 106.0
    },
    {
        "item": "结构顾问",
        "mlh": "结构设计单位",
        "quantity": 105.0
    },
    {
        "item": "合作建筑师",
        "quantity": 102.0
    },
    {
        "item": "Client",
        "mlh": "开发建设方",
        "quantity": 96.0
    },
    {
        "item": "机电工程师",
        "quantity": 94.0
    },
    {
        "item": "工程",
        "quantity": 94.0
    },
    {
        "item": "责任建筑师",
        "quantity": 93.0
    },
    {
        "item": "项目负责人",
        "quantity": 93.0
    },
    {
        "item": "项目面积",
        "mlh": "建筑面积",
        "quantity": 91.0
    },
    {
        "item": "建造",
        "mlh": "施工单位",
        "quantity": 91.0
    },
    {
        "item": "施工方",
        "mlh": "施工单位",
        "quantity": 86.0
    },
    {
        "item": "位置",
        "mlh": "项目地址",
        "quantity": 86.0
    },
    {
        "item": "合作方",
        "quantity": 86.0
    },
    {
        "item": "项目位置",
        "mlh": "项目地址",
        "quantity": 84.0
    },
    {
        "item": "主建筑师",
        "mlh": "建筑主创设计师",
        "quantity": 81.0
    },
    {
        "item": "建造者",
        "mlh": "施工单位",
        "quantity": 81.0
    },
    {
        "item": "年份",
        "mlh": "建成时间",
        "quantity": 78.0
    },
    {
        "item": "照明",
        "quantity": 76.0
    },
    {
        "item": "负责建筑师",
        "quantity": 75.0
    },
    {
        "item": "Design Team",
        "quantity": 72.0
    },
    {
        "item": "占地面积",
        "mlh": "占地面积",
        "quantity": 71.0
    },
    {
        "item": "技术建筑师",
        "quantity": 67.0
    },
    {
        "item": "建筑设计",
        "mlh": "建筑设计单位",
        "quantity": 66.0
    },
    {
        "item": "承包人",
        "mlh": "工程总承包",
        "quantity": 65.0
    },
    {
        "item": "声学",
        "quantity": 65.0
    },
    {
        "item": "Architect",
        "mlh": "建筑主创设计师",
        "quantity": 65.0
    },
    {
        "item": "Project Team",
        "quantity": 64.0
    },
    {
        "item": "委托人",
        "mlh": "投资方",
        "quantity": 60.0
    },
    {
        "item": "土木工程",
        "quantity": 59.0
    },
    {
        "item": "主管建筑师",
        "quantity": 58.0
    },
    {
        "item": "作者",
        "quantity": 58.0
    },
    {
        "item": "甲方",
        "mlh": "开发建设方",
        "quantity": 56.0
    },
    {
        "item": "合伙人",
        "quantity": 55.0
    },
    {
        "item": "Contractor",
        "quantity": 54.0
    },
    {
        "item": "地点",
        "mlh": "项目地址",
        "quantity": 54.0
    },
    {
        "item": "项目业主",
        "mlh": "投资方",
        "quantity": 53.0
    },
    {
        "item": "成本",
        "mlh": "投资总额",
        "quantity": 53.0
    },
    {
        "item": "总建筑面积",
        "mlh": "建筑面积",
        "quantity": 53.0
    },
    {
        "item": "平面设计",
        "quantity": 52.0
    },
    {
        "item": "Architect in Charge",
        "quantity": 52.0
    },
    {
        "item": "设备工程师",
        "quantity": 52.0
    },
    {
        "item": "承建商",
        "mlh": "工程总承包",
        "quantity": 52.0
    },
    {
        "item": "助理建筑师",
        "quantity": 51.0
    },
    {
        "item": "照明顾问",
        "quantity": 51.0
    },
    {
        "item": "声学顾问",
        "quantity": 49.0
    },
    {
        "item": "设备",
        "quantity": 49.0
    },
    {
        "item": "施工管理",
        "mlh": "施工单位",
        "quantity": 48.0
    },
    {
        "item": "合作伙伴",
        "quantity": 48.0
    },
    {
        "item": "Structural Engineer",
        "mlh": "结构工程师",
        "quantity": 48.0
    },
    {
        "item": "施工技术员",
        "quantity": 47.0
    },
    {
        "item": "设计总监",
        "quantity": 47.0
    },
    {
        "item": "施工单位",
        "mlh": "施工单位",
        "quantity": 46.0
    },
    {
        "item": "造价",
        "mlh": "投资总额",
        "quantity": 46.0
    },
    {
        "item": "设计",
        "mlh": "建筑设计单位",
        "quantity": 45.0
    },
    {
        "item": "建造商",
        "mlh": "施工单位",
        "quantity": 44.0
    },
    {
        "item": "灯光设计师",
        "quantity": 44.0
    },
    {
        "item": "电力工程师",
        "mlh": "电气工程师",
        "quantity": 43.0
    },
    {
        "item": "基地面积",
        "mlh": "占地面积",
        "quantity": 41.0
    },
    {
        "item": "当地建筑师",
        "quantity": 41.0
    },
    {
        "item": "机械工程",
        "quantity": 41.0
    },
    {
        "item": "地段面积",
        "mlh": "占地面积",
        "quantity": 41.0
    },
    {
        "item": "项目设计师",
        "mlh": "建筑主创设计师",
        "quantity": 40.0
    },
    {
        "item": "建筑事务所",
        "mlh": "建筑设计单位",
        "quantity": 40.0
    },
    {
        "item": "主创设计师",
        "mlh": "建筑主创设计师",
        "quantity": 40.0
    },
    {
        "item": "声学设计",
        "quantity": 40.0
    },
    {
        "item": "建筑物理",
        "quantity": 40.0
    },
    {
        "item": "建筑公司",
        "mlh": "施工单位",
        "quantity": 40.0
    },
    {
        "item": "项目负责建筑师",
        "mlh": "建筑主创设计师",
        "quantity": 39.0
    },
    {
        "item": "建设",
        "mlh": "施工单位",
        "quantity": 39.0
    },
    {
        "item": "主要承包商",
        "mlh": "工程总承包",
        "quantity": 39.0
    },
    {
        "item": "电气工程",
        "mlh": "电气工程师",
        "quantity": 39.0
    },
    {
        "item": "项目总监",
        "quantity": 38.0
    },
    {
        "item": "艺术家",
        "quantity": 37.0
    },
    {
        "item": "施工经理",
        "quantity": 36.0
    },
    {
        "item": "用地面积",
        "mlh": "占地面积",
        "quantity": 36.0
    },
    {
        "item": "项目",
        "quantity": 36.0
    },
    {
        "item": "室内",
        "mlh": "室内主创设计师",
        "quantity": 36.0
    },
    {
        "item": "记录建筑师",
        "quantity": 36.0
    },
    {
        "item": "服务工程师",
        "quantity": 35.0
    },
    {
        "item": "项目主管",
        "quantity": 35.0
    },
    {
        "item": "合作",
        "quantity": 35.0
    },
    {
        "item": "照明设计师",
        "quantity": 34.0
    },
    {
        "item": "Collaborators",
        "quantity": 34.0
    },
    {
        "item": "项目领导",
        "quantity": 33.0
    },
    {
        "item": "结构设计师",
        "mlh": "结构工程师",
        "quantity": 33.0
    },
    {
        "item": "木工",
        "quantity": 32.0
    },
    {
        "item": "家具",
        "quantity": 31.0
    },
    {
        "item": "合作团队",
        "quantity": 30.0
    },
    {
        "item": "设计时间",
        "mlh": "设计时间",
        "quantity": 30.0
    },
    {
        "item": "承包商 ",
        "mlh": "工程总承包",
        "quantity": 30.0
    },
    {
        "item": "建造方",
        "mlh": "施工单位",
        "quantity": 29.0
    },
    {
        "item": "设计建筑师",
        "mlh": "建筑主创设计师",
        "quantity": 29.0
    },
    {
        "item": "主持设计师",
        "mlh": "建筑主创设计师",
        "quantity": 29.0
    },
    {
        "item": "主设计师",
        "mlh": "建筑主创设计师",
        "quantity": 29.0
    },
    {
        "item": "建设管理",
        "quantity": 28.0
    },
    {
        "item": "执行建筑师",
        "quantity": 28.0
    },
    {
        "item": "质量监测",
        "mlh": "监理单位",
        "quantity": 27.0
    },
    {
        "item": "负责人",
        "quantity": 27.0
    },
    {
        "item": "建筑设计师",
        "mlh": "建筑主创设计师",
        "quantity": 27.0
    },
    {
        "item": "建筑承包商",
        "mlh": "工程总承包",
        "quantity": 27.0
    },
    {
        "item": "模型",
        "quantity": 27.0
    },
    {
        "item": "电气设计",
        "mlh": "电气工程师",
        "quantity": 27.0
    },
    {
        "item": "总承包人",
        "quantity": 27.0
    },
    {
        "item": "材料",
        "quantity": 26.0
    },
    {
        "item": "施工团队",
        "mlh": "施工单位",
        "quantity": 26.0
    },
    {
        "item": "总面积",
        "mlh": "建筑面积",
        "quantity": 26.0
    },
    {
        "item": "结构师",
        "mlh": "结构工程师",
        "quantity": 25.0
    },
    {
        "item": "安装",
        "quantity": 25.0
    },
    {
        "item": "委托方",
        "mlh": "投资方",
        "quantity": 25.0
    },
    {
        "item": "参考",
        "quantity": 25.0
    },
    {
        "item": "发起人",
        "quantity": 25.0
    },
    {
        "item": "建筑工程师",
        "mlh": "建筑主创设计师",
        "quantity": 25.0
    },
    {
        "item": "建造师",
        "quantity": 25.0
    },
    {
        "item": "其他参与者",
        "quantity": 25.0
    },
    {
        "item": "服务",
        "quantity": 25.0
    },
    {
        "item": "项目时间",
        "mlh": "建成时间",
        "quantity": 24.0
    },
    {
        "item": "电气",
        "mlh": "电气工程师",
        "quantity": 24.0
    },
    {
        "item": "室内建筑师",
        "mlh": "室内主创设计师",
        "quantity": 24.0
    },
    {
        "item": "Architects in Charge",
        "mlh": "建筑主创设计师",
        "quantity": 23.0
    },
    {
        "item": "市政工程师",
        "quantity": 23.0
    },
    {
        "item": "主承包商",
        "mlh": "工程总承包",
        "quantity": 23.0
    },
    {
        "item": "首席设计师",
        "mlh": "建筑主创设计师",
        "quantity": 23.0
    },
    {
        "item": "Site Area",
        "mlh": "占地面积",
        "quantity": 23.0
    },
    {
        "item": "建筑团队",
        "mlh": "建筑设计单位",
        "quantity": 23.0
    },
    {
        "item": "立面顾问",
        "quantity": 23.0
    },
    {
        "item": "花费",
        "mlh": "投资总额",
        "quantity": 23.0
    },
    {
        "item": "项目预算",
        "mlh": "投资总额",
        "quantity": 21.0
    },
    {
        "item": "规划顾问",
        "mlh": "规划设计单位",
        "quantity": 21.0
    },
    {
        "item": "景观顾问",
        "mlh": "景观设计单位",
        "quantity": 21.0
    },
    {
        "item": "灯光",
        "quantity": 20.0
    },
    {
        "item": "装置",
        "quantity": 20.0
    },
    {
        "item": "Budget",
        "mlh": "投资总额",
        "quantity": 20.0
    },
    {
        "item": "项目造价",
        "mlh": "投资总额",
        "quantity": 20.0
    },
    {
        "item": "竞赛团队",
        "quantity": 20.0
    },
    {
        "item": "协作者",
        "quantity": 20.0
    },
    {
        "item": "供稿人",
        "quantity": 19.0
    },
    {
        "item": "结构计算",
        "mlh": "结构设计单位",
        "quantity": 19.0
    },
    {
        "item": "建筑服务",
        "quantity": 19.0
    },
    {
        "item": "主要负责人",
        "quantity": 19.0
    },
    {
        "item": "Project Manager",
        "quantity": 19.0
    },
    {
        "item": "合作商",
        "quantity": 19.0
    },
    {
        "item": "音响设计",
        "quantity": 18.0
    },
    {
        "item": "声学工程师",
        "quantity": 18.0
    },
    {
        "item": "设计负责人",
        "quantity": 18.0
    },
    {
        "item": "钢结构",
        "quantity": 18.0
    },
    {
        "item": "建筑师团队",
        "quantity": 17.0
    },
    {
        "item": "Structure",
        "mlh": "结构设计单位",
        "quantity": 17.0
    },
    {
        "item": "施工监理",
        "mlh": "监理单位",
        "quantity": 17.0
    },
    {
        "item": "总设计师",
        "quantity": 17.0
    },
    {
        "item": "Project Architect",
        "mlh": "建筑主创设计师",
        "quantity": 17.0
    },
    {
        "item": "建筑负责人",
        "mlh": "建筑主创设计师",
        "quantity": 17.0
    },
    {
        "item": "立面",
        "quantity": 17.0
    },
    {
        "item": "承包者",
        "mlh": "工程总承包",
        "quantity": 17.0
    },
    {
        "item": "机械",
        "quantity": 17.0
    },
    {
        "item": "工程管理",
        "quantity": 16.0
    },
    {
        "item": "助理",
        "quantity": 16.0
    },
    {
        "item": "景观工程师",
        "mlh": "景观主创设计师",
        "quantity": 16.0
    },
    {
        "item": "电力工程",
        "mlh": "电气设计单位",
        "quantity": 16.0
    },
    {
        "item": "机电工程",
        "mlh": "暖通设计单位",
        "quantity": 16.0
    },
    {
        "item": "机电管道工程师",
        "mlh": "暖通工程师",
        "quantity": 16.0
    },
    {
        "item": "Construction",
        "mlh": "施工单位",
        "quantity": 16.0
    },
    {
        "item": "电力",
        "mlh": "电气设计单位",
        "quantity": 16.0
    },
    {
        "item": "竣工时间",
        "mlh": "建成时间",
        "quantity": 16.0
    },
    {
        "item": "测绘",
        "quantity": 16.0
    },
    {
        "item": "总承建商",
        "mlh": "工程总承包",
        "quantity": 16.0
    },
    {
        "item": "总承包",
        "mlh": "工程总承包",
        "quantity": 15.0
    },
    {
        "item": "Arquitectos",
        "mlh": "建筑设计单位",
        "quantity": 15.0
    },
    {
        "item": "设施",
        "quantity": 15.0
    },
    {
        "item": "环境工程师",
        "mlh": "景观主创设计师",
        "quantity": 15.0
    },
    {
        "item": "机电顾问",
        "quantity": 15.0
    },
    {
        "item": "Landscape Architect",
        "mlh": "景观主创设计师",
        "quantity": 15.0
    },
    {
        "item": "灯光顾问",
        "quantity": 15.0
    },
    {
        "item": "主要材料",
        "quantity": 15.0
    },
    {
        "item": "项目类型",
        "mlh": "项目类型",
        "quantity": 15.0
    },
    {
        "item": "工程设计",
        "quantity": 15.0
    },
    {
        "item": "建设单位",
        "mlh": "施工单位",
        "quantity": 15.0
    },
    {
        "item": "Fotografías",
        "quantity": 15.0
    },
    {
        "item": "咨询公司",
        "quantity": 15.0
    },
    {
        "item": "建筑高度",
        "quantity": 15.0
    },
    {
        "item": "家具设计",
        "quantity": 15.0
    },
    {
        "item": "Structural Engineering",
        "mlh": "结构工程师",
        "quantity": 14.0
    },
    {
        "item": "General Contractor",
        "quantity": 14.0
    },
    {
        "item": "合作设计",
        "quantity": 14.0
    },
    {
        "item": "环境设计",
        "quantity": 14.0
    },
    {
        "item": "合作人",
        "quantity": 14.0
    },
    {
        "item": "规划",
        "mlh": "规划设计单位",
        "quantity": 14.0
    },
    {
        "item": "本地建筑师",
        "quantity": 14.0
    },
    {
        "item": "Ubicación",
        "quantity": 14.0
    },
    {
        "item": "建筑年份",
        "mlh": "建成时间",
        "quantity": 14.0
    },
    {
        "item": "Constructor",
        "quantity": 14.0
    },
    {
        "item": "工程顾问",
        "quantity": 14.0
    },
    {
        "item": "团队成员",
        "quantity": 14.0
    },
    {
        "item": "建筑设备",
        "quantity": 14.0
    },
    {
        "item": "暖通空调",
        "mlh": "暖通设计单位",
        "quantity": 14.0
    },
    {
        "item": "赞助商",
        "mlh": "投资方",
        "quantity": 14.0
    },
    {
        "item": "合作者 ",
        "quantity": 14.0
    },
    {
        "item": "环境顾问",
        "quantity": 14.0
    },
    {
        "item": "类型",
        "mlh": "建筑类型",
        "quantity": 13.0
    },
    {
        "item": "功能",
        "quantity": 13.0
    },
    {
        "item": "质量监督",
        "quantity": 13.0
    },
    {
        "item": "立面设计",
        "quantity": 13.0
    },
    {
        "item": "Main Contractor",
        "quantity": 13.0
    },
    {
        "item": "空调系统",
        "quantity": 13.0
    },
    {
        "item": "幕墙顾问",
        "quantity": 13.0
    },
    {
        "item": "消防顾问",
        "quantity": 13.0
    },
    {
        "item": "项目协调",
        "quantity": 13.0
    },
    {
        "item": "音响效果",
        "quantity": 13.0
    },
    {
        "item": "建造公司",
        "mlh": "施工单位",
        "quantity": 13.0
    },
    {
        "item": "建筑",
        "quantity": 12.0
    },
    {
        "item": "主要承包人",
        "quantity": 12.0
    },
    {
        "item": "Electrical Engineer",
        "mlh": "电气工程师",
        "quantity": 12.0
    },
    {
        "item": "监理",
        "mlh": "监理单位",
        "quantity": 12.0
    },
    {
        "item": "项目组",
        "quantity": 12.0
    },
    {
        "item": "构造",
        "quantity": 12.0
    },
    {
        "item": "咨询",
        "quantity": 12.0
    },
    {
        "item": "Año Proyecto",
        "quantity": 12.0
    },
    {
        "item": "项目负责",
        "quantity": 12.0
    },
    {
        "item": "机械设计",
        "quantity": 12.0
    },
    {
        "item": "年期",
        "quantity": 12.0
    },
    {
        "item": "投资方",
        "mlh": "投资方",
        "quantity": 11.0
    },
    {
        "item": "混凝土结构",
        "quantity": 11.0
    },
    {
        "item": "安装顾问",
        "quantity": 11.0
    },
    {
        "item": "MEP",
        "mlh": "暖通设计单位",
        "quantity": 11.0
    },
    {
        "item": "合作单位",
        "quantity": 11.0
    },
    {
        "item": "设备工程",
        "mlh": "暖通设计单位",
        "quantity": 11.0
    },
    {
        "item": "效果图",
        "quantity": 11.0
    },
    {
        "item": "主管",
        "quantity": 11.0
    },
    {
        "item": "协调",
        "quantity": 11.0
    },
    {
        "item": "规划师",
        "quantity": 11.0
    },
    {
        "item": "木匠",
        "quantity": 11.0
    },
    {
        "item": "项目顾问",
        "quantity": 11.0
    },
    {
        "item": "电气顾问",
        "quantity": 11.0
    },
    {
        "item": "成本顾问",
        "quantity": 11.0
    },
    {
        "item": "Mechanical Engineer",
        "quantity": 11.0
    },
    {
        "item": "项目设计",
        "quantity": 11.0
    },
    {
        "item": "项目指导",
        "quantity": 11.0
    },
    {
        "item": "施工公司",
        "mlh": "施工单位",
        "quantity": 11.0
    },
    {
        "item": "外观设计",
        "quantity": 11.0
    },
    {
        "item": "MEP 工程师",
        "mlh": "暖通工程师",
        "quantity": 11.0
    },
    {
        "item": "能源顾问",
        "quantity": 11.0
    },
    {
        "item": "市政工程",
        "quantity": 11.0
    },
    {
        "item": "项目地址",
        "quantity": 11.0
    },
    {
        "item": "机械顾问",
        "quantity": 11.0
    },
    {
        "item": "主持合伙人",
        "quantity": 10.0
    },
    {
        "item": "建筑工程",
        "quantity": 10.0
    },
    {
        "item": "项目组长",
        "quantity": 10.0
    },
    {
        "item": "建设公司",
        "quantity": 10.0
    },
    {
        "item": "防火",
        "quantity": 10.0
    },
    {
        "item": "机电",
        "quantity": 10.0
    },
    {
        "item": "建造团队",
        "quantity": 10.0
    },
    {
        "item": "投资者",
        "quantity": 10.0
    },
    {
        "item": "渲染",
        "quantity": 10.0
    },
    {
        "item": "完成时间",
        "mlh": "建成时间",
        "quantity": 10.0
    },
    {
        "item": "展览设计",
        "quantity": 10.0
    },
    {
        "item": "声学工程",
        "quantity": 10.0
    },
    {
        "item": "模型制作",
        "quantity": 10.0
    },
    {
        "item": "造价顾问",
        "quantity": 10.0
    },
    {
        "item": "董事",
        "quantity": 10.0
    },
    {
        "item": "建筑顾问",
        "quantity": 10.0
    },
    {
        "item": "设计单位",
        "quantity": 10.0
    },
    {
        "item": "设计主管",
        "quantity": 10.0
    },
    {
        "item": "图形设计",
        "quantity": 10.0
    },
    {
        "item": "费用",
        "quantity": 10.0
    },
    {
        "item": "Engineering",
        "quantity": 10.0
    },
    {
        "item": "服务顾问",
        "quantity": 10.0
    },
    {
        "item": "Civil Engineer",
        "quantity": 10.0
    },
    {
        "item": "尺寸",
        "quantity": 10.0
    },
    {
        "item": "建造单位",
        "quantity": 10.0
    },
    {
        "item": "合作伙伴负责人",
        "quantity": 10.0
    },
    {
        "item": "合作作者",
        "quantity": 10.0
    },
    {
        "item": "电梯",
        "quantity": 10.0
    },
    {
        "item": "景观承包商",
        "quantity": 10.0
    },
    {
        "item": "参与者",
        "quantity": 10.0
    },
    {
        "item": "结构咨询",
        "quantity": 9.0
    },
    {
        "item": "建造时间",
        "quantity": 9.0
    },
    {
        "item": "结构方",
        "quantity": 9.0
    },
    {
        "item": "项目助理",
        "quantity": 9.0
    },
    {
        "item": "工料测量师",
        "quantity": 9.0
    },
    {
        "item": "室内承包商",
        "quantity": 9.0
    },
    {
        "item": "监督",
        "quantity": 9.0
    },
    {
        "item": "Builder",
        "quantity": 9.0
    },
    {
        "item": "实习生",
        "quantity": 9.0
    },
    {
        "item": "交通顾问",
        "quantity": 9.0
    },
    {
        "item": "投资商",
        "quantity": 9.0
    },
    {
        "item": "暖通工程师",
        "quantity": 9.0
    },
    {
        "item": "电气安装",
        "quantity": 9.0
    },
    {
        "item": "投资人",
        "quantity": 9.0
    },
    {
        "item": "建筑测量师",
        "quantity": 9.0
    },
    {
        "item": "室内设计团队",
        "quantity": 9.0
    },
    {
        "item": "技术顾问",
        "quantity": 9.0
    },
    {
        "item": "施工时间",
        "quantity": 9.0
    },
    {
        "item": "当地设计院",
        "quantity": 9.0
    },
    {
        "item": "技术设计",
        "quantity": 9.0
    },
    {
        "item": "建筑管理",
        "quantity": 9.0
    },
    {
        "item": "景观建筑",
        "quantity": 9.0
    },
    {
        "item": "文本",
        "quantity": 9.0
    },
    {
        "item": "业主代表",
        "quantity": 9.0
    },
    {
        "item": "灯光工程师",
        "quantity": 9.0
    },
    {
        "item": "项目管理团队",
        "quantity": 9.0
    },
    {
        "item": "室内装饰",
        "quantity": 9.0
    },
    {
        "item": "设备设计",
        "quantity": 9.0
    },
    {
        "item": "施工顾问",
        "quantity": 8.0
    },
    {
        "item": "设计周期",
        "quantity": 8.0
    },
    {
        "item": "所有者",
        "quantity": 8.0
    },
    {
        "item": "立面工程师",
        "quantity": 8.0
    },
    {
        "item": "供应商",
        "quantity": 8.0
    },
    {
        "item": "机电设计",
        "quantity": 8.0
    },
    {
        "item": "总楼面面积",
        "quantity": 8.0
    },
    {
        "item": "岩土工程师",
        "quantity": 8.0
    },
    {
        "item": "技术控制",
        "quantity": 8.0
    },
    {
        "item": "高度",
        "quantity": 8.0
    },
    {
        "item": "Colaboradores",
        "quantity": 8.0
    },
    {
        "item": "给排水工程师",
        "quantity": 8.0
    },
    {
        "item": "防火工程",
        "quantity": 8.0
    },
    {
        "item": "系统工程师",
        "quantity": 8.0
    },
    {
        "item": "施工队",
        "quantity": 8.0
    },
    {
        "item": "总工程师",
        "quantity": 8.0
    },
    {
        "item": "经济",
        "quantity": 8.0
    },
    {
        "item": "制图",
        "quantity": 8.0
    },
    {
        "item": "项目合伙人",
        "quantity": 8.0
    },
    {
        "item": "Área",
        "quantity": 8.0
    },
    {
        "item": "结构系统",
        "quantity": 8.0
    },
    {
        "item": "Structural Engineers",
        "quantity": 8.0
    },
    {
        "item": "Consultants",
        "quantity": 8.0
    },
    {
        "item": "绘图",
        "quantity": 8.0
    },
    {
        "item": "总体规划",
        "quantity": 8.0
    },
    {
        "item": "参考资料",
        "quantity": 8.0
    },
    {
        "item": "建筑工程管理",
        "quantity": 8.0
    },
    {
        "item": "平面设计师",
        "quantity": 8.0
    },
    {
        "item": "空调",
        "quantity": 8.0
    },
    {
        "item": "工程造价",
        "quantity": 8.0
    },
    {
        "item": "总监",
        "quantity": 8.0
    },
    {
        "item": "设计小组",
        "quantity": 8.0
    },
    {
        "item": "可持续发展顾问",
        "quantity": 8.0
    },
    {
        "item": "设备顾问",
        "quantity": 8.0
    },
    {
        "item": "概念设计",
        "quantity": 8.0
    },
    {
        "item": "Interior Design",
        "quantity": 8.0
    },
    {
        "item": "技术工程师",
        "quantity": 8.0
    },
    {
        "item": "垂直交通",
        "quantity": 8.0
    },
    {
        "item": "总承包商 ",
        "quantity": 8.0
    },
    {
        "item": "土地面积",
        "quantity": 8.0
    },
    {
        "item": "可持续性",
        "quantity": 8.0
    },
    {
        "item": "Cost",
        "quantity": 8.0
    },
    {
        "item": "设计主持",
        "quantity": 7.0
    },
    {
        "item": "软件",
        "quantity": 7.0
    },
    {
        "item": "主创设计",
        "quantity": 7.0
    },
    {
        "item": "参与设计",
        "quantity": 7.0
    },
    {
        "item": "容积率",
        "quantity": 7.0
    },
    {
        "item": "Collaborator",
        "quantity": 7.0
    },
    {
        "item": "顾问公司",
        "quantity": 7.0
    },
    {
        "item": "场地管理",
        "quantity": 7.0
    },
    {
        "item": "照明设计顾问",
        "quantity": 7.0
    },
    {
        "item": "项目设计团队",
        "quantity": 7.0
    },
    {
        "item": "顾问工程师",
        "quantity": 7.0
    },
    {
        "item": "合作艺术家",
        "quantity": 7.0
    },
    {
        "item": "景观师",
        "quantity": 7.0
    },
    {
        "item": "宣传",
        "quantity": 7.0
    },
    {
        "item": "设计伙伴",
        "quantity": 7.0
    },
    {
        "item": "建造面积",
        "quantity": 7.0
    },
    {
        "item": "光环境设计",
        "quantity": 7.0
    },
    {
        "item": "Lighting",
        "quantity": 7.0
    },
    {
        "item": "建成年份",
        "quantity": 7.0
    },
    {
        "item": "学生",
        "quantity": 7.0
    },
    {
        "item": "施工承包商",
        "quantity": 7.0
    },
    {
        "item": "木结构",
        "quantity": 7.0
    },
    {
        "item": "给排水",
        "quantity": 7.0
    },
    {
        "item": "发展商",
        "quantity": 7.0
    },
    {
        "item": "MEP工程师",
        "quantity": 7.0
    },
    {
        "item": "估算师",
        "quantity": 7.0
    },
    {
        "item": "经济学家",
        "quantity": 7.0
    },
    {
        "item": "项目成员",
        "quantity": 7.0
    },
    {
        "item": "创意总监",
        "quantity": 7.0
    },
    {
        "item": "Interior Designer",
        "quantity": 7.0
    },
    {
        "item": "项目地点",
        "quantity": 7.0
    },
    {
        "item": "Team",
        "quantity": 7.0
    },
    {
        "item": "协调员",
        "quantity": 7.0
    },
    {
        "item": "总花费",
        "quantity": 7.0
    },
    {
        "item": "设计助理",
        "quantity": 7.0
    },
    {
        "item": "策展人",
        "quantity": 7.0
    },
    {
        "item": "装配",
        "quantity": 7.0
    },
    {
        "item": "标识设计",
        "quantity": 7.0
    },
    {
        "item": "景观设计顾问",
        "quantity": 7.0
    },
    {
        "item": "展陈设计",
        "quantity": 7.0
    },
    {
        "item": "主要建筑师",
        "quantity": 7.0
    },
    {
        "item": "视频",
        "quantity": 7.0
    },
    {
        "item": "Architects",
        "quantity": 7.0
    },
    {
        "item": "建筑设计团队",
        "quantity": 7.0
    },
    {
        "item": "Landscape",
        "quantity": 7.0
    },
    {
        "item": "水力工程师",
        "quantity": 7.0
    },
    {
        "item": "建筑技术",
        "quantity": 7.0
    },
    {
        "item": "建成时间",
        "quantity": 7.0
    },
    {
        "item": "剧院顾问",
        "quantity": 7.0
    },
    {
        "item": "遗产顾问",
        "quantity": 7.0
    },
    {
        "item": "土建工程师",
        "quantity": 7.0
    },
    {
        "item": "电工",
        "quantity": 7.0
    },
    {
        "item": "助手",
        "quantity": 7.0
    },
    {
        "item": "室内设计顾问",
        "quantity": 7.0
    },
    {
        "item": "项目成本",
        "quantity": 7.0
    },
    {
        "item": "电力系统",
        "quantity": 7.0
    },
    {
        "item": "图片",
        "quantity": 7.0
    },
    {
        "item": "其他合伙人",
        "quantity": 6.0
    },
    {
        "item": "主持设计",
        "quantity": 6.0
    },
    {
        "item": "Quantity Surveyor",
        "quantity": 6.0
    },
    {
        "item": "幕墙",
        "quantity": 6.0
    },
    {
        "item": "现场监理",
        "quantity": 6.0
    },
    {
        "item": "其他顾问",
        "quantity": 6.0
    },
    {
        "item": "景观建筑师 ",
        "quantity": 6.0
    },
    {
        "item": "厨房",
        "quantity": 6.0
    },
    {
        "item": "地基",
        "quantity": 6.0
    },
    {
        "item": "使用者",
        "quantity": 6.0
    },
    {
        "item": "Engineers",
        "quantity": 6.0
    },
    {
        "item": "资金额",
        "quantity": 6.0
    },
    {
        "item": "开发者",
        "quantity": 6.0
    },
    {
        "item": "代码顾问",
        "quantity": 6.0
    },
    {
        "item": "Principal In Charge",
        "quantity": 6.0
    },
    {
        "item": "建筑总面积",
        "quantity": 6.0
    },
    {
        "item": "References",
        "quantity": 6.0
    },
    {
        "item": "层数",
        "quantity": 6.0
    },
    {
        "item": "建成面积",
        "quantity": 6.0
    },
    {
        "item": "土地测量师",
        "quantity": 6.0
    },
    {
        "item": "责任合伙人",
        "quantity": 6.0
    },
    {
        "item": "安全顾问",
        "quantity": 6.0
    },
    {
        "item": "顾问团队",
        "quantity": 6.0
    },
    {
        "item": "建造年份",
        "quantity": 6.0
    },
    {
        "item": "标志设计",
        "quantity": 6.0
    },
    {
        "item": "暖通空调设计",
        "quantity": 6.0
    },
    {
        "item": "经济师",
        "quantity": 6.0
    },
    {
        "item": "施工监督",
        "quantity": 6.0
    },
    {
        "item": "管道",
        "quantity": 6.0
    },
    {
        "item": "服务工程",
        "quantity": 6.0
    },
    {
        "item": "Project Architects",
        "quantity": 6.0
    },
    {
        "item": "认证",
        "quantity": 6.0
    },
    {
        "item": "艺术",
        "quantity": 6.0
    },
    {
        "item": "施工成本",
        "quantity": 6.0
    },
    {
        "item": "预算顾问",
        "quantity": 6.0
    },
    {
        "item": "工程经理",
        "quantity": 6.0
    },
    {
        "item": "客户 ",
        "quantity": 6.0
    },
    {
        "item": "声效",
        "quantity": 6.0
    },
    {
        "item": "首层面积",
        "quantity": 6.0
    },
    {
        "item": "Installations",
        "quantity": 6.0
    },
    {
        "item": "建造成本",
        "quantity": 6.0
    },
    {
        "item": "立面工程",
        "quantity": 6.0
    },
    {
        "item": "安装公司",
        "quantity": 6.0
    },
    {
        "item": "城市设计",
        "quantity": 6.0
    },
    {
        "item": "项目工程师",
        "quantity": 6.0
    },
    {
        "item": "金属结构",
        "quantity": 6.0
    },
    {
        "item": "结构设计顾问",
        "quantity": 6.0
    },
    {
        "item": "消防",
        "quantity": 6.0
    },
    {
        "item": "土建工程",
        "quantity": 6.0
    },
    {
        "item": "业主 ",
        "quantity": 6.0
    },
    {
        "item": "参考文献",
        "quantity": 6.0
    },
    {
        "item": "电机工程",
        "quantity": 6.0
    },
    {
        "item": "灯光设计顾问",
        "quantity": 6.0
    },
    {
        "item": "表面积",
        "quantity": 6.0
    },
    {
        "item": "厨房设计",
        "quantity": 6.0
    },
    {
        "item": "承包方",
        "quantity": 6.0
    },
    {
        "item": "调研",
        "quantity": 6.0
    },
    {
        "item": "电力设计",
        "quantity": 6.0
    },
    {
        "item": "照片",
        "quantity": 6.0
    },
    {
        "item": "Investor",
        "quantity": 6.0
    },
    {
        "item": "可持续性发展",
        "quantity": 6.0
    },
    {
        "item": "暖通",
        "quantity": 6.0
    },
    {
        "item": "市政",
        "quantity": 5.0
    },
    {
        "item": "技术团队",
        "quantity": 5.0
    },
    {
        "item": "导师",
        "quantity": 5.0
    },
    {
        "item": "安全",
        "quantity": 5.0
    },
    {
        "item": "立面承包商",
        "quantity": 5.0
    },
    {
        "item": "管理",
        "quantity": 5.0
    },
    {
        "item": "学生团队",
        "quantity": 5.0
    },
    {
        "item": "光学顾问",
        "quantity": 5.0
    },
    {
        "item": "副建筑师",
        "quantity": 5.0
    },
    {
        "item": "技术",
        "quantity": 5.0
    },
    {
        "item": "岩土工程",
        "quantity": 5.0
    },
    {
        "item": "艺术指导",
        "quantity": 5.0
    },
    {
        "item": "总经理",
        "quantity": 5.0
    },
    {
        "item": "主案设计",
        "quantity": 5.0
    },
    {
        "item": "项目内容",
        "quantity": 5.0
    },
    {
        "item": "电器工程",
        "quantity": 5.0
    },
    {
        "item": "标准顾问",
        "quantity": 5.0
    },
    {
        "item": "体积",
        "quantity": 5.0
    },
    {
        "item": "总成本",
        "quantity": 5.0
    },
    {
        "item": "执行",
        "quantity": 5.0
    },
    {
        "item": "暖通空调工程师",
        "quantity": 5.0
    },
    {
        "item": "流体工程师",
        "quantity": 5.0
    },
    {
        "item": "土地测绘",
        "quantity": 5.0
    },
    {
        "item": "Construction Manager",
        "quantity": 5.0
    },
    {
        "item": "Equipo de Diseño",
        "quantity": 5.0
    },
    {
        "item": "LEED顾问",
        "quantity": 5.0
    },
    {
        "item": "厨房顾问",
        "quantity": 5.0
    },
    {
        "item": "暖通工程",
        "quantity": 5.0
    },
    {
        "item": "建筑结构",
        "quantity": 5.0
    },
    {
        "item": "贡献者",
        "quantity": 5.0
    },
    {
        "item": "Developer",
        "quantity": 5.0
    },
    {
        "item": "餐饮顾问",
        "quantity": 5.0
    },
    {
        "item": "景观面积",
        "quantity": 5.0
    },
    {
        "item": "高级设计师",
        "quantity": 5.0
    },
    {
        "item": "Designer",
        "quantity": 5.0
    },
    {
        "item": "主导建筑师",
        "quantity": 5.0
    },
    {
        "item": "建筑成本",
        "quantity": 5.0
    },
    {
        "item": "房屋勘测员",
        "quantity": 5.0
    },
    {
        "item": "技术检验",
        "quantity": 5.0
    },
    {
        "item": "交通工程",
        "quantity": 5.0
    },
    {
        "item": "设计人员",
        "quantity": 5.0
    },
    {
        "item": "规模",
        "quantity": 5.0
    },
    {
        "item": "高级建筑师",
        "quantity": 5.0
    },
    {
        "item": "总楼层面积",
        "quantity": 5.0
    },
    {
        "item": "可持续顾问",
        "quantity": 5.0
    },
    {
        "item": "城市规划",
        "quantity": 5.0
    },
    {
        "item": "流体工程",
        "quantity": 5.0
    },
    {
        "item": "装修",
        "quantity": 5.0
    },
    {
        "item": "Partner In Charge",
        "quantity": 5.0
    },
    {
        "item": "Architect In Charge",
        "quantity": 5.0
    },
    {
        "item": "Designers",
        "quantity": 5.0
    },
    {
        "item": "停车场",
        "quantity": 5.0
    },
    {
        "item": "管道设计",
        "quantity": 5.0
    },
    {
        "item": "给排水设计",
        "quantity": 5.0
    },
    {
        "item": "建设成本",
        "quantity": 5.0
    },
    {
        "item": "电器工程师",
        "quantity": 5.0
    },
    {
        "item": "副总建筑师",
        "quantity": 5.0
    },
    {
        "item": "Design Principal",
        "quantity": 5.0
    },
    {
        "item": "管理团队",
        "quantity": 5.0
    },
    {
        "item": "剧场顾问",
        "quantity": 5.0
    },
    {
        "item": "机械装置",
        "quantity": 5.0
    },
    {
        "item": "建筑合作者",
        "quantity": 5.0
    },
    {
        "item": "生态顾问",
        "quantity": 5.0
    },
    {
        "item": "管道工程",
        "quantity": 5.0
    },
    {
        "item": "Architecture",
        "quantity": 5.0
    },
    {
        "item": "建设时间",
        "quantity": 5.0
    },
    {
        "item": "Associate Architect",
        "quantity": 5.0
    },
    {
        "item": "工料测量",
        "quantity": 5.0
    },
    {
        "item": "设计者",
        "quantity": 5.0
    },
    {
        "item": "防火工程师",
        "quantity": 5.0
    },
    {
        "item": "建筑服务工程师",
        "quantity": 5.0
    },
    {
        "item": "管道工程师",
        "quantity": 5.0
    },
    {
        "item": "项目合作者",
        "quantity": 5.0
    },
    {
        "item": "机械电气工程师",
        "quantity": 5.0
    },
    {
        "item": "基础承包商",
        "quantity": 5.0
    },
    {
        "item": "电力顾问",
        "quantity": 5.0
    },
    {
        "item": "结构工程师 ",
        "quantity": 5.0
    },
    {
        "item": "造价估算",
        "quantity": 5.0
    },
    {
        "item": "视觉传达",
        "quantity": 5.0
    },
    {
        "item": "建设团队",
        "quantity": 5.0
    },
    {
        "item": "制造商",
        "quantity": 5.0
    },
    {
        "item": "建设顾问",
        "quantity": 5.0
    },
    {
        "item": "设计顾问",
        "quantity": 5.0
    },
    {
        "item": "技术咨询",
        "quantity": 5.0
    },
    {
        "item": "合作设计院",
        "quantity": 5.0
    },
    {
        "item": "音效",
        "quantity": 5.0
    },
    {
        "item": "项目作者",
        "quantity": 5.0
    },
    {
        "item": "灯光咨询",
        "quantity": 5.0
    },
    {
        "item": "建设者",
        "quantity": 5.0
    },
    {
        "item": "Interiors Designers",
        "quantity": 5.0
    },
    {
        "item": "结构公司",
        "quantity": 5.0
    },
    {
        "item": "音响设计师",
        "quantity": 5.0
    },
    {
        "item": "餐饮服务",
        "quantity": 5.0
    },
    {
        "item": "成本核算",
        "quantity": 5.0
    },
    {
        "item": "机电管道设计",
        "quantity": 5.0
    },
    {
        "item": "景观咨询",
        "quantity": 5.0
    },
    {
        "item": "现场经理",
        "quantity": 5.0
    },
    {
        "item": "主任设计师",
        "quantity": 5.0
    },
    {
        "item": "驻场建筑师",
        "quantity": 5.0
    },
    {
        "item": "合作公司",
        "quantity": 5.0
    },
    {
        "item": "文字",
        "quantity": 5.0
    },
    {
        "item": "装配工",
        "quantity": 5.0
    },
    {
        "item": "交通",
        "quantity": 5.0
    },
    {
        "item": "机电管道工程",
        "quantity": 5.0
    },
    {
        "item": "完工时间",
        "quantity": 4.0
    },
    {
        "item": "电器",
        "quantity": 4.0
    },
    {
        "item": "作者建筑师",
        "quantity": 4.0
    },
    {
        "item": "总承包方",
        "quantity": 4.0
    },
    {
        "item": "设备/给排水工程师",
        "quantity": 4.0
    },
    {
        "item": "装置设计",
        "quantity": 4.0
    },
    {
        "item": "预算师",
        "quantity": 4.0
    },
    {
        "item": "机械管道工程师",
        "quantity": 4.0
    },
    {
        "item": "规划设计",
        "quantity": 4.0
    },
    {
        "item": "机电管道",
        "quantity": 4.0
    },
    {
        "item": "设计经理",
        "quantity": 4.0
    },
    {
        "item": "竞赛年份",
        "quantity": 4.0
    },
    {
        "item": "自动化",
        "quantity": 4.0
    },
    {
        "item": "节能顾问",
        "quantity": 4.0
    },
    {
        "item": "玻璃",
        "quantity": 4.0
    },
    {
        "item": "一层面积",
        "quantity": 4.0
    },
    {
        "item": "木结构工程师",
        "quantity": 4.0
    },
    {
        "item": "生物气候顾问",
        "quantity": 4.0
    },
    {
        "item": "总费用",
        "quantity": 4.0
    },
    {
        "item": "音效顾问",
        "quantity": 4.0
    },
    {
        "item": "可持续设计",
        "quantity": 4.0
    },
    {
        "item": "环境工程",
        "quantity": 4.0
    },
    {
        "item": "园林绿化",
        "quantity": 4.0
    },
    {
        "item": "结构工程设计",
        "quantity": 4.0
    },
    {
        "item": "结构和土木工程师",
        "quantity": 4.0
    },
    {
        "item": "总预算",
        "quantity": 4.0
    },
    {
        "item": "质量控制",
        "quantity": 4.0
    },
    {
        "item": "Building area",
        "quantity": 4.0
    },
    {
        "item": "木结构设计",
        "quantity": 4.0
    },
    {
        "item": "造价工程师",
        "quantity": 4.0
    },
    {
        "item": "设计年份",
        "quantity": 4.0
    },
    {
        "item": "Materials",
        "quantity": 4.0
    },
    {
        "item": "LDI",
        "quantity": 4.0
    },
    {
        "item": "Principal Architect",
        "quantity": 4.0
    },
    {
        "item": "Authors",
        "quantity": 4.0
    },
    {
        "item": "工程服务",
        "quantity": 4.0
    },
    {
        "item": "照明工程师",
        "quantity": 4.0
    },
    {
        "item": "Engineer",
        "quantity": 4.0
    },
    {
        "item": "时间",
        "quantity": 4.0
    },
    {
        "item": "主要设计师",
        "quantity": 4.0
    },
    {
        "item": "景观建筑设计",
        "quantity": 4.0
    },
    {
        "item": "助理设计师",
        "quantity": 4.0
    },
    {
        "item": "设备与电力",
        "quantity": 4.0
    },
    {
        "item": "测量师",
        "quantity": 4.0
    },
    {
        "item": "水电风工程",
        "quantity": 4.0
    },
    {
        "item": "合约商",
        "quantity": 4.0
    },
    {
        "item": "合伙建筑师",
        "quantity": 4.0
    },
    {
        "item": "卫生工程",
        "quantity": 4.0
    },
    {
        "item": "总承包者",
        "quantity": 4.0
    },
    {
        "item": "协调建筑师",
        "quantity": 4.0
    },
    {
        "item": "Construction Management",
        "quantity": 4.0
    },
    {
        "item": "基础工程",
        "quantity": 4.0
    },
    {
        "item": "木作",
        "quantity": 4.0
    },
    {
        "item": "艺术设计",
        "quantity": 4.0
    },
    {
        "item": "管理伙伴",
        "quantity": 4.0
    },
    {
        "item": "电路设计",
        "quantity": 4.0
    },
    {
        "item": "工程监理",
        "quantity": 4.0
    },
    {
        "item": "建筑监理",
        "quantity": 4.0
    },
    {
        "item": "施工面积",
        "quantity": 4.0
    },
    {
        "item": "灯光师",
        "quantity": 4.0
    },
    {
        "item": "地质技术",
        "quantity": 4.0
    },
    {
        "item": "测量和预算",
        "quantity": 4.0
    },
    {
        "item": "项目经理 ",
        "quantity": 4.0
    },
    {
        "item": "屋顶",
        "quantity": 4.0
    },
    {
        "item": "空间设计",
        "quantity": 4.0
    },
    {
        "item": "合作设计师",
        "quantity": 4.0
    },
    {
        "item": "年",
        "quantity": 4.0
    },
    {
        "item": "土木结构",
        "quantity": 4.0
    },
    {
        "item": "Program",
        "quantity": 4.0
    },
    {
        "item": "舞台设计",
        "quantity": 4.0
    },
    {
        "item": "土建承包商",
        "quantity": 4.0
    },
    {
        "item": "景观设计顾问 ",
        "quantity": 4.0
    },
    {
        "item": "艺术总监",
        "quantity": 4.0
    },
    {
        "item": "工程建造",
        "quantity": 4.0
    },
    {
        "item": "景观施工",
        "quantity": 4.0
    },
    {
        "item": "使用面积",
        "quantity": 4.0
    },
    {
        "item": "施工人员",
        "quantity": 4.0
    },
    {
        "item": "Promotor",
        "quantity": 4.0
    },
    {
        "item": "木工制作",
        "quantity": 4.0
    },
    {
        "item": "绘画",
        "quantity": 4.0
    },
    {
        "item": "Lighting Designer",
        "quantity": 4.0
    },
    {
        "item": "消防工程师",
        "quantity": 4.0
    },
    {
        "item": "测量员",
        "quantity": 4.0
    },
    {
        "item": "建筑表面积",
        "quantity": 4.0
    },
    {
        "item": "其他合作伙伴",
        "quantity": 4.0
    },
    {
        "item": "毛建筑面积",
        "quantity": 4.0
    },
    {
        "item": "照明工程",
        "quantity": 4.0
    },
    {
        "item": "建筑物理顾问",
        "quantity": 4.0
    },
    {
        "item": "电梯顾问",
        "quantity": 4.0
    },
    {
        "item": "和伙伴",
        "quantity": 4.0
    },
    {
        "item": "Project Area",
        "quantity": 4.0
    },
    {
        "item": "项目合作",
        "quantity": 4.0
    },
    {
        "item": "技术指导",
        "quantity": 4.0
    },
    {
        "item": "接哦股",
        "quantity": 4.0
    },
    {
        "item": "钢结构设计",
        "quantity": 4.0
    },
    {
        "item": "检验员",
        "quantity": 4.0
    },
    {
        "item": "工程咨询",
        "quantity": 4.0
    },
    {
        "item": "总规划师",
        "quantity": 4.0
    },
    {
        "item": "协调者",
        "quantity": 4.0
    },
    {
        "item": "环境",
        "quantity": 4.0
    },
    {
        "item": "土木",
        "quantity": 4.0
    },
    {
        "item": "建筑类型",
        "quantity": 4.0
    },
    {
        "item": "景观设计团队",
        "quantity": 4.0
    },
    {
        "item": "主要功能",
        "quantity": 4.0
    },
    {
        "item": "内部设计",
        "quantity": 4.0
    },
    {
        "item": "项目完成时间",
        "quantity": 4.0
    },
    {
        "item": "造价师",
        "quantity": 4.0
    },
    {
        "item": "电气承包商",
        "quantity": 4.0
    },
    {
        "item": "建设预算",
        "quantity": 4.0
    },
    {
        "item": "幕墙承包商",
        "quantity": 4.0
    },
    {
        "item": "翻译",
        "quantity": 4.0
    },
    {
        "item": "现场管理",
        "quantity": 4.0
    },
    {
        "item": "场地经理",
        "quantity": 4.0
    },
    {
        "item": "水利工程师",
        "quantity": 4.0
    },
    {
        "item": "基础设施",
        "quantity": 4.0
    },
    {
        "item": "首席顾问",
        "quantity": 4.0
    },
    {
        "item": "建筑测量",
        "quantity": 4.0
    },
    {
        "item": "室内装修",
        "quantity": 4.0
    },
    {
        "item": "防火顾问",
        "quantity": 4.0
    },
    {
        "item": "设计合伙人",
        "quantity": 4.0
    },
    {
        "item": "外观设计顾问",
        "quantity": 4.0
    },
    {
        "item": "合作工程师",
        "quantity": 4.0
    },
    {
        "item": "透视图",
        "quantity": 4.0
    },
    {
        "item": "价值",
        "quantity": 4.0
    },
    {
        "item": "视觉化",
        "quantity": 4.0
    },
    {
        "item": "预算估计",
        "quantity": 4.0
    },
    {
        "item": "场地",
        "quantity": 4.0
    },
    {
        "item": "建筑和室内设计",
        "quantity": 4.0
    },
    {
        "item": "M&E 工程师",
        "quantity": 4.0
    },
    {
        "item": "总平面面积",
        "quantity": 4.0
    },
    {
        "item": "安装工程",
        "quantity": 4.0
    },
    {
        "item": "木工艺",
        "quantity": 3.0
    },
    {
        "item": "HVAC",
        "quantity": 3.0
    },
    {
        "item": "容量",
        "quantity": 3.0
    },
    {
        "item": "建筑项目团队",
        "quantity": 3.0
    },
    {
        "item": "楼层",
        "quantity": 3.0
    },
    {
        "item": "标识系统",
        "quantity": 3.0
    },
    {
        "item": "水力设计",
        "quantity": 3.0
    },
    {
        "item": "厨房专家",
        "quantity": 3.0
    },
    {
        "item": "特别感谢",
        "quantity": 3.0
    },
    {
        "item": "建筑测绘",
        "quantity": 3.0
    },
    {
        "item": "设备与给排水",
        "quantity": 3.0
    },
    {
        "item": "支持",
        "quantity": 3.0
    },
    {
        "item": "当地建筑师 ",
        "quantity": 3.0
    },
    {
        "item": "文案",
        "quantity": 3.0
    },
    {
        "item": "木材工程师",
        "quantity": 3.0
    },
    {
        "item": "设计主创",
        "quantity": 3.0
    },
    {
        "item": "空间性质",
        "quantity": 3.0
    },
    {
        "item": "建筑师合伙人",
        "quantity": 3.0
    },
    {
        "item": "造价预算",
        "quantity": 3.0
    },
    {
        "item": "建筑师助理",
        "quantity": 3.0
    },
    {
        "item": "声学效果",
        "quantity": 3.0
    },
    {
        "item": "建筑师合作伙伴",
        "quantity": 3.0
    },
    {
        "item": "合作创始人",
        "quantity": 3.0
    },
    {
        "item": "创始人",
        "quantity": 3.0
    },
    {
        "item": "项目控制",
        "quantity": 3.0
    },
    {
        "item": "协调管理",
        "quantity": 3.0
    },
    {
        "item": "楼层数",
        "quantity": 3.0
    },
    {
        "item": "中方合作设计单位",
        "quantity": 3.0
    },
    {
        "item": "参与设计师",
        "quantity": 3.0
    },
    {
        "item": "入口顾问",
        "quantity": 3.0
    },
    {
        "item": "照明设计团队",
        "quantity": 3.0
    },
    {
        "item": "施工周期",
        "quantity": 3.0
    },
    {
        "item": "花园设计",
        "quantity": 3.0
    },
    {
        "item": "洁具",
        "quantity": 3.0
    },
    {
        "item": "实施阶段项目负责人",
        "quantity": 3.0
    },
    {
        "item": "竞赛阶段项目负责人",
        "quantity": 3.0
    },
    {
        "item": "文章",
        "quantity": 3.0
    },
    {
        "item": "项目管理 ",
        "quantity": 3.0
    },
    {
        "item": "项目花费",
        "quantity": 3.0
    },
    {
        "item": "结构和土木工程",
        "quantity": 3.0
    },
    {
        "item": "木框架",
        "quantity": 3.0
    },
    {
        "item": "施工者",
        "quantity": 3.0
    },
    {
        "item": "建成年代",
        "quantity": 3.0
    },
    {
        "item": "工程团队",
        "quantity": 3.0
    },
    {
        "item": "Landscape Design",
        "quantity": 3.0
    },
    {
        "item": "幕墙施工",
        "quantity": 3.0
    },
    {
        "item": "客户顾问",
        "quantity": 3.0
    },
    {
        "item": "规格",
        "quantity": 3.0
    },
    {
        "item": "表皮",
        "quantity": 3.0
    },
    {
        "item": "物理模型",
        "quantity": 3.0
    },
    {
        "item": "施工技术人员",
        "quantity": 3.0
    },
    {
        "item": "主要负责",
        "quantity": 3.0
    },
    {
        "item": "工程建设",
        "quantity": 3.0
    },
    {
        "item": "木材",
        "quantity": 3.0
    },
    {
        "item": "结构工程顾问",
        "quantity": 3.0
    },
    {
        "item": "合同价值",
        "quantity": 3.0
    },
    {
        "item": "地质工程",
        "quantity": 3.0
    },
    {
        "item": "水利工程",
        "quantity": 3.0
    },
    {
        "item": "项目日期",
        "quantity": 3.0
    },
    {
        "item": "静态项目",
        "quantity": 3.0
    },
    {
        "item": "经济顾问",
        "quantity": 3.0
    },
    {
        "item": "主任伙伴",
        "quantity": 3.0
    },
    {
        "item": "建筑密度",
        "quantity": 3.0
    },
    {
        "item": "厂商",
        "quantity": 3.0
    },
    {
        "item": "Floor Area",
        "quantity": 3.0
    },
    {
        "item": "交通工程师",
        "quantity": 3.0
    },
    {
        "item": "造价咨询",
        "quantity": 3.0
    },
    {
        "item": "承包公司",
        "quantity": 3.0
    },
    {
        "item": "幕墙设计",
        "quantity": 3.0
    },
    {
        "item": "体量",
        "quantity": 3.0
    },
    {
        "item": "咨询建筑师",
        "quantity": 3.0
    },
    {
        "item": "建造周期",
        "quantity": 3.0
    },
    {
        "item": "业主和开发商",
        "quantity": 3.0
    },
    {
        "item": "Landscape Architects",
        "quantity": 3.0
    },
    {
        "item": "竞赛阶段设计人员",
        "quantity": 3.0
    },
    {
        "item": "设计公司",
        "quantity": 3.0
    },
    {
        "item": "预算内",
        "quantity": 3.0
    },
    {
        "item": "水电工程师",
        "quantity": 3.0
    },
    {
        "item": "组织者",
        "quantity": 3.0
    },
    {
        "item": "景观规划",
        "quantity": 3.0
    },
    {
        "item": "工程面积",
        "quantity": 3.0
    },
    {
        "item": "项目施工",
        "quantity": 3.0
    },
    {
        "item": "建筑规范顾问",
        "quantity": 3.0
    },
    {
        "item": "项目承包商",
        "quantity": 3.0
    },
    {
        "item": "音响",
        "quantity": 3.0
    },
    {
        "item": "监工",
        "quantity": 3.0
    },
    {
        "item": "艺术合作",
        "quantity": 3.0
    },
    {
        "item": "项目统筹",
        "quantity": 3.0
    },
    {
        "item": "建筑预算",
        "quantity": 3.0
    },
    {
        "item": "装饰",
        "quantity": 3.0
    },
    {
        "item": "方案",
        "quantity": 3.0
    },
    {
        "item": "LEED 认证",
        "quantity": 3.0
    },
    {
        "item": "主要设计人员",
        "quantity": 3.0
    },
    {
        "item": "设计合作伙伴",
        "quantity": 3.0
    },
    {
        "item": "设计组",
        "quantity": 3.0
    },
    {
        "item": "CDM协调员",
        "quantity": 3.0
    },
    {
        "item": "首席工程师",
        "quantity": 3.0
    },
    {
        "item": "电气设计师",
        "quantity": 3.0
    },
    {
        "item": "声音设计",
        "quantity": 3.0
    },
    {
        "item": "博物馆顾问",
        "quantity": 3.0
    },
    {
        "item": "联合建筑师",
        "quantity": 3.0
    },
    {
        "item": "土建",
        "quantity": 3.0
    },
    {
        "item": " Collaborators",
        "quantity": 3.0
    },
    {
        "item": "管道系统",
        "quantity": 3.0
    },
    {
        "item": "施工技术员 ",
        "quantity": 3.0
    },
    {
        "item": "窗户",
        "quantity": 3.0
    },
    {
        "item": "Structures",
        "quantity": 3.0
    },
    {
        "item": "C&S 工程师",
        "quantity": 3.0
    },
    {
        "item": "项目执行",
        "quantity": 3.0
    },
    {
        "item": "造型",
        "quantity": 3.0
    },
    {
        "item": "土木顾问",
        "quantity": 3.0
    },
    {
        "item": "Acoustic",
        "quantity": 3.0
    },
    {
        "item": "宽度",
        "quantity": 3.0
    },
    {
        "item": "Project Leader",
        "quantity": 3.0
    },
    {
        "item": "Project Management",
        "quantity": 3.0
    },
    {
        "item": "Building Contractor",
        "quantity": 3.0
    },
    {
        "item": "业主及运营者",
        "quantity": 3.0
    },
    {
        "item": "指导",
        "quantity": 3.0
    },
    {
        "item": "长度",
        "quantity": 3.0
    },
    {
        "item": "场地监督",
        "quantity": 3.0
    },
    {
        "item": "外观工程师",
        "quantity": 3.0
    },
    {
        "item": "岩土工程顾问",
        "quantity": 3.0
    },
    {
        "item": "机械和电气工程师",
        "quantity": 3.0
    },
    {
        "item": "图像设计",
        "quantity": 3.0
    },
    {
        "item": "施工年份",
        "quantity": 3.0
    },
    {
        "item": "建设花费",
        "quantity": 3.0
    },
    {
        "item": "其他合作者",
        "quantity": 3.0
    },
    {
        "item": "管道顾问",
        "quantity": 3.0
    },
    {
        "item": "管理合作伙伴",
        "quantity": 3.0
    },
    {
        "item": "项目管理人",
        "quantity": 3.0
    },
    {
        "item": "承建方",
        "quantity": 3.0
    },
    {
        "item": "机电咨询",
        "quantity": 3.0
    },
    {
        "item": "工程公司",
        "quantity": 3.0
    },
    {
        "item": "设计内容",
        "quantity": 3.0
    },
    {
        "item": "楼层面积",
        "quantity": 3.0
    },
    {
        "item": "Project Director",
        "quantity": 3.0
    },
    {
        "item": "项目经历",
        "quantity": 3.0
    },
    {
        "item": "可持续",
        "quantity": 3.0
    },
    {
        "item": "经济咨询",
        "quantity": 3.0
    },
    {
        "item": "Total Floor Area",
        "quantity": 3.0
    },
    {
        "item": "设计指导",
        "quantity": 3.0
    },
    {
        "item": "展览",
        "quantity": 3.0
    },
    {
        "item": "MEP 工程",
        "quantity": 3.0
    },
    {
        "item": "协调人",
        "quantity": 3.0
    },
    {
        "item": "照明咨询",
        "quantity": 3.0
    },
    {
        "item": "Mep",
        "quantity": 3.0
    },
    {
        "item": "Lighting Design",
        "quantity": 3.0
    },
    {
        "item": "LEED 认证顾问",
        "quantity": 3.0
    },
    {
        "item": "赞助者",
        "quantity": 3.0
    },
    {
        "item": "成本估算",
        "quantity": 3.0
    },
    {
        "item": "可持续性顾问",
        "quantity": 3.0
    },
    {
        "item": "土木和结构工程师",
        "quantity": 3.0
    },
    {
        "item": "概念",
        "quantity": 3.0
    },
    {
        "item": "基金会",
        "quantity": 3.0
    },
    {
        "item": "图片提供",
        "quantity": 3.0
    },
    {
        "item": "主要设计团队",
        "quantity": 3.0
    },
    {
        "item": "绘图员",
        "quantity": 3.0
    },
    {
        "item": "空间规划",
        "quantity": 3.0
    },
    {
        "item": "外墙顾问",
        "quantity": 3.0
    },
    {
        "item": "规划监督",
        "quantity": 3.0
    },
    {
        "item": "工作团队",
        "quantity": 3.0
    },
    {
        "item": "美术师",
        "quantity": 3.0
    },
    {
        "item": "LEED认证",
        "quantity": 3.0
    },
    {
        "item": "基础",
        "quantity": 3.0
    },
    {
        "item": "估价师",
        "quantity": 3.0
    },
    {
        "item": "建造工程师",
        "quantity": 3.0
    },
    {
        "item": "围护结构",
        "quantity": 3.0
    },
    {
        "item": "室外",
        "quantity": 3.0
    },
    {
        "item": "建筑体积",
        "quantity": 3.0
    },
    {
        "item": "结构体系",
        "quantity": 3.0
    },
    {
        "item": "技术监督",
        "quantity": 3.0
    },
    {
        "item": "钢结构承包商",
        "quantity": 3.0
    },
    {
        "item": "状态",
        "quantity": 3.0
    },
    {
        "item": "施工图",
        "quantity": 3.0
    },
    {
        "item": "经理",
        "quantity": 3.0
    },
    {
        "item": "用途",
        "quantity": 3.0
    },
    {
        "item": "电力服务",
        "quantity": 3.0
    },
    {
        "item": "礼堂",
        "quantity": 3.0
    },
    {
        "item": "太阳能",
        "quantity": 3.0
    },
    {
        "item": "电气装置",
        "quantity": 3.0
    },
    {
        "item": "技术设备",
        "quantity": 3.0
    },
    {
        "item": "获奖",
        "quantity": 3.0
    },
    {
        "item": "工地监管",
        "quantity": 3.0
    },
    {
        "item": "草图",
        "quantity": 3.0
    },
    {
        "item": "木制品",
        "quantity": 3.0
    },
    {
        "item": "气候工程师",
        "quantity": 3.0
    },
    {
        "item": "制造",
        "quantity": 3.0
    },
    {
        "item": "标识顾问",
        "quantity": 3.0
    },
    {
        "item": "家庭自动化",
        "quantity": 3.0
    },
    {
        "item": "施工预算",
        "quantity": 3.0
    },
    {
        "item": "主要设计",
        "quantity": 3.0
    },
    {
        "item": "质量检测",
        "quantity": 3.0
    },
    {
        "item": "节点",
        "quantity": 3.0
    },
    {
        "item": "保护建筑师",
        "quantity": 3.0
    },
    {
        "item": "建造经理",
        "quantity": 3.0
    },
    {
        "item": "建设费用",
        "quantity": 3.0
    },
    {
        "item": "设计团队 ",
        "quantity": 3.0
    },
    {
        "item": "工程监管",
        "quantity": 3.0
    },
    {
        "item": "Construcción",
        "quantity": 3.0
    },
    {
        "item": "零售顾问",
        "quantity": 3.0
    },
    {
        "item": "赞助",
        "quantity": 3.0
    },
    {
        "item": "协助建筑师",
        "quantity": 3.0
    },
    {
        "item": "声学设计师",
        "quantity": 3.0
    },
    {
        "item": "项目小组",
        "quantity": 3.0
    },
    {
        "item": "建筑规模",
        "quantity": 3.0
    },
    {
        "item": "内部设计师",
        "quantity": 3.0
    },
    {
        "item": "主要材质",
        "quantity": 3.0
    },
    {
        "item": "客户助理",
        "quantity": 3.0
    },
    {
        "item": "家居设计",
        "quantity": 3.0
    },
    {
        "item": "使用软件",
        "quantity": 3.0
    },
    {
        "item": "施工设计",
        "quantity": 3.0
    },
    {
        "item": "数字模型",
        "quantity": 3.0
    },
    {
        "item": "园林设计",
        "quantity": 3.0
    },
    {
        "item": "协同者",
        "quantity": 3.0
    },
    {
        "item": "室外家具",
        "quantity": 3.0
    },
    {
        "item": "项目规模",
        "quantity": 3.0
    },
    {
        "item": "园艺师",
        "quantity": 3.0
    },
    {
        "item": "地形",
        "quantity": 3.0
    },
    {
        "item": "室外面积",
        "quantity": 3.0
    },
    {
        "item": "电子工程",
        "quantity": 3.0
    },
    {
        "item": "工程施工",
        "quantity": 3.0
    },
    {
        "item": "施工图设计",
        "quantity": 3.0
    },
    {
        "item": "机械及电气",
        "quantity": 3.0
    },
    {
        "item": "编码",
        "quantity": 3.0
    },
    {
        "item": "品牌顾问",
        "quantity": 3.0
    },
    {
        "item": "Millwork",
        "quantity": 3.0
    },
    {
        "item": "LEED",
        "quantity": 3.0
    },
    {
        "item": "室外装饰",
        "quantity": 3.0
    },
    {
        "item": "场地监理",
        "quantity": 3.0
    },
    {
        "item": "模型师",
        "quantity": 3.0
    },
    {
        "item": "地形测量",
        "quantity": 3.0
    },
    {
        "item": "土木结构工程师",
        "quantity": 3.0
    },
    {
        "item": "雕塑",
        "quantity": 3.0
    },
    {
        "item": "生产商",
        "quantity": 3.0
    },
    {
        "item": "项目主持",
        "quantity": 3.0
    },
    {
        "item": "执行董事",
        "quantity": 3.0
    },
    {
        "item": "金属工艺",
        "quantity": 3.0
    },
    {
        "item": "资金",
        "quantity": 3.0
    },
    {
        "item": "建筑施工",
        "quantity": 3.0
    },
    {
        "item": "管理公司",
        "quantity": 3.0
    },
    {
        "item": "导向系统",
        "quantity": 3.0
    },
    {
        "item": "技术总监",
        "quantity": 3.0
    },
    {
        "item": "形象设计",
        "quantity": 3.0
    },
    {
        "item": "专业",
        "quantity": 3.0
    },
    {
        "item": "水利顾问",
        "quantity": 3.0
    },
    {
        "item": "其它参与者",
        "quantity": 2.0
    },
    {
        "item": "规划咨询",
        "quantity": 2.0
    },
    {
        "item": "水景顾问",
        "quantity": 2.0
    },
    {
        "item": "教师",
        "quantity": 2.0
    },
    {
        "item": "视觉陈列",
        "quantity": 2.0
    },
    {
        "item": "施工期",
        "quantity": 2.0
    },
    {
        "item": "志愿者",
        "quantity": 2.0
    },
    {
        "item": "成本管理",
        "quantity": 2.0
    },
    {
        "item": "绿地率",
        "quantity": 2.0
    },
    {
        "item": "可视化",
        "quantity": 2.0
    },
    {
        "item": "室内灯光设计团队",
        "quantity": 2.0
    },
    {
        "item": "室内灯光顾问",
        "quantity": 2.0
    },
    {
        "item": "质量检查员",
        "quantity": 2.0
    },
    {
        "item": "Competition",
        "quantity": 2.0
    },
    {
        "item": "厨房工程师",
        "quantity": 2.0
    },
    {
        "item": "单位造价",
        "quantity": 2.0
    },
    {
        "item": "Collaborator Architects",
        "quantity": 2.0
    },
    {
        "item": "餐饮服务顾问",
        "quantity": 2.0
    },
    {
        "item": "机电管道设计顾问",
        "quantity": 2.0
    },
    {
        "item": "咨询顾问",
        "quantity": 2.0
    },
    {
        "item": "安全健康",
        "quantity": 2.0
    },
    {
        "item": "橱柜",
        "quantity": 2.0
    },
    {
        "item": "工程负责",
        "quantity": 2.0
    },
    {
        "item": "机械电气管道",
        "quantity": 2.0
    },
    {
        "item": "监测",
        "quantity": 2.0
    },
    {
        "item": "建筑师合作者",
        "quantity": 2.0
    },
    {
        "item": "项目组成员",
        "quantity": 2.0
    },
    {
        "item": "HVAC 工程",
        "quantity": 2.0
    },
    {
        "item": "考古学",
        "quantity": 2.0
    },
    {
        "item": "剧场",
        "quantity": 2.0
    },
    {
        "item": "生命安全",
        "quantity": 2.0
    },
    {
        "item": "生态系统",
        "quantity": 2.0
    },
    {
        "item": "施工现场监理",
        "quantity": 2.0
    },
    {
        "item": "交通设计",
        "quantity": 2.0
    },
    {
        "item": "继承权",
        "quantity": 2.0
    },
    {
        "item": "造型摄影",
        "quantity": 2.0
    },
    {
        "item": "结构机电设计",
        "quantity": 2.0
    },
    {
        "item": "数据",
        "quantity": 2.0
    },
    {
        "item": "渲染图",
        "quantity": 2.0
    },
    {
        "item": "排水",
        "quantity": 2.0
    },
    {
        "item": "视频编辑",
        "quantity": 2.0
    },
    {
        "item": "绿色认证",
        "quantity": 2.0
    },
    {
        "item": "亮化顾问",
        "quantity": 2.0
    },
    {
        "item": "室内面积",
        "quantity": 2.0
    },
    {
        "item": "概念团队",
        "quantity": 2.0
    },
    {
        "item": "现有建筑面积",
        "quantity": 2.0
    },
    {
        "item": "主持建筑",
        "quantity": 2.0
    },
    {
        "item": "土地测量员",
        "quantity": 2.0
    },
    {
        "item": "水力学",
        "quantity": 2.0
    },
    {
        "item": "绘图师",
        "quantity": 2.0
    },
    {
        "item": "建造花费",
        "quantity": 2.0
    },
    {
        "item": "BE结构",
        "quantity": 2.0
    },
    {
        "item": "室内团队",
        "quantity": 2.0
    },
    {
        "item": "投资建设",
        "quantity": 2.0
    },
    {
        "item": "次承包商",
        "quantity": 2.0
    },
    {
        "item": "Interior and furniture design",
        "quantity": 2.0
    },
    {
        "item": "项目目标",
        "quantity": 2.0
    },
    {
        "item": "项目开发商",
        "quantity": 2.0
    },
    {
        "item": "控制系统",
        "quantity": 2.0
    },
    {
        "item": "框架",
        "quantity": 2.0
    },
    {
        "item": "遮阳",
        "quantity": 2.0
    },
    {
        "item": "实验室规划",
        "quantity": 2.0
    },
    {
        "item": "技术协调",
        "quantity": 2.0
    },
    {
        "item": "机械工程师 ",
        "quantity": 2.0
    },
    {
        "item": "管工",
        "quantity": 2.0
    },
    {
        "item": "其余参与者",
        "quantity": 2.0
    },
    {
        "item": "建筑师助理支持",
        "quantity": 2.0
    },
    {
        "item": "试运行",
        "quantity": 2.0
    },
    {
        "item": "室内设计总监",
        "quantity": 2.0
    },
    {
        "item": "构建服务工程师",
        "quantity": 2.0
    },
    {
        "item": "流体工程 ",
        "quantity": 2.0
    },
    {
        "item": "结构/市政工程师",
        "quantity": 2.0
    },
    {
        "item": "设计管理",
        "quantity": 2.0
    },
    {
        "item": "设计类型",
        "quantity": 2.0
    },
    {
        "item": "机电管道设计师",
        "quantity": 2.0
    },
    {
        "item": "建筑设计公司",
        "quantity": 2.0
    },
    {
        "item": "人体工学",
        "quantity": 2.0
    },
    {
        "item": "建筑占地面积",
        "quantity": 2.0
    },
    {
        "item": "监控",
        "quantity": 2.0
    },
    {
        "item": "暖通顾问",
        "quantity": 2.0
    },
    {
        "item": "模型设计",
        "quantity": 2.0
    },
    {
        "item": "总用地面积",
        "quantity": 2.0
    },
    {
        "item": "舞台设计师",
        "quantity": 2.0
    },
    {
        "item": "土木设计",
        "quantity": 2.0
    },
    {
        "item": "液压顾问",
        "quantity": 2.0
    },
    {
        "item": "服务商",
        "quantity": 2.0
    },
    {
        "item": "电力装置",
        "quantity": 2.0
    },
    {
        "item": "修复",
        "quantity": 2.0
    },
    {
        "item": "当地设计机构",
        "quantity": 2.0
    },
    {
        "item": "稳定工程师",
        "quantity": 2.0
    },
    {
        "item": "垂直通道",
        "quantity": 2.0
    },
    {
        "item": "木材工艺",
        "quantity": 2.0
    },
    {
        "item": "建筑师联系人",
        "quantity": 2.0
    },
    {
        "item": "项目建筑师 ",
        "quantity": 2.0
    },
    {
        "item": "责任公司",
        "quantity": 2.0
    },
    {
        "item": "项目监理",
        "quantity": 2.0
    },
    {
        "item": "建设服务",
        "quantity": 2.0
    },
    {
        "item": "实施阶段设计人员",
        "quantity": 2.0
    },
    {
        "item": "橱柜设计",
        "quantity": 2.0
    },
    {
        "item": "合同方",
        "quantity": 2.0
    },
    {
        "item": "CDM合作者",
        "quantity": 2.0
    },
    {
        "item": "设备与电力工程师",
        "quantity": 2.0
    },
    {
        "item": "开发经理",
        "quantity": 2.0
    },
    {
        "item": "结构与市政工程",
        "quantity": 2.0
    },
    {
        "item": "计算工程师",
        "quantity": 2.0
    },
    {
        "item": "工程学",
        "quantity": 2.0
    },
    {
        "item": "LEED 顾问",
        "quantity": 2.0
    },
    {
        "item": "结构机电",
        "quantity": 2.0
    },
    {
        "item": "标准",
        "quantity": 2.0
    },
    {
        "item": "净建筑面积",
        "quantity": 2.0
    },
    {
        "item": "市政/结构/设备",
        "quantity": 2.0
    },
    {
        "item": "JCY项目团队",
        "quantity": 2.0
    },
    {
        "item": "电气项目",
        "quantity": 2.0
    },
    {
        "item": "细部设计团队",
        "quantity": 2.0
    },
    {
        "item": "结构/建筑服务工程",
        "quantity": 2.0
    },
    {
        "item": "助理项目建筑师",
        "quantity": 2.0
    },
    {
        "item": "结构团队",
        "quantity": 2.0
    },
    {
        "item": "赞助方",
        "quantity": 2.0
    },
    {
        "item": "陈述",
        "quantity": 2.0
    },
    {
        "item": "市政承包商",
        "quantity": 2.0
    },
    {
        "item": "泳池",
        "quantity": 2.0
    },
    {
        "item": "消防设计",
        "quantity": 2.0
    },
    {
        "item": "电机",
        "quantity": 2.0
    },
    {
        "item": "机电设备",
        "quantity": 2.0
    },
    {
        "item": "外墙设计",
        "quantity": 2.0
    },
    {
        "item": "结构机电工程师",
        "quantity": 2.0
    },
    {
        "item": "海拔",
        "quantity": 2.0
    },
    {
        "item": "实习建筑师",
        "quantity": 2.0
    },
    {
        "item": "总负责人",
        "quantity": 2.0
    },
    {
        "item": "主持合作者",
        "quantity": 2.0
    },
    {
        "item": "预算咨询",
        "quantity": 2.0
    },
    {
        "item": "Superficie Terreno",
        "quantity": 2.0
    },
    {
        "item": "Principals",
        "quantity": 2.0
    },
    {
        "item": "场地总面积",
        "quantity": 2.0
    },
    {
        "item": "规范",
        "quantity": 2.0
    },
    {
        "item": "电气系统",
        "quantity": 2.0
    },
    {
        "item": "水力顾问",
        "quantity": 2.0
    },
    {
        "item": "Structural",
        "quantity": 2.0
    },
    {
        "item": "协作建筑师",
        "quantity": 2.0
    },
    {
        "item": "视听顾问",
        "quantity": 2.0
    },
    {
        "item": "公司",
        "quantity": 2.0
    },
    {
        "item": "机械系统设计",
        "quantity": 2.0
    },
    {
        "item": "竣工日期",
        "quantity": 2.0
    },
    {
        "item": "结构物理",
        "quantity": 2.0
    },
    {
        "item": "Structural Design ",
        "quantity": 2.0
    },
    {
        "item": "Instalaciones",
        "quantity": 2.0
    },
    {
        "item": "土木/岩土工程师",
        "quantity": 2.0
    },
    {
        "item": "机械电气顾问",
        "quantity": 2.0
    },
    {
        "item": "楼面总面积",
        "quantity": 2.0
    },
    {
        "item": "水工程师",
        "quantity": 2.0
    },
    {
        "item": "钢结构工程师",
        "quantity": 2.0
    },
    {
        "item": "项目城市",
        "quantity": 2.0
    },
    {
        "item": "项目支持",
        "quantity": 2.0
    },
    {
        "item": "Leed",
        "quantity": 2.0
    },
    {
        "item": "财务",
        "quantity": 2.0
    },
    {
        "item": "技术图纸",
        "quantity": 2.0
    },
    {
        "item": "项目性质",
        "quantity": 2.0
    },
    {
        "item": "设计合作",
        "quantity": 2.0
    },
    {
        "item": "公共艺术家",
        "quantity": 2.0
    },
    {
        "item": "工艺工程师",
        "quantity": 2.0
    },
    {
        "item": "结构与市政工程师",
        "quantity": 2.0
    },
    {
        "item": "结构材料",
        "quantity": 2.0
    },
    {
        "item": "Project Period",
        "quantity": 2.0
    },
    {
        "item": "Structure Design",
        "quantity": 2.0
    },
    {
        "item": "外部合作者",
        "quantity": 2.0
    },
    {
        "item": "Architect Of Record",
        "quantity": 2.0
    },
    {
        "item": "Architects In Charge",
        "quantity": 2.0
    },
    {
        "item": "Electrical Engineering",
        "quantity": 2.0
    },
    {
        "item": "单层面积",
        "quantity": 2.0
    },
    {
        "item": "结构与服务",
        "quantity": 2.0
    },
    {
        "item": "节能认证",
        "quantity": 2.0
    },
    {
        "item": "整理",
        "quantity": 2.0
    },
    {
        "item": "Acoustic Engineer",
        "quantity": 2.0
    },
    {
        "item": "可持续性咨询",
        "quantity": 2.0
    },
    {
        "item": "联合设计",
        "quantity": 2.0
    },
    {
        "item": "Technical Architect",
        "quantity": 2.0
    },
    {
        "item": "工程实践",
        "quantity": 2.0
    },
    {
        "item": "Interiors",
        "quantity": 2.0
    },
    {
        "item": "暖通空调工程",
        "quantity": 2.0
    },
    {
        "item": "专业负责人",
        "quantity": 2.0
    },
    {
        "item": "地段",
        "quantity": 2.0
    },
    {
        "item": "3D",
        "quantity": 2.0
    },
    {
        "item": "建设方",
        "quantity": 2.0
    },
    {
        "item": "水景设计",
        "quantity": 2.0
    },
    {
        "item": "文章作者",
        "quantity": 2.0
    },
    {
        "item": "Directors In Charge",
        "quantity": 2.0
    },
    {
        "item": "管理负责人",
        "quantity": 2.0
    },
    {
        "item": "Architect ",
        "quantity": 2.0
    },
    {
        "item": "标示顾问",
        "quantity": 2.0
    },
    {
        "item": "Structural Design",
        "quantity": 2.0
    },
    {
        "item": "电梯设计",
        "quantity": 2.0
    },
    {
        "item": "结构规划",
        "quantity": 2.0
    },
    {
        "item": "Estructura",
        "quantity": 2.0
    },
    {
        "item": "清洁工程师",
        "quantity": 2.0
    },
    {
        "item": "采暖工程师",
        "quantity": 2.0
    },
    {
        "item": "Total floor area",
        "quantity": 2.0
    },
    {
        "item": "Site area",
        "quantity": 2.0
    },
    {
        "item": "建筑材料",
        "quantity": 2.0
    },
    {
        "item": "Design",
        "quantity": 2.0
    },
    {
        "item": "结构管理",
        "quantity": 2.0
    },
    {
        "item": "可持续工程",
        "quantity": 2.0
    },
    {
        "item": "施工检查",
        "quantity": 2.0
    },
    {
        "item": "合作建筑师和工程师",
        "quantity": 2.0
    },
    {
        "item": "音响工程",
        "quantity": 2.0
    },
    {
        "item": "Collaboration",
        "quantity": 2.0
    },
    {
        "item": "项目计划",
        "quantity": 2.0
    },
    {
        "item": "地面层面积",
        "quantity": 2.0
    },
    {
        "item": "高级助理",
        "quantity": 2.0
    },
    {
        "item": "Constructed Area",
        "quantity": 2.0
    },
    {
        "item": "Principal Use",
        "quantity": 2.0
    },
    {
        "item": "Structure System",
        "quantity": 2.0
    },
    {
        "item": "土地调研",
        "quantity": 2.0
    },
    {
        "item": "建筑助理",
        "quantity": 2.0
    },
    {
        "item": "Contractor ",
        "quantity": 2.0
    },
    {
        "item": "机械设备",
        "quantity": 2.0
    },
    {
        "item": "Building Cost",
        "quantity": 2.0
    },
    {
        "item": "工匠",
        "quantity": 2.0
    },
    {
        "item": "建筑经理",
        "quantity": 2.0
    },
    {
        "item": "项目团队成员",
        "quantity": 2.0
    },
    {
        "item": "Construction Company",
        "quantity": 2.0
    },
    {
        "item": "建筑负责",
        "quantity": 2.0
    },
    {
        "item": "协作",
        "quantity": 2.0
    },
    {
        "item": "项目监督",
        "quantity": 2.0
    },
    {
        "item": "首席建筑师 ",
        "quantity": 2.0
    },
    {
        "item": "Co Author",
        "quantity": 2.0
    },
    {
        "item": "户主",
        "quantity": 2.0
    },
    {
        "item": "节能",
        "quantity": 2.0
    },
    {
        "item": "声学工程师 ",
        "quantity": 2.0
    },
    {
        "item": "规划团队",
        "quantity": 2.0
    },
    {
        "item": "总造价",
        "quantity": 2.0
    },
    {
        "item": "主要建造方",
        "quantity": 2.0
    },
    {
        "item": "项目协调人",
        "quantity": 2.0
    },
    {
        "item": "项目联络",
        "quantity": 2.0
    },
    {
        "item": "风水顾问",
        "quantity": 2.0
    },
    {
        "item": "玻璃顾问",
        "quantity": 2.0
    },
    {
        "item": "石膏板",
        "quantity": 2.0
    },
    {
        "item": "编辑",
        "quantity": 2.0
    },
    {
        "item": "电气服务",
        "quantity": 2.0
    },
    {
        "item": "项目发起人",
        "quantity": 2.0
    },
    {
        "item": "装置顾问",
        "quantity": 2.0
    },
    {
        "item": "场景设计",
        "quantity": 2.0
    },
    {
        "item": "助理技术建筑师",
        "quantity": 2.0
    },
    {
        "item": "建造顾问",
        "quantity": 2.0
    },
    {
        "item": "建筑物理和可持续性",
        "quantity": 2.0
    },
    {
        "item": "伙伴建筑师",
        "quantity": 2.0
    },
    {
        "item": "建造管理",
        "quantity": 2.0
    },
    {
        "item": "建造经济学家",
        "quantity": 2.0
    },
    {
        "item": "主要承建商",
        "quantity": 2.0
    },
    {
        "item": "电力与给排水",
        "quantity": 2.0
    },
    {
        "item": "排水工程师",
        "quantity": 2.0
    },
    {
        "item": "安装工程师",
        "quantity": 2.0
    },
    {
        "item": "灯具",
        "quantity": 2.0
    },
    {
        "item": "SPS",
        "quantity": 2.0
    },
    {
        "item": "质量勘测",
        "quantity": 2.0
    },
    {
        "item": "原建筑师",
        "quantity": 2.0
    },
    {
        "item": "混凝土分包商",
        "quantity": 2.0
    },
    {
        "item": "宣传方",
        "quantity": 2.0
    },
    {
        "item": "水电卫生设计",
        "quantity": 2.0
    },
    {
        "item": "项目设计师 ",
        "quantity": 2.0
    },
    {
        "item": "总承包公司",
        "quantity": 2.0
    },
    {
        "item": "Size",
        "quantity": 2.0
    },
    {
        "item": "家具经销商",
        "quantity": 2.0
    },
    {
        "item": "消防工程",
        "quantity": 2.0
    },
    {
        "item": "建筑立面",
        "quantity": 2.0
    },
    {
        "item": "地面总面积",
        "quantity": 2.0
    },
    {
        "item": "主供应商",
        "quantity": 2.0
    },
    {
        "item": "Design team",
        "quantity": 2.0
    },
    {
        "item": "保护顾问",
        "quantity": 2.0
    },
    {
        "item": "结构建筑师",
        "quantity": 2.0
    },
    {
        "item": "当事人",
        "quantity": 2.0
    },
    {
        "item": "电气设施",
        "quantity": 2.0
    },
    {
        "item": "项目伙伴",
        "quantity": 2.0
    },
    {
        "item": "设备与电力工程",
        "quantity": 2.0
    },
    {
        "item": "联络",
        "quantity": 2.0
    },
    {
        "item": "声学系统",
        "quantity": 2.0
    },
    {
        "item": "质量工程师",
        "quantity": 2.0
    },
    {
        "item": "图标",
        "quantity": 2.0
    },
    {
        "item": "高级项目建筑师",
        "quantity": 2.0
    },
    {
        "item": "Electrical",
        "quantity": 2.0
    },
    {
        "item": "房屋测量师",
        "quantity": 2.0
    },
    {
        "item": "绿地设计",
        "quantity": 2.0
    },
    {
        "item": "机械系统",
        "quantity": 2.0
    },
    {
        "item": "城市规划师",
        "quantity": 2.0
    },
    {
        "item": "质量安全",
        "quantity": 2.0
    },
    {
        "item": "Site Area ",
        "quantity": 2.0
    },
    {
        "item": "建筑造价",
        "quantity": 2.0
    },
    {
        "item": "J建筑师",
        "quantity": 2.0
    },
    {
        "item": "金属承包商",
        "quantity": 2.0
    },
    {
        "item": "地理工程",
        "quantity": 2.0
    },
    {
        "item": "视听设计",
        "quantity": 2.0
    },
    {
        "item": "土木工程顾问",
        "quantity": 2.0
    },
    {
        "item": "土壤研究",
        "quantity": 2.0
    },
    {
        "item": "建筑记录",
        "quantity": 2.0
    },
    {
        "item": "建设工程",
        "quantity": 2.0
    },
    {
        "item": "卫生设施",
        "quantity": 2.0
    },
    {
        "item": "地板",
        "quantity": 2.0
    },
    {
        "item": "工程总监",
        "quantity": 2.0
    },
    {
        "item": "Coordination",
        "quantity": 2.0
    },
    {
        "item": "照相",
        "quantity": 2.0
    },
    {
        "item": "主建筑商",
        "quantity": 2.0
    },
    {
        "item": "工程技术",
        "quantity": 2.0
    },
    {
        "item": "Área Terreno",
        "quantity": 2.0
    },
    {
        "item": "展览顾问",
        "quantity": 2.0
    },
    {
        "item": "建筑技术员",
        "quantity": 2.0
    },
    {
        "item": "土方工程",
        "quantity": 2.0
    },
    {
        "item": "照片拥有权",
        "quantity": 2.0
    },
    {
        "item": "施工主任",
        "quantity": 2.0
    },
    {
        "item": "Structural Consultant",
        "quantity": 2.0
    },
    {
        "item": "Graphics",
        "quantity": 2.0
    },
    {
        "item": "Title 24",
        "quantity": 2.0
    },
    {
        "item": "用地规模",
        "quantity": 2.0
    },
    {
        "item": "Principals In Charge",
        "quantity": 2.0
    },
    {
        "item": "项目策划",
        "quantity": 2.0
    },
    {
        "item": "照明设备",
        "quantity": 2.0
    },
    {
        "item": "资金来源",
        "quantity": 2.0
    },
    {
        "item": "M&E 顾问",
        "quantity": 2.0
    },
    {
        "item": "设计师助理",
        "quantity": 2.0
    },
    {
        "item": "多媒体",
        "quantity": 2.0
    },
    {
        "item": "金属作业",
        "quantity": 2.0
    },
    {
        "item": "光线设计师",
        "quantity": 2.0
    },
    {
        "item": "监理工程师",
        "quantity": 2.0
    },
    {
        "item": "方案设计",
        "quantity": 2.0
    },
    {
        "item": "室内设计合作者",
        "quantity": 2.0
    },
    {
        "item": "合同",
        "quantity": 2.0
    },
    {
        "item": "投资",
        "quantity": 2.0
    },
    {
        "item": "业态类型",
        "quantity": 2.0
    },
    {
        "item": "Landscaping",
        "quantity": 2.0
    },
    {
        "item": "推荐人",
        "quantity": 2.0
    },
    {
        "item": "设计和建造",
        "quantity": 2.0
    },
    {
        "item": "电气设备",
        "quantity": 2.0
    },
    {
        "item": "管理合伙人",
        "quantity": 2.0
    },
    {
        "item": "景观建筑是",
        "quantity": 2.0
    },
    {
        "item": "Contractors",
        "quantity": 2.0
    },
    {
        "item": "混凝土工程",
        "quantity": 2.0
    },
    {
        "item": "标识",
        "quantity": 2.0
    },
    {
        "item": "建设经理",
        "quantity": 2.0
    },
    {
        "item": "Local Architects",
        "quantity": 2.0
    },
    {
        "item": "QS",
        "quantity": 2.0
    },
    {
        "item": "插图",
        "quantity": 2.0
    },
    {
        "item": "版权",
        "quantity": 2.0
    },
    {
        "item": "标牌",
        "quantity": 2.0
    },
    {
        "item": "设计团队领导、项目经理",
        "quantity": 2.0
    },
    {
        "item": "其他合作方",
        "quantity": 2.0
    },
    {
        "item": "主任",
        "quantity": 2.0
    },
    {
        "item": "空间格局",
        "quantity": 2.0
    },
    {
        "item": "考古",
        "quantity": 2.0
    },
    {
        "item": "施工企业",
        "quantity": 2.0
    },
    {
        "item": "控制",
        "quantity": 2.0
    },
    {
        "item": "座位",
        "quantity": 2.0
    },
    {
        "item": "Chief Designer",
        "quantity": 2.0
    },
    {
        "item": "Mep Engineer",
        "quantity": 2.0
    },
    {
        "item": "地下层面积",
        "quantity": 2.0
    },
    {
        "item": "机械电器管道工程",
        "quantity": 2.0
    },
    {
        "item": "工程事务所",
        "quantity": 2.0
    },
    {
        "item": "Credits",
        "quantity": 2.0
    },
    {
        "item": "音效设计",
        "quantity": 2.0
    },
    {
        "item": "实习",
        "quantity": 2.0
    },
    {
        "item": "剧院设计顾问",
        "quantity": 2.0
    },
    {
        "item": "音响顾问",
        "quantity": 2.0
    },
    {
        "item": "木材承包商",
        "quantity": 2.0
    },
    {
        "item": "Acoustical Consultant",
        "quantity": 2.0
    },
    {
        "item": "企业",
        "quantity": 2.0
    },
    {
        "item": "图纸",
        "quantity": 2.0
    },
    {
        "item": "副主管",
        "quantity": 2.0
    },
    {
        "item": "施工建筑",
        "quantity": 2.0
    },
    {
        "item": "技术支持",
        "quantity": 2.0
    },
    {
        "item": "玻璃安装",
        "quantity": 2.0
    },
    {
        "item": "Lights And Illumination",
        "quantity": 2.0
    },
    {
        "item": "执行经理",
        "quantity": 2.0
    },
    {
        "item": "建筑师事务所",
        "quantity": 2.0
    },
    {
        "item": "消防安全",
        "quantity": 2.0
    },
    {
        "item": "建筑工人",
        "quantity": 2.0
    },
    {
        "item": "当地建筑顾问",
        "quantity": 2.0
    },
    {
        "item": "水暖工程师",
        "quantity": 2.0
    },
    {
        "item": "Furniture",
        "quantity": 2.0
    },
    {
        "item": "工期",
        "quantity": 2.0
    },
    {
        "item": "建筑勘测",
        "quantity": 2.0
    },
    {
        "item": "团队领导",
        "quantity": 2.0
    },
    {
        "item": "Architect of Record",
        "quantity": 2.0
    },
    {
        "item": "建筑执行",
        "quantity": 2.0
    },
    {
        "item": "2D 艺术家",
        "quantity": 2.0
    },
    {
        "item": "工程承包商",
        "quantity": 2.0
    },
    {
        "item": "致谢",
        "quantity": 2.0
    },
    {
        "item": "成本控制",
        "quantity": 2.0
    },
    {
        "item": "地面",
        "quantity": 2.0
    },
    {
        "item": "安防",
        "quantity": 2.0
    },
    {
        "item": "当地建筑事务所",
        "quantity": 2.0
    },
    {
        "item": "机械和电气工程",
        "quantity": 2.0
    },
    {
        "item": "建筑监督",
        "quantity": 2.0
    },
    {
        "item": "设计范围",
        "quantity": 2.0
    },
    {
        "item": "参照",
        "quantity": 2.0
    },
    {
        "item": "水力",
        "quantity": 2.0
    },
    {
        "item": "通风",
        "quantity": 2.0
    },
    {
        "item": "项目所在地",
        "quantity": 2.0
    },
    {
        "item": "工艺",
        "quantity": 2.0
    },
    {
        "item": "能源概念",
        "quantity": 2.0
    },
    {
        "item": "防水",
        "quantity": 2.0
    },
    {
        "item": "执行总监",
        "quantity": 2.0
    },
    {
        "item": "联系人",
        "quantity": 2.0
    },
    {
        "item": "架构工程师",
        "quantity": 2.0
    },
    {
        "item": "Year Of Enchargement",
        "quantity": 2.0
    },
    {
        "item": "Principal",
        "quantity": 2.0
    },
    {
        "item": "电机工程师",
        "quantity": 2.0
    },
    {
        "item": "Lighting Consultant",
        "quantity": 2.0
    },
    {
        "item": "策划",
        "quantity": 2.0
    },
    {
        "item": "咨询方",
        "quantity": 2.0
    },
    {
        "item": "ESD",
        "quantity": 2.0
    },
    {
        "item": "酒店顾问",
        "quantity": 2.0
    },
    {
        "item": "细木",
        "quantity": 2.0
    },
    {
        "item": "艺术工作",
        "quantity": 2.0
    },
    {
        "item": "建筑表面",
        "quantity": 2.0
    },
    {
        "item": "建筑调研",
        "quantity": 2.0
    },
    {
        "item": "Promoter",
        "quantity": 2.0
    },
    {
        "item": "石工",
        "quantity": 2.0
    },
    {
        "item": "建筑基底总面积 ",
        "quantity": 2.0
    },
    {
        "item": "开工时间",
        "quantity": 2.0
    },
    {
        "item": "视觉设计",
        "quantity": 2.0
    },
    {
        "item": "安装咨询",
        "quantity": 2.0
    },
    {
        "item": "业主方",
        "quantity": 2.0
    },
    {
        "item": "建筑服务顾问",
        "quantity": 2.0
    },
    {
        "item": "用户",
        "quantity": 2.0
    },
    {
        "item": "引导标志",
        "quantity": 2.0
    },
    {
        "item": "服务内容",
        "quantity": 2.0
    },
    {
        "item": "油漆工",
        "quantity": 2.0
    },
    {
        "item": "电器设计",
        "quantity": 2.0
    },
    {
        "item": "工业设计",
        "quantity": 2.0
    },
    {
        "item": "主笔设计师",
        "quantity": 2.0
    },
    {
        "item": "机械/电气工程师",
        "quantity": 2.0
    },
    {
        "item": "结构/土木工程师",
        "quantity": 2.0
    },
    {
        "item": "建筑计划",
        "quantity": 2.0
    },
    {
        "item": "项目经理－深化设计",
        "quantity": 2.0
    },
    {
        "item": "设计地段",
        "quantity": 2.0
    },
    {
        "item": "地面面积",
        "quantity": 2.0
    },
    {
        "item": "二层面积",
        "quantity": 2.0
    },
    {
        "item": "基础和结构",
        "quantity": 2.0
    },
    {
        "item": "暖通空调系统",
        "quantity": 2.0
    },
    {
        "item": "设备与机电工程师",
        "quantity": 2.0
    },
    {
        "item": "高环境质量",
        "quantity": 2.0
    },
    {
        "item": "工程设计师",
        "quantity": 2.0
    },
    {
        "item": "教授",
        "quantity": 2.0
    },
    {
        "item": "信息技术",
        "quantity": 2.0
    },
    {
        "item": "工程承包单位",
        "quantity": 2.0
    },
    {
        "item": "艺术项目",
        "quantity": 2.0
    },
    {
        "item": "Diseño Arquitectónico",
        "quantity": 2.0
    },
    {
        "item": "建筑/室内设计",
        "quantity": 2.0
    },
    {
        "item": "实施阶段设计团队",
        "quantity": 2.0
    },
    {
        "item": "建筑队",
        "quantity": 2.0
    },
    {
        "item": "艺术作品",
        "quantity": 2.0
    },
    {
        "item": "能源工程师",
        "quantity": 2.0
    },
    {
        "item": "电气工程顾问",
        "quantity": 2.0
    },
    {
        "item": "项目合作方",
        "quantity": 2.0
    },
    {
        "item": "结构与基础",
        "quantity": 2.0
    },
    {
        "item": "场地顾问",
        "quantity": 2.0
    },
    {
        "item": "建设日期",
        "quantity": 2.0
    },
    {
        "item": "标示设计",
        "quantity": 2.0
    },
    {
        "item": "内饰顾问",
        "quantity": 2.0
    },
    {
        "item": "捐助者",
        "quantity": 2.0
    },
    {
        "item": "设计理念",
        "quantity": 2.0
    },
    {
        "item": "构造师",
        "quantity": 2.0
    },
    {
        "item": "基础工程师",
        "quantity": 2.0
    },
    {
        "item": "代码",
        "quantity": 2.0
    },
    {
        "item": "接入顾问",
        "quantity": 2.0
    },
    {
        "item": "建筑项目",
        "quantity": 2.0
    },
    {
        "item": "结构专家",
        "quantity": 2.0
    },
    {
        "item": "水暖设计",
        "quantity": 2.0
    },
    {
        "item": "建设施工",
        "quantity": 2.0
    },
    {
        "item": "Leed 顾问",
        "quantity": 2.0
    },
    {
        "item": "壁画",
        "quantity": 2.0
    },
    {
        "item": "执行指导",
        "quantity": 2.0
    },
    {
        "item": "完成日期",
        "quantity": 2.0
    },
    {
        "item": "当地景观设计师",
        "quantity": 2.0
    },
    {
        "item": "机械与电气工程师",
        "quantity": 2.0
    },
    {
        "item": "BCA 顾问",
        "quantity": 2.0
    },
    {
        "item": "环境平面设计",
        "quantity": 2.0
    },
    {
        "item": "菜式",
        "quantity": 2.0
    },
    {
        "item": "场地工程师",
        "quantity": 2.0
    },
    {
        "item": "公共艺术",
        "quantity": 2.0
    },
    {
        "item": "成本预算",
        "quantity": 2.0
    },
    {
        "item": "Status",
        "quantity": 2.0
    },
    {
        "item": "供暖系统",
        "quantity": 2.0
    },
    {
        "item": "项目与场地管理",
        "quantity": 2.0
    },
    {
        "item": "施工主管",
        "quantity": 2.0
    },
    {
        "item": "液压工程师",
        "quantity": 2.0
    },
    {
        "item": "获奖情况",
        "quantity": 2.0
    },
    {
        "item": "视觉识别",
        "quantity": 2.0
    },
    {
        "item": "建筑检验员",
        "quantity": 2.0
    },
    {
        "item": "声环境顾问",
        "quantity": 2.0
    },
    {
        "item": "建筑范围",
        "quantity": 2.0
    },
    {
        "item": "结构工程咨询",
        "quantity": 2.0
    },
    {
        "item": "建筑表皮",
        "quantity": 2.0
    },
    {
        "item": "顾客",
        "quantity": 2.0
    },
    {
        "item": "BET",
        "quantity": 2.0
    },
    {
        "item": "检验",
        "quantity": 2.0
    },
    {
        "item": "项目总监 ",
        "quantity": 2.0
    },
    {
        "item": "建造施工",
        "quantity": 2.0
    },
    {
        "item": "音频/视频",
        "quantity": 2.0
    },
    {
        "item": "外墙",
        "quantity": 2.0
    },
    {
        "item": "项目总建筑师",
        "quantity": 2.0
    },
    {
        "item": "年竣工",
        "quantity": 2.0
    },
    {
        "item": "园林设计师",
        "quantity": 2.0
    },
    {
        "item": "Acoustics",
        "quantity": 2.0
    },
    {
        "item": "Services Engineer",
        "quantity": 2.0
    },
    {
        "item": "Software",
        "quantity": 2.0
    },
    {
        "item": "水利设计",
        "quantity": 2.0
    },
    {
        "item": "Coordinator",
        "quantity": 2.0
    },
    {
        "item": "基底面积",
        "quantity": 2.0
    },
    {
        "item": "节能设计",
        "quantity": 2.0
    },
    {
        "item": "交通规划师",
        "quantity": 2.0
    },
    {
        "item": "结构土木工程",
        "quantity": 2.0
    },
    {
        "item": "监理方",
        "quantity": 2.0
    },
    {
        "item": "建筑总监",
        "quantity": 2.0
    },
    {
        "item": "住宅面积",
        "quantity": 2.0
    },
    {
        "item": "客户/业主",
        "quantity": 2.0
    },
    {
        "item": "建筑设计单位",
        "quantity": 2.0
    },
    {
        "item": "风格",
        "quantity": 2.0
    },
    {
        "item": "光",
        "quantity": 2.0
    },
    {
        "item": "安全与健康协调",
        "quantity": 2.0
    },
    {
        "item": "花园",
        "quantity": 2.0
    },
    {
        "item": "开发顾问",
        "quantity": 2.0
    },
    {
        "item": "机械承包商",
        "quantity": 2.0
    },
    {
        "item": "设计机构",
        "quantity": 2.0
    },
    {
        "item": "建筑合作",
        "quantity": 2.0
    },
    {
        "item": "场地建筑师",
        "quantity": 2.0
    },
    {
        "item": "主任建筑死",
        "quantity": 2.0
    },
    {
        "item": "结构和服务工程师",
        "quantity": 2.0
    },
    {
        "item": "可视化设计",
        "quantity": 2.0
    },
    {
        "item": "封闭空间",
        "quantity": 2.0
    },
    {
        "item": "Craftspeople",
        "quantity": 2.0
    },
    {
        "item": "表面",
        "quantity": 2.0
    },
    {
        "item": "能源设计",
        "quantity": 2.0
    },
    {
        "item": "成本咨询顾问",
        "quantity": 2.0
    },
    {
        "item": "地理工程师",
        "quantity": 2.0
    },
    {
        "item": "无障碍设计",
        "quantity": 2.0
    },
    {
        "item": "技术参数",
        "quantity": 2.0
    },
    {
        "item": "运输",
        "quantity": 2.0
    },
    {
        "item": "建筑工程团队",
        "quantity": 2.0
    },
    {
        "item": "顾问建筑师",
        "quantity": 2.0
    },
    {
        "item": "窗户承包商",
        "quantity": 2.0
    },
    {
        "item": "质量顾问",
        "quantity": 2.0
    },
    {
        "item": "总投资",
        "quantity": 2.0
    },
    {
        "item": "CDM协调",
        "quantity": 2.0
    },
    {
        "item": "Structure Engineer",
        "quantity": 2.0
    },
    {
        "item": "推广",
        "quantity": 2.0
    },
    {
        "item": "混凝土结构工程师",
        "quantity": 2.0
    },
    {
        "item": "Managing Principal",
        "quantity": 2.0
    },
    {
        "item": "设计阶段",
        "quantity": 2.0
    },
    {
        "item": "废物管理",
        "quantity": 2.0
    },
    {
        "item": "数量调查",
        "quantity": 2.0
    },
    {
        "item": "项目高度",
        "quantity": 2.0
    },
    {
        "item": "绿色建筑认证",
        "quantity": 2.0
    },
    {
        "item": "净面积",
        "quantity": 2.0
    },
    {
        "item": "表皮设计",
        "quantity": 2.0
    },
    {
        "item": "墙",
        "quantity": 2.0
    },
    {
        "item": "项目建筑史",
        "quantity": 2.0
    },
    {
        "item": "主要合作人",
        "quantity": 2.0
    },
    {
        "item": "木材公司",
        "quantity": 2.0
    },
    {
        "item": "建筑花费",
        "quantity": 2.0
    },
    {
        "item": "项目名称",
        "quantity": 2.0
    },
    {
        "item": "经济学",
        "quantity": 2.0
    },
    {
        "item": "技术服务",
        "quantity": 2.0
    },
    {
        "item": "建筑测量员",
        "quantity": 2.0
    },
    {
        "item": "总规划",
        "quantity": 2.0
    },
    {
        "item": "图解",
        "quantity": 2.0
    },
    {
        "item": "建设用地比率",
        "quantity": 2.0
    },
    {
        "item": "引导标识",
        "quantity": 2.0
    },
    {
        "item": "防火设计",
        "quantity": 2.0
    },
    {
        "item": "Associated Architects",
        "quantity": 2.0
    },
    {
        "item": "技术专家",
        "quantity": 2.0
    },
    {
        "item": "材料商",
        "quantity": 2.0
    },
    {
        "item": "电气管道工程",
        "quantity": 2.0
    },
    {
        "item": "绿色建筑顾问",
        "quantity": 2.0
    },
    {
        "item": "项目开始时间",
        "quantity": 2.0
    },
    {
        "item": "设备负责人",
        "quantity": 2.0
    },
    {
        "item": "室内材料",
        "quantity": 2.0
    },
    {
        "item": "施工工程师",
        "quantity": 2.0
    },
    {
        "item": "程序",
        "quantity": 2.0
    },
    {
        "item": "调研员",
        "quantity": 2.0
    },
    {
        "item": "管线工程师",
        "quantity": 2.0
    },
    {
        "item": "水管工程师",
        "quantity": 2.0
    },
    {
        "item": "建筑学生",
        "quantity": 2.0
    },
    {
        "item": "项目主创",
        "quantity": 2.0
    },
    {
        "item": "机械服务",
        "quantity": 2.0
    },
    {
        "item": "建筑技术顾问",
        "quantity": 2.0
    },
    {
        "item": "总顾问",
        "quantity": 2.0
    },
    {
        "item": "项目所有者",
        "quantity": 2.0
    },
    {
        "item": "建筑规范",
        "quantity": 2.0
    },
    {
        "item": "工作指导",
        "quantity": 2.0
    },
    {
        "item": "勘测",
        "quantity": 2.0
    },
    {
        "item": "其他参与人员",
        "quantity": 2.0
    },
    {
        "item": "设计师负责人",
        "quantity": 2.0
    },
    {
        "item": "工程预算",
        "quantity": 2.0
    },
    {
        "item": "剧场设计",
        "quantity": 2.0
    },
    {
        "item": "总平面图",
        "quantity": 2.0
    },
    {
        "item": "力学工程师",
        "quantity": 2.0
    },
    {
        "item": "室内顾问",
        "quantity": 2.0
    },
    {
        "item": "地毯",
        "quantity": 2.0
    },
    {
        "item": "工作室",
        "quantity": 2.0
    },
    {
        "item": "景观团队",
        "quantity": 2.0
    },
    {
        "item": "液压设计",
        "quantity": 2.0
    },
    {
        "item": "内饰设计",
        "quantity": 2.0
    },
    {
        "item": "门",
        "quantity": 2.0
    },
    {
        "item": "统计",
        "quantity": 2.0
    },
    {
        "item": "建筑物理 ",
        "quantity": 2.0
    },
    {
        "item": "泥水匠",
        "quantity": 2.0
    },
    {
        "item": "BE流体",
        "quantity": 2.0
    },
    {
        "item": "首席设计顾问",
        "quantity": 2.0
    },
    {
        "item": "考古学 ",
        "quantity": 2.0
    },
    {
        "item": "立面咨询",
        "quantity": 2.0
    },
    {
        "item": "支持者",
        "quantity": 2.0
    },
    {
        "item": "特别顾问",
        "quantity": 2.0
    },
    {
        "item": "博物馆学",
        "quantity": 2.0
    },
    {
        "item": "木材供应",
        "quantity": 2.0
    },
    {
        "item": "细木工",
        "quantity": 2.0
    },
    {
        "item": "舞台技术",
        "quantity": 2.0
    },
    {
        "item": "总建筑师 ",
        "quantity": 2.0
    },
    {
        "item": "项目开发",
        "quantity": 2.0
    },
    {
        "item": "建筑毛面积",
        "quantity": 2.0
    },
    {
        "item": "地块面积",
        "quantity": 2.0
    },
    {
        "item": "外立面",
        "quantity": 2.0
    },
    {
        "item": "植物设计",
        "quantity": 2.0
    },
    {
        "item": "管理总监",
        "quantity": 2.0
    },
    {
        "item": "给排水工程",
        "quantity": 2.0
    },
    {
        "item": "酒店管理",
        "quantity": 2.0
    },
    {
        "item": "园艺",
        "quantity": 2.0
    },
    {
        "item": "结构分析师",
        "quantity": 2.0
    },
    {
        "item": "当地执行建筑师",
        "quantity": 2.0
    },
    {
        "item": "建筑师和室内设计师",
        "quantity": 2.0
    },
    {
        "item": "动画设计",
        "quantity": 2.0
    },
    {
        "item": "建设建筑师",
        "quantity": 2.0
    },
    {
        "item": "项目建设时间",
        "quantity": 2.0
    },
    {
        "item": "现场主管",
        "quantity": 2.0
    },
    {
        "item": "考古学家",
        "quantity": 2.0
    },
    {
        "item": "建筑与室内设计",
        "quantity": 2.0
    },
    {
        "item": "系统设计",
        "quantity": 2.0
    },
    {
        "item": "室内设计承包商",
        "quantity": 2.0
    },
    {
        "item": "稳定性设计",
        "quantity": 2.0
    },
    {
        "item": "项目总花费",
        "quantity": 2.0
    },
    {
        "item": "厨房规划",
        "quantity": 2.0
    },
    {
        "item": "建筑容量",
        "quantity": 2.0
    },
    {
        "item": "环保顾问",
        "quantity": 2.0
    },
    {
        "item": "环境概貌",
        "quantity": 2.0
    },
    {
        "item": "幕墙工程",
        "quantity": 2.0
    },
    {
        "item": "植物顾问",
        "quantity": 2.0
    },
    {
        "item": "3D 艺术家",
        "quantity": 2.0
    },
    {
        "item": "项目主创设计师",
        "quantity": 2.0
    },
    {
        "item": "景观工程",
        "quantity": 2.0
    },
    {
        "item": "营造商",
        "quantity": 2.0
    },
    {
        "item": "其他",
        "quantity": 2.0
    },
    {
        "item": "CAD制图",
        "quantity": 2.0
    },
    {
        "item": "声学工程顾问",
        "quantity": 2.0
    },
    {
        "item": "负责合伙人",
        "quantity": 2.0
    },
    {
        "item": "图纸绘制",
        "quantity": 1.0
    },
    {
        "item": "造价监理",
        "quantity": 1.0
    },
    {
        "item": "机械设计师",
        "quantity": 1.0
    },
    {
        "item": "体验式设计",
        "quantity": 1.0
    },
    {
        "item": "Foster + Partners 团队",
        "quantity": 1.0
    },
    {
        "item": "技术工程顾问",
        "quantity": 1.0
    },
    {
        "item": "灯光工程师/设计师",
        "quantity": 1.0
    },
    {
        "item": "工程安装",
        "quantity": 1.0
    },
    {
        "item": "合作艺术家 1",
        "quantity": 1.0
    },
    {
        "item": "HEQ",
        "quantity": 1.0
    },
    {
        "item": "附楼面积",
        "quantity": 1.0
    },
    {
        "item": "主楼面积",
        "quantity": 1.0
    },
    {
        "item": "Aborist",
        "quantity": 1.0
    },
    {
        "item": "土木工程师（更新后）",
        "quantity": 1.0
    },
    {
        "item": "土木工程师（方案设计）",
        "quantity": 1.0
    },
    {
        "item": "节点处理",
        "quantity": 1.0
    },
    {
        "item": "泳池顾问",
        "quantity": 1.0
    },
    {
        "item": "结构屋顶",
        "quantity": 1.0
    },
    {
        "item": "CarpentryAmish Carpentry Crews from",
        "quantity": 1.0
    },
    {
        "item": "方案概念",
        "quantity": 1.0
    },
    {
        "item": "受邀艺术家",
        "quantity": 1.0
    },
    {
        "item": "MEP Engineers",
        "quantity": 1.0
    },
    {
        "item": "项目阶段",
        "quantity": 1.0
    },
    {
        "item": "印度专利石地板",
        "quantity": 1.0
    },
    {
        "item": "阳光房结构绘图员",
        "quantity": 1.0
    },
    {
        "item": "阳光房结构团队",
        "quantity": 1.0
    },
    {
        "item": "人行桥结构绘图员",
        "quantity": 1.0
    },
    {
        "item": "人行桥设计师",
        "quantity": 1.0
    },
    {
        "item": "绘图负责",
        "quantity": 1.0
    },
    {
        "item": "区位",
        "quantity": 1.0
    },
    {
        "item": "装置／W&E顾问",
        "quantity": 1.0
    },
    {
        "item": "重建指导",
        "quantity": 1.0
    },
    {
        "item": "照明专家",
        "quantity": 1.0
    },
    {
        "item": "风能植被",
        "quantity": 1.0
    },
    {
        "item": "框架/ 玻璃/ 外观",
        "quantity": 1.0
    },
    {
        "item": "砖结构",
        "quantity": 1.0
    },
    {
        "item": "科学技术支持",
        "quantity": 1.0
    },
    {
        "item": "表皮 CNC 生产",
        "quantity": 1.0
    },
    {
        "item": "建筑及结构计算",
        "quantity": 1.0
    },
    {
        "item": "建筑物理学",
        "quantity": 1.0
    },
    {
        "item": "建筑服务工程与EPB",
        "quantity": 1.0
    },
    {
        "item": "铝板建造方",
        "quantity": 1.0
    },
    {
        "item": "施工负责人",
        "quantity": 1.0
    },
    {
        "item": "设计   建造者",
        "quantity": 1.0
    },
    {
        "item": "木结构建造方",
        "quantity": 1.0
    },
    {
        "item": "教师之村一号楼",
        "quantity": 1.0
    },
    {
        "item": "雇主",
        "quantity": 1.0
    },
    {
        "item": "建筑设备：电气",
        "quantity": 1.0
    },
    {
        "item": "声音图像",
        "quantity": 1.0
    },
    {
        "item": "合作咨询师",
        "quantity": 1.0
    },
    {
        "item": "设计开发团队",
        "quantity": 1.0
    },
    {
        "item": "重建",
        "quantity": 1.0
    },
    {
        "item": "座位区域 (室外)",
        "quantity": 1.0
    },
    {
        "item": "座位数量",
        "quantity": 1.0
    },
    {
        "item": "楼宇自动化承包商",
        "quantity": 1.0
    },
    {
        "item": "通风承包商",
        "quantity": 1.0
    },
    {
        "item": "水暖承包商",
        "quantity": 1.0
    },
    {
        "item": "声学和隔音",
        "quantity": 1.0
    },
    {
        "item": "LCC 设计者 \t",
        "quantity": 1.0
    },
    {
        "item": "项目建筑师 SAFA",
        "quantity": 1.0
    },
    {
        "item": "建筑/结构/机电设计",
        "quantity": 1.0
    },
    {
        "item": "撰文",
        "quantity": 1.0
    },
    {
        "item": "滑动混凝土",
        "quantity": 1.0
    },
    {
        "item": "合作设计者",
        "quantity": 1.0
    },
    {
        "item": "栏杆承包商",
        "quantity": 1.0
    },
    {
        "item": "钢材承包商",
        "quantity": 1.0
    },
    {
        "item": "工程方",
        "quantity": 1.0
    },
    {
        "item": "竞赛项目和规划许可项目",
        "quantity": 1.0
    },
    {
        "item": "O-塔楼",
        "quantity": 1.0
    },
    {
        "item": "空间方案作者",
        "quantity": 1.0
    },
    {
        "item": "建筑经济学家",
        "quantity": 1.0
    },
    {
        "item": "客户协调",
        "quantity": 1.0
    },
    {
        "item": "金属加工承包商",
        "quantity": 1.0
    },
    {
        "item": "墙体勘测",
        "quantity": 1.0
    },
    {
        "item": "几何专家",
        "quantity": 1.0
    },
    {
        "item": "摄影风格",
        "quantity": 1.0
    },
    {
        "item": "LEED 等级",
        "quantity": 1.0
    },
    {
        "item": "机械，电力+给排水工程师",
        "quantity": 1.0
    },
    {
        "item": "LEED绿建筑设计",
        "quantity": 1.0
    },
    {
        "item": "日期",
        "quantity": 1.0
    },
    {
        "item": "环保部和暖通空调工程师",
        "quantity": 1.0
    },
    {
        "item": "艺术顾问",
        "quantity": 1.0
    },
    {
        "item": "景观设计  方案阶段",
        "quantity": 1.0
    },
    {
        "item": "项目建筑师 建造阶段",
        "quantity": 1.0
    },
    {
        "item": "项目建筑师 方案阶段",
        "quantity": 1.0
    },
    {
        "item": "电气和管道工程",
        "quantity": 1.0
    },
    {
        "item": "垂直风洞装置",
        "quantity": 1.0
    },
    {
        "item": "主创",
        "quantity": 1.0
    },
    {
        "item": "印刷",
        "quantity": 1.0
    },
    {
        "item": "视听系统",
        "quantity": 1.0
    },
    {
        "item": "洗手间系统",
        "quantity": 1.0
    },
    {
        "item": "Associate",
        "quantity": 1.0
    },
    {
        "item": "服务对象",
        "quantity": 1.0
    },
    {
        "item": "结构模型",
        "quantity": 1.0
    },
    {
        "item": "家具建造方",
        "quantity": 1.0
    },
    {
        "item": "测绘和预算",
        "quantity": 1.0
    },
    {
        "item": "索具装配人",
        "quantity": 1.0
    },
    {
        "item": "土木规划",
        "quantity": 1.0
    },
    {
        "item": "气候控制系统",
        "quantity": 1.0
    },
    {
        "item": "预算设计",
        "quantity": 1.0
    },
    {
        "item": "消防设施",
        "quantity": 1.0
    },
    {
        "item": "文物保护设计",
        "quantity": 1.0
    },
    {
        "item": "建筑科学顾问",
        "quantity": 1.0
    },
    {
        "item": "声音工程师",
        "quantity": 1.0
    },
    {
        "item": "研究设计团队",
        "quantity": 1.0
    },
    {
        "item": "结构和环境工程",
        "quantity": 1.0
    },
    {
        "item": "预算管理",
        "quantity": 1.0
    },
    {
        "item": "展览负责人",
        "quantity": 1.0
    },
    {
        "item": "广场和建筑设计首席建筑师",
        "quantity": 1.0
    },
    {
        "item": "竞赛入围作品首席建筑师",
        "quantity": 1.0
    },
    {
        "item": "声学咨询",
        "quantity": 1.0
    },
    {
        "item": "预制混凝土承包商",
        "quantity": 1.0
    },
    {
        "item": "Urban Regeneration",
        "quantity": 1.0
    },
    {
        "item": "Agronomy",
        "quantity": 1.0
    },
    {
        "item": "Landscape and Environmental Analysis",
        "quantity": 1.0
    },
    {
        "item": "Landscape and Environmental Strategy",
        "quantity": 1.0
    },
    {
        "item": "Transport Consultant",
        "quantity": 1.0
    },
    {
        "item": "UNILAB Team",
        "quantity": 1.0
    },
    {
        "item": "Stefano Boeri Team",
        "quantity": 1.0
    },
    {
        "item": "天线和飞越",
        "quantity": 1.0
    },
    {
        "item": "私人酒柜定制",
        "quantity": 1.0
    },
    {
        "item": "客户和协作",
        "quantity": 1.0
    },
    {
        "item": "原始结构",
        "quantity": 1.0
    },
    {
        "item": "原始项目",
        "quantity": 1.0
    },
    {
        "item": "结构体",
        "quantity": 1.0
    },
    {
        "item": "视频集成",
        "quantity": 1.0
    },
    {
        "item": "保育顾问",
        "quantity": 1.0
    },
    {
        "item": "展出时间",
        "quantity": 1.0
    },
    {
        "item": "厨房及后勤系统咨询",
        "quantity": 1.0
    },
    {
        "item": "灯光咨询 ",
        "quantity": 1.0
    },
    {
        "item": "机电管综咨询",
        "quantity": 1.0
    },
    {
        "item": "结构咨询 ",
        "quantity": 1.0
    },
    {
        "item": "水压测试",
        "quantity": 1.0
    },
    {
        "item": "土壤专家",
        "quantity": 1.0
    },
    {
        "item": "石匠",
        "quantity": 1.0
    },
    {
        "item": "音效工程师",
        "quantity": 1.0
    },
    {
        "item": "窗户工程",
        "quantity": 1.0
    },
    {
        "item": "房地产开发顾问",
        "quantity": 1.0
    },
    {
        "item": "锡艺",
        "quantity": 1.0
    },
    {
        "item": "室内建造",
        "quantity": 1.0
    },
    {
        "item": "合伙经营",
        "quantity": 1.0
    },
    {
        "item": "机械安装",
        "quantity": 1.0
    },
    {
        "item": "OPC ",
        "quantity": 1.0
    },
    {
        "item": "结构与外观",
        "quantity": 1.0
    },
    {
        "item": "幕墙设计/维护顾问",
        "quantity": 1.0
    },
    {
        "item": "混凝土工程顾问",
        "quantity": 1.0
    },
    {
        "item": "室内设计单位",
        "quantity": 1.0
    },
    {
        "item": "施工图设计单位",
        "quantity": 1.0
    },
    {
        "item": "建筑设计和艺术指导",
        "quantity": 1.0
    },
    {
        "item": "拓展总监",
        "quantity": 1.0
    },
    {
        "item": "结构专业",
        "quantity": 1.0
    },
    {
        "item": "水幕设计",
        "quantity": 1.0
    },
    {
        "item": "展会（承包商）",
        "quantity": 1.0
    },
    {
        "item": "美术总监",
        "quantity": 1.0
    },
    {
        "item": "当地苗圃",
        "quantity": 1.0
    },
    {
        "item": "涂鸦作品",
        "quantity": 1.0
    },
    {
        "item": "捐赠者",
        "quantity": 1.0
    },
    {
        "item": "工程总价",
        "quantity": 1.0
    },
    {
        "item": "防水设计",
        "quantity": 1.0
    },
    {
        "item": "科罗拉多建筑事务所盐工",
        "quantity": 1.0
    },
    {
        "item": "数字化制造顾问",
        "quantity": 1.0
    },
    {
        "item": "钢筋混凝土工程师",
        "quantity": 1.0
    },
    {
        "item": "木工设计师",
        "quantity": 1.0
    },
    {
        "item": "建筑设计和景观设计",
        "quantity": 1.0
    },
    {
        "item": "深化设计施工",
        "quantity": 1.0
    },
    {
        "item": "有限责任公司",
        "quantity": 1.0
    },
    {
        "item": "CLT（交叉层压木材）供应商",
        "quantity": 1.0
    },
    {
        "item": "Arquitectos a cargo",
        "quantity": 1.0
    },
    {
        "item": "项目用地面积",
        "quantity": 1.0
    },
    {
        "item": "竣工时间：",
        "quantity": 1.0
    },
    {
        "item": "机电管线,，防火及电信工程",
        "quantity": 1.0
    },
    {
        "item": "声学/隔热",
        "quantity": 1.0
    },
    {
        "item": "Leed 认证工程师",
        "quantity": 1.0
    },
    {
        "item": "框架结构",
        "quantity": 1.0
    },
    {
        "item": "建筑承包商与合作商",
        "quantity": 1.0
    },
    {
        "item": "地址  ",
        "quantity": 1.0
    },
    {
        "item": "建筑方案设计咨询单位",
        "quantity": 1.0
    },
    {
        "item": "结构形式",
        "quantity": 1.0
    },
    {
        "item": "供水和公共卫生 ",
        "quantity": 1.0
    },
    {
        "item": "建筑挖掘",
        "quantity": 1.0
    },
    {
        "item": "联合创始人/设计总监 ",
        "quantity": 1.0
    },
    {
        "item": "生物气候设计",
        "quantity": 1.0
    },
    {
        "item": "Specifications",
        "quantity": 1.0
    },
    {
        "item": "土木结构师",
        "quantity": 1.0
    },
    {
        "item": "模块设计",
        "quantity": 1.0
    },
    {
        "item": "厨房计划",
        "quantity": 1.0
    },
    {
        "item": "价值计划",
        "quantity": 1.0
    },
    {
        "item": "可持续发展与建筑物理",
        "quantity": 1.0
    },
    {
        "item": "施工和打磨",
        "quantity": 1.0
    },
    {
        "item": "艺术创作",
        "quantity": 1.0
    },
    {
        "item": "内饰风格",
        "quantity": 1.0
    },
    {
        "item": "礼拜顾问",
        "quantity": 1.0
    },
    {
        "item": "环境工程师– HQE",
        "quantity": 1.0
    },
    {
        "item": "钢铁划分",
        "quantity": 1.0
    },
    {
        "item": "金属墙／底板",
        "quantity": 1.0
    },
    {
        "item": "阳极氧化",
        "quantity": 1.0
    },
    {
        "item": "能源工程",
        "quantity": 1.0
    },
    {
        "item": "土木工程承包商",
        "quantity": 1.0
    },
    {
        "item": "艺术 艺术",
        "quantity": 1.0
    },
    {
        "item": "土力工程",
        "quantity": 1.0
    },
    {
        "item": "开放空间规划",
        "quantity": 1.0
    },
    {
        "item": "防火/ 建筑设备",
        "quantity": 1.0
    },
    {
        "item": "能源概念竞赛",
        "quantity": 1.0
    },
    {
        "item": "铝板供应商",
        "quantity": 1.0
    },
    {
        "item": "Text",
        "quantity": 1.0
    },
    {
        "item": "ART FM Team",
        "quantity": 1.0
    },
    {
        "item": "设计辅助",
        "quantity": 1.0
    },
    {
        "item": "预算与计量",
        "quantity": 1.0
    },
    {
        "item": "泊车位",
        "quantity": 1.0
    },
    {
        "item": "铝材顾问 ",
        "quantity": 1.0
    },
    {
        "item": "设计和实施设计团队",
        "quantity": 1.0
    },
    {
        "item": "结构土木工程师",
        "quantity": 1.0
    },
    {
        "item": "总楼地板面积",
        "quantity": 1.0
    },
    {
        "item": "文化技术",
        "quantity": 1.0
    },
    {
        "item": "竞争评委",
        "quantity": 1.0
    },
    {
        "item": "建造价值顾问",
        "quantity": 1.0
    },
    {
        "item": "施工安装",
        "quantity": 1.0
    },
    {
        "item": "领导和设计合作伙伴",
        "quantity": 1.0
    },
    {
        "item": "艺术学生",
        "quantity": 1.0
    },
    {
        "item": "展馆制造和生产",
        "quantity": 1.0
    },
    {
        "item": "厨房咨询",
        "quantity": 1.0
    },
    {
        "item": "W-安装",
        "quantity": 1.0
    },
    {
        "item": "建筑物理学顾问",
        "quantity": 1.0
    },
    {
        "item": "ovic, Silvia Sandor, Jim Shi, Yushang Zhang室内设计团队",
        "quantity": 1.0
    },
    {
        "item": "历史建筑保护咨询",
        "quantity": 1.0
    },
    {
        "item": "雨水工程师",
        "quantity": 1.0
    },
    {
        "item": "工程企业",
        "quantity": 1.0
    },
    {
        "item": "公共卫生工程",
        "quantity": 1.0
    },
    {
        "item": "IND Team",
        "quantity": 1.0
    },
    {
        "item": "驻马德里设计配合团队",
        "quantity": 1.0
    },
    {
        "item": "建筑记录员",
        "quantity": 1.0
    },
    {
        "item": "驻利马设计配合团队",
        "quantity": 1.0
    },
    {
        "item": " 主创建筑师",
        "quantity": 1.0
    },
    {
        "item": "滑雪机合作方",
        "quantity": 1.0
    },
    {
        "item": "团队其他成员",
        "quantity": 1.0
    },
    {
        "item": "主要用材",
        "quantity": 1.0
    },
    {
        "item": "灯光设计及咨询",
        "quantity": 1.0
    },
    {
        "item": "电气暖通工程",
        "quantity": 1.0
    },
    {
        "item": "3D 渲染",
        "quantity": 1.0
    },
    {
        "item": "项目建筑",
        "quantity": 1.0
    },
    {
        "item": "项目合作人",
        "quantity": 1.0
    },
    {
        "item": "供暖",
        "quantity": 1.0
    },
    {
        "item": "导视及平面设计",
        "quantity": 1.0
    },
    {
        "item": "本地办公",
        "quantity": 1.0
    },
    {
        "item": "图形表现",
        "quantity": 1.0
    },
    {
        "item": "水力工程",
        "quantity": 1.0
    },
    {
        "item": "垃圾处理设施",
        "quantity": 1.0
    },
    {
        "item": "电气与防火",
        "quantity": 1.0
    },
    {
        "item": "建筑系统工程师",
        "quantity": 1.0
    },
    {
        "item": "总建筑规模",
        "quantity": 1.0
    },
    {
        "item": "环境绘图",
        "quantity": 1.0
    },
    {
        "item": "机械与电子工程师",
        "quantity": 1.0
    },
    {
        "item": "机械技术",
        "quantity": 1.0
    },
    {
        "item": "机电气工程",
        "quantity": 1.0
    },
    {
        "item": "管道设计承建商",
        "quantity": 1.0
    },
    {
        "item": "电力设计承建商",
        "quantity": 1.0
    },
    {
        "item": "ID - 办公室通用设计",
        "quantity": 1.0
    },
    {
        "item": "ID - 办公室室内",
        "quantity": 1.0
    },
    {
        "item": "软质景观",
        "quantity": 1.0
    },
    {
        "item": "铝 & 釉",
        "quantity": 1.0
    },
    {
        "item": "水池 & 水景",
        "quantity": 1.0
    },
    {
        "item": "管道, 卫生, 燃气",
        "quantity": 1.0
    },
    {
        "item": "合作项目建筑师",
        "quantity": 1.0
    },
    {
        "item": "Parking Planning",
        "quantity": 1.0
    },
    {
        "item": "注册区域",
        "quantity": 1.0
    },
    {
        "item": "助理建筑师，结构工程师",
        "quantity": 1.0
    },
    {
        "item": "机构与环境工程师",
        "quantity": 1.0
    },
    {
        "item": "展示时间",
        "quantity": 1.0
    },
    {
        "item": "主要建材",
        "quantity": 1.0
    },
    {
        "item": "植物和植物养护",
        "quantity": 1.0
    },
    {
        "item": "施工现场面积",
        "quantity": 1.0
    },
    {
        "item": "屋顶细部设计",
        "quantity": 1.0
    },
    {
        "item": "灯光（屋顶概念及方案设计）",
        "quantity": 1.0
    },
    {
        "item": "结构团队成员",
        "quantity": 1.0
    },
    {
        "item": "屋顶及人行步道结构设计",
        "quantity": 1.0
    },
    {
        "item": "合作事务所",
        "quantity": 1.0
    },
    {
        "item": "巴西项目经理",
        "quantity": 1.0
    },
    {
        "item": "Barcode 团队",
        "quantity": 1.0
    },
    {
        "item": "Tirana Municipality Team",
        "quantity": 1.0
    },
    {
        "item": "剧场设计顾问",
        "quantity": 1.0
    },
    {
        "item": "外墙装饰",
        "quantity": 1.0
    },
    {
        "item": "设计图案度",
        "quantity": 1.0
    },
    {
        "item": "经济学家，TCE",
        "quantity": 1.0
    },
    {
        "item": "机械及电力工程",
        "quantity": 1.0
    },
    {
        "item": "市政及结构工程",
        "quantity": 1.0
    },
    {
        "item": "建筑经济",
        "quantity": 1.0
    },
    {
        "item": "CDM联络员",
        "quantity": 1.0
    },
    {
        "item": "水生物管理",
        "quantity": 1.0
    },
    {
        "item": "水族科技",
        "quantity": 1.0
    },
    {
        "item": "环境指引",
        "quantity": 1.0
    },
    {
        "item": "Project Completion Date",
        "quantity": 1.0
    },
    {
        "item": "Registered Structural Engineer (RSE)",
        "quantity": 1.0
    },
    {
        "item": "Authorised Person (AP)",
        "quantity": 1.0
    },
    {
        "item": "Research Assistants (RA)",
        "quantity": 1.0
    },
    {
        "item": "主要研究者 (PI)",
        "quantity": 1.0
    },
    {
        "item": "MSCP",
        "quantity": 1.0
    },
    {
        "item": "维多利亚之门拱廊建筑看起来像三个人身份与彼此不同的元素和利兹白话。 ",
        "quantity": 1.0
    },
    {
        "item": "联络员",
        "quantity": 1.0
    },
    {
        "item": "建筑结构工程",
        "quantity": 1.0
    },
    {
        "item": "Cheng Bao",
        "quantity": 1.0
    },
    {
        "item": "项目联络员",
        "quantity": 1.0
    },
    {
        "item": "户外庭院面积",
        "quantity": 1.0
    },
    {
        "item": "国际照明设计",
        "quantity": 1.0
    },
    {
        "item": "项目管理和研究",
        "quantity": 1.0
    },
    {
        "item": "国际景观设计师",
        "quantity": 1.0
    },
    {
        "item": "国际室内设计师",
        "quantity": 1.0
    },
    {
        "item": "当地议员工程",
        "quantity": 1.0
    },
    {
        "item": "VCA设计团队",
        "quantity": 1.0
    },
    {
        "item": "国际设计建筑师",
        "quantity": 1.0
    },
    {
        "item": "建筑设计& 助理",
        "quantity": 1.0
    },
    {
        "item": "设计建造",
        "quantity": 1.0
    },
    {
        "item": "改造后建筑面积",
        "quantity": 1.0
    },
    {
        "item": "Cliente",
        "quantity": 1.0
    },
    {
        "item": "台球室面积",
        "quantity": 1.0
    },
    {
        "item": "商铺面积",
        "quantity": 1.0
    },
    {
        "item": "住房面积",
        "quantity": 1.0
    },
    {
        "item": "绿地面积",
        "quantity": 1.0
    },
    {
        "item": "安全性能",
        "quantity": 1.0
    },
    {
        "item": "建筑设计及室内设计",
        "quantity": 1.0
    },
    {
        "item": "Installatio nDesign",
        "quantity": 1.0
    },
    {
        "item": "Extension GIA",
        "quantity": 1.0
    },
    {
        "item": "Existing GIA",
        "quantity": 1.0
    },
    {
        "item": "净使用面积",
        "quantity": 1.0
    },
    {
        "item": "机械学 / 铅功能",
        "quantity": 1.0
    },
    {
        "item": "组织方",
        "quantity": 1.0
    },
    {
        "item": "外立面工程师",
        "quantity": 1.0
    },
    {
        "item": "店铺面积",
        "quantity": 1.0
    },
    {
        "item": "认证机构",
        "quantity": 1.0
    },
    {
        "item": "负责公司",
        "quantity": 1.0
    },
    {
        "item": "节能减排专家",
        "quantity": 1.0
    },
    {
        "item": "地质勘测师",
        "quantity": 1.0
    },
    {
        "item": "Max Lamb 麦克斯·兰姆",
        "quantity": 1.0
    },
    {
        "item": "Building Site",
        "quantity": 1.0
    },
    {
        "item": "[\"Heerim Architects & Planners Heerim Architects & Planners\", \"Heerim Architects & Planners Heerim Architects & Planners\"]",
        "quantity": 1.0
    },
    {
        "item": "[\"UNStudio UNStudio\", \"UNStudio UNStudio\"]",
        "quantity": 1.0
    },
    {
        "item": "音响工程顾问",
        "quantity": 1.0
    },
    {
        "item": "Allies and Morrison设计团队",
        "quantity": 1.0
    },
    {
        "item": "Allies and Morrison副董事",
        "quantity": 1.0
    },
    {
        "item": "Allies and Morrison合伙人",
        "quantity": 1.0
    },
    {
        "item": "OMA 项目建筑师",
        "quantity": 1.0
    },
    {
        "item": "OMA 执行董事",
        "quantity": 1.0
    },
    {
        "item": "OMA 项目合伙人",
        "quantity": 1.0
    },
    {
        "item": "结构/核心筒",
        "quantity": 1.0
    },
    {
        "item": "参与人员",
        "quantity": 1.0
    },
    {
        "item": "Structural Engineer and Distributor of KLH in Germany ",
        "quantity": 1.0
    },
    {
        "item": "领导建筑师",
        "quantity": 1.0
    },
    {
        "item": "保育建筑师",
        "quantity": 1.0
    },
    {
        "item": "项目监管",
        "quantity": 1.0
    },
    {
        "item": "环境标识设计",
        "quantity": 1.0
    },
    {
        "item": "原设计师",
        "quantity": 1.0
    },
    {
        "item": "结构设计成员",
        "quantity": 1.0
    },
    {
        "item": "建筑设计成员",
        "quantity": 1.0
    },
    {
        "item": "外围钢结构",
        "quantity": 1.0
    },
    {
        "item": "垂直绿化顾问",
        "quantity": 1.0
    },
    {
        "item": "音乐顾问",
        "quantity": 1.0
    },
    {
        "item": "项目建筑是",
        "quantity": 1.0
    },
    {
        "item": "座位数目",
        "quantity": 1.0
    },
    {
        "item": "编织",
        "quantity": 1.0
    },
    {
        "item": "赞助和捐赠",
        "quantity": 1.0
    },
    {
        "item": "驻场施工团队",
        "quantity": 1.0
    },
    {
        "item": "直升机服务",
        "quantity": 1.0
    },
    {
        "item": "冬日木屋维护",
        "quantity": 1.0
    },
    {
        "item": "结构工程和主要承包商",
        "quantity": 1.0
    },
    {
        "item": "建筑规范咨询",
        "quantity": 1.0
    },
    {
        "item": "建筑修复",
        "quantity": 1.0
    },
    {
        "item": "室内设计／景观",
        "quantity": 1.0
    },
    {
        "item": "主要合作方",
        "quantity": 1.0
    },
    {
        "item": "混凝土结构和地基顾问",
        "quantity": 1.0
    },
    {
        "item": "特别合作方",
        "quantity": 1.0
    },
    {
        "item": "总支持",
        "quantity": 1.0
    },
    {
        "item": "基金援助与支持",
        "quantity": 1.0
    },
    {
        "item": "协办单位",
        "quantity": 1.0
    },
    {
        "item": "捐助单位",
        "quantity": 1.0
    },
    {
        "item": "作者团队",
        "quantity": 1.0
    },
    {
        "item": "二期完工时间",
        "quantity": 1.0
    },
    {
        "item": "室内灯光主持设计师",
        "quantity": 1.0
    },
    {
        "item": "Children's Pool Artist",
        "quantity": 1.0
    },
    {
        "item": "Building Area ",
        "quantity": 1.0
    },
    {
        "item": "MEP承包商",
        "quantity": 1.0
    },
    {
        "item": "地理科技顾问",
        "quantity": 1.0
    },
    {
        "item": "检查员",
        "quantity": 1.0
    },
    {
        "item": "场景",
        "quantity": 1.0
    },
    {
        "item": "Scenography",
        "quantity": 1.0
    },
    {
        "item": "Lightning",
        "quantity": 1.0
    },
    {
        "item": "屋顶结构工程",
        "quantity": 1.0
    },
    {
        "item": "设计合作, 建造",
        "quantity": 1.0
    },
    {
        "item": "证书",
        "quantity": 1.0
    },
    {
        "item": "城镇规划",
        "quantity": 1.0
    },
    {
        "item": "项目监督管理",
        "quantity": 1.0
    },
    {
        "item": "灯光设计 ",
        "quantity": 1.0
    },
    {
        "item": " 设计责任人 ",
        "quantity": 1.0
    },
    {
        "item": "艺术品管理",
        "quantity": 1.0
    },
    {
        "item": "模型摄影",
        "quantity": 1.0
    },
    {
        "item": "项目建筑师 (室内)",
        "quantity": 1.0
    },
    {
        "item": "项目建筑师(建筑)",
        "quantity": 1.0
    },
    {
        "item": "主要的承包商",
        "quantity": 1.0
    },
    {
        "item": "CDM项目协调员",
        "quantity": 1.0
    },
    {
        "item": "消防策略工程师",
        "quantity": 1.0
    },
    {
        "item": "Executive Architects",
        "quantity": 1.0
    },
    {
        "item": "园林",
        "quantity": 1.0
    },
    {
        "item": "铁艺",
        "quantity": 1.0
    },
    {
        "item": "木器工程师",
        "quantity": 1.0
    },
    {
        "item": "BTA",
        "quantity": 1.0
    },
    {
        "item": "Grading and Septic",
        "quantity": 1.0
    },
    {
        "item": "室内设计及施工团队 ",
        "quantity": 1.0
    },
    {
        "item": "结构发展",
        "quantity": 1.0
    },
    {
        "item": "机电设施，电梯和照明设计顾问",
        "quantity": 1.0
    },
    {
        "item": "艺术家合作(壁纸&品牌图形)",
        "quantity": 1.0
    },
    {
        "item": "Bioclimatic Consultants",
        "quantity": 1.0
    },
    {
        "item": "Enviromental and Lansdcape Consultants",
        "quantity": 1.0
    },
    {
        "item": "Technical Designs Consultant",
        "quantity": 1.0
    },
    {
        "item": "泳池设计顾问",
        "quantity": 1.0
    },
    {
        "item": "检察员",
        "quantity": 1.0
    },
    {
        "item": "可达性设计",
        "quantity": 1.0
    },
    {
        "item": "给水工程",
        "quantity": 1.0
    },
    {
        "item": "安保设计",
        "quantity": 1.0
    },
    {
        "item": "当地建筑团队",
        "quantity": 1.0
    },
    {
        "item": "酒店室内设计",
        "quantity": 1.0
    },
    {
        "item": "建筑房屋面积",
        "quantity": 1.0
    },
    {
        "item": "室外活动面积",
        "quantity": 1.0
    },
    {
        "item": "总结构公司",
        "quantity": 1.0
    },
    {
        "item": "低合金高强度立面和幕墙穿孔",
        "quantity": 1.0
    },
    {
        "item": "基地面积:",
        "quantity": 1.0
    },
    {
        "item": "工程实施方",
        "quantity": 1.0
    },
    {
        "item": "结构工厂",
        "quantity": 1.0
    },
    {
        "item": "工程设计配合",
        "quantity": 1.0
    },
    {
        "item": "规划/建筑/室内设计",
        "quantity": 1.0
    },
    {
        "item": "消防咨询",
        "quantity": 1.0
    },
    {
        "item": "MEP顾问及制造",
        "quantity": 1.0
    },
    {
        "item": "主要供应商",
        "quantity": 1.0
    },
    {
        "item": "MEP + FP工程师",
        "quantity": 1.0
    },
    {
        "item": "施工测量师",
        "quantity": 1.0
    },
    {
        "item": "审计",
        "quantity": 1.0
    },
    {
        "item": "交通流线研究",
        "quantity": 1.0
    },
    {
        "item": "安全和控制",
        "quantity": 1.0
    },
    {
        "item": "宣传团队",
        "quantity": 1.0
    },
    {
        "item": "通用工程解决方案",
        "quantity": 1.0
    },
    {
        "item": "机械及管工",
        "quantity": 1.0
    },
    {
        "item": "品牌和市场合作",
        "quantity": 1.0
    },
    {
        "item": "设施设计",
        "quantity": 1.0
    },
    {
        "item": "项目总管",
        "quantity": 1.0
    },
    {
        "item": "电影摄像",
        "quantity": 1.0
    },
    {
        "item": "风向",
        "quantity": 1.0
    },
    {
        "item": "设计工程师",
        "quantity": 1.0
    },
    {
        "item": "Lead Designers",
        "quantity": 1.0
    },
    {
        "item": "Design and Project Management Architects",
        "quantity": 1.0
    },
    {
        "item": "声学 / AV / 剧场 / 多媒体咨询",
        "quantity": 1.0
    },
    {
        "item": "促进执行者",
        "quantity": 1.0
    },
    {
        "item": "M/E/P 顾问",
        "quantity": 1.0
    },
    {
        "item": "土壤工程",
        "quantity": 1.0
    },
    {
        "item": "室内设计/装饰",
        "quantity": 1.0
    },
    {
        "item": "计量师",
        "quantity": 1.0
    },
    {
        "item": "艺术展览",
        "quantity": 1.0
    },
    {
        "item": "生物气候学",
        "quantity": 1.0
    },
    {
        "item": "艺术品",
        "quantity": 1.0
    },
    {
        "item": "影音及照明硬件",
        "quantity": 1.0
    },
    {
        "item": "装饰和家具生产",
        "quantity": 1.0
    },
    {
        "item": "Building Architectural Design",
        "quantity": 1.0
    },
    {
        "item": "大厦单位",
        "quantity": 1.0
    },
    {
        "item": "PMC",
        "quantity": 1.0
    },
    {
        "item": "接缝顾问",
        "quantity": 1.0
    },
    {
        "item": "总体设计",
        "quantity": 1.0
    },
    {
        "item": "竞赛时间",
        "quantity": 1.0
    },
    {
        "item": "LEED 咨询",
        "quantity": 1.0
    },
    {
        "item": "行车道净宽度",
        "quantity": 1.0
    },
    {
        "item": " AECOM与展厅设计合作单位",
        "quantity": 1.0
    },
    {
        "item": "AECOM分包 幕墙顾问",
        "quantity": 1.0
    },
    {
        "item": "AECOM分包 照明顾问",
        "quantity": 1.0
    },
    {
        "item": " 室内",
        "quantity": 1.0
    },
    {
        "item": "首席策展人",
        "quantity": 1.0
    },
    {
        "item": "机械、电气、管道工程",
        "quantity": 1.0
    },
    {
        "item": "装置设计提供",
        "quantity": 1.0
    },
    {
        "item": "功能设置",
        "quantity": 1.0
    },
    {
        "item": "标志系统",
        "quantity": 1.0
    },
    {
        "item": "摄影与后期",
        "quantity": 1.0
    },
    {
        "item": "业主顾问",
        "quantity": 1.0
    },
    {
        "item": "一层比例",
        "quantity": 1.0
    },
    {
        "item": "图表设计",
        "quantity": 1.0
    },
    {
        "item": "树艺设计",
        "quantity": 1.0
    },
    {
        "item": "ESD Consultant",
        "quantity": 1.0
    },
    {
        "item": "Mechanical & Electrical Engineer",
        "quantity": 1.0
    },
    {
        "item": "座位区域 (室内)",
        "quantity": 1.0
    },
    {
        "item": "Civil and Structural Engineer",
        "quantity": 1.0
    },
    {
        "item": "地热能源",
        "quantity": 1.0
    },
    {
        "item": "气候控制",
        "quantity": 1.0
    },
    {
        "item": "指导工作",
        "quantity": 1.0
    },
    {
        "item": "零售专家",
        "quantity": 1.0
    },
    {
        "item": "液体工程师",
        "quantity": 1.0
    },
    {
        "item": "暖通空调和电力设计",
        "quantity": 1.0
    },
    {
        "item": "展示家具与定制灯具设计",
        "quantity": 1.0
    },
    {
        "item": "有顶建筑面积",
        "quantity": 1.0
    },
    {
        "item": "建成办公面积",
        "quantity": 1.0
    },
    {
        "item": "木工工程师",
        "quantity": 1.0
    },
    {
        "item": "场地表面",
        "quantity": 1.0
    },
    {
        "item": "光照咨询",
        "quantity": 1.0
    },
    {
        "item": "场地知道",
        "quantity": 1.0
    },
    {
        "item": "领衔设计师",
        "quantity": 1.0
    },
    {
        "item": "主项目工程师",
        "quantity": 1.0
    },
    {
        "item": "建筑物理与消防顾问",
        "quantity": 1.0
    },
    {
        "item": "Buró 4事务所主任建筑师",
        "quantity": 1.0
    },
    {
        "item": "公寓内部装饰",
        "quantity": 1.0
    },
    {
        "item": "加工生产",
        "quantity": 1.0
    },
    {
        "item": "场地结构工程",
        "quantity": 1.0
    },
    {
        "item": "数据管理",
        "quantity": 1.0
    },
    {
        "item": "可持续性评价",
        "quantity": 1.0
    },
    {
        "item": "水上顾问",
        "quantity": 1.0
    },
    {
        "item": "座位数: 奥林匹克皮划艇激流运动场",
        "quantity": 1.0
    },
    {
        "item": "监察办公室",
        "quantity": 1.0
    },
    {
        "item": "客户，总建设",
        "quantity": 1.0
    },
    {
        "item": "创意/设计/艺术总监",
        "quantity": 1.0
    },
    {
        "item": "建筑专业负责人",
        "quantity": 1.0
    },
    {
        "item": "大堂家具与艺术陈设",
        "quantity": 1.0
    },
    {
        "item": "结构，土方工程，防水屋面，电梯，金属制品",
        "quantity": 1.0
    },
    {
        "item": "防火咨询",
        "quantity": 1.0
    },
    {
        "item": "博物馆专家",
        "quantity": 1.0
    },
    {
        "item": "幕墙咨询",
        "quantity": 1.0
    },
    {
        "item": "可容纳人数",
        "quantity": 1.0
    },
    {
        "item": "协商",
        "quantity": 1.0
    },
    {
        "item": "能源供热",
        "quantity": 1.0
    },
    {
        "item": "建筑尺度",
        "quantity": 1.0
    },
    {
        "item": "小区面积",
        "quantity": 1.0
    },
    {
        "item": "干墙安装",
        "quantity": 1.0
    },
    {
        "item": "Architectus团队",
        "quantity": 1.0
    },
    {
        "item": "重建公司",
        "quantity": 1.0
    },
    {
        "item": "设计师来自",
        "quantity": 1.0
    },
    {
        "item": "交通及人群流通顾问",
        "quantity": 1.0
    },
    {
        "item": "项目室内建筑师",
        "quantity": 1.0
    },
    {
        "item": "开发团队",
        "quantity": 1.0
    },
    {
        "item": "景观设计 ",
        "quantity": 1.0
    },
    {
        "item": "CVSE工程师",
        "quantity": 1.0
    },
    {
        "item": "参与方",
        "quantity": 1.0
    },
    {
        "item": "合作主任",
        "quantity": 1.0
    },
    {
        "item": "场地操作",
        "quantity": 1.0
    },
    {
        "item": "场地主持",
        "quantity": 1.0
    },
    {
        "item": "建筑界限",
        "quantity": 1.0
    },
    {
        "item": "赞助人",
        "quantity": 1.0
    },
    {
        "item": "安全协调与健康",
        "quantity": 1.0
    },
    {
        "item": "AECOM建筑",
        "quantity": 1.0
    },
    {
        "item": " 合作商",
        "quantity": 1.0
    },
    {
        "item": "文章翻译",
        "quantity": 1.0
    },
    {
        "item": "执行项目经理",
        "quantity": 1.0
    },
    {
        "item": "设计施工时间",
        "quantity": 1.0
    },
    {
        "item": "艺术咨询",
        "quantity": 1.0
    },
    {
        "item": "发布团队",
        "quantity": 1.0
    },
    {
        "item": "M+E 工程师",
        "quantity": 1.0
    },
    {
        "item": "铝合金窗户",
        "quantity": 1.0
    },
    {
        "item": "M&E建造方",
        "quantity": 1.0
    },
    {
        "item": "装配员",
        "quantity": 1.0
    },
    {
        "item": "石膏板安装",
        "quantity": 1.0
    },
    {
        "item": "采暖/洁具",
        "quantity": 1.0
    },
    {
        "item": "地面工程",
        "quantity": 1.0
    },
    {
        "item": "住宅",
        "quantity": 1.0
    },
    {
        "item": "电力与暖通空调",
        "quantity": 1.0
    },
    {
        "item": "环境和能源项目经理",
        "quantity": 1.0
    },
    {
        "item": "项目经理/发起人",
        "quantity": 1.0
    },
    {
        "item": " 伍兹贝格服务范畴",
        "quantity": 1.0
    },
    {
        "item": "导航系统",
        "quantity": 1.0
    },
    {
        "item": "海岸工程",
        "quantity": 1.0
    },
    {
        "item": "其他参与者 ",
        "quantity": 1.0
    },
    {
        "item": "项目团队 （公共区域）",
        "quantity": 1.0
    },
    {
        "item": "高压电项目",
        "quantity": 1.0
    },
    {
        "item": "电力和安全项目",
        "quantity": 1.0
    },
    {
        "item": "二期项目实施体",
        "quantity": 1.0
    },
    {
        "item": "二期施工团队",
        "quantity": 1.0
    },
    {
        "item": "一期 LEED顾问",
        "quantity": 1.0
    },
    {
        "item": "Facebook & Instagram",
        "quantity": 1.0
    },
    {
        "item": "一期景观设计",
        "quantity": 1.0
    },
    {
        "item": "项目实施",
        "quantity": 1.0
    },
    {
        "item": "一期设计和总负责",
        "quantity": 1.0
    },
    {
        "item": "行人模型",
        "quantity": 1.0
    },
    {
        "item": "风力工程师",
        "quantity": 1.0
    },
    {
        "item": "ZHA 项目团队",
        "quantity": 1.0
    },
    {
        "item": "ZHA 项目总监",
        "quantity": 1.0
    },
    {
        "item": "结构和木框架",
        "quantity": 1.0
    },
    {
        "item": "承建者",
        "quantity": 1.0
    },
    {
        "item": "LAVA团队",
        "quantity": 1.0
    },
    {
        "item": "饮食服务顾问",
        "quantity": 1.0
    },
    {
        "item": "结构及立面设计",
        "quantity": 1.0
    },
    {
        "item": "扎哈事务所项目主管",
        "quantity": 1.0
    },
    {
        "item": "MEP Engineer",
        "quantity": 1.0
    },
    {
        "item": "介绍文字",
        "quantity": 1.0
    },
    {
        "item": "起草",
        "quantity": 1.0
    },
    {
        "item": "Hvac",
        "quantity": 1.0
    },
    {
        "item": "拓展项目亚美尼亚 1929",
        "quantity": 1.0
    },
    {
        "item": "总宽度",
        "quantity": 1.0
    },
    {
        "item": "项目状态",
        "quantity": 1.0
    },
    {
        "item": "古建修复",
        "quantity": 1.0
    },
    {
        "item": "考古学研究",
        "quantity": 1.0
    },
    {
        "item": "Henning Larsen建筑事务所室内设计团队",
        "quantity": 1.0
    },
    {
        "item": "园艺顾问",
        "quantity": 1.0
    },
    {
        "item": "预算控制",
        "quantity": 1.0
    },
    {
        "item": "电子设计",
        "quantity": 1.0
    },
    {
        "item": "现场质量控制",
        "quantity": 1.0
    },
    {
        "item": "场地考古",
        "quantity": 1.0
    },
    {
        "item": "组织支持",
        "quantity": 1.0
    },
    {
        "item": "监督总监",
        "quantity": 1.0
    },
    {
        "item": "项目服务咨询",
        "quantity": 1.0
    },
    {
        "item": "M&E",
        "quantity": 1.0
    },
    {
        "item": "项目结构y",
        "quantity": 1.0
    },
    {
        "item": "城市规划和建筑署",
        "quantity": 1.0
    },
    {
        "item": "牛粪泥调和的地板工程",
        "quantity": 1.0
    },
    {
        "item": "项目经理与场地顾问",
        "quantity": 1.0
    },
    {
        "item": "CGI",
        "quantity": 1.0
    },
    {
        "item": "剧院顾问（技术）",
        "quantity": 1.0
    },
    {
        "item": "标志平面设计",
        "quantity": 1.0
    },
    {
        "item": "团队主持",
        "quantity": 1.0
    },
    {
        "item": "承包商 Authority",
        "quantity": 1.0
    },
    {
        "item": "总场地面积",
        "quantity": 1.0
    },
    {
        "item": "User Group",
        "quantity": 1.0
    },
    {
        "item": "Allies and Morrison副合伙人",
        "quantity": 1.0
    },
    {
        "item": "Planning Consultant",
        "quantity": 1.0
    },
    {
        "item": "Muralist",
        "quantity": 1.0
    },
    {
        "item": "镜面设计",
        "quantity": 1.0
    },
    {
        "item": "立式展陈",
        "quantity": 1.0
    },
    {
        "item": "墙壁和机械展陈",
        "quantity": 1.0
    },
    {
        "item": "平均造价",
        "quantity": 1.0
    },
    {
        "item": "Book Direction",
        "quantity": 1.0
    },
    {
        "item": "预算造价",
        "quantity": 1.0
    },
    {
        "item": "材料统计员",
        "quantity": 1.0
    },
    {
        "item": "室内外标牌设计",
        "quantity": 1.0
    },
    {
        "item": "录影",
        "quantity": 1.0
    },
    {
        "item": "大厅",
        "quantity": 1.0
    },
    {
        "item": "钢结构组装",
        "quantity": 1.0
    },
    {
        "item": "屋面覆盖",
        "quantity": 1.0
    },
    {
        "item": "机械紧固",
        "quantity": 1.0
    },
    {
        "item": "工具",
        "quantity": 1.0
    },
    {
        "item": "瑞士理工学院团队",
        "quantity": 1.0
    },
    {
        "item": "经济记录",
        "quantity": 1.0
    },
    {
        "item": "Henning Larsen建筑事务所的建筑师团队",
        "quantity": 1.0
    },
    {
        "item": "档案研究",
        "quantity": 1.0
    },
    {
        "item": "木家具承包商",
        "quantity": 1.0
    },
    {
        "item": "HVAC 承包商",
        "quantity": 1.0
    },
    {
        "item": "声热",
        "quantity": 1.0
    },
    {
        "item": "家具生产",
        "quantity": 1.0
    },
    {
        "item": "电力承包商",
        "quantity": 1.0
    },
    {
        "item": "HVAC-设计",
        "quantity": 1.0
    },
    {
        "item": "操作者",
        "quantity": 1.0
    },
    {
        "item": "最高层高",
        "quantity": 1.0
    },
    {
        "item": "幼儿园顾问",
        "quantity": 1.0
    },
    {
        "item": "推广人",
        "quantity": 1.0
    },
    {
        "item": "地理信息技术顾问",
        "quantity": 1.0
    },
    {
        "item": "质量监测与施工监理",
        "quantity": 1.0
    },
    {
        "item": "自助式公寓",
        "quantity": 1.0
    },
    {
        "item": "工程系统",
        "quantity": 1.0
    },
    {
        "item": "创始建筑师",
        "quantity": 1.0
    },
    {
        "item": "Surface area",
        "quantity": 1.0
    },
    {
        "item": "Contructora",
        "quantity": 1.0
    },
    {
        "item": "执行与施工",
        "quantity": 1.0
    },
    {
        "item": "声学与照明",
        "quantity": 1.0
    },
    {
        "item": "油漆业务",
        "quantity": 1.0
    },
    {
        "item": "工程师·",
        "quantity": 1.0
    },
    {
        "item": "玻璃大师",
        "quantity": 1.0
    },
    {
        "item": "玻璃生产",
        "quantity": 1.0
    },
    {
        "item": "结构咨询师",
        "quantity": 1.0
    },
    {
        "item": "建筑用途",
        "quantity": 1.0
    },
    {
        "item": "美术馆面积",
        "quantity": 1.0
    },
    {
        "item": "景观、基础设施与市政工程",
        "quantity": 1.0
    },
    {
        "item": "合作建筑师 (PSP)",
        "quantity": 1.0
    },
    {
        "item": "图形文件",
        "quantity": 1.0
    },
    {
        "item": "项目交付",
        "quantity": 1.0
    },
    {
        "item": "参数化编程",
        "quantity": 1.0
    },
    {
        "item": "项目过程",
        "quantity": 1.0
    },
    {
        "item": "住宅公寓3 (顶层+阁楼层)",
        "quantity": 1.0
    },
    {
        "item": "住宅公寓2 (第二层)",
        "quantity": 1.0
    },
    {
        "item": "E设计师",
        "quantity": 1.0
    },
    {
        "item": "HLS（采暖、通风和设备）设计师",
        "quantity": 1.0
    },
    {
        "item": "信息通信工程",
        "quantity": 1.0
    },
    {
        "item": "结构物理学家",
        "quantity": 1.0
    },
    {
        "item": "工作区管理",
        "quantity": 1.0
    },
    {
        "item": "防火技术平面图",
        "quantity": 1.0
    },
    {
        "item": "信号/防火安全",
        "quantity": 1.0
    },
    {
        "item": "信息/声效/视觉",
        "quantity": 1.0
    },
    {
        "item": "定制制造商",
        "quantity": 1.0
    },
    {
        "item": "Presupuesto",
        "quantity": 1.0
    },
    {
        "item": "建设服务工程",
        "quantity": 1.0
    },
    {
        "item": "造价管理",
        "quantity": 1.0
    },
    {
        "item": "管理主持",
        "quantity": 1.0
    },
    {
        "item": "设计和施工",
        "quantity": 1.0
    },
    {
        "item": "管理部门",
        "quantity": 1.0
    },
    {
        "item": "影音与音响设计",
        "quantity": 1.0
    },
    {
        "item": "结构设计咨询",
        "quantity": 1.0
    },
    {
        "item": "占用空间",
        "quantity": 1.0
    },
    {
        "item": "质量检测员",
        "quantity": 1.0
    },
    {
        "item": "工程规划",
        "quantity": 1.0
    },
    {
        "item": "建筑检测员",
        "quantity": 1.0
    },
    {
        "item": "项目指导 ",
        "quantity": 1.0
    },
    {
        "item": "机械与卫生",
        "quantity": 1.0
    },
    {
        "item": "客房数",
        "quantity": 1.0
    },
    {
        "item": "空调系统工程",
        "quantity": 1.0
    },
    {
        "item": "室内设计合作",
        "quantity": 1.0
    },
    {
        "item": "施工状态",
        "quantity": 1.0
    },
    {
        "item": "建设单元",
        "quantity": 1.0
    },
    {
        "item": "燃气装置",
        "quantity": 1.0
    },
    {
        "item": "安全措施和消防咨询",
        "quantity": 1.0
    },
    {
        "item": "Exterior Architects",
        "quantity": 1.0
    },
    {
        "item": "Interior Architects",
        "quantity": 1.0
    },
    {
        "item": "苏黎世建筑物理",
        "quantity": 1.0
    },
    {
        "item": "结构工程师 / 立面顾问",
        "quantity": 1.0
    },
    {
        "item": "Lead Project Designer",
        "quantity": 1.0
    },
    {
        "item": "项目要求",
        "quantity": 1.0
    },
    {
        "item": "竞赛作者",
        "quantity": 1.0
    },
    {
        "item": "合作负责建筑师",
        "quantity": 1.0
    },
    {
        "item": "Mechanical services",
        "quantity": 1.0
    },
    {
        "item": "剧院和音响",
        "quantity": 1.0
    },
    {
        "item": "安全与协调",
        "quantity": 1.0
    },
    {
        "item": "施工承包",
        "quantity": 1.0
    },
    {
        "item": "设计发展团队",
        "quantity": 1.0
    },
    {
        "item": "概念合作者",
        "quantity": 1.0
    },
    {
        "item": "木料提供",
        "quantity": 1.0
    },
    {
        "item": "供热通风与空气调节",
        "quantity": 1.0
    },
    {
        "item": "机电设计成员",
        "quantity": 1.0
    },
    {
        "item": "钢铁工艺",
        "quantity": 1.0
    },
    {
        "item": "Baaq团队",
        "quantity": 1.0
    },
    {
        "item": "Taaa团队",
        "quantity": 1.0
    },
    {
        "item": "设计与结构",
        "quantity": 1.0
    },
    {
        "item": "可视化效果",
        "quantity": 1.0
    },
    {
        "item": "Fluids",
        "quantity": 1.0
    },
    {
        "item": "消防和声学顾问",
        "quantity": 1.0
    },
    {
        "item": "灯光设计师（宗教中心）",
        "quantity": 1.0
    },
    {
        "item": "建筑师 /总体规划",
        "quantity": 1.0
    },
    {
        "item": "建筑项目经理",
        "quantity": 1.0
    },
    {
        "item": "主咨询师",
        "quantity": 1.0
    },
    {
        "item": "国际所获奖项",
        "quantity": 1.0
    },
    {
        "item": "集团执行首席建筑师",
        "quantity": 1.0
    },
    {
        "item": "医疗和安保协调",
        "quantity": 1.0
    },
    {
        "item": "建设控制",
        "quantity": 1.0
    },
    {
        "item": "设备与电力顾问",
        "quantity": 1.0
    },
    {
        "item": "标签",
        "quantity": 1.0
    },
    {
        "item": "Graphic Designers",
        "quantity": 1.0
    },
    {
        "item": "食品服务顾问",
        "quantity": 1.0
    },
    {
        "item": "听觉礼堂",
        "quantity": 1.0
    },
    {
        "item": "联系建筑师",
        "quantity": 1.0
    },
    {
        "item": "机械/给排水工程师",
        "quantity": 1.0
    },
    {
        "item": "CDM咨询",
        "quantity": 1.0
    },
    {
        "item": "标志及路牌",
        "quantity": 1.0
    },
    {
        "item": "结构及土木工程",
        "quantity": 1.0
    },
    {
        "item": "纪录整理",
        "quantity": 1.0
    },
    {
        "item": "建筑师&设计师",
        "quantity": 1.0
    },
    {
        "item": "工料估算师",
        "quantity": 1.0
    },
    {
        "item": "Senior Associate - Graphic Design",
        "quantity": 1.0
    },
    {
        "item": "建筑勘测员",
        "quantity": 1.0
    },
    {
        "item": "外遮阳卷帘设计",
        "quantity": 1.0
    },
    {
        "item": "窗户设计",
        "quantity": 1.0
    },
    {
        "item": "未建设区域面积",
        "quantity": 1.0
    },
    {
        "item": "市政设计",
        "quantity": 1.0
    },
    {
        "item": "特别工程顾问",
        "quantity": 1.0
    },
    {
        "item": "工程主管",
        "quantity": 1.0
    },
    {
        "item": "水景观设计",
        "quantity": 1.0
    },
    {
        "item": "Mep/Fp/E",
        "quantity": 1.0
    },
    {
        "item": "功放顾问",
        "quantity": 1.0
    },
    {
        "item": "农业顾问",
        "quantity": 1.0
    },
    {
        "item": "Author Architects",
        "quantity": 1.0
    },
    {
        "item": "礼拜建议",
        "quantity": 1.0
    },
    {
        "item": "责任总监",
        "quantity": 1.0
    },
    {
        "item": "家具，配件和厨房成本",
        "quantity": 1.0
    },
    {
        "item": "可持续发展工程",
        "quantity": 1.0
    },
    {
        "item": "施工成本核算",
        "quantity": 1.0
    },
    {
        "item": "施工质量监测",
        "quantity": 1.0
    },
    {
        "item": "体量 1 ",
        "quantity": 1.0
    },
    {
        "item": "建筑与施工",
        "quantity": 1.0
    },
    {
        "item": "风洞实验",
        "quantity": 1.0
    },
    {
        "item": "安全工程师",
        "quantity": 1.0
    },
    {
        "item": "3D视觉",
        "quantity": 1.0
    },
    {
        "item": "入口",
        "quantity": 1.0
    },
    {
        "item": "设备/电气",
        "quantity": 1.0
    },
    {
        "item": "项目联盟",
        "quantity": 1.0
    },
    {
        "item": "音频视觉",
        "quantity": 1.0
    },
    {
        "item": "地窖和市场区面积",
        "quantity": 1.0
    },
    {
        "item": "瞭望台面积",
        "quantity": 1.0
    },
    {
        "item": "Fabrication",
        "quantity": 1.0
    },
    {
        "item": "承租人",
        "quantity": 1.0
    },
    {
        "item": "地面设计",
        "quantity": 1.0
    },
    {
        "item": "委员会",
        "quantity": 1.0
    },
    {
        "item": "承包",
        "quantity": 1.0
    },
    {
        "item": "SFMOMA咖啡吧景观窗设计",
        "quantity": 1.0
    },
    {
        "item": "电力网设计",
        "quantity": 1.0
    },
    {
        "item": "室内设计主管",
        "quantity": 1.0
    },
    {
        "item": "博物馆商店设计",
        "quantity": 1.0
    },
    {
        "item": "灯光、音响、AV及立面工程师",
        "quantity": 1.0
    },
    {
        "item": "立面设计助理",
        "quantity": 1.0
    },
    {
        "item": "植被建设公司, 特殊项目负责",
        "quantity": 1.0
    },
    {
        "item": "EHDD团队",
        "quantity": 1.0
    },
    {
        "item": "照明 / 安全",
        "quantity": 1.0
    },
    {
        "item": "Equipo de Trabajo",
        "quantity": 1.0
    },
    {
        "item": "协调 ",
        "quantity": 1.0
    },
    {
        "item": "建筑项目设计",
        "quantity": 1.0
    },
    {
        "item": "剧院系统",
        "quantity": 1.0
    },
    {
        "item": "设计主团队",
        "quantity": 1.0
    },
    {
        "item": "SIO室内设计",
        "quantity": 1.0
    },
    {
        "item": "Architect SAFA,合伙人",
        "quantity": 1.0
    },
    {
        "item": "构件数量",
        "quantity": 1.0
    },
    {
        "item": "科学研究",
        "quantity": 1.0
    },
    {
        "item": "行政",
        "quantity": 1.0
    },
    {
        "item": "HEQ 顾问",
        "quantity": 1.0
    },
    {
        "item": "高级领导",
        "quantity": 1.0
    },
    {
        "item": "净水设计",
        "quantity": 1.0
    },
    {
        "item": "合资董事",
        "quantity": 1.0
    },
    {
        "item": "遗产专家",
        "quantity": 1.0
    },
    {
        "item": "Allies and Morrison 团队",
        "quantity": 1.0
    },
    {
        "item": "Allies and Morrison 负责人助理",
        "quantity": 1.0
    },
    {
        "item": "OMA 项目经理",
        "quantity": 1.0
    },
    {
        "item": "OMA 项目负责人",
        "quantity": 1.0
    },
    {
        "item": "项目设计建造",
        "quantity": 1.0
    },
    {
        "item": "效果设计师",
        "quantity": 1.0
    },
    {
        "item": "产品标准",
        "quantity": 1.0
    },
    {
        "item": "搭档",
        "quantity": 1.0
    },
    {
        "item": "承办人",
        "quantity": 1.0
    },
    {
        "item": "总建设公司",
        "quantity": 1.0
    },
    {
        "item": "环境设计与绿色建筑委员会审阅",
        "quantity": 1.0
    },
    {
        "item": "标识系统承包商",
        "quantity": 1.0
    },
    {
        "item": "软景观承包商",
        "quantity": 1.0
    },
    {
        "item": "历史学家及市政指导",
        "quantity": 1.0
    },
    {
        "item": "市政设施设计",
        "quantity": 1.0
    },
    {
        "item": "团队指导",
        "quantity": 1.0
    },
    {
        "item": "DDA 顾问",
        "quantity": 1.0
    },
    {
        "item": "Local Architect ",
        "quantity": 1.0
    },
    {
        "item": "In Situ 酒店设计",
        "quantity": 1.0
    },
    {
        "item": "新建建筑面积",
        "quantity": 1.0
    },
    {
        "item": "导向标识系统设计，室内设计，模型设计",
        "quantity": 1.0
    },
    {
        "item": "Waterliniecentrum新展亭设计",
        "quantity": 1.0
    },
    {
        "item": "停车，道路， Castellum Fectio",
        "quantity": 1.0
    },
    {
        "item": "规划与景观合作, Begroeiing, Bestrating, Verlichting, Meubilair, Natuurbeheer",
        "quantity": 1.0
    },
    {
        "item": "建造价值",
        "quantity": 1.0
    },
    {
        "item": "基础工作",
        "quantity": 1.0
    },
    {
        "item": "Vastu顾问",
        "quantity": 1.0
    },
    {
        "item": "执行机构",
        "quantity": 1.0
    },
    {
        "item": "设计领队",
        "quantity": 1.0
    },
    {
        "item": "通风规划",
        "quantity": 1.0
    },
    {
        "item": "建设企业",
        "quantity": 1.0
    },
    {
        "item": "设备/电气工程师",
        "quantity": 1.0
    },
    {
        "item": "Construction system",
        "quantity": 1.0
    },
    {
        "item": "国际关系",
        "quantity": 1.0
    },
    {
        "item": "特许权所有人",
        "quantity": 1.0
    },
    {
        "item": "健康安全",
        "quantity": 1.0
    },
    {
        "item": "调度，监督和协调",
        "quantity": 1.0
    },
    {
        "item": "风力工程顾问",
        "quantity": 1.0
    },
    {
        "item": "主控制系统",
        "quantity": 1.0
    },
    {
        "item": "户外设计",
        "quantity": 1.0
    },
    {
        "item": "流体学",
        "quantity": 1.0
    },
    {
        "item": "数量",
        "quantity": 1.0
    },
    {
        "item": "静力学设计师",
        "quantity": 1.0
    },
    {
        "item": "主要机械/电力/管道工程",
        "quantity": 1.0
    },
    {
        "item": "现状",
        "quantity": 1.0
    },
    {
        "item": "构造顾问",
        "quantity": 1.0
    },
    {
        "item": "工程师和特殊顾问",
        "quantity": 1.0
    },
    {
        "item": "可持续性发展认证",
        "quantity": 1.0
    },
    {
        "item": "“代芬特尔框架”设计",
        "quantity": 1.0
    },
    {
        "item": "室内设计  分离装饰",
        "quantity": 1.0
    },
    {
        "item": "室内设计  固定装饰",
        "quantity": 1.0
    },
    {
        "item": "BCA 双边合规协议",
        "quantity": 1.0
    },
    {
        "item": "工程和船舶建筑公司",
        "quantity": 1.0
    },
    {
        "item": "总施工",
        "quantity": 1.0
    },
    {
        "item": "规格标准",
        "quantity": 1.0
    },
    {
        "item": "环保方法",
        "quantity": 1.0
    },
    {
        "item": "行政美学委托",
        "quantity": 1.0
    },
    {
        "item": "竹制作",
        "quantity": 1.0
    },
    {
        "item": "通行卡系统",
        "quantity": 1.0
    },
    {
        "item": "土建装饰工程",
        "quantity": 1.0
    },
    {
        "item": "集合石膏",
        "quantity": 1.0
    },
    {
        "item": "总土建承包商",
        "quantity": 1.0
    },
    {
        "item": "建筑控制批准检查员",
        "quantity": 1.0
    },
    {
        "item": "电力与管道",
        "quantity": 1.0
    },
    {
        "item": "水上运动设计顾问",
        "quantity": 1.0
    },
    {
        "item": "成本估计",
        "quantity": 1.0
    },
    {
        "item": "机电管道顾问",
        "quantity": 1.0
    },
    {
        "item": "体育建筑设计师",
        "quantity": 1.0
    },
    {
        "item": "街景设计",
        "quantity": 1.0
    },
    {
        "item": "外观制造",
        "quantity": 1.0
    },
    {
        "item": "铝材技术",
        "quantity": 1.0
    },
    {
        "item": "Leed认证",
        "quantity": 1.0
    },
    {
        "item": "特殊工艺",
        "quantity": 1.0
    },
    {
        "item": "石头景观",
        "quantity": 1.0
    },
    {
        "item": "结构和机电管道工程",
        "quantity": 1.0
    },
    {
        "item": "建筑施工图设计",
        "quantity": 1.0
    },
    {
        "item": "监督人",
        "quantity": 1.0
    },
    {
        "item": "铁器",
        "quantity": 1.0
    },
    {
        "item": "学院",
        "quantity": 1.0
    },
    {
        "item": "Maymester 学生",
        "quantity": 1.0
    },
    {
        "item": "合作者建筑师",
        "quantity": 1.0
    },
    {
        "item": "测绘员",
        "quantity": 1.0
    },
    {
        "item": "景观设计总监",
        "quantity": 1.0
    },
    {
        "item": "安全、建规咨询",
        "quantity": 1.0
    },
    {
        "item": "建筑师 / BIM模型",
        "quantity": 1.0
    },
    {
        "item": "早期基础设施",
        "quantity": 1.0
    },
    {
        "item": "块项目",
        "quantity": 1.0
    },
    {
        "item": "视觉体验",
        "quantity": 1.0
    },
    {
        "item": "经济控制办公室",
        "quantity": 1.0
    },
    {
        "item": "合同授权",
        "quantity": 1.0
    },
    {
        "item": "Ingenhoven Architects建筑师事务所",
        "quantity": 1.0
    },
    {
        "item": "大楼业主",
        "quantity": 1.0
    },
    {
        "item": "3D模型制作",
        "quantity": 1.0
    },
    {
        "item": "社区督导委员会",
        "quantity": 1.0
    },
    {
        "item": "项目管理和实施",
        "quantity": 1.0
    },
    {
        "item": "市政、交通、景观工程",
        "quantity": 1.0
    },
    {
        "item": "色彩设计",
        "quantity": 1.0
    },
    {
        "item": "球队",
        "quantity": 1.0
    },
    {
        "item": "场地安全系统",
        "quantity": 1.0
    },
    {
        "item": "景观计划",
        "quantity": 1.0
    },
    {
        "item": "工料测量及场地测量",
        "quantity": 1.0
    },
    {
        "item": "Associate in Charge",
        "quantity": 1.0
    },
    {
        "item": "安防工程师",
        "quantity": 1.0
    },
    {
        "item": "结构和暖通工程师",
        "quantity": 1.0
    },
    {
        "item": "商铺总监",
        "quantity": 1.0
    },
    {
        "item": "工程管理咨询",
        "quantity": 1.0
    },
    {
        "item": "自动化设计",
        "quantity": 1.0
    },
    {
        "item": "安防系统设计",
        "quantity": 1.0
    },
    {
        "item": "室内设计、颜色和装修",
        "quantity": 1.0
    },
    {
        "item": "土地研发",
        "quantity": 1.0
    },
    {
        "item": "砌砖",
        "quantity": 1.0
    },
    {
        "item": "结构，MEP工程师",
        "quantity": 1.0
    },
    {
        "item": "概算",
        "quantity": 1.0
    },
    {
        "item": "使用权",
        "quantity": 1.0
    },
    {
        "item": "顾问 2",
        "quantity": 1.0
    },
    {
        "item": "顾问 1",
        "quantity": 1.0
    },
    {
        "item": "Ennead管理搭档",
        "quantity": 1.0
    },
    {
        "item": "业主项目团队",
        "quantity": 1.0
    },
    {
        "item": "Ennead设计搭档",
        "quantity": 1.0
    },
    {
        "item": "执行景观建筑师",
        "quantity": 1.0
    },
    {
        "item": "客户与建造",
        "quantity": 1.0
    },
    {
        "item": "建筑开发商",
        "quantity": 1.0
    },
    {
        "item": "延伸材料",
        "quantity": 1.0
    },
    {
        "item": "空间音响效果",
        "quantity": 1.0
    },
    {
        "item": "材料供应商",
        "quantity": 1.0
    },
    {
        "item": "建设造价",
        "quantity": 1.0
    },
    {
        "item": "房屋测量",
        "quantity": 1.0
    },
    {
        "item": "吕贝克项目团队",
        "quantity": 1.0
    },
    {
        "item": "地面区域",
        "quantity": 1.0
    },
    {
        "item": "其他设施",
        "quantity": 1.0
    },
    {
        "item": "供暖、通风、空调",
        "quantity": 1.0
    },
    {
        "item": "景观与排水",
        "quantity": 1.0
    },
    {
        "item": "土工程师",
        "quantity": 1.0
    },
    {
        "item": "专用门设计",
        "quantity": 1.0
    },
    {
        "item": "照片版权",
        "quantity": 1.0
    },
    {
        "item": "总建设花费",
        "quantity": 1.0
    },
    {
        "item": "地下总面积",
        "quantity": 1.0
    },
    {
        "item": "项目许可证",
        "quantity": 1.0
    },
    {
        "item": "钢结构建设",
        "quantity": 1.0
    },
    {
        "item": "防火&人防",
        "quantity": 1.0
    },
    {
        "item": "结构、土建、机械工程师",
        "quantity": 1.0
    },
    {
        "item": "登记建筑师",
        "quantity": 1.0
    },
    {
        "item": "设计方案",
        "quantity": 1.0
    },
    {
        "item": "景观项目团队",
        "quantity": 1.0
    },
    {
        "item": "执行理事, CIC",
        "quantity": 1.0
    },
    {
        "item": "重建建筑师",
        "quantity": 1.0
    },
    {
        "item": "项目副主管",
        "quantity": 1.0
    },
    {
        "item": "原主持建筑师",
        "quantity": 1.0
    },
    {
        "item": "结构与设备",
        "quantity": 1.0
    },
    {
        "item": "锌板供应商",
        "quantity": 1.0
    },
    {
        "item": "木工及家具建造",
        "quantity": 1.0
    },
    {
        "item": "管理和协调",
        "quantity": 1.0
    },
    {
        "item": "屋顶甲板",
        "quantity": 1.0
    },
    {
        "item": "设计师 ",
        "quantity": 1.0
    },
    {
        "item": "土地工程",
        "quantity": 1.0
    },
    {
        "item": "项目功能",
        "quantity": 1.0
    },
    {
        "item": "特约作者",
        "quantity": 1.0
    },
    {
        "item": "Architectural reconstruction",
        "quantity": 1.0
    },
    {
        "item": "生产及物料控制",
        "quantity": 1.0
    },
    {
        "item": "副协调",
        "quantity": 1.0
    },
    {
        "item": "建筑控制办公室",
        "quantity": 1.0
    },
    {
        "item": "木材建造",
        "quantity": 1.0
    },
    {
        "item": "Exhibition Designers",
        "quantity": 1.0
    },
    {
        "item": "Bet Tce",
        "quantity": 1.0
    },
    {
        "item": "平面图，绘图，剖面图",
        "quantity": 1.0
    },
    {
        "item": "餐厅咖啡",
        "quantity": 1.0
    },
    {
        "item": "总承包商   室内装饰",
        "quantity": 1.0
    },
    {
        "item": "总承包商   核心和外壳",
        "quantity": 1.0
    },
    {
        "item": "评估机构",
        "quantity": 1.0
    },
    {
        "item": "产品规格",
        "quantity": 1.0
    },
    {
        "item": "水管安装",
        "quantity": 1.0
    },
    {
        "item": "土木工程师/土力工程师",
        "quantity": 1.0
    },
    {
        "item": "助理建筑师   室内设计",
        "quantity": 1.0
    },
    {
        "item": "助理建筑师   核心和外壳设计",
        "quantity": 1.0
    },
    {
        "item": "总建设成本",
        "quantity": 1.0
    },
    {
        "item": "结构工作",
        "quantity": 1.0
    },
    {
        "item": "HVAC/ 管道 ",
        "quantity": 1.0
    },
    {
        "item": "预制结构",
        "quantity": 1.0
    },
    {
        "item": "承包总监",
        "quantity": 1.0
    },
    {
        "item": "执行团队",
        "quantity": 1.0
    },
    {
        "item": "土地所有者",
        "quantity": 1.0
    },
    {
        "item": "建设助理",
        "quantity": 1.0
    },
    {
        "item": "客户和业主",
        "quantity": 1.0
    },
    {
        "item": "本地结构工程师",
        "quantity": 1.0
    },
    {
        "item": "建筑实习生",
        "quantity": 1.0
    },
    {
        "item": "本地咨询工程师",
        "quantity": 1.0
    },
    {
        "item": "定位及导航系统",
        "quantity": 1.0
    },
    {
        "item": "专业规划",
        "quantity": 1.0
    },
    {
        "item": "总建设承包商",
        "quantity": 1.0
    },
    {
        "item": "结构&机械设计",
        "quantity": 1.0
    },
    {
        "item": "主导设计师",
        "quantity": 1.0
    },
    {
        "item": "标识设计师",
        "quantity": 1.0
    },
    {
        "item": "钢材用量",
        "quantity": 1.0
    },
    {
        "item": "可达性",
        "quantity": 1.0
    },
    {
        "item": "混凝土基础",
        "quantity": 1.0
    },
    {
        "item": "建筑业主",
        "quantity": 1.0
    },
    {
        "item": "总设计师和供应商",
        "quantity": 1.0
    },
    {
        "item": "BET结构工程师",
        "quantity": 1.0
    },
    {
        "item": "前端技术",
        "quantity": 1.0
    },
    {
        "item": "施工   木材",
        "quantity": 1.0
    },
    {
        "item": "MEP 工程顾问",
        "quantity": 1.0
    },
    {
        "item": "建成区面积",
        "quantity": 1.0
    },
    {
        "item": "立面建筑师",
        "quantity": 1.0
    },
    {
        "item": "构造研究",
        "quantity": 1.0
    },
    {
        "item": "装修承包商",
        "quantity": 1.0
    },
    {
        "item": "建筑设备工程师",
        "quantity": 1.0
    },
    {
        "item": "执行ACA与协调",
        "quantity": 1.0
    },
    {
        "item": "合作建筑师 ",
        "quantity": 1.0
    },
    {
        "item": "搬迁经理",
        "quantity": 1.0
    },
    {
        "item": "本地土木工程师",
        "quantity": 1.0
    },
    {
        "item": "视频制作",
        "quantity": 1.0
    },
    {
        "item": "护栏和数控加工工作",
        "quantity": 1.0
    },
    {
        "item": "花园面积",
        "quantity": 1.0
    },
    {
        "item": "土建及室内施工",
        "quantity": 1.0
    },
    {
        "item": "Land Area",
        "quantity": 1.0
    },
    {
        "item": "团队（室内设计）",
        "quantity": 1.0
    },
    {
        "item": "照明布置",
        "quantity": 1.0
    },
    {
        "item": "土地勘测",
        "quantity": 1.0
    },
    {
        "item": " Landscape Architect",
        "quantity": 1.0
    },
    {
        "item": "商业空间面积",
        "quantity": 1.0
    },
    {
        "item": "车站面积",
        "quantity": 1.0
    },
    {
        "item": "木结构建设",
        "quantity": 1.0
    },
    {
        "item": "底层面积",
        "quantity": 1.0
    },
    {
        "item": "结构工程、机械服务、建筑物理",
        "quantity": 1.0
    },
    {
        "item": "透视",
        "quantity": 1.0
    },
    {
        "item": "建造阶段",
        "quantity": 1.0
    },
    {
        "item": "法国纪念碑建筑师",
        "quantity": 1.0
    },
    {
        "item": "木材用量",
        "quantity": 1.0
    },
    {
        "item": "外观装饰",
        "quantity": 1.0
    },
    {
        "item": "社会总监",
        "quantity": 1.0
    },
    {
        "item": "景观和环境设计",
        "quantity": 1.0
    },
    {
        "item": "技术设计顾问",
        "quantity": 1.0
    },
    {
        "item": " 建筑师",
        "quantity": 1.0
    },
    {
        "item": "EDU 工作团队",
        "quantity": 1.0
    },
    {
        "item": "文本修订",
        "quantity": 1.0
    },
    {
        "item": "砖石砌筑建筑工程",
        "quantity": 1.0
    },
    {
        "item": "安装设计",
        "quantity": 1.0
    },
    {
        "item": "混凝土表皮",
        "quantity": 1.0
    },
    {
        "item": "大理石制品",
        "quantity": 1.0
    },
    {
        "item": "Consultant acoustics",
        "quantity": 1.0
    },
    {
        "item": "SPS协调员",
        "quantity": 1.0
    },
    {
        "item": "Lighting design",
        "quantity": 1.0
    },
    {
        "item": "Schematic design",
        "quantity": 1.0
    },
    {
        "item": "城北大学团队",
        "quantity": 1.0
    },
    {
        "item": "结构和电气工程",
        "quantity": 1.0
    },
    {
        "item": "结构化布线",
        "quantity": 1.0
    },
    {
        "item": "道路和延伸工作",
        "quantity": 1.0
    },
    {
        "item": "水体和绿色建筑",
        "quantity": 1.0
    },
    {
        "item": "嵌入技术",
        "quantity": 1.0
    },
    {
        "item": "钢框架",
        "quantity": 1.0
    },
    {
        "item": "机械电气设计",
        "quantity": 1.0
    },
    {
        "item": "门禁咨询",
        "quantity": 1.0
    },
    {
        "item": "主要学院",
        "quantity": 1.0
    },
    {
        "item": "艺术比例",
        "quantity": 1.0
    },
    {
        "item": "AV设计",
        "quantity": 1.0
    },
    {
        "item": "平面设计/视觉控制系统",
        "quantity": 1.0
    },
    {
        "item": "EI/CA布设",
        "quantity": 1.0
    },
    {
        "item": "暖通空调与洁具布设",
        "quantity": 1.0
    },
    {
        "item": "隔断墙监测",
        "quantity": 1.0
    },
    {
        "item": "资格认证机构",
        "quantity": 1.0
    },
    {
        "item": "项目/ 设计总监",
        "quantity": 1.0
    },
    {
        "item": "水利发电工程",
        "quantity": 1.0
    },
    {
        "item": "博物馆技术",
        "quantity": 1.0
    },
    {
        "item": "CAD软件",
        "quantity": 1.0
    },
    {
        "item": "建筑审核",
        "quantity": 1.0
    },
    {
        "item": "机电与设备工程师",
        "quantity": 1.0
    },
    {
        "item": "室内设计师 ",
        "quantity": 1.0
    },
    {
        "item": "CDM 顾问",
        "quantity": 1.0
    },
    {
        "item": "计划主管",
        "quantity": 1.0
    },
    {
        "item": "结构工程师、消防和交通工程",
        "quantity": 1.0
    },
    {
        "item": "企业标识",
        "quantity": 1.0
    },
    {
        "item": "工业工程师，通风设备",
        "quantity": 1.0
    },
    {
        "item": "实物模型",
        "quantity": 1.0
    },
    {
        "item": "Surfaces « brutes » / « nettes » ",
        "quantity": 1.0
    },
    {
        "item": "租赁管理",
        "quantity": 1.0
    },
    {
        "item": "透视法",
        "quantity": 1.0
    },
    {
        "item": "Peripheriques 团队",
        "quantity": 1.0
    },
    {
        "item": "MEP 顾问",
        "quantity": 1.0
    },
    {
        "item": "人行桥设计团队",
        "quantity": 1.0
    },
    {
        "item": "造价规划",
        "quantity": 1.0
    },
    {
        "item": "净表面面积",
        "quantity": 1.0
    },
    {
        "item": "建造方案解决",
        "quantity": 1.0
    },
    {
        "item": "Allies and Morrison执行董事",
        "quantity": 1.0
    },
    {
        "item": "物流设计",
        "quantity": 1.0
    },
    {
        "item": "地形工程",
        "quantity": 1.0
    },
    {
        "item": "药品工程",
        "quantity": 1.0
    },
    {
        "item": "钢结构建造",
        "quantity": 1.0
    },
    {
        "item": "建筑商和施工经理",
        "quantity": 1.0
    },
    {
        "item": "停车场面积",
        "quantity": 1.0
    },
    {
        "item": "Sociology",
        "quantity": 1.0
    },
    {
        "item": "预算 Material PEM",
        "quantity": 1.0
    },
    {
        "item": "指导安装执行阶段",
        "quantity": 1.0
    },
    {
        "item": "Collaborating Designer",
        "quantity": 1.0
    },
    {
        "item": "工程师设计阶段(结构和建筑服务)",
        "quantity": 1.0
    },
    {
        "item": "主承包方",
        "quantity": 1.0
    },
    {
        "item": "艺术项目指南",
        "quantity": 1.0
    },
    {
        "item": "电梯里的城市地图",
        "quantity": 1.0
    },
    {
        "item": "都市风光宣传画",
        "quantity": 1.0
    },
    {
        "item": "主要承包商、项目经理、资产管理",
        "quantity": 1.0
    },
    {
        "item": "大楼承租方",
        "quantity": 1.0
    },
    {
        "item": "设备花费",
        "quantity": 1.0
    },
    {
        "item": "Artist",
        "quantity": 1.0
    },
    {
        "item": "知名雕塑人民大厅",
        "quantity": 1.0
    },
    {
        "item": "人权海报壁画",
        "quantity": 1.0
    },
    {
        "item": "展览制造商",
        "quantity": 1.0
    },
    {
        "item": "媒体内容",
        "quantity": 1.0
    },
    {
        "item": "高级技术协调员",
        "quantity": 1.0
    },
    {
        "item": "高级建筑设计师",
        "quantity": 1.0
    },
    {
        "item": "房间数量",
        "quantity": 1.0
    },
    {
        "item": "D&W 承包商",
        "quantity": 1.0
    },
    {
        "item": "卫生工程师",
        "quantity": 1.0
    },
    {
        "item": "水利系统",
        "quantity": 1.0
    },
    {
        "item": "项目规划",
        "quantity": 1.0
    },
    {
        "item": "Special Paint",
        "quantity": 1.0
    },
    {
        "item": "实施阶段当地项目领导",
        "quantity": 1.0
    },
    {
        "item": "比利时建筑师",
        "quantity": 1.0
    },
    {
        "item": "UNStudio 设计团队",
        "quantity": 1.0
    },
    {
        "item": "密码与安检顾问",
        "quantity": 1.0
    },
    {
        "item": "信息顾问",
        "quantity": 1.0
    },
    {
        "item": "衣架",
        "quantity": 1.0
    },
    {
        "item": "KSS建筑事务所项目团队",
        "quantity": 1.0
    },
    {
        "item": "木地板",
        "quantity": 1.0
    },
    {
        "item": "主材",
        "quantity": 1.0
    },
    {
        "item": "土木承包人",
        "quantity": 1.0
    },
    {
        "item": "Henning Larsen设计事务所团队",
        "quantity": 1.0
    },
    {
        "item": "陶艺",
        "quantity": 1.0
    },
    {
        "item": "木制家具",
        "quantity": 1.0
    },
    {
        "item": "陈设设计",
        "quantity": 1.0
    },
    {
        "item": "楼层系统",
        "quantity": 1.0
    },
    {
        "item": "土建和建筑",
        "quantity": 1.0
    },
    {
        "item": "Energic 认证",
        "quantity": 1.0
    },
    {
        "item": "制图并执行",
        "quantity": 1.0
    },
    {
        "item": "副承包商及供应商",
        "quantity": 1.0
    },
    {
        "item": "生命安全系统",
        "quantity": 1.0
    },
    {
        "item": "幕布",
        "quantity": 1.0
    },
    {
        "item": "电力/给排水",
        "quantity": 1.0
    },
    {
        "item": "开发与工程",
        "quantity": 1.0
    },
    {
        "item": "项目委托",
        "quantity": 1.0
    },
    {
        "item": "场地平面图",
        "quantity": 1.0
    },
    {
        "item": "Helen & Hard 团队",
        "quantity": 1.0
    },
    {
        "item": "Aquascaping and Aquarium Lighting Concept",
        "quantity": 1.0
    },
    {
        "item": "建筑&室内团队",
        "quantity": 1.0
    },
    {
        "item": "屋顶花园",
        "quantity": 1.0
    },
    {
        "item": "建筑师与木匠",
        "quantity": 1.0
    },
    {
        "item": "Natuurpodium合作标志设计",
        "quantity": 1.0
    },
    {
        "item": "Stayokay室内设计",
        "quantity": 1.0
    },
    {
        "item": "Natuurpodium室内设计",
        "quantity": 1.0
    },
    {
        "item": "家具制造商",
        "quantity": 1.0
    },
    {
        "item": "基地与花园",
        "quantity": 1.0
    },
    {
        "item": "建筑外围建设",
        "quantity": 1.0
    },
    {
        "item": "房间清理",
        "quantity": 1.0
    },
    {
        "item": "声学/AV/安保",
        "quantity": 1.0
    },
    {
        "item": "建筑检测",
        "quantity": 1.0
    },
    {
        "item": "实验室布局",
        "quantity": 1.0
    },
    {
        "item": "封面",
        "quantity": 1.0
    },
    {
        "item": "建设行政",
        "quantity": 1.0
    },
    {
        "item": "电气专业",
        "quantity": 1.0
    },
    {
        "item": "工地负责人",
        "quantity": 1.0
    },
    {
        "item": "幕墙工程师",
        "quantity": 1.0
    },
    {
        "item": "安装管理",
        "quantity": 1.0
    },
    {
        "item": "主持经理",
        "quantity": 1.0
    },
    {
        "item": "合作 LDI",
        "quantity": 1.0
    },
    {
        "item": "Estudio Arquitectura S A  de C V  团队",
        "quantity": 1.0
    },
    {
        "item": "Consulting structural engineers",
        "quantity": 1.0
    },
    {
        "item": "玻璃厂",
        "quantity": 1.0
    },
    {
        "item": "生产单元",
        "quantity": 1.0
    },
    {
        "item": "操作规程负责人",
        "quantity": 1.0
    },
    {
        "item": "石膏",
        "quantity": 1.0
    },
    {
        "item": "壁炉",
        "quantity": 1.0
    },
    {
        "item": "食品服务",
        "quantity": 1.0
    },
    {
        "item": "设计与技术支持",
        "quantity": 1.0
    },
    {
        "item": "催料员",
        "quantity": 1.0
    },
    {
        "item": "风管实验",
        "quantity": 1.0
    },
    {
        "item": "立面维护",
        "quantity": 1.0
    },
    {
        "item": "形态技术",
        "quantity": 1.0
    },
    {
        "item": "住宅室内设计",
        "quantity": 1.0
    },
    {
        "item": "住宅室内布局",
        "quantity": 1.0
    },
    {
        "item": "包围结构技术",
        "quantity": 1.0
    },
    {
        "item": "捐赠人",
        "quantity": 1.0
    },
    {
        "item": "设计软件",
        "quantity": 1.0
    },
    {
        "item": "设备电力工程",
        "quantity": 1.0
    },
    {
        "item": "管道和空调系统",
        "quantity": 1.0
    },
    {
        "item": "纺织品协调",
        "quantity": 1.0
    },
    {
        "item": "机械电气和管道咨询",
        "quantity": 1.0
    },
    {
        "item": "租赁顾问",
        "quantity": 1.0
    },
    {
        "item": "钢材制造",
        "quantity": 1.0
    },
    {
        "item": "总控承包商",
        "quantity": 1.0
    },
    {
        "item": "流体技术设计",
        "quantity": 1.0
    },
    {
        "item": "总表面面积",
        "quantity": 1.0
    },
    {
        "item": "结构技术设计",
        "quantity": 1.0
    },
    {
        "item": "竞赛评委",
        "quantity": 1.0
    },
    {
        "item": "Gen´08执行团队",
        "quantity": 1.0
    },
    {
        "item": "HQE 目标",
        "quantity": 1.0
    },
    {
        "item": "土木和管道工程",
        "quantity": 1.0
    },
    {
        "item": "结构工程方",
        "quantity": 1.0
    },
    {
        "item": "泥水匠监督",
        "quantity": 1.0
    },
    {
        "item": "模拟环境合作",
        "quantity": 1.0
    },
    {
        "item": "可持续设计顾问",
        "quantity": 1.0
    },
    {
        "item": "风声效果合作设计",
        "quantity": 1.0
    },
    {
        "item": "力学项目",
        "quantity": 1.0
    },
    {
        "item": "土墙结构合作实验  ",
        "quantity": 1.0
    },
    {
        "item": "节能管理",
        "quantity": 1.0
    },
    {
        "item": "室内外照明",
        "quantity": 1.0
    },
    {
        "item": "门窗",
        "quantity": 1.0
    },
    {
        "item": "结构/立面/电机工程",
        "quantity": 1.0
    },
    {
        "item": "施工   混凝土",
        "quantity": 1.0
    },
    {
        "item": "声学+声像顾问",
        "quantity": 1.0
    },
    {
        "item": "规划管理局",
        "quantity": 1.0
    },
    {
        "item": "电力维护",
        "quantity": 1.0
    },
    {
        "item": "室内座位",
        "quantity": 1.0
    },
    {
        "item": "木结构总工程师",
        "quantity": 1.0
    },
    {
        "item": "设备电力",
        "quantity": 1.0
    },
    {
        "item": "表现",
        "quantity": 1.0
    },
    {
        "item": "悬挂设计",
        "quantity": 1.0
    },
    {
        "item": "设计团队 (2015年竞赛)",
        "quantity": 1.0
    },
    {
        "item": "研发",
        "quantity": 1.0
    },
    {
        "item": "海运/交通运输工程",
        "quantity": 1.0
    },
    {
        "item": "金属加工",
        "quantity": 1.0
    },
    {
        "item": "通风设备",
        "quantity": 1.0
    },
    {
        "item": "采光设计",
        "quantity": 1.0
    },
    {
        "item": "室内景观设计",
        "quantity": 1.0
    },
    {
        "item": "儿童顾问",
        "quantity": 1.0
    },
    {
        "item": "品牌",
        "quantity": 1.0
    },
    {
        "item": "Job Inspection",
        "quantity": 1.0
    },
    {
        "item": "被动房顾问",
        "quantity": 1.0
    },
    {
        "item": "Party墙",
        "quantity": 1.0
    },
    {
        "item": "合同形式",
        "quantity": 1.0
    },
    {
        "item": "助理建筑师 ",
        "quantity": 1.0
    },
    {
        "item": "客户项目经理",
        "quantity": 1.0
    },
    {
        "item": "保护团队",
        "quantity": 1.0
    },
    {
        "item": "图纸、草图、模型",
        "quantity": 1.0
    },
    {
        "item": "装潢师",
        "quantity": 1.0
    },
    {
        "item": "视听影音",
        "quantity": 1.0
    },
    {
        "item": "本地合伙人",
        "quantity": 1.0
    },
    {
        "item": "音响系统",
        "quantity": 1.0
    },
    {
        "item": "外墙维护",
        "quantity": 1.0
    },
    {
        "item": "结构 / MEP/FP",
        "quantity": 1.0
    },
    {
        "item": "项目管理和监督",
        "quantity": 1.0
    },
    {
        "item": "Core and Shell team",
        "quantity": 1.0
    },
    {
        "item": "建筑设计总监 ",
        "quantity": 1.0
    },
    {
        "item": "开发承包商",
        "quantity": 1.0
    },
    {
        "item": "MIT",
        "quantity": 1.0
    },
    {
        "item": "电力/设备",
        "quantity": 1.0
    },
    {
        "item": "设计期",
        "quantity": 1.0
    },
    {
        "item": "HVAC设计",
        "quantity": 1.0
    },
    {
        "item": "计划说明",
        "quantity": 1.0
    },
    {
        "item": "外部建造",
        "quantity": 1.0
    },
    {
        "item": "外部细木工业",
        "quantity": 1.0
    },
    {
        "item": "广场雕塑",
        "quantity": 1.0
    },
    {
        "item": "项目总价值",
        "quantity": 1.0
    },
    {
        "item": "旋转楼梯",
        "quantity": 1.0
    },
    {
        "item": "AV",
        "quantity": 1.0
    },
    {
        "item": "建筑师与技术建造管理",
        "quantity": 1.0
    },
    {
        "item": "MEP 服务",
        "quantity": 1.0
    },
    {
        "item": "室内设计公司",
        "quantity": 1.0
    },
    {
        "item": "室内玻璃安装",
        "quantity": 1.0
    },
    {
        "item": "Paisagismo",
        "quantity": 1.0
    },
    {
        "item": "家具和固定装置",
        "quantity": 1.0
    },
    {
        "item": "BREEAM 环境评估",
        "quantity": 1.0
    },
    {
        "item": "经济学家 ",
        "quantity": 1.0
    },
    {
        "item": " 项目建筑师",
        "quantity": 1.0
    },
    {
        "item": "设计团队 ",
        "quantity": 1.0
    },
    {
        "item": "执行设计",
        "quantity": 1.0
    },
    {
        "item": "室内外的主要结构设计",
        "quantity": 1.0
    },
    {
        "item": "外观承包商",
        "quantity": 1.0
    },
    {
        "item": "楼梯",
        "quantity": 1.0
    },
    {
        "item": "计量师 ",
        "quantity": 1.0
    },
    {
        "item": "HVAC 工程设计",
        "quantity": 1.0
    },
    {
        "item": "岩土工程/结构工程/机电管道工程/外观工程",
        "quantity": 1.0
    },
    {
        "item": "三维",
        "quantity": 1.0
    },
    {
        "item": "重量",
        "quantity": 1.0
    },
    {
        "item": "农业工程师",
        "quantity": 1.0
    },
    {
        "item": "隔离",
        "quantity": 1.0
    },
    {
        "item": "HQE",
        "quantity": 1.0
    },
    {
        "item": "供水",
        "quantity": 1.0
    },
    {
        "item": "国际景观",
        "quantity": 1.0
    },
    {
        "item": "当地规划顾问",
        "quantity": 1.0
    },
    {
        "item": "当地能源分析顾问",
        "quantity": 1.0
    },
    {
        "item": "特别致谢",
        "quantity": 1.0
    },
    {
        "item": "人权斗争者雕塑",
        "quantity": 1.0
    },
    {
        "item": "当地噪音顾问",
        "quantity": 1.0
    },
    {
        "item": "艺术策展人",
        "quantity": 1.0
    },
    {
        "item": "当地文化建筑顾问",
        "quantity": 1.0
    },
    {
        "item": "当地土建顾问",
        "quantity": 1.0
    },
    {
        "item": "当地立面顾问",
        "quantity": 1.0
    },
    {
        "item": "当地电力顾问",
        "quantity": 1.0
    },
    {
        "item": "当地机械顾问",
        "quantity": 1.0
    },
    {
        "item": "当地结构顾问",
        "quantity": 1.0
    },
    {
        "item": "ZHA 竞赛团队",
        "quantity": 1.0
    },
    {
        "item": "ZHA 项目托段",
        "quantity": 1.0
    },
    {
        "item": "ZHA 项目经理",
        "quantity": 1.0
    },
    {
        "item": "ZHA 项目领导",
        "quantity": 1.0
    },
    {
        "item": "项目总造价",
        "quantity": 1.0
    },
    {
        "item": "设备、电力与ESP",
        "quantity": 1.0
    },
    {
        "item": "建筑装备工程师",
        "quantity": 1.0
    },
    {
        "item": "服务方",
        "quantity": 1.0
    },
    {
        "item": "合作建筑事务所",
        "quantity": 1.0
    },
    {
        "item": "结构/细部",
        "quantity": 1.0
    },
    {
        "item": "Sculptor ",
        "quantity": 1.0
    },
    {
        "item": "容积",
        "quantity": 1.0
    },
    {
        "item": "工期管理",
        "quantity": 1.0
    },
    {
        "item": "结构布局",
        "quantity": 1.0
    },
    {
        "item": "环境评估顾问",
        "quantity": 1.0
    },
    {
        "item": "质量保证体系",
        "quantity": 1.0
    },
    {
        "item": "防水处理",
        "quantity": 1.0
    },
    {
        "item": "大楼管理办公室",
        "quantity": 1.0
    },
    {
        "item": "管理与合作 ",
        "quantity": 1.0
    },
    {
        "item": "Publicity, ZCB",
        "quantity": 1.0
    },
    {
        "item": "气温",
        "quantity": 1.0
    },
    {
        "item": "合伙人/顾问",
        "quantity": 1.0
    },
    {
        "item": "展厅边建筑面积",
        "quantity": 1.0
    },
    {
        "item": "农学顾问",
        "quantity": 1.0
    },
    {
        "item": "项目经理/成本顾问",
        "quantity": 1.0
    },
    {
        "item": "结构暖通",
        "quantity": 1.0
    },
    {
        "item": "内容编辑",
        "quantity": 1.0
    },
    {
        "item": "施工团队 2",
        "quantity": 1.0
    },
    {
        "item": "施工团队 1",
        "quantity": 1.0
    },
    {
        "item": "引导设计",
        "quantity": 1.0
    },
    {
        "item": "舞台灯光设计",
        "quantity": 1.0
    },
    {
        "item": "视觉与听觉设计",
        "quantity": 1.0
    },
    {
        "item": "立面建设",
        "quantity": 1.0
    },
    {
        "item": "职工",
        "quantity": 1.0
    },
    {
        "item": "BIG 团队",
        "quantity": 1.0
    },
    {
        "item": "VIP休息室项目管理",
        "quantity": 1.0
    },
    {
        "item": "VIP休息室照明设计",
        "quantity": 1.0
    },
    {
        "item": "机场照明设计",
        "quantity": 1.0
    },
    {
        "item": "机场项目视觉传达",
        "quantity": 1.0
    },
    {
        "item": "标志和相关设计",
        "quantity": 1.0
    },
    {
        "item": "航行设计",
        "quantity": 1.0
    },
    {
        "item": "VIP休息室创作团队",
        "quantity": 1.0
    },
    {
        "item": "建设记录",
        "quantity": 1.0
    },
    {
        "item": "后期设计团队",
        "quantity": 1.0
    },
    {
        "item": "前期设计团队",
        "quantity": 1.0
    },
    {
        "item": "总供货商",
        "quantity": 1.0
    },
    {
        "item": "合作者Blaf",
        "quantity": 1.0
    },
    {
        "item": "剧院设计",
        "quantity": 1.0
    },
    {
        "item": "主要建材供应商",
        "quantity": 1.0
    },
    {
        "item": "赞助机构",
        "quantity": 1.0
    },
    {
        "item": "&E [机电工程师]",
        "quantity": 1.0
    },
    {
        "item": "C&S [土木与结构工程师]",
        "quantity": 1.0
    },
    {
        "item": "项目总监 / 电器",
        "quantity": 1.0
    },
    {
        "item": "环境保护工作室, 实验室和艺术设计",
        "quantity": 1.0
    },
    {
        "item": "结构和设施",
        "quantity": 1.0
    },
    {
        "item": "Projektleitung (Project Management)",
        "quantity": 1.0
    },
    {
        "item": "当地防火顾问",
        "quantity": 1.0
    },
    {
        "item": "家具与木工",
        "quantity": 1.0
    },
    {
        "item": "现场协调系统",
        "quantity": 1.0
    },
    {
        "item": "生态设计",
        "quantity": 1.0
    },
    {
        "item": "功能顾问",
        "quantity": 1.0
    },
    {
        "item": "翻译与文本编辑",
        "quantity": 1.0
    },
    {
        "item": "项目监测",
        "quantity": 1.0
    },
    {
        "item": "残疾通道设计顾问",
        "quantity": 1.0
    },
    {
        "item": "服务期数",
        "quantity": 1.0
    },
    {
        "item": "视频内容设计师",
        "quantity": 1.0
    },
    {
        "item": "服装设计/实现",
        "quantity": 1.0
    },
    {
        "item": "SFX 设计师",
        "quantity": 1.0
    },
    {
        "item": "表演/机械设计师",
        "quantity": 1.0
    },
    {
        "item": "节目总监/编排",
        "quantity": 1.0
    },
    {
        "item": "屏蔽和接地设计",
        "quantity": 1.0
    },
    {
        "item": "投影专家",
        "quantity": 1.0
    },
    {
        "item": "音效设计师",
        "quantity": 1.0
    },
    {
        "item": "建筑师总监",
        "quantity": 1.0
    },
    {
        "item": "布景设计师",
        "quantity": 1.0
    },
    {
        "item": "概念工程师",
        "quantity": 1.0
    },
    {
        "item": "室内 LDI",
        "quantity": 1.0
    },
    {
        "item": "投资出租公寓",
        "quantity": 1.0
    },
    {
        "item": "采暖通风",
        "quantity": 1.0
    },
    {
        "item": "重木建造",
        "quantity": 1.0
    },
    {
        "item": "玻璃画廊面积",
        "quantity": 1.0
    },
    {
        "item": "室内/专业钢工与地板承包商",
        "quantity": 1.0
    },
    {
        "item": "建筑工程管理 ",
        "quantity": 1.0
    },
    {
        "item": "林业",
        "quantity": 1.0
    },
    {
        "item": "效果设计",
        "quantity": 1.0
    },
    {
        "item": "基础设计",
        "quantity": 1.0
    },
    {
        "item": "合同和采购形式",
        "quantity": 1.0
    },
    {
        "item": "实施阶段设计人",
        "quantity": 1.0
    },
    {
        "item": "建筑和项目经理",
        "quantity": 1.0
    },
    {
        "item": "Building Control",
        "quantity": 1.0
    },
    {
        "item": "当地环境顾问",
        "quantity": 1.0
    },
    {
        "item": "外部装饰",
        "quantity": 1.0
    },
    {
        "item": "景观协助",
        "quantity": 1.0
    },
    {
        "item": "总协助",
        "quantity": 1.0
    },
    {
        "item": "残疾人服务顾问",
        "quantity": 1.0
    },
    {
        "item": "光伏系统",
        "quantity": 1.0
    },
    {
        "item": "建筑师及总监",
        "quantity": 1.0
    },
    {
        "item": "项目管理与监测",
        "quantity": 1.0
    },
    {
        "item": "电气工程哈斯",
        "quantity": 1.0
    },
    {
        "item": "产品",
        "quantity": 1.0
    },
    {
        "item": "风和日光模拟系统",
        "quantity": 1.0
    },
    {
        "item": "M&E 机电工程师",
        "quantity": 1.0
    },
    {
        "item": "C&S 土木与结构工程师",
        "quantity": 1.0
    },
    {
        "item": "描绘",
        "quantity": 1.0
    },
    {
        "item": "新面积（二层）",
        "quantity": 1.0
    },
    {
        "item": "项目经理/合同管理员",
        "quantity": 1.0
    },
    {
        "item": "建筑与工程",
        "quantity": 1.0
    },
    {
        "item": "塑料水果箱重量",
        "quantity": 1.0
    },
    {
        "item": "项目合作建造阶段",
        "quantity": 1.0
    },
    {
        "item": "Construction tender",
        "quantity": 1.0
    },
    {
        "item": "结构分析",
        "quantity": 1.0
    },
    {
        "item": "建筑可持续",
        "quantity": 1.0
    },
    {
        "item": "过程管理",
        "quantity": 1.0
    },
    {
        "item": "模型照片（竞赛）",
        "quantity": 1.0
    },
    {
        "item": "Architect of record",
        "quantity": 1.0
    },
    {
        "item": "可持续顾问（竞赛）",
        "quantity": 1.0
    },
    {
        "item": "舞台计划",
        "quantity": 1.0
    },
    {
        "item": "参与方案设计",
        "quantity": 1.0
    },
    {
        "item": "工程、结构、装置（竞赛）",
        "quantity": 1.0
    },
    {
        "item": "设计咨询",
        "quantity": 1.0
    },
    {
        "item": "项目建筑师（室内设计）",
        "quantity": 1.0
    },
    {
        "item": "主持合伙人（发展设计）",
        "quantity": 1.0
    },
    {
        "item": "项目建筑师（发展设计）",
        "quantity": 1.0
    },
    {
        "item": "主持合作者（发展设计）",
        "quantity": 1.0
    },
    {
        "item": "项目团队（预设计）",
        "quantity": 1.0
    },
    {
        "item": "面积: 奥林匹克皮划艇激流运动场",
        "quantity": 1.0
    },
    {
        "item": "主持合作者（预设计）",
        "quantity": 1.0
    },
    {
        "item": "项目团队（设计）",
        "quantity": 1.0
    },
    {
        "item": "概念设计成员",
        "quantity": 1.0
    },
    {
        "item": "项目领导（设计）",
        "quantity": 1.0
    },
    {
        "item": "主持合作者（设计）",
        "quantity": 1.0
    },
    {
        "item": "项目团队（建设）",
        "quantity": 1.0
    },
    {
        "item": "主持合伙人（建设）",
        "quantity": 1.0
    },
    {
        "item": "立面/长廊",
        "quantity": 1.0
    },
    {
        "item": "建筑用地",
        "quantity": 1.0
    },
    {
        "item": "屋顶景观设计",
        "quantity": 1.0
    },
    {
        "item": "环境图像",
        "quantity": 1.0
    },
    {
        "item": "防水顾问",
        "quantity": 1.0
    },
    {
        "item": "市政工程与LEED顾问",
        "quantity": 1.0
    },
    {
        "item": "日光与照明设计",
        "quantity": 1.0
    },
    {
        "item": "基础工程 ",
        "quantity": 1.0
    },
    {
        "item": "AWP 团队",
        "quantity": 1.0
    },
    {
        "item": "管道/通风/地板采暖",
        "quantity": 1.0
    },
    {
        "item": "施工文档 施工管理",
        "quantity": 1.0
    },
    {
        "item": "3D 渲染图制作",
        "quantity": 1.0
    },
    {
        "item": "项目团队（室内设计）",
        "quantity": 1.0
    },
    {
        "item": "采暖/通风",
        "quantity": 1.0
    },
    {
        "item": "立面图",
        "quantity": 1.0
    },
    {
        "item": "工作经历",
        "quantity": 1.0
    },
    {
        "item": "背景设计",
        "quantity": 1.0
    },
    {
        "item": "视觉艺术家",
        "quantity": 1.0
    },
    {
        "item": "建筑覆盖面积",
        "quantity": 1.0
    },
    {
        "item": "设计建设团队",
        "quantity": 1.0
    },
    {
        "item": "Scenographer ",
        "quantity": 1.0
    },
    {
        "item": "Educational Wall Illustration and Design",
        "quantity": 1.0
    },
    {
        "item": "外墙承包商",
        "quantity": 1.0
    },
    {
        "item": "市政与结构工程师",
        "quantity": 1.0
    },
    {
        "item": "其他合作机构 ",
        "quantity": 1.0
    },
    {
        "item": "建造设备",
        "quantity": 1.0
    },
    {
        "item": "主要品牌",
        "quantity": 1.0
    },
    {
        "item": "Time & Tender Management",
        "quantity": 1.0
    },
    {
        "item": "营销和销售",
        "quantity": 1.0
    },
    {
        "item": "Project & Construction Management",
        "quantity": 1.0
    },
    {
        "item": "项目名",
        "quantity": 1.0
    },
    {
        "item": "Local Submission Architect",
        "quantity": 1.0
    },
    {
        "item": "Detailed Design",
        "quantity": 1.0
    },
    {
        "item": "Aesthetic Supervision of Works",
        "quantity": 1.0
    },
    {
        "item": "Constr  Manager",
        "quantity": 1.0
    },
    {
        "item": "MEP/FP Engineer",
        "quantity": 1.0
    },
    {
        "item": "风力咨询",
        "quantity": 1.0
    },
    {
        "item": "围栏设计",
        "quantity": 1.0
    },
    {
        "item": "Exhibit Consultant",
        "quantity": 1.0
    },
    {
        "item": "Director of Museum Services",
        "quantity": 1.0
    },
    {
        "item": "LHSA+DP Project Team",
        "quantity": 1.0
    },
    {
        "item": "构造者",
        "quantity": 1.0
    },
    {
        "item": "残疾人设施建议",
        "quantity": 1.0
    },
    {
        "item": "建筑物理和消防安全",
        "quantity": 1.0
    },
    {
        "item": "项目管理和工程建议",
        "quantity": 1.0
    },
    {
        "item": "D&W承包商",
        "quantity": 1.0
    },
    {
        "item": "人造景观承包商",
        "quantity": 1.0
    },
    {
        "item": "首席电气工程师",
        "quantity": 1.0
    },
    {
        "item": "Interactive Design ",
        "quantity": 1.0
    },
    {
        "item": "结构和电气",
        "quantity": 1.0
    },
    {
        "item": "Ground work",
        "quantity": 1.0
    },
    {
        "item": "Building construction",
        "quantity": 1.0
    },
    {
        "item": "项目组织设计",
        "quantity": 1.0
    },
    {
        "item": "装饰工作室",
        "quantity": 1.0
    },
    {
        "item": "编程",
        "quantity": 1.0
    },
    {
        "item": "PLAZMA 建筑事务所团队",
        "quantity": 1.0
    },
    {
        "item": "建筑维护系统",
        "quantity": 1.0
    },
    {
        "item": "Paleko Arch Studija建筑事务团队",
        "quantity": 1.0
    },
    {
        "item": "能源方案",
        "quantity": 1.0
    },
    {
        "item": "恢复/保护顾问",
        "quantity": 1.0
    },
    {
        "item": "承重结构",
        "quantity": 1.0
    },
    {
        "item": "建筑设计师 & 助理",
        "quantity": 1.0
    },
    {
        "item": "交互式媒体",
        "quantity": 1.0
    },
    {
        "item": "当地维护顾问",
        "quantity": 1.0
    },
    {
        "item": "能效",
        "quantity": 1.0
    },
    {
        "item": "楼层高度",
        "quantity": 1.0
    },
    {
        "item": "顾问与项目管理",
        "quantity": 1.0
    },
    {
        "item": "电力安装",
        "quantity": 1.0
    },
    {
        "item": "设计董事",
        "quantity": 1.0
    },
    {
        "item": "墙体模板制造",
        "quantity": 1.0
    },
    {
        "item": "墙体模板设计",
        "quantity": 1.0
    },
    {
        "item": "效果图制作",
        "quantity": 1.0
    },
    {
        "item": "机电工程 ",
        "quantity": 1.0
    },
    {
        "item": "洁具系统",
        "quantity": 1.0
    },
    {
        "item": "室外地板",
        "quantity": 1.0
    },
    {
        "item": "铝框架",
        "quantity": 1.0
    },
    {
        "item": "二期MEP",
        "quantity": 1.0
    },
    {
        "item": "二期结构",
        "quantity": 1.0
    },
    {
        "item": "二期总承包商",
        "quantity": 1.0
    },
    {
        "item": "一期总承包商",
        "quantity": 1.0
    },
    {
        "item": "捐助人 （按姓氏字母顺序排列）",
        "quantity": 1.0
    },
    {
        "item": "钢材",
        "quantity": 1.0
    },
    {
        "item": "财务总监",
        "quantity": 1.0
    },
    {
        "item": "展示团队",
        "quantity": 1.0
    },
    {
        "item": "质量调查员",
        "quantity": 1.0
    },
    {
        "item": "五金制作",
        "quantity": 1.0
    },
    {
        "item": "健康和安全",
        "quantity": 1.0
    },
    {
        "item": "其他参与设计者",
        "quantity": 1.0
    },
    {
        "item": "景观施工团队",
        "quantity": 1.0
    },
    {
        "item": "环境质量工程",
        "quantity": 1.0
    },
    {
        "item": "液体、暖通空调和电力",
        "quantity": 1.0
    },
    {
        "item": "农业工程",
        "quantity": 1.0
    },
    {
        "item": "热气设计",
        "quantity": 1.0
    },
    {
        "item": "建筑服务工程（管井） ",
        "quantity": 1.0
    },
    {
        "item": "主题公园顾问",
        "quantity": 1.0
    },
    {
        "item": "伙伴",
        "quantity": 1.0
    },
    {
        "item": "主要赞助商",
        "quantity": 1.0
    },
    {
        "item": "水系统顾问",
        "quantity": 1.0
    },
    {
        "item": "机电管道承包商",
        "quantity": 1.0
    },
    {
        "item": "电气和通信",
        "quantity": 1.0
    },
    {
        "item": " 新建建筑设计",
        "quantity": 1.0
    },
    {
        "item": "Master Plan",
        "quantity": 1.0
    },
    {
        "item": "室内设计与景观",
        "quantity": 1.0
    },
    {
        "item": "城市空间",
        "quantity": 1.0
    },
    {
        "item": "公私合作运营商",
        "quantity": 1.0
    },
    {
        "item": "阶段",
        "quantity": 1.0
    },
    {
        "item": "Principal Architects",
        "quantity": 1.0
    },
    {
        "item": "椅子",
        "quantity": 1.0
    },
    {
        "item": "电气及交通",
        "quantity": 1.0
    },
    {
        "item": "石层",
        "quantity": 1.0
    },
    {
        "item": "基础及结构",
        "quantity": 1.0
    },
    {
        "item": "屋顶防水层",
        "quantity": 1.0
    },
    {
        "item": "木屋顶结构分析",
        "quantity": 1.0
    },
    {
        "item": "联合创始人/设计总监",
        "quantity": 1.0
    },
    {
        "item": "Artificial Rock",
        "quantity": 1.0
    },
    {
        "item": "木屋顶",
        "quantity": 1.0
    },
    {
        "item": "木屋顶结构设计",
        "quantity": 1.0
    },
    {
        "item": "墙体",
        "quantity": 1.0
    },
    {
        "item": "透视法顾问",
        "quantity": 1.0
    },
    {
        "item": "声波工程师",
        "quantity": 1.0
    },
    {
        "item": "展厅团队",
        "quantity": 1.0
    },
    {
        "item": "策略",
        "quantity": 1.0
    },
    {
        "item": "造型咨询",
        "quantity": 1.0
    },
    {
        "item": "组织团队",
        "quantity": 1.0
    },
    {
        "item": "剧院咨询服务",
        "quantity": 1.0
    },
    {
        "item": "供电和卫生",
        "quantity": 1.0
    },
    {
        "item": "厨房供应商",
        "quantity": 1.0
    },
    {
        "item": "礼拜权威",
        "quantity": 1.0
    },
    {
        "item": "防鸽系统",
        "quantity": 1.0
    },
    {
        "item": "Guymer Bailey 团队",
        "quantity": 1.0
    },
    {
        "item": "工作主管",
        "quantity": 1.0
    },
    {
        "item": "建设工作总管",
        "quantity": 1.0
    },
    {
        "item": "地质顾问，交通顾问",
        "quantity": 1.0
    },
    {
        "item": "规范咨询",
        "quantity": 1.0
    },
    {
        "item": "机电液压工程师",
        "quantity": 1.0
    },
    {
        "item": "照明和电气设计",
        "quantity": 1.0
    },
    {
        "item": "安装技术顾问",
        "quantity": 1.0
    },
    {
        "item": "员工安全与可达性",
        "quantity": 1.0
    },
    {
        "item": "Joowon Moon",
        "quantity": 1.0
    },
    {
        "item": "铁件制作 (悬浮铁制楼梯)",
        "quantity": 1.0
    },
    {
        "item": "户外木作",
        "quantity": 1.0
    },
    {
        "item": "施工建筑师",
        "quantity": 1.0
    },
    {
        "item": "赵敏该设计",
        "quantity": 1.0
    },
    {
        "item": "机械设施",
        "quantity": 1.0
    },
    {
        "item": "消防工程顾问",
        "quantity": 1.0
    },
    {
        "item": "Associate - Product Design",
        "quantity": 1.0
    },
    {
        "item": "石作业",
        "quantity": 1.0
    },
    {
        "item": "安全和IT顾问",
        "quantity": 1.0
    },
    {
        "item": "年碳排放",
        "quantity": 1.0
    },
    {
        "item": "工业安装",
        "quantity": 1.0
    },
    {
        "item": "地方建筑院",
        "quantity": 1.0
    },
    {
        "item": "底层建筑面积",
        "quantity": 1.0
    },
    {
        "item": "陶器产品合作方",
        "quantity": 1.0
    },
    {
        "item": "建筑技术概念",
        "quantity": 1.0
    },
    {
        "item": "数字立面解决",
        "quantity": 1.0
    },
    {
        "item": "Visualization",
        "quantity": 1.0
    },
    {
        "item": "CNC加工",
        "quantity": 1.0
    },
    {
        "item": "能源技术",
        "quantity": 1.0
    },
    {
        "item": "标志、引导",
        "quantity": 1.0
    },
    {
        "item": "制造组装",
        "quantity": 1.0
    },
    {
        "item": "照明供给",
        "quantity": 1.0
    },
    {
        "item": "机电/给排水工程师",
        "quantity": 1.0
    },
    {
        "item": "音响视听设计",
        "quantity": 1.0
    },
    {
        "item": "城堡肾功能",
        "quantity": 1.0
    },
    {
        "item": "执行理事",
        "quantity": 1.0
    },
    {
        "item": "追踪设计顾问",
        "quantity": 1.0
    },
    {
        "item": "安保 / 自动化系统",
        "quantity": 1.0
    },
    {
        "item": "暖通空调，中央供暖系统",
        "quantity": 1.0
    },
    {
        "item": "镀锌外观施工",
        "quantity": 1.0
    },
    {
        "item": "项目协调和可持续性",
        "quantity": 1.0
    },
    {
        "item": "研究伙伴",
        "quantity": 1.0
    },
    {
        "item": "Equipe de Projeto",
        "quantity": 1.0
    },
    {
        "item": "技术系统",
        "quantity": 1.0
    },
    {
        "item": "照明提供",
        "quantity": 1.0
    },
    {
        "item": "金属",
        "quantity": 1.0
    },
    {
        "item": "木工安装",
        "quantity": 1.0
    },
    {
        "item": "木工制造",
        "quantity": 1.0
    },
    {
        "item": "绿色标志顾问",
        "quantity": 1.0
    },
    {
        "item": "Senior Interior Designer",
        "quantity": 1.0
    },
    {
        "item": "艺术指导与设计",
        "quantity": 1.0
    },
    {
        "item": "Senior Project Architects",
        "quantity": 1.0
    },
    {
        "item": "室外景观设计",
        "quantity": 1.0
    },
    {
        "item": "Senior Project Designer",
        "quantity": 1.0
    },
    {
        "item": "地理信息/土壤工程",
        "quantity": 1.0
    },
    {
        "item": "Principal/Design Principal",
        "quantity": 1.0
    },
    {
        "item": "施工文件",
        "quantity": 1.0
    },
    {
        "item": "Floor Tile Designer",
        "quantity": 1.0
    },
    {
        "item": "消防项目",
        "quantity": 1.0
    },
    {
        "item": "铺地",
        "quantity": 1.0
    },
    {
        "item": "平面",
        "quantity": 1.0
    },
    {
        "item": "花费顾问",
        "quantity": 1.0
    },
    {
        "item": "MEP HVAC 顾问",
        "quantity": 1.0
    },
    {
        "item": "机场特殊系统顾问",
        "quantity": 1.0
    },
    {
        "item": "路径寻找",
        "quantity": 1.0
    },
    {
        "item": "当地执行工程师",
        "quantity": 1.0
    },
    {
        "item": "概念发展, 系统开发, 构造与结构",
        "quantity": 1.0
    },
    {
        "item": "格式",
        "quantity": 1.0
    },
    {
        "item": "外形尺寸",
        "quantity": 1.0
    },
    {
        "item": "壳结构施工",
        "quantity": 1.0
    },
    {
        "item": "Technical Installation Advisor",
        "quantity": 1.0
    },
    {
        "item": "停车空间",
        "quantity": 1.0
    },
    {
        "item": "休闲空间",
        "quantity": 1.0
    },
    {
        "item": "单元数",
        "quantity": 1.0
    },
    {
        "item": "教育顾问",
        "quantity": 1.0
    },
    {
        "item": "项目参与者",
        "quantity": 1.0
    },
    {
        "item": "建筑主承包商",
        "quantity": 1.0
    },
    {
        "item": "图形和数据可视化",
        "quantity": 1.0
    },
    {
        "item": "建筑风格",
        "quantity": 1.0
    },
    {
        "item": "地理服务",
        "quantity": 1.0
    },
    {
        "item": "住宅室内",
        "quantity": 1.0
    },
    {
        "item": "成本 / 每平方英尺",
        "quantity": 1.0
    },
    {
        "item": "暖通空调，游泳池",
        "quantity": 1.0
    },
    {
        "item": "A/V 顾问",
        "quantity": 1.0
    },
    {
        "item": "厨房/食品服务",
        "quantity": 1.0
    },
    {
        "item": "安保系统",
        "quantity": 1.0
    },
    {
        "item": "预算顾问（竞赛）",
        "quantity": 1.0
    },
    {
        "item": "机械、电气、管道",
        "quantity": 1.0
    },
    {
        "item": "窗门供应商",
        "quantity": 1.0
    },
    {
        "item": "Eco",
        "quantity": 1.0
    },
    {
        "item": "结构&土建",
        "quantity": 1.0
    },
    {
        "item": "电气和机械工程设计",
        "quantity": 1.0
    },
    {
        "item": "餐饮设备",
        "quantity": 1.0
    },
    {
        "item": "锁匠",
        "quantity": 1.0
    },
    {
        "item": "能源策略",
        "quantity": 1.0
    },
    {
        "item": "Design Architect",
        "quantity": 1.0
    },
    {
        "item": "立面面积",
        "quantity": 1.0
    },
    {
        "item": "多媒体设计",
        "quantity": 1.0
    },
    {
        "item": "外墙安装",
        "quantity": 1.0
    },
    {
        "item": "Area Of Footprint",
        "quantity": 1.0
    },
    {
        "item": "外观设计师",
        "quantity": 1.0
    },
    {
        "item": "Equipo",
        "quantity": 1.0
    },
    {
        "item": "Socio Fundador",
        "quantity": 1.0
    },
    {
        "item": "绿色设计认证",
        "quantity": 1.0
    },
    {
        "item": "实施阶段设计员",
        "quantity": 1.0
    },
    {
        "item": "助手团队",
        "quantity": 1.0
    },
    {
        "item": "玻璃幕墙安装顾问",
        "quantity": 1.0
    },
    {
        "item": "居民监督员",
        "quantity": 1.0
    },
    {
        "item": "施工翻样 ",
        "quantity": 1.0
    },
    {
        "item": "3D 插图",
        "quantity": 1.0
    },
    {
        "item": "开发商/承包商",
        "quantity": 1.0
    },
    {
        "item": "ICT顾问",
        "quantity": 1.0
    },
    {
        "item": "批准监理",
        "quantity": 1.0
    },
    {
        "item": "项目责任单位",
        "quantity": 1.0
    },
    {
        "item": "FF&E",
        "quantity": 1.0
    },
    {
        "item": "分区墙监理",
        "quantity": 1.0
    },
    {
        "item": "室内设计及办公场所策划",
        "quantity": 1.0
    },
    {
        "item": "声学与安全顾问",
        "quantity": 1.0
    },
    {
        "item": "承包商，项目经理",
        "quantity": 1.0
    },
    {
        "item": " 羽管键琴",
        "quantity": 1.0
    },
    {
        "item": "起重机",
        "quantity": 1.0
    },
    {
        "item": "演员",
        "quantity": 1.0
    },
    {
        "item": "助理导演",
        "quantity": 1.0
    },
    {
        "item": "Senior Designer",
        "quantity": 1.0
    },
    {
        "item": "电影导演",
        "quantity": 1.0
    },
    {
        "item": "15F 室内景观设计",
        "quantity": 1.0
    },
    {
        "item": "15F 室内设计",
        "quantity": 1.0
    },
    {
        "item": "金属预制件",
        "quantity": 1.0
    },
    {
        "item": "建筑合作伙伴",
        "quantity": 1.0
    },
    {
        "item": "展示模型",
        "quantity": 1.0
    },
    {
        "item": "道路和网络设计师",
        "quantity": 1.0
    },
    {
        "item": "金属表面与幕墙分包商",
        "quantity": 1.0
    },
    {
        "item": "电梯工程师",
        "quantity": 1.0
    },
    {
        "item": "GFRP 立面分承包商",
        "quantity": 1.0
    },
    {
        "item": "GFRP 立面质量控制",
        "quantity": 1.0
    },
    {
        "item": "建造物理与声学",
        "quantity": 1.0
    },
    {
        "item": "图片集成 (彩色)",
        "quantity": 1.0
    },
    {
        "item": "站台预算 (RFF)",
        "quantity": 1.0
    },
    {
        "item": "车站预算(Gares & Connexions)",
        "quantity": 1.0
    },
    {
        "item": "计划顾问",
        "quantity": 1.0
    },
    {
        "item": "Blackwell Structural Engineers (当地结构工程师)",
        "quantity": 1.0
    },
    {
        "item": "徽标&引导标示",
        "quantity": 1.0
    },
    {
        "item": "机场创作团队",
        "quantity": 1.0
    },
    {
        "item": "Thornton Thomasetti （设计结构建设)",
        "quantity": 1.0
    },
    {
        "item": "Hariri Pontarini Architects (建筑师)",
        "quantity": 1.0
    },
    {
        "item": "其他参与",
        "quantity": 1.0
    },
    {
        "item": "Designers and Fabricators",
        "quantity": 1.0
    },
    {
        "item": "规划设计顾问",
        "quantity": 1.0
    },
    {
        "item": "结构与设备工程",
        "quantity": 1.0
    },
    {
        "item": "项目与设计经理",
        "quantity": 1.0
    },
    {
        "item": "软件使用",
        "quantity": 1.0
    },
    {
        "item": "表面模型",
        "quantity": 1.0
    },
    {
        "item": " Architect",
        "quantity": 1.0
    },
    {
        "item": "批准建筑检查",
        "quantity": 1.0
    },
    {
        "item": "场地测绘",
        "quantity": 1.0
    },
    {
        "item": "承包合同或采购路线",
        "quantity": 1.0
    },
    {
        "item": "钢筋混凝土弓",
        "quantity": 1.0
    },
    {
        "item": "竹钢制作",
        "quantity": 1.0
    },
    {
        "item": "协作建筑事务所",
        "quantity": 1.0
    },
    {
        "item": "ESD 工程师",
        "quantity": 1.0
    },
    {
        "item": "音响概念",
        "quantity": 1.0
    },
    {
        "item": "客户j顾问",
        "quantity": 1.0
    },
    {
        "item": "燧石顾问",
        "quantity": 1.0
    },
    {
        "item": "市政基础工程师",
        "quantity": 1.0
    },
    {
        "item": "协会",
        "quantity": 1.0
    },
    {
        "item": "合作者与顾问",
        "quantity": 1.0
    },
    {
        "item": "社区筹资",
        "quantity": 1.0
    },
    {
        "item": "无障碍入口设计",
        "quantity": 1.0
    },
    {
        "item": "入口设计",
        "quantity": 1.0
    },
    {
        "item": "Scénography ",
        "quantity": 1.0
    },
    {
        "item": "历史保护设计",
        "quantity": 1.0
    },
    {
        "item": "建设过程",
        "quantity": 1.0
    },
    {
        "item": "隔墙/照明使用顾问",
        "quantity": 1.0
    },
    {
        "item": "VRD工作室",
        "quantity": 1.0
    },
    {
        "item": "消防策略顾问",
        "quantity": 1.0
    },
    {
        "item": "批准检验",
        "quantity": 1.0
    },
    {
        "item": "项目经理/雇佣中介",
        "quantity": 1.0
    },
    {
        "item": "水利",
        "quantity": 1.0
    },
    {
        "item": "拆除/预施工承包商",
        "quantity": 1.0
    },
    {
        "item": "建筑师设计组",
        "quantity": 1.0
    },
    {
        "item": "估算",
        "quantity": 1.0
    },
    {
        "item": "认证检查",
        "quantity": 1.0
    },
    {
        "item": "建筑师伙伴",
        "quantity": 1.0
    },
    {
        "item": "竞赛设计师",
        "quantity": 1.0
    },
    {
        "item": "施工服务",
        "quantity": 1.0
    },
    {
        "item": "外观顾问",
        "quantity": 1.0
    },
    {
        "item": "建筑构造",
        "quantity": 1.0
    },
    {
        "item": "空间扩建与家具安装",
        "quantity": 1.0
    },
    {
        "item": "电力设施",
        "quantity": 1.0
    },
    {
        "item": "Photometrics与照明",
        "quantity": 1.0
    },
    {
        "item": "拆除，墙体与粉刷",
        "quantity": 1.0
    },
    {
        "item": "场地监管",
        "quantity": 1.0
    },
    {
        "item": "公共艺术合作者",
        "quantity": 1.0
    },
    {
        "item": "开发商与投资人",
        "quantity": 1.0
    },
    {
        "item": "建筑成本顾问",
        "quantity": 1.0
    },
    {
        "item": "U & Me 酒店室内设计",
        "quantity": 1.0
    },
    {
        "item": "可持续发展计划",
        "quantity": 1.0
    },
    {
        "item": "Sistema Constructivo",
        "quantity": 1.0
    },
    {
        "item": "国际地形",
        "quantity": 1.0
    },
    {
        "item": "Ingeniero Estructural",
        "quantity": 1.0
    },
    {
        "item": "Representante del Cliente / Coordinación de Diseño",
        "quantity": 1.0
    },
    {
        "item": "音响和视频设计顾问",
        "quantity": 1.0
    },
    {
        "item": "加热、通风和空调(CVAA)",
        "quantity": 1.0
    },
    {
        "item": "Shou Sugi Ban木板",
        "quantity": 1.0
    },
    {
        "item": "系统工程和专项设施",
        "quantity": 1.0
    },
    {
        "item": "空调工程",
        "quantity": 1.0
    },
    {
        "item": "SMA 室内设备",
        "quantity": 1.0
    },
    {
        "item": "媒体和营销",
        "quantity": 1.0
    },
    {
        "item": "厨房区域设计",
        "quantity": 1.0
    },
    {
        "item": "工程设备",
        "quantity": 1.0
    },
    {
        "item": "工程协调",
        "quantity": 1.0
    },
    {
        "item": "品牌设计",
        "quantity": 1.0
    },
    {
        "item": "立面供应商",
        "quantity": 1.0
    },
    {
        "item": "证明/建筑调查",
        "quantity": 1.0
    },
    {
        "item": "太阳能板",
        "quantity": 1.0
    },
    {
        "item": "PM",
        "quantity": 1.0
    },
    {
        "item": "项目主管建筑师",
        "quantity": 1.0
    },
    {
        "item": "设计主要材料",
        "quantity": 1.0
    },
    {
        "item": "上漆与室内",
        "quantity": 1.0
    },
    {
        "item": "执行者",
        "quantity": 1.0
    },
    {
        "item": "AOR",
        "quantity": 1.0
    },
    {
        "item": "创意指导",
        "quantity": 1.0
    },
    {
        "item": "设计业主",
        "quantity": 1.0
    },
    {
        "item": "Phyllis Wattis剧院咨询",
        "quantity": 1.0
    },
    {
        "item": "项目团队 SSP",
        "quantity": 1.0
    },
    {
        "item": "Lead Architect",
        "quantity": 1.0
    },
    {
        "item": "能源环境技术咨询",
        "quantity": 1.0
    },
    {
        "item": "研讨与发展",
        "quantity": 1.0
    },
    {
        "item": "硬件顾问",
        "quantity": 1.0
    },
    {
        "item": "设计成本顾问",
        "quantity": 1.0
    },
    {
        "item": "业主成本顾问",
        "quantity": 1.0
    },
    {
        "item": "可持续发展设计顾问",
        "quantity": 1.0
    },
    {
        "item": "声学和音频/视频顾问",
        "quantity": 1.0
    },
    {
        "item": "可持续设计团队",
        "quantity": 1.0
    },
    {
        "item": "工程师/经济师",
        "quantity": 1.0
    },
    {
        "item": "Plot",
        "quantity": 1.0
    },
    {
        "item": "平面图",
        "quantity": 1.0
    },
    {
        "item": "博物馆业主代表",
        "quantity": 1.0
    },
    {
        "item": "总建造者",
        "quantity": 1.0
    },
    {
        "item": "博物馆LEED顾问",
        "quantity": 1.0
    },
    {
        "item": "高级项目设计师",
        "quantity": 1.0
    },
    {
        "item": "博物馆结构工程师",
        "quantity": 1.0
    },
    {
        "item": "博物馆注册建筑师",
        "quantity": 1.0
    },
    {
        "item": "健康和安全协调员",
        "quantity": 1.0
    },
    {
        "item": "博物馆照明设计",
        "quantity": 1.0
    },
    {
        "item": "基座建筑业主代表",
        "quantity": 1.0
    },
    {
        "item": "基座建筑立面顾问",
        "quantity": 1.0
    },
    {
        "item": "基座建筑注册建筑师",
        "quantity": 1.0
    },
    {
        "item": "基座建筑设计顾问",
        "quantity": 1.0
    },
    {
        "item": "工业设计与木工",
        "quantity": 1.0
    },
    {
        "item": "音乐",
        "quantity": 1.0
    },
    {
        "item": "特殊制造",
        "quantity": 1.0
    },
    {
        "item": "结构/机电工程",
        "quantity": 1.0
    },
    {
        "item": "防火及安保",
        "quantity": 1.0
    },
    {
        "item": "RAAAF 工作室的协助",
        "quantity": 1.0
    },
    {
        "item": "水系统",
        "quantity": 1.0
    },
    {
        "item": "设计安装",
        "quantity": 1.0
    },
    {
        "item": "结构及市政工程师",
        "quantity": 1.0
    },
    {
        "item": "景观施工图",
        "quantity": 1.0
    },
    {
        "item": "立面结构顾问",
        "quantity": 1.0
    },
    {
        "item": "建筑配合设计院",
        "quantity": 1.0
    },
    {
        "item": "建筑组",
        "quantity": 1.0
    },
    {
        "item": "石材纹理专家",
        "quantity": 1.0
    },
    {
        "item": "设计合作单位",
        "quantity": 1.0
    },
    {
        "item": "调查",
        "quantity": 1.0
    },
    {
        "item": "建筑与城市设计",
        "quantity": 1.0
    },
    {
        "item": "结构工程师和电气设计师",
        "quantity": 1.0
    },
    {
        "item": "Residente de Obra",
        "quantity": 1.0
    },
    {
        "item": "Sculptor",
        "quantity": 1.0
    },
    {
        "item": "深灰色木板条长度",
        "quantity": 1.0
    },
    {
        "item": "立面图文",
        "quantity": 1.0
    },
    {
        "item": "金属框架",
        "quantity": 1.0
    },
    {
        "item": "外壳表面积",
        "quantity": 1.0
    },
    {
        "item": "拱板间距离",
        "quantity": 1.0
    },
    {
        "item": "北面横梁",
        "quantity": 1.0
    },
    {
        "item": "支持主管",
        "quantity": 1.0
    },
    {
        "item": "钟楼高度",
        "quantity": 1.0
    },
    {
        "item": "营造",
        "quantity": 1.0
    },
    {
        "item": "代理人",
        "quantity": 1.0
    },
    {
        "item": "第二集团",
        "quantity": 1.0
    },
    {
        "item": "窗户生产",
        "quantity": 1.0
    },
    {
        "item": "体量 2",
        "quantity": 1.0
    },
    {
        "item": "彩色玻璃窗口设计概念",
        "quantity": 1.0
    },
    {
        "item": "联合创始人/总监",
        "quantity": 1.0
    },
    {
        "item": "木材专家 ",
        "quantity": 1.0
    },
    {
        "item": "稳定性顾问",
        "quantity": 1.0
    },
    {
        "item": "业主助理",
        "quantity": 1.0
    },
    {
        "item": "商标",
        "quantity": 1.0
    },
    {
        "item": "人类学顾问",
        "quantity": 1.0
    },
    {
        "item": " Architects in Charge",
        "quantity": 1.0
    },
    {
        "item": "助理，项目经理",
        "quantity": 1.0
    },
    {
        "item": "助理，项目总监",
        "quantity": 1.0
    },
    {
        "item": "阶段2艺术家",
        "quantity": 1.0
    },
    {
        "item": "阶段1艺术家",
        "quantity": 1.0
    },
    {
        "item": "阶段2承包商",
        "quantity": 1.0
    },
    {
        "item": "阶段1承包商",
        "quantity": 1.0
    },
    {
        "item": "可持续性和零能耗顾问",
        "quantity": 1.0
    },
    {
        "item": "基座设备与电力",
        "quantity": 1.0
    },
    {
        "item": "竞赛阶段设计团队",
        "quantity": 1.0
    },
    {
        "item": "工业化厨房:",
        "quantity": 1.0
    },
    {
        "item": "教师之村六号楼",
        "quantity": 1.0
    },
    {
        "item": "当地建筑公司",
        "quantity": 1.0
    },
    {
        "item": "遗产保护",
        "quantity": 1.0
    },
    {
        "item": "电力 / 水力 / 电信 / 电子设备",
        "quantity": 1.0
    },
    {
        "item": "SIP 建造",
        "quantity": 1.0
    },
    {
        "item": "联协建筑师事务所",
        "quantity": 1.0
    },
    {
        "item": "Project by",
        "quantity": 1.0
    },
    {
        "item": "主要合伙人",
        "quantity": 1.0
    },
    {
        "item": "电气与设备工程",
        "quantity": 1.0
    },
    {
        "item": "三维模拟",
        "quantity": 1.0
    },
    {
        "item": "保护规划和爬行动物学家",
        "quantity": 1.0
    },
    {
        "item": "建筑混凝土顾问",
        "quantity": 1.0
    },
    {
        "item": "机电管道工程师及灯光设计师",
        "quantity": 1.0
    },
    {
        "item": "执行建筑师 ",
        "quantity": 1.0
    },
    {
        "item": "学校面积",
        "quantity": 1.0
    },
    {
        "item": "麦当劳Calberson 仓库协调员",
        "quantity": 1.0
    },
    {
        "item": "合作团体",
        "quantity": 1.0
    },
    {
        "item": "纳曼度假村总体规划",
        "quantity": 1.0
    },
    {
        "item": "玻璃承包商",
        "quantity": 1.0
    },
    {
        "item": "艺术融合",
        "quantity": 1.0
    },
    {
        "item": "联络建筑师",
        "quantity": 1.0
    },
    {
        "item": "结局",
        "quantity": 1.0
    },
    {
        "item": "电力 MEP",
        "quantity": 1.0
    },
    {
        "item": "价格顾问",
        "quantity": 1.0
    },
    {
        "item": "水泥工程师",
        "quantity": 1.0
    },
    {
        "item": "概念设计 (ZHA)",
        "quantity": 1.0
    },
    {
        "item": "室内灯光首席设计师",
        "quantity": 1.0
    },
    {
        "item": "贡献者 (ZHA)",
        "quantity": 1.0
    },
    {
        "item": "技术照明",
        "quantity": 1.0
    },
    {
        "item": "施工图单位",
        "quantity": 1.0
    },
    {
        "item": "SMA 室内设计",
        "quantity": 1.0
    },
    {
        "item": "照片设计",
        "quantity": 1.0
    },
    {
        "item": "旅游顾问",
        "quantity": 1.0
    },
    {
        "item": "灯光工程",
        "quantity": 1.0
    },
    {
        "item": "家具供应商",
        "quantity": 1.0
    },
    {
        "item": "室内设计/顾问",
        "quantity": 1.0
    },
    {
        "item": "立面工程 ",
        "quantity": 1.0
    },
    {
        "item": "Socio",
        "quantity": 1.0
    },
    {
        "item": "金属/水泥结构:",
        "quantity": 1.0
    },
    {
        "item": "单价",
        "quantity": 1.0
    },
    {
        "item": "Msc  机械工程师",
        "quantity": 1.0
    },
    {
        "item": "主资金赞助",
        "quantity": 1.0
    },
    {
        "item": "表面设计",
        "quantity": 1.0
    },
    {
        "item": "原预算",
        "quantity": 1.0
    },
    {
        "item": "土建施工",
        "quantity": 1.0
    },
    {
        "item": "竞赛阶段",
        "quantity": 1.0
    },
    {
        "item": "Geo",
        "quantity": 1.0
    },
    {
        "item": "标志与图形设计",
        "quantity": 1.0
    },
    {
        "item": "过程工程师",
        "quantity": 1.0
    },
    {
        "item": "零售服务",
        "quantity": 1.0
    },
    {
        "item": "创意总监（展览）",
        "quantity": 1.0
    },
    {
        "item": "MBS 员工",
        "quantity": 1.0
    },
    {
        "item": "覆盖率",
        "quantity": 1.0
    },
    {
        "item": "室内艺术设计",
        "quantity": 1.0
    },
    {
        "item": "水泥结构设计师",
        "quantity": 1.0
    },
    {
        "item": "历史研究",
        "quantity": 1.0
    },
    {
        "item": "水泥结构",
        "quantity": 1.0
    },
    {
        "item": "合作建筑师／工程师",
        "quantity": 1.0
    },
    {
        "item": "完成面施工方",
        "quantity": 1.0
    },
    {
        "item": "结构施工方",
        "quantity": 1.0
    },
    {
        "item": "UNStudio 团队",
        "quantity": 1.0
    },
    {
        "item": "立面表面积",
        "quantity": 1.0
    },
    {
        "item": "翻新的表面积",
        "quantity": 1.0
    },
    {
        "item": "员工（初步设计）",
        "quantity": 1.0
    },
    {
        "item": "室内铁件制作",
        "quantity": 1.0
    },
    {
        "item": "三维图片",
        "quantity": 1.0
    },
    {
        "item": "BET TCE-ECO-HQE-VRD",
        "quantity": 1.0
    },
    {
        "item": "Girard-Hébert, 游泳池工程师",
        "quantity": 1.0
    },
    {
        "item": "GLT+, 项目经理 ",
        "quantity": 1.0
    },
    {
        "item": "Bota Bota ",
        "quantity": 1.0
    },
    {
        "item": "项目工作组",
        "quantity": 1.0
    },
    {
        "item": "稳定性、欧洲议会议员、消防安全、声学、可持续性",
        "quantity": 1.0
    },
    {
        "item": "气候控制工程师",
        "quantity": 1.0
    },
    {
        "item": "当地工程师",
        "quantity": 1.0
    },
    {
        "item": "其他制造商",
        "quantity": 1.0
    },
    {
        "item": "复原",
        "quantity": 1.0
    },
    {
        "item": "LEED® 认证",
        "quantity": 1.0
    },
    {
        "item": "安全健康负责人",
        "quantity": 1.0
    },
    {
        "item": "现场测量工程师",
        "quantity": 1.0
    },
    {
        "item": "木制品工程师，音乐厅",
        "quantity": 1.0
    },
    {
        "item": "相关建筑师",
        "quantity": 1.0
    },
    {
        "item": "树供应商",
        "quantity": 1.0
    },
    {
        "item": "Enginnering",
        "quantity": 1.0
    },
    {
        "item": "衣柜和壁橱",
        "quantity": 1.0
    },
    {
        "item": "酒店室内建筑师",
        "quantity": 1.0
    },
    {
        "item": "拍照",
        "quantity": 1.0
    },
    {
        "item": "设计团队负责人",
        "quantity": 1.0
    },
    {
        "item": "地产开发商",
        "quantity": 1.0
    },
    {
        "item": "内部承包商",
        "quantity": 1.0
    },
    {
        "item": "开始时间",
        "quantity": 1.0
    },
    {
        "item": "地下面积",
        "quantity": 1.0
    },
    {
        "item": "执行师",
        "quantity": 1.0
    },
    {
        "item": "安全管理",
        "quantity": 1.0
    },
    {
        "item": "Mechanical Engineers",
        "quantity": 1.0
    },
    {
        "item": "钻井",
        "quantity": 1.0
    },
    {
        "item": "ARUP",
        "quantity": 1.0
    },
    {
        "item": "主负责人",
        "quantity": 1.0
    },
    {
        "item": "水力、暖气设施",
        "quantity": 1.0
    },
    {
        "item": "能量性能",
        "quantity": 1.0
    },
    {
        "item": "Security",
        "quantity": 1.0
    },
    {
        "item": "PE",
        "quantity": 1.0
    },
    {
        "item": "工程实践手册",
        "quantity": 1.0
    },
    {
        "item": "土建工程师 ",
        "quantity": 1.0
    },
    {
        "item": "造园技师",
        "quantity": 1.0
    },
    {
        "item": "电影厅设计顾问",
        "quantity": 1.0
    },
    {
        "item": "基础&结构",
        "quantity": 1.0
    },
    {
        "item": "景观执行",
        "quantity": 1.0
    },
    {
        "item": "历史建筑师",
        "quantity": 1.0
    },
    {
        "item": "改造建设",
        "quantity": 1.0
    },
    {
        "item": "安装系统",
        "quantity": 1.0
    },
    {
        "item": "自然顾问",
        "quantity": 1.0
    },
    {
        "item": "展示设计",
        "quantity": 1.0
    },
    {
        "item": "结构、服务工程师",
        "quantity": 1.0
    },
    {
        "item": "给排水和天然气设施",
        "quantity": 1.0
    },
    {
        "item": "本地结构和建筑工程师",
        "quantity": 1.0
    },
    {
        "item": "物理层协议控制信息",
        "quantity": 1.0
    },
    {
        "item": "总图建筑师",
        "quantity": 1.0
    },
    {
        "item": "OPC",
        "quantity": 1.0
    },
    {
        "item": "彩色玻璃窗户艺术指导",
        "quantity": 1.0
    },
    {
        "item": "标牌制作",
        "quantity": 1.0
    },
    {
        "item": "结构指导",
        "quantity": 1.0
    },
    {
        "item": "Lead Architects",
        "quantity": 1.0
    },
    {
        "item": "景观 / 顾问",
        "quantity": 1.0
    },
    {
        "item": "各层总面积",
        "quantity": 1.0
    },
    {
        "item": "家具柜",
        "quantity": 1.0
    },
    {
        "item": "施工管理者",
        "quantity": 1.0
    },
    {
        "item": "机械通气设计",
        "quantity": 1.0
    },
    {
        "item": "技术员 ",
        "quantity": 1.0
    },
    {
        "item": "室内墙图片",
        "quantity": 1.0
    },
    {
        "item": "土壤和湿地",
        "quantity": 1.0
    },
    {
        "item": "基础与结构",
        "quantity": 1.0
    },
    {
        "item": "估算员",
        "quantity": 1.0
    },
    {
        "item": "电气、电信和安全安装工程",
        "quantity": 1.0
    },
    {
        "item": "Other participants",
        "quantity": 1.0
    },
    {
        "item": "地下室",
        "quantity": 1.0
    },
    {
        "item": "Predominant Materiality",
        "quantity": 1.0
    },
    {
        "item": "行政建筑师",
        "quantity": 1.0
    },
    {
        "item": "租赁/主管",
        "quantity": 1.0
    },
    {
        "item": "生物工程师",
        "quantity": 1.0
    },
    {
        "item": "其他设计人员",
        "quantity": 1.0
    },
    {
        "item": "平面设计团队",
        "quantity": 1.0
    },
    {
        "item": "电力及光学顾问",
        "quantity": 1.0
    },
    {
        "item": "主要用途",
        "quantity": 1.0
    },
    {
        "item": "网站",
        "quantity": 1.0
    },
    {
        "item": "火炉",
        "quantity": 1.0
    },
    {
        "item": "项目耗资",
        "quantity": 1.0
    },
    {
        "item": "施工及竣工日期",
        "quantity": 1.0
    },
    {
        "item": "业主、建设管理",
        "quantity": 1.0
    },
    {
        "item": "IT顾问",
        "quantity": 1.0
    },
    {
        "item": "结构与系统",
        "quantity": 1.0
    },
    {
        "item": "视效",
        "quantity": 1.0
    },
    {
        "item": "Structural Design Company",
        "quantity": 1.0
    },
    {
        "item": "LEED Consultant",
        "quantity": 1.0
    },
    {
        "item": "社饮食",
        "quantity": 1.0
    },
    {
        "item": "室内设计伙伴",
        "quantity": 1.0
    },
    {
        "item": "安全协调员",
        "quantity": 1.0
    },
    {
        "item": "业主／客户",
        "quantity": 1.0
    },
    {
        "item": "内饰和景观工程师",
        "quantity": 1.0
    },
    {
        "item": "数字顾问",
        "quantity": 1.0
    },
    {
        "item": "项目概述",
        "quantity": 1.0
    },
    {
        "item": "CDM",
        "quantity": 1.0
    },
    {
        "item": "影像顾问",
        "quantity": 1.0
    },
    {
        "item": "媒体",
        "quantity": 1.0
    },
    {
        "item": "施工图配合单位",
        "quantity": 1.0
    },
    {
        "item": "工程经济顾问 历史古迹专家",
        "quantity": 1.0
    },
    {
        "item": "声学，视听和数据顾问",
        "quantity": 1.0
    },
    {
        "item": "三维模型建立",
        "quantity": 1.0
    },
    {
        "item": "会计",
        "quantity": 1.0
    },
    {
        "item": "玻璃幕墙",
        "quantity": 1.0
    },
    {
        "item": "Signage",
        "quantity": 1.0
    },
    {
        "item": "项目执行及施工管理",
        "quantity": 1.0
    },
    {
        "item": "奠基人",
        "quantity": 1.0
    },
    {
        "item": "建筑承包商 ",
        "quantity": 1.0
    },
    {
        "item": "项目委托方",
        "quantity": 1.0
    },
    {
        "item": "工程监督团队",
        "quantity": 1.0
    },
    {
        "item": "水泥地面",
        "quantity": 1.0
    },
    {
        "item": "LDI Interior",
        "quantity": 1.0
    },
    {
        "item": "MEP 工程师: Arup ",
        "quantity": 1.0
    },
    {
        "item": "地面铺装",
        "quantity": 1.0
    },
    {
        "item": "装饰设计",
        "quantity": 1.0
    },
    {
        "item": "静态结构指导",
        "quantity": 1.0
    },
    {
        "item": "LDI Façade",
        "quantity": 1.0
    },
    {
        "item": "设备及结构专业合作",
        "quantity": 1.0
    },
    {
        "item": "特殊细节建造",
        "quantity": 1.0
    },
    {
        "item": "LDI Architecture",
        "quantity": 1.0
    },
    {
        "item": "木制品手工制作",
        "quantity": 1.0
    },
    {
        "item": "Model Makers",
        "quantity": 1.0
    },
    {
        "item": "机械/管道工程师",
        "quantity": 1.0
    },
    {
        "item": "立面板",
        "quantity": 1.0
    },
    {
        "item": "创作领导",
        "quantity": 1.0
    },
    {
        "item": "建筑总包",
        "quantity": 1.0
    },
    {
        "item": "架构师",
        "quantity": 1.0
    },
    {
        "item": "媒体顾问",
        "quantity": 1.0
    },
    {
        "item": "连接结构设计",
        "quantity": 1.0
    },
    {
        "item": "本地建筑工程师",
        "quantity": 1.0
    },
    {
        "item": "声环境设计",
        "quantity": 1.0
    },
    {
        "item": "水电管道工程师",
        "quantity": 1.0
    },
    {
        "item": "建筑维护",
        "quantity": 1.0
    },
    {
        "item": "Garden Design",
        "quantity": 1.0
    },
    {
        "item": "业主建造师",
        "quantity": 1.0
    },
    {
        "item": "地质技术工程",
        "quantity": 1.0
    },
    {
        "item": "Mass Studies 工程团队",
        "quantity": 1.0
    },
    {
        "item": "舞台技术设计",
        "quantity": 1.0
    },
    {
        "item": "Architecture Of Record",
        "quantity": 1.0
    },
    {
        "item": "监管",
        "quantity": 1.0
    },
    {
        "item": "玻璃结构",
        "quantity": 1.0
    },
    {
        "item": "Project Designers",
        "quantity": 1.0
    },
    {
        "item": "人行桥技术咨询",
        "quantity": 1.0
    },
    {
        "item": "木工专家",
        "quantity": 1.0
    },
    {
        "item": "Off-grid顾问",
        "quantity": 1.0
    },
    {
        "item": "机械、电气、影音、 IT",
        "quantity": 1.0
    },
    {
        "item": "电子产品",
        "quantity": 1.0
    },
    {
        "item": "环境舒适度",
        "quantity": 1.0
    },
    {
        "item": "玻璃材料",
        "quantity": 1.0
    },
    {
        "item": "土地顾问",
        "quantity": 1.0
    },
    {
        "item": "技术架构工程师",
        "quantity": 1.0
    },
    {
        "item": "室内项目设计",
        "quantity": 1.0
    },
    {
        "item": "成本顾问与合同管理",
        "quantity": 1.0
    },
    {
        "item": "前期设计",
        "quantity": 1.0
    },
    {
        "item": "栖息地修复",
        "quantity": 1.0
    },
    {
        "item": "Project Type",
        "quantity": 1.0
    },
    {
        "item": "Total Cost",
        "quantity": 1.0
    },
    {
        "item": "家具这几",
        "quantity": 1.0
    },
    {
        "item": "建设周期",
        "quantity": 1.0
    },
    {
        "item": "專案设计团队",
        "quantity": 1.0
    },
    {
        "item": "Envelope Consultant",
        "quantity": 1.0
    },
    {
        "item": "设施顾问",
        "quantity": 1.0
    },
    {
        "item": "支撑钢铁",
        "quantity": 1.0
    },
    {
        "item": "Concrete Furniture",
        "quantity": 1.0
    },
    {
        "item": "把手",
        "quantity": 1.0
    },
    {
        "item": "音频和视频设计",
        "quantity": 1.0
    },
    {
        "item": "建造编码",
        "quantity": 1.0
    },
    {
        "item": "设计建造/结构",
        "quantity": 1.0
    },
    {
        "item": "质量",
        "quantity": 1.0
    },
    {
        "item": "建筑物理/声学",
        "quantity": 1.0
    },
    {
        "item": "记录建筑师及工程师",
        "quantity": 1.0
    },
    {
        "item": "总承建商 ",
        "quantity": 1.0
    },
    {
        "item": "机械电力工程师",
        "quantity": 1.0
    },
    {
        "item": "Project Managers",
        "quantity": 1.0
    },
    {
        "item": "绿化工程",
        "quantity": 1.0
    },
    {
        "item": "CDM 协调者",
        "quantity": 1.0
    },
    {
        "item": "项目经理 (第二阶段)",
        "quantity": 1.0
    },
    {
        "item": "地理信息工程",
        "quantity": 1.0
    },
    {
        "item": "索具设计",
        "quantity": 1.0
    },
    {
        "item": "Local Companies",
        "quantity": 1.0
    },
    {
        "item": "设计师/学生",
        "quantity": 1.0
    },
    {
        "item": "水平",
        "quantity": 1.0
    },
    {
        "item": "一般企业",
        "quantity": 1.0
    },
    {
        "item": "效果图团队",
        "quantity": 1.0
    },
    {
        "item": "伊东丰雄团队",
        "quantity": 1.0
    },
    {
        "item": "副承包商",
        "quantity": 1.0
    },
    {
        "item": "机械，电气，水暖，HVAC顾问",
        "quantity": 1.0
    },
    {
        "item": "预制钢制造",
        "quantity": 1.0
    },
    {
        "item": "平面布局",
        "quantity": 1.0
    },
    {
        "item": "图像显示",
        "quantity": 1.0
    },
    {
        "item": "持续性顾问",
        "quantity": 1.0
    },
    {
        "item": "每平方米成本",
        "quantity": 1.0
    },
    {
        "item": "机械电气管道工程师 ",
        "quantity": 1.0
    },
    {
        "item": "项目建筑师·",
        "quantity": 1.0
    },
    {
        "item": "标书团队",
        "quantity": 1.0
    },
    {
        "item": "餐厅室内设计",
        "quantity": 1.0
    },
    {
        "item": "Vison Sitting Kills + The End of Sitting",
        "quantity": 1.0
    },
    {
        "item": "景观绿化",
        "quantity": 1.0
    },
    {
        "item": "大学生团队",
        "quantity": 1.0
    },
    {
        "item": "项目出资人",
        "quantity": 1.0
    },
    {
        "item": "CUAC建筑设计团队",
        "quantity": 1.0
    },
    {
        "item": "展览主题",
        "quantity": 1.0
    },
    {
        "item": "种植乔木",
        "quantity": 1.0
    },
    {
        "item": "灯光/LED",
        "quantity": 1.0
    },
    {
        "item": "夯土墙承包商",
        "quantity": 1.0
    },
    {
        "item": "Construction Coordinator",
        "quantity": 1.0
    },
    {
        "item": "灌溉顾问",
        "quantity": 1.0
    },
    {
        "item": "城市",
        "quantity": 1.0
    },
    {
        "item": "消防局 防火顾问",
        "quantity": 1.0
    },
    {
        "item": "文本编辑",
        "quantity": 1.0
    },
    {
        "item": "主要赞助",
        "quantity": 1.0
    },
    {
        "item": "行政管理",
        "quantity": 1.0
    },
    {
        "item": "主持合作者（施工文件）",
        "quantity": 1.0
    },
    {
        "item": "土地评定师",
        "quantity": 1.0
    },
    {
        "item": "鉴定人",
        "quantity": 1.0
    },
    {
        "item": "功能管理",
        "quantity": 1.0
    },
    {
        "item": "电气及液压工程师",
        "quantity": 1.0
    },
    {
        "item": "机械电器管道和装置管道设计",
        "quantity": 1.0
    },
    {
        "item": "经济测算",
        "quantity": 1.0
    },
    {
        "item": "3D 图片",
        "quantity": 1.0
    },
    {
        "item": "环境顾问 ",
        "quantity": 1.0
    },
    {
        "item": "规范作者",
        "quantity": 1.0
    },
    {
        "item": "室内总设计师",
        "quantity": 1.0
    },
    {
        "item": "建筑方案设计",
        "quantity": 1.0
    },
    {
        "item": "创作建筑师",
        "quantity": 1.0
    },
    {
        "item": "Ffe",
        "quantity": 1.0
    },
    {
        "item": "公园面积",
        "quantity": 1.0
    },
    {
        "item": "团队2008 2013(施工/装饰)",
        "quantity": 1.0
    },
    {
        "item": "图像和标志",
        "quantity": 1.0
    },
    {
        "item": "Slade 建筑事务所",
        "quantity": 1.0
    },
    {
        "item": "Photographers",
        "quantity": 1.0
    },
    {
        "item": "咨询服务",
        "quantity": 1.0
    },
    {
        "item": "景观/园艺设计",
        "quantity": 1.0
    },
    {
        "item": "团队2001-2008(50% SD –建筑许可)",
        "quantity": 1.0
    },
    {
        "item": "承包所有者",
        "quantity": 1.0
    },
    {
        "item": "定做顾问",
        "quantity": 1.0
    },
    {
        "item": "参与建筑师",
        "quantity": 1.0
    },
    {
        "item": "主要工程公司",
        "quantity": 1.0
    },
    {
        "item": "Façade Consultant",
        "quantity": 1.0
    },
    {
        "item": "Lightning Design",
        "quantity": 1.0
    },
    {
        "item": "楼主",
        "quantity": 1.0
    },
    {
        "item": "Project Leadership",
        "quantity": 1.0
    },
    {
        "item": "总支出",
        "quantity": 1.0
    },
    {
        "item": "环境项目管理",
        "quantity": 1.0
    },
    {
        "item": "Hydraulics",
        "quantity": 1.0
    },
    {
        "item": "建筑智能",
        "quantity": 1.0
    },
    {
        "item": "建筑设计负责",
        "quantity": 1.0
    },
    {
        "item": "项目领导（建设）",
        "quantity": 1.0
    },
    {
        "item": "表皮材料",
        "quantity": 1.0
    },
    {
        "item": "Diamond And Schmitt Project Team",
        "quantity": 1.0
    },
    {
        "item": "发起",
        "quantity": 1.0
    },
    {
        "item": "机械电器管道工程师",
        "quantity": 1.0
    },
    {
        "item": "方案设计团队",
        "quantity": 1.0
    },
    {
        "item": "建设项目经理",
        "quantity": 1.0
    },
    {
        "item": "当地建筑与工程顾问 ",
        "quantity": 1.0
    },
    {
        "item": "Pocket-Park",
        "quantity": 1.0
    },
    {
        "item": "彩色影像设计",
        "quantity": 1.0
    },
    {
        "item": "Technical Services, ZCB",
        "quantity": 1.0
    },
    {
        "item": "M+E工程师",
        "quantity": 1.0
    },
    {
        "item": "质量监理",
        "quantity": 1.0
    },
    {
        "item": "Autores",
        "quantity": 1.0
    },
    {
        "item": "Aparejador",
        "quantity": 1.0
    },
    {
        "item": "BTUA",
        "quantity": 1.0
    },
    {
        "item": "立面承包者",
        "quantity": 1.0
    },
    {
        "item": "外部产品",
        "quantity": 1.0
    },
    {
        "item": "立面装修",
        "quantity": 1.0
    },
    {
        "item": "Http://www davidbessongirard-paysagistes fr/",
        "quantity": 1.0
    },
    {
        "item": "太阳能装置",
        "quantity": 1.0
    },
    {
        "item": "CDM 协调员",
        "quantity": 1.0
    },
    {
        "item": "废料顾问",
        "quantity": 1.0
    },
    {
        "item": "测绘顾问",
        "quantity": 1.0
    },
    {
        "item": "室内装潢加工",
        "quantity": 1.0
    },
    {
        "item": "Decoration",
        "quantity": 1.0
    },
    {
        "item": "设计及建造",
        "quantity": 1.0
    },
    {
        "item": "视觉交互设计",
        "quantity": 1.0
    },
    {
        "item": "钢结构、玻璃结构",
        "quantity": 1.0
    },
    {
        "item": "一层平面面积",
        "quantity": 1.0
    },
    {
        "item": "原项目亚美尼亚 1933",
        "quantity": 1.0
    },
    {
        "item": "电气咨询",
        "quantity": 1.0
    },
    {
        "item": "承包商/企业",
        "quantity": 1.0
    },
    {
        "item": "滑板运动场地施工",
        "quantity": 1.0
    },
    {
        "item": "Contratista",
        "quantity": 1.0
    },
    {
        "item": "音乐厅面积",
        "quantity": 1.0
    },
    {
        "item": "地基面积",
        "quantity": 1.0
    },
    {
        "item": "监管建筑设计",
        "quantity": 1.0
    },
    {
        "item": "特邀作者",
        "quantity": 1.0
    },
    {
        "item": "房屋技术",
        "quantity": 1.0
    },
    {
        "item": "交互游戏",
        "quantity": 1.0
    },
    {
        "item": "M/E/P工程师",
        "quantity": 1.0
    },
    {
        "item": "铝材和玻璃",
        "quantity": 1.0
    },
    {
        "item": "房屋设计",
        "quantity": 1.0
    },
    {
        "item": "财产拥有人",
        "quantity": 1.0
    },
    {
        "item": "Electrical Project",
        "quantity": 1.0
    },
    {
        "item": "合伙伙伴",
        "quantity": 1.0
    },
    {
        "item": "Square Footage",
        "quantity": 1.0
    },
    {
        "item": "现场协调",
        "quantity": 1.0
    },
    {
        "item": "设计合作者和制造商",
        "quantity": 1.0
    },
    {
        "item": "合伙设计师",
        "quantity": 1.0
    },
    {
        "item": "Project Team ",
        "quantity": 1.0
    },
    {
        "item": "项目建筑师（施工文件）",
        "quantity": 1.0
    },
    {
        "item": "Structural Calculation",
        "quantity": 1.0
    },
    {
        "item": "Technical Inspector And Engineering",
        "quantity": 1.0
    },
    {
        "item": "客户工程监管代表",
        "quantity": 1.0
    },
    {
        "item": "规范顾问",
        "quantity": 1.0
    },
    {
        "item": "Phyllis Wattis剧院以及Gina and Stuart Peterson White Box设计建筑师",
        "quantity": 1.0
    },
    {
        "item": "Sanitary",
        "quantity": 1.0
    },
    {
        "item": "预算与建设管理",
        "quantity": 1.0
    },
    {
        "item": "建筑管理主任",
        "quantity": 1.0
    },
    {
        "item": "贵宾休息室显示器",
        "quantity": 1.0
    },
    {
        "item": "承建公司",
        "quantity": 1.0
    },
    {
        "item": "合同流程",
        "quantity": 1.0
    },
    {
        "item": "Electrical project",
        "quantity": 1.0
    },
    {
        "item": "合作室外设计",
        "quantity": 1.0
    },
    {
        "item": "Co-workers",
        "quantity": 1.0
    },
    {
        "item": "Clients / Builders",
        "quantity": 1.0
    },
    {
        "item": "消防节能",
        "quantity": 1.0
    },
    {
        "item": "Services Consultant",
        "quantity": 1.0
    },
    {
        "item": "工作经理",
        "quantity": 1.0
    },
    {
        "item": "海洋结构",
        "quantity": 1.0
    },
    {
        "item": "设计师/建造师",
        "quantity": 1.0
    },
    {
        "item": "喷泉设计",
        "quantity": 1.0
    },
    {
        "item": "Project Lead Designer",
        "quantity": 1.0
    },
    {
        "item": "Development Effort",
        "quantity": 1.0
    },
    {
        "item": "景观及土建",
        "quantity": 1.0
    },
    {
        "item": "对外顾问",
        "quantity": 1.0
    },
    {
        "item": "消防安全/建筑物理",
        "quantity": 1.0
    },
    {
        "item": "服务工程 ",
        "quantity": 1.0
    },
    {
        "item": "项目资金",
        "quantity": 1.0
    },
    {
        "item": "AV Consultant",
        "quantity": 1.0
    },
    {
        "item": "主要设计人",
        "quantity": 1.0
    },
    {
        "item": "项目建筑师/设计师",
        "quantity": 1.0
    },
    {
        "item": "环境影响评估顾问",
        "quantity": 1.0
    },
    {
        "item": "电力敷设",
        "quantity": 1.0
    },
    {
        "item": "给排水与消防",
        "quantity": 1.0
    },
    {
        "item": "T2+1面积",
        "quantity": 1.0
    },
    {
        "item": "Cooperative Civil Engineer",
        "quantity": 1.0
    },
    {
        "item": "结构市政工程师",
        "quantity": 1.0
    },
    {
        "item": "建设指标",
        "quantity": 1.0
    },
    {
        "item": "幕布供给",
        "quantity": 1.0
    },
    {
        "item": "本土建筑师",
        "quantity": 1.0
    },
    {
        "item": "环保合作",
        "quantity": 1.0
    },
    {
        "item": "Model",
        "quantity": 1.0
    },
    {
        "item": "Economist",
        "quantity": 1.0
    },
    {
        "item": "Students participating in the Wilderness Summer School",
        "quantity": 1.0
    },
    {
        "item": "通风工程师",
        "quantity": 1.0
    },
    {
        "item": "业主/发展商",
        "quantity": 1.0
    },
    {
        "item": "主要建筑材料s",
        "quantity": 1.0
    },
    {
        "item": "建筑尺寸",
        "quantity": 1.0
    },
    {
        "item": "室外喷涂",
        "quantity": 1.0
    },
    {
        "item": "规范以及安全",
        "quantity": 1.0
    },
    {
        "item": "研究助理",
        "quantity": 1.0
    },
    {
        "item": "Project And Construction Team",
        "quantity": 1.0
    },
    {
        "item": "Associates",
        "quantity": 1.0
    },
    {
        "item": "Maquetas",
        "quantity": 1.0
    },
    {
        "item": "Colaborators",
        "quantity": 1.0
    },
    {
        "item": "氩气调节",
        "quantity": 1.0
    },
    {
        "item": "地质探测",
        "quantity": 1.0
    },
    {
        "item": "木工及木构架",
        "quantity": 1.0
    },
    {
        "item": "光环境顾问",
        "quantity": 1.0
    },
    {
        "item": "原设计",
        "quantity": 1.0
    },
    {
        "item": "结构元素/系统",
        "quantity": 1.0
    },
    {
        "item": "绘图/渲染",
        "quantity": 1.0
    },
    {
        "item": "Clients",
        "quantity": 1.0
    },
    {
        "item": "工程量清单",
        "quantity": 1.0
    },
    {
        "item": "Colaborador",
        "quantity": 1.0
    },
    {
        "item": "电设计师",
        "quantity": 1.0
    },
    {
        "item": "热环境访问",
        "quantity": 1.0
    },
    {
        "item": "Producer",
        "quantity": 1.0
    },
    {
        "item": "Diseño de Interiores, Mobiliario y Paisajismo",
        "quantity": 1.0
    },
    {
        "item": "建筑师主管",
        "quantity": 1.0
    },
    {
        "item": "Site Supervisor",
        "quantity": 1.0
    },
    {
        "item": "Mason木匠",
        "quantity": 1.0
    },
    {
        "item": "Gross floor area ",
        "quantity": 1.0
    },
    {
        "item": "Enterprise Work Team",
        "quantity": 1.0
    },
    {
        "item": "Photographer",
        "quantity": 1.0
    },
    {
        "item": "Principle  Architects",
        "quantity": 1.0
    },
    {
        "item": "电器，空调，水暖",
        "quantity": 1.0
    },
    {
        "item": "结构，热学和声学顾问",
        "quantity": 1.0
    },
    {
        "item": "项目经理 (第一阶段)",
        "quantity": 1.0
    },
    {
        "item": "HVAC 工程 \t",
        "quantity": 1.0
    },
    {
        "item": "直向建筑合伙人",
        "quantity": 1.0
    },
    {
        "item": "电器机械",
        "quantity": 1.0
    },
    {
        "item": "办公家具顾问",
        "quantity": 1.0
    },
    {
        "item": "Construction Supervisor",
        "quantity": 1.0
    },
    {
        "item": "内部拱门设计",
        "quantity": 1.0
    },
    {
        "item": "混凝土工程承包 ",
        "quantity": 1.0
    },
    {
        "item": "建设商",
        "quantity": 1.0
    },
    {
        "item": "Detailing Consultant",
        "quantity": 1.0
    },
    {
        "item": "结构工程企业",
        "quantity": 1.0
    },
    {
        "item": "公寓数量",
        "quantity": 1.0
    },
    {
        "item": "绘图设计",
        "quantity": 1.0
    },
    {
        "item": "二楼面积",
        "quantity": 1.0
    },
    {
        "item": "设计协调人",
        "quantity": 1.0
    },
    {
        "item": "摄影导演",
        "quantity": 1.0
    },
    {
        "item": "Leed Coordinators",
        "quantity": 1.0
    },
    {
        "item": "General Contractor and Manager",
        "quantity": 1.0
    },
    {
        "item": "建造监督",
        "quantity": 1.0
    },
    {
        "item": "Dear Architects 主创建筑师",
        "quantity": 1.0
    },
    {
        "item": "图形设计顾问",
        "quantity": 1.0
    },
    {
        "item": "Interior Design Collaboration",
        "quantity": 1.0
    },
    {
        "item": "电影的趋势",
        "quantity": 1.0
    },
    {
        "item": "BCA",
        "quantity": 1.0
    },
    {
        "item": "协调与监督",
        "quantity": 1.0
    },
    {
        "item": "建筑师团队 ",
        "quantity": 1.0
    },
    {
        "item": "家具预算",
        "quantity": 1.0
    },
    {
        "item": "灯光设计师 ",
        "quantity": 1.0
    },
    {
        "item": "Collaborating Architect",
        "quantity": 1.0
    },
    {
        "item": "石笼网",
        "quantity": 1.0
    },
    {
        "item": "工程单位 ",
        "quantity": 1.0
    },
    {
        "item": "场地覆盖面积",
        "quantity": 1.0
    },
    {
        "item": "MEPFP 工程师",
        "quantity": 1.0
    },
    {
        "item": "博物馆设计建造者",
        "quantity": 1.0
    },
    {
        "item": "Safety",
        "quantity": 1.0
    },
    {
        "item": "M&E Engineer",
        "quantity": 1.0
    },
    {
        "item": "项目团队 (客人房间)",
        "quantity": 1.0
    },
    {
        "item": "艺术大师",
        "quantity": 1.0
    },
    {
        "item": "经理合伙人",
        "quantity": 1.0
    },
    {
        "item": "技术管理规划",
        "quantity": 1.0
    },
    {
        "item": "设计审核总监",
        "quantity": 1.0
    },
    {
        "item": "Electrical Lighting Design",
        "quantity": 1.0
    },
    {
        "item": "酒廊家具定制",
        "quantity": 1.0
    },
    {
        "item": "车库面积",
        "quantity": 1.0
    },
    {
        "item": "水管设计",
        "quantity": 1.0
    },
    {
        "item": "Hombre de Piedra事务所主任建筑师",
        "quantity": 1.0
    },
    {
        "item": "硬件",
        "quantity": 1.0
    },
    {
        "item": "声设计",
        "quantity": 1.0
    },
    {
        "item": "业主和主要承包商",
        "quantity": 1.0
    },
    {
        "item": "3D 模型",
        "quantity": 1.0
    },
    {
        "item": "检查结构",
        "quantity": 1.0
    },
    {
        "item": "实体施工工程",
        "quantity": 1.0
    },
    {
        "item": "Lighting Facade",
        "quantity": 1.0
    },
    {
        "item": "现存建筑总设计师",
        "quantity": 1.0
    },
    {
        "item": "Terraces Area",
        "quantity": 1.0
    },
    {
        "item": "Wood Construction",
        "quantity": 1.0
    },
    {
        "item": "都市化设计",
        "quantity": 1.0
    },
    {
        "item": "Concrete Consultant",
        "quantity": 1.0
    },
    {
        "item": "Security Consultant",
        "quantity": 1.0
    },
    {
        "item": "Co-Investigator (Co-I)",
        "quantity": 1.0
    },
    {
        "item": "景观谁",
        "quantity": 1.0
    },
    {
        "item": "视觉传达设计",
        "quantity": 1.0
    },
    {
        "item": "HQE 咨询",
        "quantity": 1.0
    },
    {
        "item": "定制家具 ",
        "quantity": 1.0
    },
    {
        "item": "CVSE 工程师",
        "quantity": 1.0
    },
    {
        "item": "Equipo ",
        "quantity": 1.0
    },
    {
        "item": "Sugarplatform 设计团队",
        "quantity": 1.0
    },
    {
        "item": "Head Designer",
        "quantity": 1.0
    },
    {
        "item": "Audio Visual Consultant",
        "quantity": 1.0
    },
    {
        "item": "安装指导",
        "quantity": 1.0
    },
    {
        "item": "责任人",
        "quantity": 1.0
    },
    {
        "item": "展览设计总监媒体",
        "quantity": 1.0
    },
    {
        "item": "织物顾问",
        "quantity": 1.0
    },
    {
        "item": "Building Surveyor",
        "quantity": 1.0
    },
    {
        "item": "普通BET ",
        "quantity": 1.0
    },
    {
        "item": "架构设计",
        "quantity": 1.0
    },
    {
        "item": "可持续性发展设计顾问",
        "quantity": 1.0
    },
    {
        "item": "项目主导",
        "quantity": 1.0
    },
    {
        "item": "北京",
        "quantity": 1.0
    },
    {
        "item": "Geotechnical Engineer",
        "quantity": 1.0
    },
    {
        "item": "建筑材料供应商",
        "quantity": 1.0
    },
    {
        "item": "表皮 ",
        "quantity": 1.0
    },
    {
        "item": "表皮顾问",
        "quantity": 1.0
    },
    {
        "item": "Hamonic + Masson团队",
        "quantity": 1.0
    },
    {
        "item": "电力与安全",
        "quantity": 1.0
    },
    {
        "item": "施工承包商和项目管理",
        "quantity": 1.0
    },
    {
        "item": "砌筑工作",
        "quantity": 1.0
    },
    {
        "item": "工程师与CDM顾问",
        "quantity": 1.0
    },
    {
        "item": "结构访问",
        "quantity": 1.0
    },
    {
        "item": "Director of Specifications",
        "quantity": 1.0
    },
    {
        "item": "照明设计与自然照明分析",
        "quantity": 1.0
    },
    {
        "item": "项目协作",
        "quantity": 1.0
    },
    {
        "item": "编码 / 生命安全",
        "quantity": 1.0
    },
    {
        "item": "城市规划秘书长",
        "quantity": 1.0
    },
    {
        "item": "具体规划",
        "quantity": 1.0
    },
    {
        "item": "总资金额",
        "quantity": 1.0
    },
    {
        "item": "住宅施工",
        "quantity": 1.0
    },
    {
        "item": "室内设计和建筑",
        "quantity": 1.0
    },
    {
        "item": "建筑概念和设计",
        "quantity": 1.0
    },
    {
        "item": "预制木质建筑材料",
        "quantity": 1.0
    },
    {
        "item": "廊桥面积",
        "quantity": 1.0
    },
    {
        "item": "OMA 管理合伙人",
        "quantity": 1.0
    },
    {
        "item": "光环境",
        "quantity": 1.0
    },
    {
        "item": "基建承包商",
        "quantity": 1.0
    },
    {
        "item": "开发生",
        "quantity": 1.0
    },
    {
        "item": "项目总额",
        "quantity": 1.0
    },
    {
        "item": "室内厨房设计",
        "quantity": 1.0
    },
    {
        "item": "Administration Budget",
        "quantity": 1.0
    },
    {
        "item": "特殊技术",
        "quantity": 1.0
    },
    {
        "item": "外围顾问",
        "quantity": 1.0
    },
    {
        "item": "项目修复",
        "quantity": 1.0
    },
    {
        "item": "室内地板",
        "quantity": 1.0
    },
    {
        "item": "家具装修",
        "quantity": 1.0
    },
    {
        "item": "Construction Budget",
        "quantity": 1.0
    },
    {
        "item": "稳固性",
        "quantity": 1.0
    },
    {
        "item": "机电服务，消防系统和结构顾问",
        "quantity": 1.0
    },
    {
        "item": "建筑基地面积",
        "quantity": 1.0
    },
    {
        "item": "屋面防护技术支持",
        "quantity": 1.0
    },
    {
        "item": "M&E Consultant",
        "quantity": 1.0
    },
    {
        "item": "能源 & 环境",
        "quantity": 1.0
    },
    {
        "item": "行政协助",
        "quantity": 1.0
    },
    {
        "item": "Cooper Robertson 合作伙伴负责人",
        "quantity": 1.0
    },
    {
        "item": "景观建设",
        "quantity": 1.0
    },
    {
        "item": "Project Manager/Architect",
        "quantity": 1.0
    },
    {
        "item": "施行项目伙伴",
        "quantity": 1.0
    },
    {
        "item": "表皮测试",
        "quantity": 1.0
    },
    {
        "item": "设计伙伴、主任",
        "quantity": 1.0
    },
    {
        "item": "Grafton Architects",
        "quantity": 1.0
    },
    {
        "item": "Total Construction Cost",
        "quantity": 1.0
    },
    {
        "item": "构建面积",
        "quantity": 1.0
    },
    {
        "item": "其它合作商",
        "quantity": 1.0
    },
    {
        "item": "垃圾填埋场高度",
        "quantity": 1.0
    },
    {
        "item": "石雕顾问",
        "quantity": 1.0
    },
    {
        "item": "铁质家具",
        "quantity": 1.0
    },
    {
        "item": "设计规范顾问",
        "quantity": 1.0
    },
    {
        "item": "工作室主任/协调员",
        "quantity": 1.0
    },
    {
        "item": "Nyserda代表",
        "quantity": 1.0
    },
    {
        "item": "卫生顾问",
        "quantity": 1.0
    },
    {
        "item": "消防救生安全及洒水工程",
        "quantity": 1.0
    },
    {
        "item": "场地检查",
        "quantity": 1.0
    },
    {
        "item": "办公区域",
        "quantity": 1.0
    },
    {
        "item": "音频顾问",
        "quantity": 1.0
    },
    {
        "item": "ID - 酒店通用设计",
        "quantity": 1.0
    },
    {
        "item": "Address execution",
        "quantity": 1.0
    },
    {
        "item": "地质顾问",
        "quantity": 1.0
    },
    {
        "item": "家具顾问",
        "quantity": 1.0
    },
    {
        "item": "支出",
        "quantity": 1.0
    },
    {
        "item": "玻璃幕墙专家",
        "quantity": 1.0
    },
    {
        "item": "Construcción y Diseño Estructural",
        "quantity": 1.0
    },
    {
        "item": "风景制做",
        "quantity": 1.0
    },
    {
        "item": "竹子承包商",
        "quantity": 1.0
    },
    {
        "item": "供热系统",
        "quantity": 1.0
    },
    {
        "item": "Thermal Analysis",
        "quantity": 1.0
    },
    {
        "item": "柜子制造商",
        "quantity": 1.0
    },
    {
        "item": "地盘总面积",
        "quantity": 1.0
    },
    {
        "item": "Costruction Company",
        "quantity": 1.0
    },
    {
        "item": "Other Participants",
        "quantity": 1.0
    },
    {
        "item": "机电管道 ",
        "quantity": 1.0
    },
    {
        "item": "Total Foor Area",
        "quantity": 1.0
    },
    {
        "item": "屋顶安全通道",
        "quantity": 1.0
    },
    {
        "item": "ADVISA 办公室出图",
        "quantity": 1.0
    },
    {
        "item": "3D模型/效果图",
        "quantity": 1.0
    },
    {
        "item": "摄影造型",
        "quantity": 1.0
    },
    {
        "item": "Project Team (MR)",
        "quantity": 1.0
    },
    {
        "item": "撰写人",
        "quantity": 1.0
    },
    {
        "item": "Executive Architect",
        "quantity": 1.0
    },
    {
        "item": "房间数",
        "quantity": 1.0
    },
    {
        "item": "结构木工",
        "quantity": 1.0
    },
    {
        "item": "Architecture Collaborators",
        "quantity": 1.0
    },
    {
        "item": "Students from The Catholic University of America",
        "quantity": 1.0
    },
    {
        "item": "立面装饰",
        "quantity": 1.0
    },
    {
        "item": "剧场和照明设计",
        "quantity": 1.0
    },
    {
        "item": "Service Engineers",
        "quantity": 1.0
    },
    {
        "item": "作品",
        "quantity": 1.0
    },
    {
        "item": "Partners in Charge",
        "quantity": 1.0
    },
    {
        "item": "Director Gerencia e interventoria de obra",
        "quantity": 1.0
    },
    {
        "item": "家具商",
        "quantity": 1.0
    },
    {
        "item": "项目合作伙伴",
        "quantity": 1.0
    },
    {
        "item": "接待顾问",
        "quantity": 1.0
    },
    {
        "item": "预制混凝土",
        "quantity": 1.0
    },
    {
        "item": "Interiorismo",
        "quantity": 1.0
    },
    {
        "item": "Grafic design",
        "quantity": 1.0
    },
    {
        "item": "Interior Furnishings",
        "quantity": 1.0
    },
    {
        "item": "项目实施团队",
        "quantity": 1.0
    },
    {
        "item": "场地规划",
        "quantity": 1.0
    },
    {
        "item": "总投资 ",
        "quantity": 1.0
    },
    {
        "item": "装饰、照明、园艺、室内",
        "quantity": 1.0
    },
    {
        "item": "休息区家具",
        "quantity": 1.0
    },
    {
        "item": "功能咨询",
        "quantity": 1.0
    },
    {
        "item": "水平遮盖",
        "quantity": 1.0
    },
    {
        "item": "客户与实行者",
        "quantity": 1.0
    },
    {
        "item": "客户及建筑总包",
        "quantity": 1.0
    },
    {
        "item": "Scale Of Building",
        "quantity": 1.0
    },
    {
        "item": "Design Team Phase 2",
        "quantity": 1.0
    },
    {
        "item": "防风工程",
        "quantity": 1.0
    },
    {
        "item": "Electrical And Hydraulics Projects",
        "quantity": 1.0
    },
    {
        "item": "制造安装",
        "quantity": 1.0
    },
    {
        "item": "污水处理设施",
        "quantity": 1.0
    },
    {
        "item": "场地建设监督",
        "quantity": 1.0
    },
    {
        "item": "木工施工工程",
        "quantity": 1.0
    },
    {
        "item": "主要大样设计",
        "quantity": 1.0
    },
    {
        "item": "质量报告",
        "quantity": 1.0
    },
    {
        "item": "技术装置顾问",
        "quantity": 1.0
    },
    {
        "item": "房屋尺寸",
        "quantity": 1.0
    },
    {
        "item": "文化遗产顾问",
        "quantity": 1.0
    },
    {
        "item": "室外墙体保温与抹灰",
        "quantity": 1.0
    },
    {
        "item": "影剧院咨询",
        "quantity": 1.0
    },
    {
        "item": "配合",
        "quantity": 1.0
    },
    {
        "item": "Bamboo Consultant",
        "quantity": 1.0
    },
    {
        "item": "施工图合作团队",
        "quantity": 1.0
    },
    {
        "item": "尺寸标注",
        "quantity": 1.0
    },
    {
        "item": "环保",
        "quantity": 1.0
    },
    {
        "item": "责任建筑师团队",
        "quantity": 1.0
    },
    {
        "item": "建筑区域",
        "quantity": 1.0
    },
    {
        "item": "Answers in Genesis ",
        "quantity": 1.0
    },
    {
        "item": "ESI",
        "quantity": 1.0
    },
    {
        "item": "SOGEA SUD",
        "quantity": 1.0
    },
    {
        "item": "当地设计师",
        "quantity": 1.0
    },
    {
        "item": "Natuurpodium室内",
        "quantity": 1.0
    },
    {
        "item": "董事长",
        "quantity": 1.0
    },
    {
        "item": "工程测量及预算",
        "quantity": 1.0
    },
    {
        "item": "Project Architects/Designers",
        "quantity": 1.0
    },
    {
        "item": "基础包层，壁橱",
        "quantity": 1.0
    },
    {
        "item": "环保绘画设计",
        "quantity": 1.0
    },
    {
        "item": "室内及景观设计师",
        "quantity": 1.0
    },
    {
        "item": "地理位置",
        "quantity": 1.0
    },
    {
        "item": "理念设计",
        "quantity": 1.0
    },
    {
        "item": "机械/电器/水暖工程师",
        "quantity": 1.0
    },
    {
        "item": "项目主创团队",
        "quantity": 1.0
    },
    {
        "item": "项目 S l  (工程)",
        "quantity": 1.0
    },
    {
        "item": "建筑服务工程（电力） ",
        "quantity": 1.0
    },
    {
        "item": "外聘艺术家",
        "quantity": 1.0
    },
    {
        "item": "TADA 设计团队",
        "quantity": 1.0
    },
    {
        "item": "剧院规划",
        "quantity": 1.0
    },
    {
        "item": "Title 24 能耗标准审核",
        "quantity": 1.0
    },
    {
        "item": "社区参与与组织",
        "quantity": 1.0
    },
    {
        "item": "项目业主 ",
        "quantity": 1.0
    },
    {
        "item": "软体开发",
        "quantity": 1.0
    },
    {
        "item": "Electrical Engineers",
        "quantity": 1.0
    },
    {
        "item": "执行建筑师/工程师",
        "quantity": 1.0
    },
    {
        "item": "开发商/甲方",
        "quantity": 1.0
    },
    {
        "item": "建筑条例顾问",
        "quantity": 1.0
    },
    {
        "item": "环境管理",
        "quantity": 1.0
    },
    {
        "item": "设计/制造",
        "quantity": 1.0
    },
    {
        "item": "照明概念设计",
        "quantity": 1.0
    },
    {
        "item": "效果图表现",
        "quantity": 1.0
    },
    {
        "item": "平台",
        "quantity": 1.0
    },
    {
        "item": "Project Assistant",
        "quantity": 1.0
    },
    {
        "item": "设计工作室",
        "quantity": 1.0
    },
    {
        "item": "负责人&设计者",
        "quantity": 1.0
    },
    {
        "item": "可持续设计工程",
        "quantity": 1.0
    },
    {
        "item": "文化设计合作",
        "quantity": 1.0
    },
    {
        "item": "香港项目团队经理",
        "quantity": 1.0
    },
    {
        "item": "单元尺寸",
        "quantity": 1.0
    },
    {
        "item": "Creative Director ",
        "quantity": 1.0
    },
    {
        "item": "Electrical Infrastructures",
        "quantity": 1.0
    },
    {
        "item": "改造城堡的预算",
        "quantity": 1.0
    },
    {
        "item": "机械和管道工程",
        "quantity": 1.0
    },
    {
        "item": "Project team",
        "quantity": 1.0
    },
    {
        "item": "Legal Counsel",
        "quantity": 1.0
    },
    {
        "item": "Mechanical & Electrical Consultant",
        "quantity": 1.0
    },
    {
        "item": "被动式房屋认证",
        "quantity": 1.0
    },
    {
        "item": "大纲",
        "quantity": 1.0
    },
    {
        "item": "团队组长",
        "quantity": 1.0
    },
    {
        "item": "城市化和专业化",
        "quantity": 1.0
    },
    {
        "item": "通讯顾问",
        "quantity": 1.0
    },
    {
        "item": "Owner",
        "quantity": 1.0
    },
    {
        "item": "海洋结构工程",
        "quantity": 1.0
    },
    {
        "item": "施工方案",
        "quantity": 1.0
    },
    {
        "item": "Carpentry Supervisor",
        "quantity": 1.0
    },
    {
        "item": "照明设计 ",
        "quantity": 1.0
    },
    {
        "item": "建筑的协调员",
        "quantity": 1.0
    },
    {
        "item": "最终方案",
        "quantity": 1.0
    },
    {
        "item": "Hok Sport Architecture 团队",
        "quantity": 1.0
    },
    {
        "item": "Building Services",
        "quantity": 1.0
    },
    {
        "item": "楼面面积",
        "quantity": 1.0
    },
    {
        "item": "客户协作和顾问",
        "quantity": 1.0
    },
    {
        "item": "水电系统",
        "quantity": 1.0
    },
    {
        "item": "Associate Architects & Engineers",
        "quantity": 1.0
    },
    {
        "item": "模型2",
        "quantity": 1.0
    },
    {
        "item": "水力咨询",
        "quantity": 1.0
    },
    {
        "item": "Maximum Height Of The Building",
        "quantity": 1.0
    },
    {
        "item": "资金总额",
        "quantity": 1.0
    },
    {
        "item": "通讯系统顾问",
        "quantity": 1.0
    },
    {
        "item": "清洁顾问",
        "quantity": 1.0
    },
    {
        "item": "管理承包商",
        "quantity": 1.0
    },
    {
        "item": "项目管理/ 基地管理",
        "quantity": 1.0
    },
    {
        "item": "Facilities Design",
        "quantity": 1.0
    },
    {
        "item": "Theatre Design",
        "quantity": 1.0
    },
    {
        "item": "照片模型",
        "quantity": 1.0
    },
    {
        "item": "机电管道及消防工程师",
        "quantity": 1.0
    },
    {
        "item": "艺术顾问与协调",
        "quantity": 1.0
    },
    {
        "item": "现有条件调查",
        "quantity": 1.0
    },
    {
        "item": "Urban Planner and Cartography ",
        "quantity": 1.0
    },
    {
        "item": "协调和设计部门",
        "quantity": 1.0
    },
    {
        "item": "内部建设办公室",
        "quantity": 1.0
    },
    {
        "item": "户外终端",
        "quantity": 1.0
    },
    {
        "item": "文章编辑",
        "quantity": 1.0
    },
    {
        "item": "结构主管",
        "quantity": 1.0
    },
    {
        "item": "室内设计 (公共区域) ",
        "quantity": 1.0
    },
    {
        "item": "技术构架工程师",
        "quantity": 1.0
    },
    {
        "item": "空调系统设计",
        "quantity": 1.0
    },
    {
        "item": "系统建设",
        "quantity": 1.0
    },
    {
        "item": "沼气集水井",
        "quantity": 1.0
    },
    {
        "item": "室内划分",
        "quantity": 1.0
    },
    {
        "item": "委托代理",
        "quantity": 1.0
    },
    {
        "item": "电器承装商 ",
        "quantity": 1.0
    },
    {
        "item": "编辑及工作主导",
        "quantity": 1.0
    },
    {
        "item": "屋顶下面积",
        "quantity": 1.0
    },
    {
        "item": "机电工程设计",
        "quantity": 1.0
    },
    {
        "item": "规划与项目指导",
        "quantity": 1.0
    },
    {
        "item": "Key Personnel",
        "quantity": 1.0
    },
    {
        "item": "2021 2021",
        "quantity": 1.0
    },
    {
        "item": "Interior Design Co Authors",
        "quantity": 1.0
    },
    {
        "item": "MEP / 装置",
        "quantity": 1.0
    },
    {
        "item": "访问工程师",
        "quantity": 1.0
    },
    {
        "item": "设施提供",
        "quantity": 1.0
    },
    {
        "item": "Architects in charge",
        "quantity": 1.0
    },
    {
        "item": "景观设计   建造阶段",
        "quantity": 1.0
    },
    {
        "item": "液压工程顾问",
        "quantity": 1.0
    },
    {
        "item": "研发合作伙伴",
        "quantity": 1.0
    },
    {
        "item": "灯光解决",
        "quantity": 1.0
    },
    {
        "item": "Mep/Fp工程",
        "quantity": 1.0
    },
    {
        "item": "Structure system",
        "quantity": 1.0
    },
    {
        "item": "咨询团队",
        "quantity": 1.0
    },
    {
        "item": "剧场设备",
        "quantity": 1.0
    },
    {
        "item": "塑料水果箱外部尺寸",
        "quantity": 1.0
    },
    {
        "item": "暖通专业",
        "quantity": 1.0
    },
    {
        "item": "设计材料",
        "quantity": 1.0
    },
    {
        "item": "商标图案",
        "quantity": 1.0
    },
    {
        "item": "建筑服务工程",
        "quantity": 1.0
    },
    {
        "item": "结构及建筑承包商",
        "quantity": 1.0
    },
    {
        "item": "建筑面积  ",
        "quantity": 1.0
    },
    {
        "item": "标识系统设计",
        "quantity": 1.0
    },
    {
        "item": "城市开发",
        "quantity": 1.0
    },
    {
        "item": "酒店内部 (2013)",
        "quantity": 1.0
    },
    {
        "item": "面板优化",
        "quantity": 1.0
    },
    {
        "item": "项目联络方",
        "quantity": 1.0
    },
    {
        "item": "结构 / 土木",
        "quantity": 1.0
    },
    {
        "item": "机电承包商",
        "quantity": 1.0
    },
    {
        "item": "副建筑师和",
        "quantity": 1.0
    },
    {
        "item": "Civil Contractors",
        "quantity": 1.0
    },
    {
        "item": "施工现场督导",
        "quantity": 1.0
    },
    {
        "item": "竞赛组织方",
        "quantity": 1.0
    },
    {
        "item": "技术工程团队",
        "quantity": 1.0
    },
    {
        "item": "Mechanical/Electrical/Plumbing Engineer",
        "quantity": 1.0
    },
    {
        "item": "调试顾问",
        "quantity": 1.0
    },
    {
        "item": "锁艺",
        "quantity": 1.0
    },
    {
        "item": "设计师和主管",
        "quantity": 1.0
    },
    {
        "item": "机械电力工程",
        "quantity": 1.0
    },
    {
        "item": "MEP & 总承包商",
        "quantity": 1.0
    },
    {
        "item": "Superflex 负责人",
        "quantity": 1.0
    },
    {
        "item": "竞赛项目建筑师",
        "quantity": 1.0
    },
    {
        "item": "主要委托方",
        "quantity": 1.0
    },
    {
        "item": "树木顾问",
        "quantity": 1.0
    },
    {
        "item": "电气，安全&电梯工程",
        "quantity": 1.0
    },
    {
        "item": "当地照明设计",
        "quantity": 1.0
    },
    {
        "item": "迭戈建筑公司",
        "quantity": 1.0
    },
    {
        "item": "每户面积",
        "quantity": 1.0
    },
    {
        "item": "Plumber",
        "quantity": 1.0
    },
    {
        "item": "家具分包商",
        "quantity": 1.0
    },
    {
        "item": "酒店内部装饰",
        "quantity": 1.0
    },
    {
        "item": "支持建筑师",
        "quantity": 1.0
    },
    {
        "item": "土地工程师",
        "quantity": 1.0
    },
    {
        "item": "写字楼合作建筑师",
        "quantity": 1.0
    },
    {
        "item": "废物累计吨/累计万吨垃圾",
        "quantity": 1.0
    },
    {
        "item": "垂直运输",
        "quantity": 1.0
    },
    {
        "item": "现场监理和",
        "quantity": 1.0
    },
    {
        "item": "Studio Name",
        "quantity": 1.0
    },
    {
        "item": "主控室",
        "quantity": 1.0
    },
    {
        "item": "水文和电气",
        "quantity": 1.0
    },
    {
        "item": "项目区",
        "quantity": 1.0
    },
    {
        "item": "照明制造商和应用列表",
        "quantity": 1.0
    },
    {
        "item": "工作人员",
        "quantity": 1.0
    },
    {
        "item": "Design Period",
        "quantity": 1.0
    },
    {
        "item": "能效顾问",
        "quantity": 1.0
    },
    {
        "item": "扎哈·哈迪德竞赛团队",
        "quantity": 1.0
    },
    {
        "item": "设计执行",
        "quantity": 1.0
    },
    {
        "item": "创意团队",
        "quantity": 1.0
    },
    {
        "item": "环境设计工作室",
        "quantity": 1.0
    },
    {
        "item": "汇报",
        "quantity": 1.0
    },
    {
        "item": "地理技术",
        "quantity": 1.0
    },
    {
        "item": "模块家具承包商",
        "quantity": 1.0
    },
    {
        "item": "基座建筑机械工程师",
        "quantity": 1.0
    },
    {
        "item": "花费估算师",
        "quantity": 1.0
    },
    {
        "item": "森林大火服务",
        "quantity": 1.0
    },
    {
        "item": "设计，现场管理",
        "quantity": 1.0
    },
    {
        "item": "建筑产品",
        "quantity": 1.0
    },
    {
        "item": "商业概念",
        "quantity": 1.0
    },
    {
        "item": "BIM",
        "quantity": 1.0
    },
    {
        "item": "木质工程",
        "quantity": 1.0
    },
    {
        "item": "Stone-restorer",
        "quantity": 1.0
    },
    {
        "item": "Picture-restorer",
        "quantity": 1.0
    },
    {
        "item": "SCMC",
        "quantity": 1.0
    },
    {
        "item": "底层结构分析",
        "quantity": 1.0
    },
    {
        "item": "Schematic design and PII",
        "quantity": 1.0
    },
    {
        "item": "建构工程师",
        "quantity": 1.0
    },
    {
        "item": "表面面积",
        "quantity": 1.0
    },
    {
        "item": "Main Diagnostician Coordinator",
        "quantity": 1.0
    },
    {
        "item": "总建筑容积面积",
        "quantity": 1.0
    },
    {
        "item": "布局工程",
        "quantity": 1.0
    },
    {
        "item": "实业顾问",
        "quantity": 1.0
    },
    {
        "item": "本地合作方",
        "quantity": 1.0
    },
    {
        "item": "座席面积",
        "quantity": 1.0
    },
    {
        "item": "Client/Owner",
        "quantity": 1.0
    },
    {
        "item": "Design Team, Phase 3",
        "quantity": 1.0
    },
    {
        "item": "照明顾问(公司名称)",
        "quantity": 1.0
    },
    {
        "item": "质检",
        "quantity": 1.0
    },
    {
        "item": "立面照明",
        "quantity": 1.0
    },
    {
        "item": "技术配合",
        "quantity": 1.0
    },
    {
        "item": "LEED 绿色建筑认证顾问",
        "quantity": 1.0
    },
    {
        "item": "结构工程师/外墙建筑顾问",
        "quantity": 1.0
    },
    {
        "item": "Project Management Assistance",
        "quantity": 1.0
    },
    {
        "item": "安全协助",
        "quantity": 1.0
    },
    {
        "item": "Steel structure/metal roofing consultants",
        "quantity": 1.0
    },
    {
        "item": "行政协调",
        "quantity": 1.0
    },
    {
        "item": "Total Floor Space",
        "quantity": 1.0
    },
    {
        "item": "特约建筑师",
        "quantity": 1.0
    },
    {
        "item": "树脂",
        "quantity": 1.0
    },
    {
        "item": "质量标准",
        "quantity": 1.0
    },
    {
        "item": "总露台面积",
        "quantity": 1.0
    },
    {
        "item": "Glass Mosaic Restorer",
        "quantity": 1.0
    },
    {
        "item": "馆藏顾问",
        "quantity": 1.0
    },
    {
        "item": "石材顾问",
        "quantity": 1.0
    },
    {
        "item": "结构与装置",
        "quantity": 1.0
    },
    {
        "item": "主要家具提供商",
        "quantity": 1.0
    },
    {
        "item": "Engineering Structures",
        "quantity": 1.0
    },
    {
        "item": "主持合伙人（预设计）",
        "quantity": 1.0
    },
    {
        "item": "业主与赞助商",
        "quantity": 1.0
    },
    {
        "item": "室内设计   会议室",
        "quantity": 1.0
    },
    {
        "item": "保护",
        "quantity": 1.0
    },
    {
        "item": "木匠工艺",
        "quantity": 1.0
    },
    {
        "item": "结构框架",
        "quantity": 1.0
    },
    {
        "item": "地面工程师",
        "quantity": 1.0
    },
    {
        "item": "立面改造预算",
        "quantity": 1.0
    },
    {
        "item": "大楼服务工程师,ESD顾问",
        "quantity": 1.0
    },
    {
        "item": "电承包商",
        "quantity": 1.0
    },
    {
        "item": "紧固解决方案/螺丝",
        "quantity": 1.0
    },
    {
        "item": "室内模型",
        "quantity": 1.0
    },
    {
        "item": "合作负责者",
        "quantity": 1.0
    },
    {
        "item": "水景观设计顾问",
        "quantity": 1.0
    },
    {
        "item": "建筑设计主管",
        "quantity": 1.0
    },
    {
        "item": "语音和数据",
        "quantity": 1.0
    },
    {
        "item": "电力能源生产/电能生产",
        "quantity": 1.0
    },
    {
        "item": "Building Foot Print",
        "quantity": 1.0
    },
    {
        "item": "发起者/业主",
        "quantity": 1.0
    },
    {
        "item": "可待续设计",
        "quantity": 1.0
    },
    {
        "item": "Acustic Consultants",
        "quantity": 1.0
    },
    {
        "item": "规划建筑承包商",
        "quantity": 1.0
    },
    {
        "item": "承包商/建造商",
        "quantity": 1.0
    },
    {
        "item": "Caixilhos",
        "quantity": 1.0
    },
    {
        "item": "控制室",
        "quantity": 1.0
    },
    {
        "item": "顶棚密封顾问工程师",
        "quantity": 1.0
    },
    {
        "item": "建筑图纸",
        "quantity": 1.0
    },
    {
        "item": "湿地（新的生态系统）",
        "quantity": 1.0
    },
    {
        "item": "竖向交通",
        "quantity": 1.0
    },
    {
        "item": "Contractor, Wood",
        "quantity": 1.0
    },
    {
        "item": "幕墙建筑师",
        "quantity": 1.0
    },
    {
        "item": "钢承包商",
        "quantity": 1.0
    },
    {
        "item": "现场团队",
        "quantity": 1.0
    },
    {
        "item": "餐厅家具提供",
        "quantity": 1.0
    },
    {
        "item": "多功能厅 & 图书馆项目负责人",
        "quantity": 1.0
    },
    {
        "item": "探测",
        "quantity": 1.0
    },
    {
        "item": "进程监理",
        "quantity": 1.0
    },
    {
        "item": "GHD 团队",
        "quantity": 1.0
    },
    {
        "item": "Consultant",
        "quantity": 1.0
    },
    {
        "item": "Superficie terreno",
        "quantity": 1.0
    },
    {
        "item": "结构工程 ",
        "quantity": 1.0
    },
    {
        "item": "竞标",
        "quantity": 1.0
    },
    {
        "item": "旋转和飞行模型顾问",
        "quantity": 1.0
    },
    {
        "item": "屏蔽设施",
        "quantity": 1.0
    },
    {
        "item": "高性能设计",
        "quantity": 1.0
    },
    {
        "item": "主要联系人",
        "quantity": 1.0
    },
    {
        "item": "合作代理机构员工",
        "quantity": 1.0
    },
    {
        "item": "空调制暖工程师",
        "quantity": 1.0
    },
    {
        "item": "Electrical & Mechanical Engineering",
        "quantity": 1.0
    },
    {
        "item": "土木和结构工程",
        "quantity": 1.0
    },
    {
        "item": "混凝土",
        "quantity": 1.0
    },
    {
        "item": "电气照明承包商",
        "quantity": 1.0
    },
    {
        "item": "建筑工程顾问",
        "quantity": 1.0
    },
    {
        "item": "执行主管",
        "quantity": 1.0
    },
    {
        "item": "Flower design",
        "quantity": 1.0
    },
    {
        "item": "景观建筑史",
        "quantity": 1.0
    },
    {
        "item": "住宅热工管理",
        "quantity": 1.0
    },
    {
        "item": "机械/电气/管道工程师",
        "quantity": 1.0
    },
    {
        "item": "设计理念新入口大楼",
        "quantity": 1.0
    },
    {
        "item": "独立承包商",
        "quantity": 1.0
    },
    {
        "item": "Furniture Designer ",
        "quantity": 1.0
    },
    {
        "item": "建造物理",
        "quantity": 1.0
    },
    {
        "item": "Ziss工作室团队",
        "quantity": 1.0
    },
    {
        "item": "机械/土木工程师",
        "quantity": 1.0
    },
    {
        "item": "建筑物理咨询",
        "quantity": 1.0
    },
    {
        "item": "Structure Designer ",
        "quantity": 1.0
    },
    {
        "item": "功能照明",
        "quantity": 1.0
    },
    {
        "item": "品鉴室家具和灯具定制",
        "quantity": 1.0
    },
    {
        "item": "预算(M&E)",
        "quantity": 1.0
    },
    {
        "item": "暖通控制顾问",
        "quantity": 1.0
    },
    {
        "item": "事务设计",
        "quantity": 1.0
    },
    {
        "item": "塑料水果箱材料",
        "quantity": 1.0
    },
    {
        "item": "Lighting Consultants",
        "quantity": 1.0
    },
    {
        "item": "多功能绿植山坡",
        "quantity": 1.0
    },
    {
        "item": "方案设计师",
        "quantity": 1.0
    },
    {
        "item": "通信工程",
        "quantity": 1.0
    },
    {
        "item": "承包商 / 项目管理",
        "quantity": 1.0
    },
    {
        "item": "生态墙咨询",
        "quantity": 1.0
    },
    {
        "item": "自动化顾问",
        "quantity": 1.0
    },
    {
        "item": "结构，机械和电气设计",
        "quantity": 1.0
    },
    {
        "item": "设计师，建筑师和艺术家",
        "quantity": 1.0
    },
    {
        "item": "规范咨询商",
        "quantity": 1.0
    },
    {
        "item": "声学专家",
        "quantity": 1.0
    },
    {
        "item": "主创建筑",
        "quantity": 1.0
    },
    {
        "item": "音乐厅设计团队",
        "quantity": 1.0
    },
    {
        "item": "建筑估算师",
        "quantity": 1.0
    },
    {
        "item": "是室内设计师",
        "quantity": 1.0
    },
    {
        "item": "Gmp 巴西代表处总监",
        "quantity": 1.0
    },
    {
        "item": "生产队",
        "quantity": 1.0
    },
    {
        "item": "最终造价",
        "quantity": 1.0
    },
    {
        "item": "M&E机电工程",
        "quantity": 1.0
    },
    {
        "item": "Civil",
        "quantity": 1.0
    },
    {
        "item": "商业",
        "quantity": 1.0
    },
    {
        "item": "质检单位（机电）",
        "quantity": 1.0
    },
    {
        "item": "M&E/节能",
        "quantity": 1.0
    },
    {
        "item": "Landscape architecture",
        "quantity": 1.0
    },
    {
        "item": "建设用地",
        "quantity": 1.0
    },
    {
        "item": "原有建筑师",
        "quantity": 1.0
    },
    {
        "item": "Local Structural Engineer",
        "quantity": 1.0
    },
    {
        "item": "剧场声学",
        "quantity": 1.0
    },
    {
        "item": "建造/施工",
        "quantity": 1.0
    },
    {
        "item": "清理评估合作方",
        "quantity": 1.0
    },
    {
        "item": "主要建筑面积",
        "quantity": 1.0
    },
    {
        "item": "户外设施，园林绿化",
        "quantity": 1.0
    },
    {
        "item": "Project Designer",
        "quantity": 1.0
    },
    {
        "item": "Height of Pylon",
        "quantity": 1.0
    },
    {
        "item": "机械、电气、通讯、安全、声学、防火及水力",
        "quantity": 1.0
    },
    {
        "item": "Ingenería Estructural",
        "quantity": 1.0
    },
    {
        "item": "景观事务所",
        "quantity": 1.0
    },
    {
        "item": "金属立面制造商",
        "quantity": 1.0
    },
    {
        "item": "门厅家具",
        "quantity": 1.0
    },
    {
        "item": "ZHA 项目建筑师",
        "quantity": 1.0
    },
    {
        "item": "游乐设备设计师",
        "quantity": 1.0
    },
    {
        "item": "集装箱房生产及装修",
        "quantity": 1.0
    },
    {
        "item": "团队1997-2001(50% SD)",
        "quantity": 1.0
    },
    {
        "item": "Soil Mechanics",
        "quantity": 1.0
    },
    {
        "item": "客户／工程管理",
        "quantity": 1.0
    },
    {
        "item": "合计团队",
        "quantity": 1.0
    },
    {
        "item": "艺术嵌板",
        "quantity": 1.0
    },
    {
        "item": "洁具工程师",
        "quantity": 1.0
    },
    {
        "item": "项目设计总监",
        "quantity": 1.0
    },
    {
        "item": "HQE顾问",
        "quantity": 1.0
    },
    {
        "item": "合作研究",
        "quantity": 1.0
    },
    {
        "item": "墙面计划",
        "quantity": 1.0
    },
    {
        "item": "LEED, 光伏设备顾问",
        "quantity": 1.0
    },
    {
        "item": "工程细部",
        "quantity": 1.0
    },
    {
        "item": "Acoustical Design ",
        "quantity": 1.0
    },
    {
        "item": "自行车道",
        "quantity": 1.0
    },
    {
        "item": "机场规划建筑师",
        "quantity": 1.0
    },
    {
        "item": "遗产建筑师",
        "quantity": 1.0
    },
    {
        "item": "结构工程师/卫生工程师",
        "quantity": 1.0
    },
    {
        "item": "材料赞助（按字母顺序排列）",
        "quantity": 1.0
    },
    {
        "item": "总指导",
        "quantity": 1.0
    },
    {
        "item": "能源管理",
        "quantity": 1.0
    },
    {
        "item": "结构水利工程",
        "quantity": 1.0
    },
    {
        "item": "立面板艺术家",
        "quantity": 1.0
    },
    {
        "item": "领导项目建筑师",
        "quantity": 1.0
    },
    {
        "item": "David Chipperfield Architects Team",
        "quantity": 1.0
    },
    {
        "item": "环境系统",
        "quantity": 1.0
    },
    {
        "item": "温室气体排放减少",
        "quantity": 1.0
    },
    {
        "item": "喷泉顾问",
        "quantity": 1.0
    },
    {
        "item": "Promoter / Client",
        "quantity": 1.0
    },
    {
        "item": "Funnel Structure",
        "quantity": 1.0
    },
    {
        "item": "流体专业顾问",
        "quantity": 1.0
    },
    {
        "item": "项目规划团队负责人",
        "quantity": 1.0
    },
    {
        "item": "展览会场设计和管理",
        "quantity": 1.0
    },
    {
        "item": "项目区域",
        "quantity": 1.0
    },
    {
        "item": "商标设计",
        "quantity": 1.0
    },
    {
        "item": "国外承包商",
        "quantity": 1.0
    },
    {
        "item": "结构、服务、火",
        "quantity": 1.0
    },
    {
        "item": "资深设计建筑师",
        "quantity": 1.0
    },
    {
        "item": "Art on the Construction",
        "quantity": 1.0
    },
    {
        "item": "滑板公园",
        "quantity": 1.0
    },
    {
        "item": "场地勘测",
        "quantity": 1.0
    },
    {
        "item": "实体建造",
        "quantity": 1.0
    },
    {
        "item": "Webcor建设团队, 总承包商",
        "quantity": 1.0
    },
    {
        "item": "能源供应的工程师",
        "quantity": 1.0
    },
    {
        "item": "KPMB 建筑事务所项目团队",
        "quantity": 1.0
    },
    {
        "item": "防护措施",
        "quantity": 1.0
    },
    {
        "item": "Window System",
        "quantity": 1.0
    },
    {
        "item": "Mechanical Engineering",
        "quantity": 1.0
    },
    {
        "item": "勘测员",
        "quantity": 1.0
    },
    {
        "item": "南面横梁",
        "quantity": 1.0
    },
    {
        "item": "價格",
        "quantity": 1.0
    },
    {
        "item": "项目中使用的产品",
        "quantity": 1.0
    },
    {
        "item": "技术助理",
        "quantity": 1.0
    },
    {
        "item": "外观设计工程师",
        "quantity": 1.0
    },
    {
        "item": "综合管理",
        "quantity": 1.0
    },
    {
        "item": "项目管理/成本和现场管理",
        "quantity": 1.0
    },
    {
        "item": "系统供货商",
        "quantity": 1.0
    },
    {
        "item": "流体设计师",
        "quantity": 1.0
    },
    {
        "item": "Cooper Robertson 项目经理",
        "quantity": 1.0
    },
    {
        "item": "Construction Cost",
        "quantity": 1.0
    },
    {
        "item": "EKA 工作室",
        "quantity": 1.0
    },
    {
        "item": "研究项目管理",
        "quantity": 1.0
    },
    {
        "item": "室内建筑师 SIO",
        "quantity": 1.0
    },
    {
        "item": "助理景观设计",
        "quantity": 1.0
    },
    {
        "item": "竞赛项目领导",
        "quantity": 1.0
    },
    {
        "item": "Branded Environments Principal",
        "quantity": 1.0
    },
    {
        "item": "建筑外围结构工程",
        "quantity": 1.0
    },
    {
        "item": "室内概念",
        "quantity": 1.0
    },
    {
        "item": "建筑结构师",
        "quantity": 1.0
    },
    {
        "item": "声学顾问，建筑物理学，可持续性和消防安全",
        "quantity": 1.0
    },
    {
        "item": "展陈概念",
        "quantity": 1.0
    },
    {
        "item": "热环境",
        "quantity": 1.0
    },
    {
        "item": "Año",
        "quantity": 1.0
    },
    {
        "item": "发起者",
        "quantity": 1.0
    },
    {
        "item": "UPTK， 利耶帕亚",
        "quantity": 1.0
    },
    {
        "item": "主持",
        "quantity": 1.0
    },
    {
        "item": "Architect On Site",
        "quantity": 1.0
    },
    {
        "item": "M＆E顾问",
        "quantity": 1.0
    },
    {
        "item": "首席",
        "quantity": 1.0
    },
    {
        "item": "设计团队（零壹城市）",
        "quantity": 1.0
    },
    {
        "item": "装饰面积",
        "quantity": 1.0
    },
    {
        "item": " Arquitectos de proyecto",
        "quantity": 1.0
    },
    {
        "item": "使用建筑面积",
        "quantity": 1.0
    },
    {
        "item": "联合融资",
        "quantity": 1.0
    },
    {
        "item": "高级产品设计",
        "quantity": 1.0
    },
    {
        "item": "灯光概念设计",
        "quantity": 1.0
    },
    {
        "item": "Structure Consultant",
        "quantity": 1.0
    },
    {
        "item": "建筑师新团队",
        "quantity": 1.0
    },
    {
        "item": "Technical inspector and engineering",
        "quantity": 1.0
    },
    {
        "item": "技术建筑师合作者",
        "quantity": 1.0
    },
    {
        "item": " 给排水",
        "quantity": 1.0
    },
    {
        "item": "机械电气咨询",
        "quantity": 1.0
    },
    {
        "item": "Structural Engineer ",
        "quantity": 1.0
    },
    {
        "item": "技术工程公司",
        "quantity": 1.0
    },
    {
        "item": "Contractor Team",
        "quantity": 1.0
    },
    {
        "item": "项目与技术定位",
        "quantity": 1.0
    },
    {
        "item": "服务分包商",
        "quantity": 1.0
    },
    {
        "item": "现场面积",
        "quantity": 1.0
    },
    {
        "item": "项目团队（发展设计）",
        "quantity": 1.0
    },
    {
        "item": "初始建筑师",
        "quantity": 1.0
    },
    {
        "item": "M+E 工程",
        "quantity": 1.0
    },
    {
        "item": "音乐厅预算",
        "quantity": 1.0
    },
    {
        "item": "数字化项目团队",
        "quantity": 1.0
    },
    {
        "item": "立面/室外/结构/景观",
        "quantity": 1.0
    },
    {
        "item": "防火安全顾问",
        "quantity": 1.0
    },
    {
        "item": "装饰工程造价师",
        "quantity": 1.0
    },
    {
        "item": "餐桌设计",
        "quantity": 1.0
    },
    {
        "item": "Services",
        "quantity": 1.0
    },
    {
        "item": "场地清理",
        "quantity": 1.0
    },
    {
        "item": "混凝土承包商",
        "quantity": 1.0
    },
    {
        "item": "泥灰",
        "quantity": 1.0
    },
    {
        "item": "技术经理",
        "quantity": 1.0
    },
    {
        "item": "援助",
        "quantity": 1.0
    },
    {
        "item": "Consulting Structural And Civil Engineers",
        "quantity": 1.0
    },
    {
        "item": "石匠 石雕天使",
        "quantity": 1.0
    },
    {
        "item": "Engineerings",
        "quantity": 1.0
    },
    {
        "item": "Ecosystem",
        "quantity": 1.0
    },
    {
        "item": "Mechanical And Electrical Engineer",
        "quantity": 1.0
    },
    {
        "item": "塑料水果箱内部尺寸",
        "quantity": 1.0
    },
    {
        "item": "电力和通讯",
        "quantity": 1.0
    },
    {
        "item": "ESD 工程师（方案设计）",
        "quantity": 1.0
    },
    {
        "item": "委托",
        "quantity": 1.0
    },
    {
        "item": "合作建筑团队",
        "quantity": 1.0
    },
    {
        "item": "展品设计师",
        "quantity": 1.0
    },
    {
        "item": "动画制作",
        "quantity": 1.0
    },
    {
        "item": "3D 制作",
        "quantity": 1.0
    },
    {
        "item": "结构建议",
        "quantity": 1.0
    },
    {
        "item": "胶合结构设计",
        "quantity": 1.0
    },
    {
        "item": "管理顾问",
        "quantity": 1.0
    },
    {
        "item": "顾问规划师",
        "quantity": 1.0
    },
    {
        "item": "参赛建筑师",
        "quantity": 1.0
    },
    {
        "item": "Project Directors",
        "quantity": 1.0
    },
    {
        "item": "图形支持",
        "quantity": 1.0
    },
    {
        "item": "Partners In Charge",
        "quantity": 1.0
    },
    {
        "item": "植被与树艺",
        "quantity": 1.0
    },
    {
        "item": "CAD与三维设计",
        "quantity": 1.0
    },
    {
        "item": "建筑师展览",
        "quantity": 1.0
    },
    {
        "item": "工程解决",
        "quantity": 1.0
    },
    {
        "item": "艺术领导",
        "quantity": 1.0
    },
    {
        "item": "工程环境质量",
        "quantity": 1.0
    },
    {
        "item": "b720 Team",
        "quantity": 1.0
    },
    {
        "item": "Architect in Charged ",
        "quantity": 1.0
    },
    {
        "item": "记录建筑师 (公司名称)",
        "quantity": 1.0
    },
    {
        "item": "项目建设它的",
        "quantity": 1.0
    },
    {
        "item": "预计完工时间",
        "quantity": 1.0
    },
    {
        "item": "分承包方 ",
        "quantity": 1.0
    },
    {
        "item": "设计图",
        "quantity": 1.0
    },
    {
        "item": "WTB安装",
        "quantity": 1.0
    },
    {
        "item": "家具/照明",
        "quantity": 1.0
    },
    {
        "item": "工程预算员",
        "quantity": 1.0
    },
    {
        "item": "建筑设计总负责人",
        "quantity": 1.0
    },
    {
        "item": "艺术整合",
        "quantity": 1.0
    },
    {
        "item": "地质工程师",
        "quantity": 1.0
    },
    {
        "item": "HEQ环保设计",
        "quantity": 1.0
    },
    {
        "item": "防火保护工程师",
        "quantity": 1.0
    },
    {
        "item": "结构工程师   木材",
        "quantity": 1.0
    },
    {
        "item": "HPAC设计师",
        "quantity": 1.0
    },
    {
        "item": "Fundaciones",
        "quantity": 1.0
    },
    {
        "item": "绿植屋顶&雨水收集",
        "quantity": 1.0
    },
    {
        "item": "台面",
        "quantity": 1.0
    },
    {
        "item": "建成区域",
        "quantity": 1.0
    },
    {
        "item": "图示",
        "quantity": 1.0
    },
    {
        "item": "项目经理 & Qs",
        "quantity": 1.0
    },
    {
        "item": "主建造商",
        "quantity": 1.0
    },
    {
        "item": "基础规划",
        "quantity": 1.0
    },
    {
        "item": "电力基础设施",
        "quantity": 1.0
    },
    {
        "item": "Project And Site Supervisor",
        "quantity": 1.0
    },
    {
        "item": "机电及管道工程",
        "quantity": 1.0
    },
    {
        "item": "主持建筑师和室内设计",
        "quantity": 1.0
    },
    {
        "item": "定量调查",
        "quantity": 1.0
    },
    {
        "item": "Superflex 项目组长",
        "quantity": 1.0
    },
    {
        "item": "辐射热",
        "quantity": 1.0
    },
    {
        "item": " 设计团队",
        "quantity": 1.0
    },
    {
        "item": "结构工程和土木工程",
        "quantity": 1.0
    },
    {
        "item": "导航顾问",
        "quantity": 1.0
    },
    {
        "item": "施工主导",
        "quantity": 1.0
    },
    {
        "item": "BIG 设计团队",
        "quantity": 1.0
    },
    {
        "item": "家具制造人员",
        "quantity": 1.0
    },
    {
        "item": "国际结构",
        "quantity": 1.0
    },
    {
        "item": "五专",
        "quantity": 1.0
    },
    {
        "item": "策划顾问",
        "quantity": 1.0
    },
    {
        "item": "Acoustical Engineer",
        "quantity": 1.0
    },
    {
        "item": "液压工程",
        "quantity": 1.0
    },
    {
        "item": "舞台设备",
        "quantity": 1.0
    },
    {
        "item": "技术建筑师 ",
        "quantity": 1.0
    },
    {
        "item": "Environmental Engineer",
        "quantity": 1.0
    },
    {
        "item": "声乐顾问",
        "quantity": 1.0
    },
    {
        "item": "主要生产厂商",
        "quantity": 1.0
    },
    {
        "item": "民事顾问",
        "quantity": 1.0
    },
    {
        "item": "建筑、室内设计",
        "quantity": 1.0
    },
    {
        "item": "视听工程师",
        "quantity": 1.0
    },
    {
        "item": "项目任务",
        "quantity": 1.0
    },
    {
        "item": "空调设备",
        "quantity": 1.0
    },
    {
        "item": "Gabriels 环境",
        "quantity": 1.0
    },
    {
        "item": "施工方设计所",
        "quantity": 1.0
    },
    {
        "item": "Technical Engineer",
        "quantity": 1.0
    },
    {
        "item": "大楼服务工程师",
        "quantity": 1.0
    },
    {
        "item": "项目负责设计师",
        "quantity": 1.0
    },
    {
        "item": "结构和服务",
        "quantity": 1.0
    },
    {
        "item": "结构协调",
        "quantity": 1.0
    },
    {
        "item": "建成区",
        "quantity": 1.0
    },
    {
        "item": "协同",
        "quantity": 1.0
    },
    {
        "item": "计算机图像设计",
        "quantity": 1.0
    },
    {
        "item": "扎哈事务所项目团队",
        "quantity": 1.0
    },
    {
        "item": "项目团队（设计与制作）",
        "quantity": 1.0
    },
    {
        "item": "材质",
        "quantity": 1.0
    },
    {
        "item": "机械与电工程师",
        "quantity": 1.0
    },
    {
        "item": "安全保证",
        "quantity": 1.0
    },
    {
        "item": "展览供应商",
        "quantity": 1.0
    },
    {
        "item": "Poland",
        "quantity": 1.0
    },
    {
        "item": "建筑与开放空间",
        "quantity": 1.0
    },
    {
        "item": "排湿",
        "quantity": 1.0
    },
    {
        "item": "实用面积",
        "quantity": 1.0
    },
    {
        "item": "综合布线",
        "quantity": 1.0
    },
    {
        "item": "General contractor",
        "quantity": 1.0
    },
    {
        "item": "建设监督",
        "quantity": 1.0
    },
    {
        "item": "博物馆机械工程师",
        "quantity": 1.0
    },
    {
        "item": "高压电",
        "quantity": 1.0
    },
    {
        "item": "建筑工作室经理",
        "quantity": 1.0
    },
    {
        "item": "施工技术员/雇主的代理人",
        "quantity": 1.0
    },
    {
        "item": "酒店大堂室内设计",
        "quantity": 1.0
    },
    {
        "item": "机电咨询工程师",
        "quantity": 1.0
    },
    {
        "item": "IEA 建筑设计团队",
        "quantity": 1.0
    },
    {
        "item": "会议室",
        "quantity": 1.0
    },
    {
        "item": "主结构系统",
        "quantity": 1.0
    },
    {
        "item": "承包商/制造商",
        "quantity": 1.0
    },
    {
        "item": "Renderings",
        "quantity": 1.0
    },
    {
        "item": "T1+1面积",
        "quantity": 1.0
    },
    {
        "item": "厨房设施",
        "quantity": 1.0
    },
    {
        "item": "职员",
        "quantity": 1.0
    },
    {
        "item": "剧院/AV",
        "quantity": 1.0
    },
    {
        "item": "协作与建造",
        "quantity": 1.0
    },
    {
        "item": "深化设计",
        "quantity": 1.0
    },
    {
        "item": "建筑工作室",
        "quantity": 1.0
    },
    {
        "item": "Sondagens",
        "quantity": 1.0
    },
    {
        "item": "Interior And Landscape Architect",
        "quantity": 1.0
    },
    {
        "item": "ZHA 总监",
        "quantity": 1.0
    },
    {
        "item": "可持续发展工程师",
        "quantity": 1.0
    },
    {
        "item": "数量监测",
        "quantity": 1.0
    },
    {
        "item": "设施计算",
        "quantity": 1.0
    },
    {
        "item": "建筑合伙人",
        "quantity": 1.0
    },
    {
        "item": "ALMA ",
        "quantity": 1.0
    },
    {
        "item": "建筑师和建造团队",
        "quantity": 1.0
    },
    {
        "item": "改变面积",
        "quantity": 1.0
    },
    {
        "item": "土木施工",
        "quantity": 1.0
    },
    {
        "item": "外墙材料",
        "quantity": 1.0
    },
    {
        "item": "Stylism",
        "quantity": 1.0
    },
    {
        "item": "外观 设计",
        "quantity": 1.0
    },
    {
        "item": "外围护顾问",
        "quantity": 1.0
    },
    {
        "item": "美工师",
        "quantity": 1.0
    },
    {
        "item": "Interior design",
        "quantity": 1.0
    },
    {
        "item": "绿色建筑",
        "quantity": 1.0
    },
    {
        "item": "Feltrinelli Porta Volta 建筑表皮面积",
        "quantity": 1.0
    },
    {
        "item": "Map Arquitectos Team",
        "quantity": 1.0
    },
    {
        "item": "草甸顾问",
        "quantity": 1.0
    },
    {
        "item": "M-塔楼",
        "quantity": 1.0
    },
    {
        "item": "架构",
        "quantity": 1.0
    },
    {
        "item": "室内设计与装饰",
        "quantity": 1.0
    },
    {
        "item": "主项目建筑师",
        "quantity": 1.0
    },
    {
        "item": "生物气集合",
        "quantity": 1.0
    },
    {
        "item": "设计咨询公司",
        "quantity": 1.0
    },
    {
        "item": "Design Team ",
        "quantity": 1.0
    },
    {
        "item": "海拔高度",
        "quantity": 1.0
    },
    {
        "item": "效果图经理",
        "quantity": 1.0
    },
    {
        "item": "品牌和平面设计",
        "quantity": 1.0
    },
    {
        "item": "项目系统",
        "quantity": 1.0
    },
    {
        "item": "MEP ",
        "quantity": 1.0
    },
    {
        "item": "住宅布局",
        "quantity": 1.0
    },
    {
        "item": "Artists, Integrated Artwork",
        "quantity": 1.0
    },
    {
        "item": "声学音响设计",
        "quantity": 1.0
    },
    {
        "item": "幕墙分包商",
        "quantity": 1.0
    },
    {
        "item": "草图与渲染",
        "quantity": 1.0
    },
    {
        "item": "建筑师工程师（初步设计）",
        "quantity": 1.0
    },
    {
        "item": "工程助理",
        "quantity": 1.0
    },
    {
        "item": "规格描述",
        "quantity": 1.0
    },
    {
        "item": "设计与建造主承包商",
        "quantity": 1.0
    },
    {
        "item": "室内家具设计",
        "quantity": 1.0
    },
    {
        "item": "导引系统",
        "quantity": 1.0
    },
    {
        "item": "MEP/Fire Protection Engineers",
        "quantity": 1.0
    },
    {
        "item": "内容",
        "quantity": 1.0
    },
    {
        "item": "施工价值",
        "quantity": 1.0
    },
    {
        "item": "图像灵感来源",
        "quantity": 1.0
    },
    {
        "item": "安全与健康设计",
        "quantity": 1.0
    },
    {
        "item": "纲要管理",
        "quantity": 1.0
    },
    {
        "item": "录音室和声环境",
        "quantity": 1.0
    },
    {
        "item": "Sound",
        "quantity": 1.0
    },
    {
        "item": "Preliminary work (art history)",
        "quantity": 1.0
    },
    {
        "item": "建筑结构设计",
        "quantity": 1.0
    },
    {
        "item": "合资方",
        "quantity": 1.0
    },
    {
        "item": "Local MEP Engineers",
        "quantity": 1.0
    },
    {
        "item": "能源消耗",
        "quantity": 1.0
    },
    {
        "item": "配电",
        "quantity": 1.0
    },
    {
        "item": "街道灯光技术",
        "quantity": 1.0
    },
    {
        "item": "MVRDV",
        "quantity": 1.0
    },
    {
        "item": "Markentreprenör",
        "quantity": 1.0
    },
    {
        "item": "竞赛类型",
        "quantity": 1.0
    },
    {
        "item": "负责设计师",
        "quantity": 1.0
    },
    {
        "item": "项目团队 (Patkau Architects): ",
        "quantity": 1.0
    },
    {
        "item": "建设经理/建造者",
        "quantity": 1.0
    },
    {
        "item": "经济分析",
        "quantity": 1.0
    },
    {
        "item": "造价专家",
        "quantity": 1.0
    },
    {
        "item": "总建筑空间  ",
        "quantity": 1.0
    },
    {
        "item": "L’Atelier建筑事务所",
        "quantity": 1.0
    },
    {
        "item": "驻场建筑师/项目管理",
        "quantity": 1.0
    },
    {
        "item": "人权展览策展人",
        "quantity": 1.0
    },
    {
        "item": "理念/建筑师领导/设计师",
        "quantity": 1.0
    },
    {
        "item": "外部空间区域",
        "quantity": 1.0
    },
    {
        "item": "Qs And Cdm Coordinator",
        "quantity": 1.0
    },
    {
        "item": "结构 & 土建顾问",
        "quantity": 1.0
    },
    {
        "item": "风力测算",
        "quantity": 1.0
    },
    {
        "item": "国际立面",
        "quantity": 1.0
    },
    {
        "item": "结构展望",
        "quantity": 1.0
    },
    {
        "item": "模块系统",
        "quantity": 1.0
    },
    {
        "item": "咨询环境工程师",
        "quantity": 1.0
    },
    {
        "item": "座位数: 山地自行车奥林匹克公园",
        "quantity": 1.0
    },
    {
        "item": "Furniture ",
        "quantity": 1.0
    },
    {
        "item": "MEPF工程师",
        "quantity": 1.0
    },
    {
        "item": "Energy, Climate and Construction Strategies Consultant",
        "quantity": 1.0
    },
    {
        "item": "工作站",
        "quantity": 1.0
    },
    {
        "item": "土壤",
        "quantity": 1.0
    },
    {
        "item": "提交建筑师",
        "quantity": 1.0
    },
    {
        "item": "Diller Scofidio + Renfro",
        "quantity": 1.0
    },
    {
        "item": "结构工程和技术安装",
        "quantity": 1.0
    },
    {
        "item": "博物馆MEP顾问",
        "quantity": 1.0
    },
    {
        "item": "SADI",
        "quantity": 1.0
    },
    {
        "item": "环境标识设计+引导标示",
        "quantity": 1.0
    },
    {
        "item": "场地总监",
        "quantity": 1.0
    },
    {
        "item": "油漆工程",
        "quantity": 1.0
    },
    {
        "item": "责任合伙",
        "quantity": 1.0
    },
    {
        "item": "电气工程与调试安装",
        "quantity": 1.0
    },
    {
        "item": "大楼检验",
        "quantity": 1.0
    },
    {
        "item": "分析图",
        "quantity": 1.0
    },
    {
        "item": "施工作业",
        "quantity": 1.0
    },
    {
        "item": "Cooper Robertson 结构技术经理",
        "quantity": 1.0
    },
    {
        "item": "合同金额",
        "quantity": 1.0
    },
    {
        "item": "Electrical, Lighting & Plumbing Engineering",
        "quantity": 1.0
    },
    {
        "item": "机场项目管理",
        "quantity": 1.0
    },
    {
        "item": "监管办公室",
        "quantity": 1.0
    },
    {
        "item": "经济管理",
        "quantity": 1.0
    },
    {
        "item": "Lighting Designer ",
        "quantity": 1.0
    },
    {
        "item": "Engineering Facilities",
        "quantity": 1.0
    },
    {
        "item": "水利设施",
        "quantity": 1.0
    },
    {
        "item": "电气方案",
        "quantity": 1.0
    },
    {
        "item": "资深航空规划师",
        "quantity": 1.0
    },
    {
        "item": "泳池设计",
        "quantity": 1.0
    },
    {
        "item": "Electricity and Comunications",
        "quantity": 1.0
    },
    {
        "item": "地面和排水",
        "quantity": 1.0
    },
    {
        "item": "Aho团队",
        "quantity": 1.0
    },
    {
        "item": "室内样板间设计",
        "quantity": 1.0
    },
    {
        "item": "游泳池",
        "quantity": 1.0
    },
    {
        "item": "Civil/Landscape",
        "quantity": 1.0
    },
    {
        "item": "符号设计",
        "quantity": 1.0
    },
    {
        "item": "结构规划师",
        "quantity": 1.0
    },
    {
        "item": "估算花费",
        "quantity": 1.0
    },
    {
        "item": "木结构和总承包商",
        "quantity": 1.0
    },
    {
        "item": "品牌推广",
        "quantity": 1.0
    },
    {
        "item": "设计及施工",
        "quantity": 1.0
    },
    {
        "item": "Energy/Leed",
        "quantity": 1.0
    },
    {
        "item": "三维图像",
        "quantity": 1.0
    },
    {
        "item": "设计和项目管理",
        "quantity": 1.0
    },
    {
        "item": "结构与 HBAC",
        "quantity": 1.0
    },
    {
        "item": "设计施工",
        "quantity": 1.0
    },
    {
        "item": "建筑工程负责人",
        "quantity": 1.0
    },
    {
        "item": "建造日期",
        "quantity": 1.0
    },
    {
        "item": "管理及建造",
        "quantity": 1.0
    },
    {
        "item": "卫浴工程师",
        "quantity": 1.0
    },
    {
        "item": "项目费用",
        "quantity": 1.0
    },
    {
        "item": "渲染师",
        "quantity": 1.0
    },
    {
        "item": "外部合作",
        "quantity": 1.0
    },
    {
        "item": "主管设计师",
        "quantity": 1.0
    },
    {
        "item": "年代",
        "quantity": 1.0
    },
    {
        "item": "场地团队",
        "quantity": 1.0
    },
    {
        "item": "装置艺术设计师",
        "quantity": 1.0
    },
    {
        "item": "创立合伙人",
        "quantity": 1.0
    },
    {
        "item": "Architect Collaborators",
        "quantity": 1.0
    },
    {
        "item": "Área Sitio",
        "quantity": 1.0
    },
    {
        "item": "展览设计三维设计和项目管理",
        "quantity": 1.0
    },
    {
        "item": "总使用面积",
        "quantity": 1.0
    },
    {
        "item": "估算成本",
        "quantity": 1.0
    },
    {
        "item": "Photography & Videography",
        "quantity": 1.0
    },
    {
        "item": "原建筑面积",
        "quantity": 1.0
    },
    {
        "item": "项目组学生",
        "quantity": 1.0
    },
    {
        "item": "Technical Design Controler ",
        "quantity": 1.0
    },
    {
        "item": "管理委员会主席",
        "quantity": 1.0
    },
    {
        "item": "屋顶安装",
        "quantity": 1.0
    },
    {
        "item": "声学工程团队",
        "quantity": 1.0
    },
    {
        "item": "景观建筑师团队",
        "quantity": 1.0
    },
    {
        "item": "产品及联络",
        "quantity": 1.0
    },
    {
        "item": "说明书",
        "quantity": 1.0
    },
    {
        "item": "Greisch",
        "quantity": 1.0
    },
    {
        "item": "环境平面设计师 ",
        "quantity": 1.0
    },
    {
        "item": "设计事务所 / 团队",
        "quantity": 1.0
    },
    {
        "item": "预算, 安全和健康咨询",
        "quantity": 1.0
    },
    {
        "item": "创始人兼主建筑设计师",
        "quantity": 1.0
    },
    {
        "item": "电子通讯系统",
        "quantity": 1.0
    },
    {
        "item": "Stylist",
        "quantity": 1.0
    },
    {
        "item": "室内施工图设计",
        "quantity": 1.0
    },
    {
        "item": "项目发起",
        "quantity": 1.0
    },
    {
        "item": "扩大套房面积",
        "quantity": 1.0
    },
    {
        "item": "声学与音像设计",
        "quantity": 1.0
    },
    {
        "item": "流体系统",
        "quantity": 1.0
    },
    {
        "item": "主要的家具供应商",
        "quantity": 1.0
    },
    {
        "item": "工程及专业顾问",
        "quantity": 1.0
    },
    {
        "item": "工作检验",
        "quantity": 1.0
    },
    {
        "item": "工程领导者",
        "quantity": 1.0
    },
    {
        "item": "立面制作",
        "quantity": 1.0
    },
    {
        "item": "扣除增值税的建筑造价（包含设备）",
        "quantity": 1.0
    },
    {
        "item": "Superficie de Terreno",
        "quantity": 1.0
    },
    {
        "item": "稳定性",
        "quantity": 1.0
    },
    {
        "item": "气候环境",
        "quantity": 1.0
    },
    {
        "item": "建筑 公司",
        "quantity": 1.0
    },
    {
        "item": "施工跟进",
        "quantity": 1.0
    },
    {
        "item": "建筑师们",
        "quantity": 1.0
    },
    {
        "item": "客户单位",
        "quantity": 1.0
    },
    {
        "item": "音像、照明、剧院、外立面/瑞士顾问（执行）",
        "quantity": 1.0
    },
    {
        "item": "创作总监",
        "quantity": 1.0
    },
    {
        "item": "建筑奖项",
        "quantity": 1.0
    },
    {
        "item": "Plumbing and aquarium technology",
        "quantity": 1.0
    },
    {
        "item": "小屋面积1&2",
        "quantity": 1.0
    },
    {
        "item": "每平米造价",
        "quantity": 1.0
    },
    {
        "item": "餐厅与礼品店",
        "quantity": 1.0
    },
    {
        "item": "居住空间",
        "quantity": 1.0
    },
    {
        "item": "Exhibit Design/Interpretive Team",
        "quantity": 1.0
    },
    {
        "item": "Fondazione 建筑表皮面积",
        "quantity": 1.0
    },
    {
        "item": "主设",
        "quantity": 1.0
    },
    {
        "item": "扎哈事务所项目助理",
        "quantity": 1.0
    },
    {
        "item": "BFLS 团队",
        "quantity": 1.0
    },
    {
        "item": "项目类别",
        "quantity": 1.0
    },
    {
        "item": "KPF工地负责人",
        "quantity": 1.0
    },
    {
        "item": "设计团队主管/总设计师",
        "quantity": 1.0
    },
    {
        "item": "Planning of Structural Framework",
        "quantity": 1.0
    },
    {
        "item": "执行日期",
        "quantity": 1.0
    },
    {
        "item": "电气和液压系统工程师",
        "quantity": 1.0
    },
    {
        "item": "发展合作伙伴和承包商",
        "quantity": 1.0
    },
    {
        "item": "景观和室内设计",
        "quantity": 1.0
    },
    {
        "item": "项目概念",
        "quantity": 1.0
    },
    {
        "item": "水利电力安装",
        "quantity": 1.0
    },
    {
        "item": "室内家具",
        "quantity": 1.0
    },
    {
        "item": "食品供应",
        "quantity": 1.0
    },
    {
        "item": "价格",
        "quantity": 1.0
    },
    {
        "item": "设备供应商",
        "quantity": 1.0
    },
    {
        "item": "Electrical Contractors ",
        "quantity": 1.0
    },
    {
        "item": "外墙工程师与安装",
        "quantity": 1.0
    },
    {
        "item": "赞助桑",
        "quantity": 1.0
    },
    {
        "item": "Environmental / M&E",
        "quantity": 1.0
    },
    {
        "item": "Client (UNStudio)",
        "quantity": 1.0
    },
    {
        "item": "家具供应",
        "quantity": 1.0
    },
    {
        "item": "Environmental Consultant",
        "quantity": 1.0
    },
    {
        "item": "执行理事成员",
        "quantity": 1.0
    },
    {
        "item": "电力、照明、卫生、管道、空调和PCI",
        "quantity": 1.0
    },
    {
        "item": "水管设施",
        "quantity": 1.0
    },
    {
        "item": "起草人",
        "quantity": 1.0
    },
    {
        "item": "Architectural Design",
        "quantity": 1.0
    },
    {
        "item": "执行承包商",
        "quantity": 1.0
    },
    {
        "item": "设计团队（华夫设计）",
        "quantity": 1.0
    },
    {
        "item": "Mechanical",
        "quantity": 1.0
    },
    {
        "item": "纹理石膏",
        "quantity": 1.0
    },
    {
        "item": "资产管理",
        "quantity": 1.0
    },
    {
        "item": "Electrician",
        "quantity": 1.0
    },
    {
        "item": "999年竞赛总设计师",
        "quantity": 1.0
    },
    {
        "item": "热效",
        "quantity": 1.0
    },
    {
        "item": "M&E可持续发展顾问",
        "quantity": 1.0
    },
    {
        "item": "SNEF",
        "quantity": 1.0
    },
    {
        "item": "Wetzikon职业学校",
        "quantity": 1.0
    },
    {
        "item": " Arquitecto a Cargo",
        "quantity": 1.0
    },
    {
        "item": "空气动力研究",
        "quantity": 1.0
    },
    {
        "item": "3D建模",
        "quantity": 1.0
    },
    {
        "item": "机电工程师(公司名称)",
        "quantity": 1.0
    },
    {
        "item": "家具、装置和设备",
        "quantity": 1.0
    },
    {
        "item": "自带花园单元数",
        "quantity": 1.0
    },
    {
        "item": "发展管理",
        "quantity": 1.0
    },
    {
        "item": "客户项目经理 ",
        "quantity": 1.0
    },
    {
        "item": "网状表皮",
        "quantity": 1.0
    },
    {
        "item": "结构设备",
        "quantity": 1.0
    },
    {
        "item": "保洁",
        "quantity": 1.0
    },
    {
        "item": "表皮、室内和建筑干预",
        "quantity": 1.0
    },
    {
        "item": "建筑咨询师",
        "quantity": 1.0
    },
    {
        "item": "建筑物理、消防和声学",
        "quantity": 1.0
    },
    {
        "item": "Architect SAFA",
        "quantity": 1.0
    },
    {
        "item": "分项目建筑师",
        "quantity": 1.0
    },
    {
        "item": "环境认证",
        "quantity": 1.0
    },
    {
        "item": "本地机电管道工程师",
        "quantity": 1.0
    },
    {
        "item": "运动场顾问",
        "quantity": 1.0
    },
    {
        "item": "陶瓷壁画画家",
        "quantity": 1.0
    },
    {
        "item": "Graphic Design Team",
        "quantity": 1.0
    },
    {
        "item": "机械师/电机师",
        "quantity": 1.0
    },
    {
        "item": "电梯/自动扶梯/建筑修复",
        "quantity": 1.0
    },
    {
        "item": "设备、电力与给排水",
        "quantity": 1.0
    },
    {
        "item": "客户代理人",
        "quantity": 1.0
    },
    {
        "item": "业主&合伙人",
        "quantity": 1.0
    },
    {
        "item": "总居住面积",
        "quantity": 1.0
    },
    {
        "item": "墙壁排水",
        "quantity": 1.0
    },
    {
        "item": "法规顾问",
        "quantity": 1.0
    },
    {
        "item": "项目咨询",
        "quantity": 1.0
    },
    {
        "item": "ID - 酒店客房",
        "quantity": 1.0
    },
    {
        "item": "项目年期",
        "quantity": 1.0
    },
    {
        "item": "光照工程师",
        "quantity": 1.0
    },
    {
        "item": "Sanitary Engineer",
        "quantity": 1.0
    },
    {
        "item": "施工工期",
        "quantity": 1.0
    },
    {
        "item": "设计和建设总监",
        "quantity": 1.0
    },
    {
        "item": "茶籽油工厂面积",
        "quantity": 1.0
    },
    {
        "item": "工程顾问公司",
        "quantity": 1.0
    },
    {
        "item": "餐厅",
        "quantity": 1.0
    },
    {
        "item": "委托人 ",
        "mlh": "开发建设方",
        "quantity": 1.0
    },
    {
        "item": "水&消防工程",
        "quantity": 1.0
    },
    {
        "item": "编辑，音乐和地形设计",
        "quantity": 1.0
    },
    {
        "item": "合同管理",
        "quantity": 1.0
    },
    {
        "item": "预算顾问与甲方监理",
        "quantity": 1.0
    },
    {
        "item": "空间面积",
        "quantity": 1.0
    },
    {
        "item": "水培系统",
        "quantity": 1.0
    },
    {
        "item": "外装修",
        "quantity": 1.0
    },
    {
        "item": "审查",
        "quantity": 1.0
    },
    {
        "item": "照明系统",
        "quantity": 1.0
    },
    {
        "item": "Metal-restorer",
        "quantity": 1.0
    },
    {
        "item": "Picture–restorer and Glass Mosaic Diagnostics",
        "quantity": 1.0
    },
    {
        "item": "树木研究者",
        "quantity": 1.0
    },
    {
        "item": "构造设计",
        "quantity": 1.0
    },
    {
        "item": "模型团队",
        "quantity": 1.0
    },
    {
        "item": "VIP休息室项目视觉传达",
        "quantity": 1.0
    },
    {
        "item": "机械／电力工程师",
        "quantity": 1.0
    },
    {
        "item": "合作开发商",
        "quantity": 1.0
    },
    {
        "item": "公共艺术顾问",
        "quantity": 1.0
    },
    {
        "item": "展览平面设计",
        "quantity": 1.0
    },
    {
        "item": "建筑协调",
        "quantity": 1.0
    },
    {
        "item": "门窗设计",
        "quantity": 1.0
    },
    {
        "item": "设备设计师",
        "quantity": 1.0
    },
    {
        "item": "生态系统设计",
        "quantity": 1.0
    },
    {
        "item": "底层总面积",
        "quantity": 1.0
    },
    {
        "item": "定制家具",
        "quantity": 1.0
    },
    {
        "item": "监管设计师",
        "quantity": 1.0
    },
    {
        "item": "原创建筑师",
        "quantity": 1.0
    },
    {
        "item": "竹承包商",
        "quantity": 1.0
    },
    {
        "item": "Interior Collaborator",
        "quantity": 1.0
    },
    {
        "item": "运动设计师",
        "quantity": 1.0
    },
    {
        "item": "电力工程与Domitica",
        "quantity": 1.0
    },
    {
        "item": "总建筑面积(包括地下室)",
        "quantity": 1.0
    },
    {
        "item": "安防系统",
        "quantity": 1.0
    },
    {
        "item": "专案经理",
        "quantity": 1.0
    },
    {
        "item": "Allies and Morrison 合作人",
        "quantity": 1.0
    },
    {
        "item": "Wood-restorer",
        "quantity": 1.0
    },
    {
        "item": "消防工程和辅助顾问",
        "quantity": 1.0
    },
    {
        "item": "设计事务所",
        "quantity": 1.0
    },
    {
        "item": "声音",
        "quantity": 1.0
    },
    {
        "item": "Author",
        "quantity": 1.0
    },
    {
        "item": "地面照明顾问",
        "quantity": 1.0
    },
    {
        "item": "驻地团队",
        "quantity": 1.0
    },
    {
        "item": "成本计算",
        "quantity": 1.0
    },
    {
        "item": "支持伙伴",
        "quantity": 1.0
    },
    {
        "item": "音响师",
        "quantity": 1.0
    },
    {
        "item": "GHD Woodhead 团队",
        "quantity": 1.0
    },
    {
        "item": "瓷砖",
        "quantity": 1.0
    },
    {
        "item": "物理工程顾问",
        "quantity": 1.0
    },
    {
        "item": "施工场地",
        "quantity": 1.0
    },
    {
        "item": "楼层扩建面积",
        "quantity": 1.0
    },
    {
        "item": "合作着",
        "quantity": 1.0
    },
    {
        "item": "文物保护 ",
        "quantity": 1.0
    },
    {
        "item": "设计竞赛",
        "quantity": 1.0
    },
    {
        "item": "锌幕墙分承包商",
        "quantity": 1.0
    },
    {
        "item": "主管合作者",
        "quantity": 1.0
    },
    {
        "item": "地址工程师",
        "quantity": 1.0
    },
    {
        "item": "其他参与方",
        "quantity": 1.0
    },
    {
        "item": "施工工程",
        "quantity": 1.0
    },
    {
        "item": "立面图形和标识",
        "quantity": 1.0
    },
    {
        "item": "Project Owner",
        "quantity": 1.0
    },
    {
        "item": "Triptyque,项目经理",
        "quantity": 1.0
    },
    {
        "item": "Logo设计",
        "quantity": 1.0
    },
    {
        "item": "桥梁设计师",
        "quantity": 1.0
    },
    {
        "item": "环境和高性能设计顾问",
        "quantity": 1.0
    },
    {
        "item": "ACMV",
        "quantity": 1.0
    },
    {
        "item": "图书馆规划",
        "quantity": 1.0
    },
    {
        "item": "供暖，通风，空调，给排水，餐饮，道路网络，ASC",
        "quantity": 1.0
    },
    {
        "item": "合作伙伴代理商",
        "quantity": 1.0
    },
    {
        "item": "指引",
        "quantity": 1.0
    },
    {
        "item": "赞助商及合伙人",
        "quantity": 1.0
    },
    {
        "item": "受益者",
        "quantity": 1.0
    },
    {
        "item": "室内和家居设计",
        "quantity": 1.0
    },
    {
        "item": "项目贡献者",
        "quantity": 1.0
    },
    {
        "item": "MEP/FP/AV/IT/SEC",
        "quantity": 1.0
    },
    {
        "item": "考古发现展示",
        "quantity": 1.0
    },
    {
        "item": "合伙工程师",
        "quantity": 1.0
    },
    {
        "item": "事务所总监",
        "quantity": 1.0
    },
    {
        "item": "验收检查",
        "quantity": 1.0
    },
    {
        "item": "Hydraulic Instalations",
        "quantity": 1.0
    },
    {
        "item": "甲级设计院",
        "quantity": 1.0
    },
    {
        "item": "客户端/开发人员",
        "quantity": 1.0
    },
    {
        "item": "工业化地板",
        "quantity": 1.0
    },
    {
        "item": "结构、防火工程",
        "quantity": 1.0
    },
    {
        "item": "室外工程设计",
        "quantity": 1.0
    },
    {
        "item": "总协调师",
        "quantity": 1.0
    },
    {
        "item": "Partners in charge",
        "quantity": 1.0
    },
    {
        "item": "交通设施规划",
        "quantity": 1.0
    },
    {
        "item": "收尾工作",
        "quantity": 1.0
    },
    {
        "item": "家具制造",
        "quantity": 1.0
    },
    {
        "item": "支持合伙",
        "quantity": 1.0
    },
    {
        "item": "数字建造团队",
        "quantity": 1.0
    },
    {
        "item": "Topotek 1 负责人",
        "quantity": 1.0
    },
    {
        "item": "工程与项目经理",
        "quantity": 1.0
    },
    {
        "item": "结构和立面工程师",
        "quantity": 1.0
    },
    {
        "item": "花销",
        "quantity": 1.0
    },
    {
        "item": "Subcontractor, Steel",
        "quantity": 1.0
    },
    {
        "item": "Project Construction Period",
        "quantity": 1.0
    },
    {
        "item": "结构和基础工程 ",
        "quantity": 1.0
    },
    {
        "item": "2004 2005设计主管合作者",
        "quantity": 1.0
    },
    {
        "item": "旧城改造公司",
        "quantity": 1.0
    },
    {
        "item": "Clothes",
        "quantity": 1.0
    },
    {
        "item": "雕刻家",
        "quantity": 1.0
    },
    {
        "item": "首长",
        "quantity": 1.0
    },
    {
        "item": "诺斯洛普历史建筑维护工程",
        "quantity": 1.0
    },
    {
        "item": "钢",
        "quantity": 1.0
    },
    {
        "item": "流体研究",
        "quantity": 1.0
    },
    {
        "item": "技术设施工程",
        "quantity": 1.0
    },
    {
        "item": "AMO",
        "quantity": 1.0
    },
    {
        "item": "机器清理",
        "quantity": 1.0
    },
    {
        "item": "作品地点",
        "quantity": 1.0
    },
    {
        "item": "高级建筑设计师 ",
        "quantity": 1.0
    },
    {
        "item": "总建筑师  ",
        "quantity": 1.0
    },
    {
        "item": "屋顶/墙体结构",
        "quantity": 1.0
    },
    {
        "item": "设施1",
        "quantity": 1.0
    },
    {
        "item": "亭子承包商",
        "quantity": 1.0
    },
    {
        "item": "设计实践",
        "quantity": 1.0
    },
    {
        "item": "公共艺术咨询",
        "quantity": 1.0
    },
    {
        "item": "Architects / Team Leaders",
        "quantity": 1.0
    },
    {
        "item": "管理和施工",
        "quantity": 1.0
    },
    {
        "item": "安防和消防",
        "quantity": 1.0
    },
    {
        "item": "调研纽约城市基础设施和水",
        "quantity": 1.0
    },
    {
        "item": "施工设计师",
        "quantity": 1.0
    },
    {
        "item": "项目建筑师及经理",
        "quantity": 1.0
    },
    {
        "item": "浴室",
        "quantity": 1.0
    },
    {
        "item": "项目完成世家",
        "quantity": 1.0
    },
    {
        "item": "轻钢结构",
        "quantity": 1.0
    },
    {
        "item": "主任工程师",
        "quantity": 1.0
    },
    {
        "item": "建设成本顾问",
        "quantity": 1.0
    },
    {
        "item": "液压设备和设施",
        "quantity": 1.0
    },
    {
        "item": "报价表",
        "quantity": 1.0
    },
    {
        "item": "室内设计/设计",
        "quantity": 1.0
    },
    {
        "item": "3D Model",
        "quantity": 1.0
    },
    {
        "item": "信息图",
        "quantity": 1.0
    },
    {
        "item": "照明技术",
        "quantity": 1.0
    },
    {
        "item": "设备成本",
        "quantity": 1.0
    },
    {
        "item": "Creative Directors",
        "quantity": 1.0
    },
    {
        "item": "植被承包商",
        "quantity": 1.0
    },
    {
        "item": "设计及建筑施工",
        "quantity": 1.0
    },
    {
        "item": "项目主任",
        "quantity": 1.0
    },
    {
        "item": "剧场技术顾问",
        "quantity": 1.0
    },
    {
        "item": "苏圣亮，夏至",
        "quantity": 1.0
    },
    {
        "item": "工程和系统",
        "quantity": 1.0
    },
    {
        "item": "城市化设计",
        "quantity": 1.0
    },
    {
        "item": "管线工程",
        "quantity": 1.0
    },
    {
        "item": "室内空间",
        "quantity": 1.0
    },
    {
        "item": "SAUCIER + PERROTTE / HCMA 团队",
        "quantity": 1.0
    },
    {
        "item": "支出/平方米",
        "quantity": 1.0
    },
    {
        "item": "图像",
        "quantity": 1.0
    },
    {
        "item": "瞭望塔和外壳的设计+规划",
        "quantity": 1.0
    },
    {
        "item": "土壤报告",
        "quantity": 1.0
    },
    {
        "item": "机场专家",
        "quantity": 1.0
    },
    {
        "item": "Graphic Consultant",
        "quantity": 1.0
    },
    {
        "item": "液压系统设计",
        "quantity": 1.0
    },
    {
        "item": "Superflex 设计团队",
        "quantity": 1.0
    },
    {
        "item": "泳池／景观设计",
        "quantity": 1.0
    },
    {
        "item": "建筑物理和声学",
        "quantity": 1.0
    },
    {
        "item": "建筑师成员",
        "quantity": 1.0
    },
    {
        "item": "Gietermans & Van Dijk",
        "quantity": 1.0
    },
    {
        "item": "装饰板",
        "quantity": 1.0
    },
    {
        "item": "博物馆总面积",
        "quantity": 1.0
    },
    {
        "item": "参赛结构顾问",
        "quantity": 1.0
    },
    {
        "item": "主要承包者和记录建筑师",
        "quantity": 1.0
    },
    {
        "item": "绿标顾问",
        "quantity": 1.0
    },
    {
        "item": "规划主管",
        "quantity": 1.0
    },
    {
        "item": "建筑环境质量工程师",
        "quantity": 1.0
    },
    {
        "item": "General Constructor",
        "quantity": 1.0
    },
    {
        "item": "总体积",
        "quantity": 1.0
    },
    {
        "item": "Control of work",
        "quantity": 1.0
    },
    {
        "item": "地热设计师",
        "quantity": 1.0
    },
    {
        "item": "建设协调",
        "quantity": 1.0
    },
    {
        "item": "主要建筑顾问",
        "quantity": 1.0
    },
    {
        "item": "总咨询商",
        "quantity": 1.0
    },
    {
        "item": "滑雪缆车顾问",
        "quantity": 1.0
    },
    {
        "item": "灯光及自动化",
        "quantity": 1.0
    },
    {
        "item": "静电防护",
        "quantity": 1.0
    },
    {
        "item": "Mechanical & Plumbing Engineer",
        "quantity": 1.0
    },
    {
        "item": "VIP休息室建筑师",
        "quantity": 1.0
    },
    {
        "item": "一期 MEP / 装置",
        "quantity": 1.0
    },
    {
        "item": "机电及能源工程师",
        "quantity": 1.0
    },
    {
        "item": " Arquitectos a Cargo",
        "quantity": 1.0
    },
    {
        "item": "管道和消防设计",
        "quantity": 1.0
    },
    {
        "item": "CDM项目联络",
        "quantity": 1.0
    },
    {
        "item": "联合董事",
        "quantity": 1.0
    },
    {
        "item": "新楼层面积",
        "quantity": 1.0
    },
    {
        "item": "电力/水力",
        "quantity": 1.0
    },
    {
        "item": "场景设置",
        "quantity": 1.0
    },
    {
        "item": "低耗家具",
        "quantity": 1.0
    },
    {
        "item": "工程经济",
        "quantity": 1.0
    },
    {
        "item": "水族馆装置",
        "quantity": 1.0
    },
    {
        "item": "安全/ 防火顾问",
        "quantity": 1.0
    },
    {
        "item": "Gestión",
        "quantity": 1.0
    },
    {
        "item": "床位数量",
        "quantity": 1.0
    },
    {
        "item": "苏黎世城市",
        "quantity": 1.0
    },
    {
        "item": "Archeology",
        "quantity": 1.0
    },
    {
        "item": "Fabrication Company",
        "quantity": 1.0
    },
    {
        "item": "BET TCE",
        "quantity": 1.0
    },
    {
        "item": "项目承建",
        "quantity": 1.0
    },
    {
        "item": "项目总负责",
        "quantity": 1.0
    },
    {
        "item": "企业基金",
        "quantity": 1.0
    },
    {
        "item": "窗框",
        "quantity": 1.0
    },
    {
        "item": "服务项目",
        "quantity": 1.0
    },
    {
        "item": "HHF 团队",
        "quantity": 1.0
    },
    {
        "item": "Drone Photography",
        "quantity": 1.0
    },
    {
        "item": "调研团队",
        "quantity": 1.0
    },
    {
        "item": "剧场面积",
        "quantity": 1.0
    },
    {
        "item": "建筑师+结构工程师",
        "quantity": 1.0
    },
    {
        "item": "Sanitation Installation",
        "quantity": 1.0
    },
    {
        "item": "Built-up area",
        "quantity": 1.0
    },
    {
        "item": "ET 热系统",
        "quantity": 1.0
    },
    {
        "item": "大教堂的高度",
        "quantity": 1.0
    },
    {
        "item": "电气工程师及安装",
        "quantity": 1.0
    },
    {
        "item": "专案建筑师",
        "quantity": 1.0
    },
    {
        "item": "安装和照明系统",
        "quantity": 1.0
    },
    {
        "item": "施工和施工经理",
        "quantity": 1.0
    },
    {
        "item": "机械，液压和电气工程师",
        "quantity": 1.0
    },
    {
        "item": "装置尺寸",
        "quantity": 1.0
    },
    {
        "item": "陈列",
        "quantity": 1.0
    },
    {
        "item": "设计管理协调员",
        "quantity": 1.0
    },
    {
        "item": "专家顾问",
        "quantity": 1.0
    },
    {
        "item": "建筑师设计",
        "quantity": 1.0
    },
    {
        "item": "品牌策略",
        "quantity": 1.0
    },
    {
        "item": "居住单元",
        "quantity": 1.0
    },
    {
        "item": "LDI Lighting",
        "quantity": 1.0
    },
    {
        "item": "教师之村七号楼",
        "quantity": 1.0
    },
    {
        "item": "可持续发展设计",
        "quantity": 1.0
    },
    {
        "item": "图形建模",
        "quantity": 1.0
    },
    {
        "item": "行政支持",
        "quantity": 1.0
    },
    {
        "item": "室外合作者",
        "quantity": 1.0
    },
    {
        "item": "机电分包",
        "quantity": 1.0
    },
    {
        "item": "E-安装",
        "quantity": 1.0
    },
    {
        "item": "园林设施",
        "quantity": 1.0
    },
    {
        "item": "升学",
        "quantity": 1.0
    },
    {
        "item": "园林家具",
        "quantity": 1.0
    },
    {
        "item": "管理/设计",
        "quantity": 1.0
    },
    {
        "item": "文件编制",
        "quantity": 1.0
    },
    {
        "item": "风的方向",
        "quantity": 1.0
    },
    {
        "item": "水暖电及可持续设计",
        "quantity": 1.0
    },
    {
        "item": "招标细节",
        "quantity": 1.0
    },
    {
        "item": "室外饰面",
        "quantity": 1.0
    },
    {
        "item": "Equipo de proyecto y construcción",
        "quantity": 1.0
    },
    {
        "item": "钢及混泥土结构",
        "quantity": 1.0
    },
    {
        "item": "Audio-video Installations",
        "quantity": 1.0
    },
    {
        "item": "设计及室内设计",
        "quantity": 1.0
    },
    {
        "item": "客户咨询",
        "quantity": 1.0
    },
    {
        "item": "工艺品设计制作",
        "quantity": 1.0
    },
    {
        "item": "人行通道结构",
        "quantity": 1.0
    },
    {
        "item": "资金赞助",
        "quantity": 1.0
    },
    {
        "item": "承办单位",
        "quantity": 1.0
    },
    {
        "item": "室内木结构",
        "quantity": 1.0
    },
    {
        "item": "小屋面积3",
        "quantity": 1.0
    },
    {
        "item": "研究所卫生",
        "quantity": 1.0
    },
    {
        "item": "地板准备与铺装",
        "quantity": 1.0
    },
    {
        "item": "视觉展现",
        "quantity": 1.0
    },
    {
        "item": "上部构造和包层",
        "quantity": 1.0
    },
    {
        "item": "高中占地面积",
        "quantity": 1.0
    },
    {
        "item": "屋宇测量师",
        "quantity": 1.0
    },
    {
        "item": "室内建造咨询",
        "quantity": 1.0
    },
    {
        "item": "马赛克壁画",
        "quantity": 1.0
    },
    {
        "item": "项目及现场管理人",
        "quantity": 1.0
    },
    {
        "item": "石料加工",
        "quantity": 1.0
    },
    {
        "item": "建设物理",
        "quantity": 1.0
    },
    {
        "item": "设计建造承包商",
        "quantity": 1.0
    },
    {
        "item": "Design Team   Urban Design",
        "quantity": 1.0
    },
    {
        "item": "包层顾问",
        "quantity": 1.0
    },
    {
        "item": "可持续性工程",
        "quantity": 1.0
    },
    {
        "item": "Designers ",
        "quantity": 1.0
    },
    {
        "item": "翻新面积",
        "quantity": 1.0
    },
    {
        "item": "设备与管道工程",
        "quantity": 1.0
    },
    {
        "item": "技术与BIM总监",
        "quantity": 1.0
    },
    {
        "item": "Structural Project",
        "quantity": 1.0
    },
    {
        "item": "环境健康咨询",
        "quantity": 1.0
    },
    {
        "item": "施工管理服务",
        "quantity": 1.0
    },
    {
        "item": "建设总监",
        "quantity": 1.0
    },
    {
        "item": "Geological Engineer",
        "quantity": 1.0
    },
    {
        "item": "Silicate-restorer",
        "quantity": 1.0
    },
    {
        "item": "建筑，风景园林和环境工程",
        "quantity": 1.0
    },
    {
        "item": "Structure And Services Engineers",
        "quantity": 1.0
    },
    {
        "item": "Arquitecto",
        "quantity": 1.0
    },
    {
        "item": "当地测绘",
        "quantity": 1.0
    },
    {
        "item": "项目设计主管",
        "quantity": 1.0
    },
    {
        "item": "清偿预算",
        "quantity": 1.0
    },
    {
        "item": "大厅室内设计",
        "quantity": 1.0
    },
    {
        "item": "健康安全咨询",
        "quantity": 1.0
    },
    {
        "item": "Cdm协调商",
        "quantity": 1.0
    },
    {
        "item": "建筑师作者",
        "quantity": 1.0
    },
    {
        "item": "视觉交流",
        "quantity": 1.0
    },
    {
        "item": "一般地板铺设",
        "quantity": 1.0
    },
    {
        "item": "生活区域",
        "quantity": 1.0
    },
    {
        "item": "Building Area",
        "quantity": 1.0
    },
    {
        "item": "代号/加快",
        "quantity": 1.0
    },
    {
        "item": "逃生规划",
        "quantity": 1.0
    },
    {
        "item": "优质环境质量顾问",
        "quantity": 1.0
    },
    {
        "item": "室外灯光",
        "quantity": 1.0
    },
    {
        "item": "优质环境质量证明人 ",
        "quantity": 1.0
    },
    {
        "item": "立体交通",
        "quantity": 1.0
    },
    {
        "item": "技术项目",
        "quantity": 1.0
    },
    {
        "item": "电子通讯",
        "quantity": 1.0
    },
    {
        "item": "Acoustics Consultant",
        "quantity": 1.0
    },
    {
        "item": "Acoustic Consultant",
        "quantity": 1.0
    },
    {
        "item": "委托年份",
        "quantity": 1.0
    },
    {
        "item": "雇员",
        "quantity": 1.0
    },
    {
        "item": "能效咨询",
        "quantity": 1.0
    },
    {
        "item": "HCMA 建筑事务所项目团队",
        "quantity": 1.0
    },
    {
        "item": "策划团队和项目经理",
        "quantity": 1.0
    },
    {
        "item": "太阳能顾问",
        "quantity": 1.0
    },
    {
        "item": "Env  图形设计师",
        "quantity": 1.0
    },
    {
        "item": "消防设施及家具",
        "quantity": 1.0
    },
    {
        "item": "代理",
        "quantity": 1.0
    },
    {
        "item": "合作者（项目执行）",
        "quantity": 1.0
    },
    {
        "item": "消防安全工程",
        "quantity": 1.0
    },
    {
        "item": "温度",
        "quantity": 1.0
    },
    {
        "item": "戏剧顾问",
        "quantity": 1.0
    },
    {
        "item": "公共区域总面积",
        "quantity": 1.0
    },
    {
        "item": "诊所面积",
        "quantity": 1.0
    },
    {
        "item": "建筑工程师团队",
        "quantity": 1.0
    },
    {
        "item": "项目团队 室内",
        "quantity": 1.0
    },
    {
        "item": "朝向",
        "quantity": 1.0
    },
    {
        "item": "主要土建施工",
        "quantity": 1.0
    },
    {
        "item": "目前顾问",
        "quantity": 1.0
    },
    {
        "item": "Detailed Design Team",
        "quantity": 1.0
    },
    {
        "item": "编程顾问",
        "quantity": 1.0
    },
    {
        "item": "On Site Representation, Associate Architects",
        "quantity": 1.0
    },
    {
        "item": "标志和图形设计",
        "quantity": 1.0
    },
    {
        "item": "展陈及景观创意总监 ",
        "quantity": 1.0
    },
    {
        "item": "竹制品经理",
        "quantity": 1.0
    },
    {
        "item": "杂技编排",
        "quantity": 1.0
    },
    {
        "item": "家庭娱乐与自动化",
        "quantity": 1.0
    },
    {
        "item": "机械及电力",
        "quantity": 1.0
    },
    {
        "item": "藤架工程",
        "quantity": 1.0
    },
    {
        "item": "当地声学顾问",
        "quantity": 1.0
    },
    {
        "item": "室内建筑",
        "quantity": 1.0
    },
    {
        "item": "名称",
        "quantity": 1.0
    },
    {
        "item": "电气工程师 ",
        "quantity": 1.0
    },
    {
        "item": "GFRP 立面开发",
        "quantity": 1.0
    },
    {
        "item": "Paisaje",
        "quantity": 1.0
    },
    {
        "item": "Colorado木构架",
        "quantity": 1.0
    },
    {
        "item": "家具选择及设计",
        "quantity": 1.0
    },
    {
        "item": "建筑单位",
        "quantity": 1.0
    },
    {
        "item": "Topotek 1 设计团队",
        "quantity": 1.0
    },
    {
        "item": "Infrastructure Utilities",
        "quantity": 1.0
    },
    {
        "item": "实验室策划",
        "quantity": 1.0
    },
    {
        "item": "工程师执行(结构和建筑图纸)",
        "quantity": 1.0
    },
    {
        "item": "高级技术支持",
        "quantity": 1.0
    },
    {
        "item": "Equipo Proyecto",
        "quantity": 1.0
    },
    {
        "item": "执行人",
        "quantity": 1.0
    },
    {
        "item": "Facade",
        "quantity": 1.0
    },
    {
        "item": "消防保护",
        "quantity": 1.0
    },
    {
        "item": "Construction (Concrete work)",
        "quantity": 1.0
    },
    {
        "item": "上层结构分析",
        "quantity": 1.0
    },
    {
        "item": "工程装备",
        "quantity": 1.0
    },
    {
        "item": "座席数",
        "quantity": 1.0
    },
    {
        "item": "景观空间",
        "quantity": 1.0
    },
    {
        "item": "Consultor",
        "quantity": 1.0
    },
    {
        "item": "铅管道",
        "quantity": 1.0
    },
    {
        "item": "医疗技术",
        "quantity": 1.0
    },
    {
        "item": "细木工作",
        "quantity": 1.0
    },
    {
        "item": "Partners",
        "quantity": 1.0
    },
    {
        "item": "交互内容",
        "quantity": 1.0
    },
    {
        "item": "能源设备",
        "quantity": 1.0
    },
    {
        "item": "设计办公室",
        "quantity": 1.0
    },
    {
        "item": "51N4E团队",
        "quantity": 1.0
    },
    {
        "item": "结构和土建工程师",
        "quantity": 1.0
    },
    {
        "item": "种植灌木",
        "quantity": 1.0
    },
    {
        "item": "地板面积",
        "quantity": 1.0
    },
    {
        "item": "羡慕协助人",
        "quantity": 1.0
    },
    {
        "item": "Wood Carpentry",
        "quantity": 1.0
    },
    {
        "item": "集成安全系统",
        "quantity": 1.0
    },
    {
        "item": "声学震动",
        "quantity": 1.0
    },
    {
        "item": "流动性设计顾问",
        "quantity": 1.0
    },
    {
        "item": "调查员",
        "quantity": 1.0
    },
    {
        "item": "主持合伙人（设计）",
        "quantity": 1.0
    },
    {
        "item": "起重",
        "quantity": 1.0
    },
    {
        "item": "景观设计:",
        "quantity": 1.0
    },
    {
        "item": "静置设备",
        "quantity": 1.0
    },
    {
        "item": "高压电气工程师",
        "quantity": 1.0
    },
    {
        "item": "照明与艺术品",
        "quantity": 1.0
    },
    {
        "item": "机械方案",
        "quantity": 1.0
    },
    {
        "item": "Electric installation",
        "quantity": 1.0
    },
    {
        "item": "Original Building Date",
        "quantity": 1.0
    },
    {
        "item": "Allies and Morrison 负责人",
        "quantity": 1.0
    },
    {
        "item": "Start construction",
        "quantity": 1.0
    },
    {
        "item": "Date Begun",
        "quantity": 1.0
    },
    {
        "item": "礼仪顾问",
        "quantity": 1.0
    },
    {
        "item": "Arquitectos Autores",
        "quantity": 1.0
    },
    {
        "item": "家具承包商",
        "quantity": 1.0
    },
    {
        "item": "博物馆平面设计",
        "quantity": 1.0
    },
    {
        "item": "景观设计师 ",
        "quantity": 1.0
    },
    {
        "item": "Design Team Phase 1",
        "quantity": 1.0
    },
    {
        "item": "L’ATELIER团队",
        "quantity": 1.0
    },
    {
        "item": "剧院",
        "quantity": 1.0
    },
    {
        "item": "大厦施工",
        "quantity": 1.0
    },
    {
        "item": "TCE, Economy, HQE ",
        "quantity": 1.0
    },
    {
        "item": "光照",
        "quantity": 1.0
    },
    {
        "item": "(LDI) Structure",
        "quantity": 1.0
    },
    {
        "item": "能源认证",
        "quantity": 1.0
    },
    {
        "item": "首席建造师",
        "quantity": 1.0
    },
    {
        "item": "网络和通信设备",
        "quantity": 1.0
    },
    {
        "item": "框架分承包商",
        "quantity": 1.0
    },
    {
        "item": "小屋面积",
        "quantity": 1.0
    },
    {
        "item": "业主与开发商",
        "quantity": 1.0
    },
    {
        "item": "市场运营",
        "quantity": 1.0
    },
    {
        "item": "Calculo Estructural",
        "quantity": 1.0
    },
    {
        "item": "屋顶绿化及景观设计师",
        "quantity": 1.0
    },
    {
        "item": "第一期预算",
        "quantity": 1.0
    },
    {
        "item": "建筑系学生",
        "quantity": 1.0
    },
    {
        "item": "EMBT上海团队",
        "quantity": 1.0
    },
    {
        "item": "机电结构工程师",
        "quantity": 1.0
    },
    {
        "item": "安全合伙人",
        "quantity": 1.0
    },
    {
        "item": "建设范围",
        "quantity": 1.0
    },
    {
        "item": "现场施工监理",
        "quantity": 1.0
    },
    {
        "item": "建议",
        "quantity": 1.0
    },
    {
        "item": "消防系统",
        "quantity": 1.0
    },
    {
        "item": "工程顾问和预算控制",
        "quantity": 1.0
    },
    {
        "item": "Code Consultancy",
        "quantity": 1.0
    },
    {
        "item": "钢片承包商",
        "quantity": 1.0
    },
    {
        "item": "BIG 负责人",
        "quantity": 1.0
    },
    {
        "item": "BIG 项目组长",
        "quantity": 1.0
    },
    {
        "item": "签字",
        "quantity": 1.0
    },
    {
        "item": "地上面积",
        "quantity": 1.0
    },
    {
        "item": "总平面&教育设施施工项目经理",
        "quantity": 1.0
    },
    {
        "item": "EL",
        "quantity": 1.0
    },
    {
        "item": "Topotek 1 项目组长",
        "quantity": 1.0
    },
    {
        "item": "竹结构领导",
        "quantity": 1.0
    },
    {
        "item": "内部总建筑面积",
        "quantity": 1.0
    },
    {
        "item": "经济支持",
        "quantity": 1.0
    },
    {
        "item": "竞赛",
        "quantity": 1.0
    },
    {
        "item": "Subcontractor, Glass",
        "quantity": 1.0
    },
    {
        "item": "著作",
        "quantity": 1.0
    },
    {
        "item": "Façade",
        "quantity": 1.0
    },
    {
        "item": "机电管道/功能设计",
        "quantity": 1.0
    },
    {
        "item": "桑拿炉",
        "quantity": 1.0
    },
    {
        "item": "Fire Consultants",
        "quantity": 1.0
    },
    {
        "item": "透视/照明顾问",
        "quantity": 1.0
    },
    {
        "item": "施工测量",
        "quantity": 1.0
    },
    {
        "item": "IT 顾问",
        "quantity": 1.0
    },
    {
        "item": "Structure And Fundation",
        "quantity": 1.0
    },
    {
        "item": "水电",
        "quantity": 1.0
    },
    {
        "item": "二楼夹层面积",
        "quantity": 1.0
    },
    {
        "item": "热力学",
        "quantity": 1.0
    },
    {
        "item": "名义建筑师与工程师",
        "quantity": 1.0
    },
    {
        "item": "陶瓷",
        "quantity": 1.0
    },
    {
        "item": "Bet",
        "quantity": 1.0
    },
    {
        "item": "国内工程",
        "quantity": 1.0
    },
    {
        "item": "稀缺创意工作室",
        "quantity": 1.0
    },
    {
        "item": "岩石锚定",
        "quantity": 1.0
    },
    {
        "item": "KVA 团队",
        "quantity": 1.0
    },
    {
        "item": "结构 & 土木结构设计",
        "quantity": 1.0
    },
    {
        "item": "Structural Diagnostics",
        "quantity": 1.0
    },
    {
        "item": "Facade drip painting",
        "quantity": 1.0
    },
    {
        "item": "Civil Contractors ",
        "quantity": 1.0
    },
    {
        "item": "客户代表人",
        "quantity": 1.0
    },
    {
        "item": "构成",
        "quantity": 1.0
    },
    {
        "item": "创意主管",
        "quantity": 1.0
    },
    {
        "item": "地方团队",
        "quantity": 1.0
    },
    {
        "item": "特殊结构",
        "quantity": 1.0
    },
    {
        "item": "结构/市政",
        "quantity": 1.0
    },
    {
        "item": "团队管理",
        "quantity": 1.0
    },
    {
        "item": "主建筑设计",
        "quantity": 1.0
    },
    {
        "item": "施工负责",
        "quantity": 1.0
    },
    {
        "item": "胶合板制造",
        "quantity": 1.0
    },
    {
        "item": "监督员",
        "quantity": 1.0
    },
    {
        "item": "预制元素",
        "quantity": 1.0
    },
    {
        "item": "Triptyque,副设计师",
        "quantity": 1.0
    },
    {
        "item": "Technical Energy",
        "quantity": 1.0
    },
    {
        "item": "藏品管理人",
        "quantity": 1.0
    },
    {
        "item": "Principal Architec",
        "quantity": 1.0
    },
    {
        "item": "工程和能源设计",
        "quantity": 1.0
    },
    {
        "item": "Floor area",
        "quantity": 1.0
    },
    {
        "item": "Culture and Events",
        "quantity": 1.0
    },
    {
        "item": "基座建筑景观建筑师",
        "quantity": 1.0
    },
    {
        "item": "Vivamar 运营公司",
        "quantity": 1.0
    },
    {
        "item": "空调制暖设计",
        "quantity": 1.0
    },
    {
        "item": "PM/预算",
        "quantity": 1.0
    },
    {
        "item": "Structural/Civil Engineer",
        "quantity": 1.0
    },
    {
        "item": "Entidad de control de calidad",
        "quantity": 1.0
    },
    {
        "item": "总建筑师和现场建筑师",
        "quantity": 1.0
    },
    {
        "item": "咨询工程公司",
        "quantity": 1.0
    },
    {
        "item": "OMA 团队",
        "quantity": 1.0
    },
    {
        "item": "主持建筑似乎",
        "quantity": 1.0
    },
    {
        "item": "LABAK LABAK LABAK LABAK",
        "quantity": 1.0
    },
    {
        "item": "历史保护",
        "quantity": 1.0
    },
    {
        "item": "砌石顾问",
        "quantity": 1.0
    },
    {
        "item": "首席建筑师和设计师",
        "quantity": 1.0
    },
    {
        "item": "Cost Consultant",
        "quantity": 1.0
    },
    {
        "item": "砖工与装饰",
        "quantity": 1.0
    },
    {
        "item": "Drawings & plans ",
        "quantity": 1.0
    },
    {
        "item": "园林建筑师",
        "quantity": 1.0
    },
    {
        "item": "质检单位（建筑）",
        "quantity": 1.0
    },
    {
        "item": "结构玻璃顾问",
        "quantity": 1.0
    },
    {
        "item": "连接材料",
        "quantity": 1.0
    },
    {
        "item": "Lenght of Bridge",
        "quantity": 1.0
    },
    {
        "item": "服务设施顾问",
        "quantity": 1.0
    },
    {
        "item": "开发商/产权人",
        "quantity": 1.0
    },
    {
        "item": "幕墙 & 天窗",
        "quantity": 1.0
    },
    {
        "item": "道路和网络工程师",
        "quantity": 1.0
    },
    {
        "item": "剧院总面积",
        "quantity": 1.0
    },
    {
        "item": "维护",
        "quantity": 1.0
    },
    {
        "item": "第一期建筑面积",
        "quantity": 1.0
    },
    {
        "item": "Mas Uno Studio",
        "quantity": 1.0
    },
    {
        "item": "施工图合作",
        "quantity": 1.0
    },
    {
        "item": "施工方  ",
        "quantity": 1.0
    },
    {
        "item": "总图",
        "quantity": 1.0
    },
    {
        "item": "馆长",
        "quantity": 1.0
    },
    {
        "item": "Concept",
        "quantity": 1.0
    },
    {
        "item": "桥长",
        "quantity": 1.0
    },
    {
        "item": "Constructional Engineer",
        "quantity": 1.0
    },
    {
        "item": "室内与家具设计",
        "quantity": 1.0
    },
    {
        "item": "城市设计者",
        "quantity": 1.0
    },
    {
        "item": "投标伙伴",
        "quantity": 1.0
    },
    {
        "item": "壁画图形",
        "quantity": 1.0
    },
    {
        "item": "设计与建造承包商",
        "quantity": 1.0
    },
    {
        "item": "消防系统提供方",
        "quantity": 1.0
    },
    {
        "item": "结构与服务顾问",
        "quantity": 1.0
    },
    {
        "item": "设计助理/现场项目经理",
        "quantity": 1.0
    },
    {
        "item": "电子设备",
        "quantity": 1.0
    },
    {
        "item": "Architect Assistant",
        "quantity": 1.0
    },
    {
        "item": "Eiffage Immobilier BDC",
        "quantity": 1.0
    },
    {
        "item": "总建筑工程师",
        "quantity": 1.0
    },
    {
        "item": "地板与滑动门木工",
        "quantity": 1.0
    },
    {
        "item": "第一阶段建设面积",
        "quantity": 1.0
    },
    {
        "item": "建模团队",
        "quantity": 1.0
    },
    {
        "item": "地方规画机构",
        "quantity": 1.0
    },
    {
        "item": "种植顾问",
        "quantity": 1.0
    },
    {
        "item": "照明装置项目",
        "quantity": 1.0
    },
    {
        "item": "钢铁和玻璃",
        "quantity": 1.0
    },
    {
        "item": "Bamboo Construction",
        "quantity": 1.0
    },
    {
        "item": "Building Height",
        "quantity": 1.0
    },
    {
        "item": "Principals in Charge",
        "quantity": 1.0
    },
    {
        "item": "总建造商",
        "quantity": 1.0
    },
    {
        "item": "51N4E合作者",
        "quantity": 1.0
    },
    {
        "item": "实际执行预算",
        "quantity": 1.0
    },
    {
        "item": "业主单位",
        "quantity": 1.0
    },
    {
        "item": "建设咨询",
        "quantity": 1.0
    },
    {
        "item": "工业管理",
        "quantity": 1.0
    },
    {
        "item": "建筑物理工程师",
        "quantity": 1.0
    },
    {
        "item": "Iluminación",
        "quantity": 1.0
    },
    {
        "item": "站立席位",
        "quantity": 1.0
    },
    {
        "item": "CAD协调",
        "quantity": 1.0
    },
    {
        "item": "模式",
        "quantity": 1.0
    },
    {
        "item": "咨询公司 ",
        "quantity": 1.0
    },
    {
        "item": "建造结构",
        "quantity": 1.0
    },
    {
        "item": "概念和项目负责人",
        "quantity": 1.0
    },
    {
        "item": "建造测量员",
        "quantity": 1.0
    },
    {
        "item": "当地的景观建筑师",
        "quantity": 1.0
    },
    {
        "item": "地质技术设计",
        "quantity": 1.0
    },
    {
        "item": "空间布局",
        "quantity": 1.0
    },
    {
        "item": "建筑构造经济学家",
        "quantity": 1.0
    },
    {
        "item": "木质结构的项目",
        "quantity": 1.0
    },
    {
        "item": "升学咨询",
        "quantity": 1.0
    },
    {
        "item": "公司持有人",
        "quantity": 1.0
    },
    {
        "item": "总承包商和项目管理",
        "quantity": 1.0
    },
    {
        "item": "每平方英尺成本",
        "quantity": 1.0
    },
    {
        "item": "搁架顾问",
        "quantity": 1.0
    },
    {
        "item": "创意顾问 ",
        "quantity": 1.0
    },
    {
        "item": "精加工",
        "quantity": 1.0
    },
    {
        "item": "制冷设计",
        "quantity": 1.0
    },
    {
        "item": "发起人/所有者",
        "quantity": 1.0
    },
    {
        "item": "新建面积",
        "quantity": 1.0
    },
    {
        "item": "位于德国的合作伙伴",
        "quantity": 1.0
    },
    {
        "item": "组织集团",
        "quantity": 1.0
    },
    {
        "item": "设计师团队",
        "quantity": 1.0
    },
    {
        "item": "诊所项目年份",
        "quantity": 1.0
    },
    {
        "item": "土工工程师  ",
        "quantity": 1.0
    },
    {
        "item": "设计开发",
        "quantity": 1.0
    },
    {
        "item": "原创设计大赛",
        "quantity": 1.0
    },
    {
        "item": "运输工程",
        "quantity": 1.0
    },
    {
        "item": "创办人",
        "quantity": 1.0
    },
    {
        "item": "消防安全顾问",
        "quantity": 1.0
    },
    {
        "item": "议员工程师记录",
        "quantity": 1.0
    },
    {
        "item": "项目总监 / 机械",
        "quantity": 1.0
    },
    {
        "item": "Mechanical/Hvac/Electrical Engineer",
        "quantity": 1.0
    },
    {
        "item": "运输顾问 ",
        "quantity": 1.0
    },
    {
        "item": "预防规划师",
        "quantity": 1.0
    },
    {
        "item": "设计时长",
        "quantity": 1.0
    },
    {
        "item": "商业规划",
        "quantity": 1.0
    },
    {
        "item": "安全顾问 ",
        "quantity": 1.0
    },
    {
        "item": "室内和景观设计",
        "quantity": 1.0
    },
    {
        "item": "总顾问和结构工程师",
        "quantity": 1.0
    },
    {
        "item": "室内设计协作",
        "quantity": 1.0
    },
    {
        "item": "行人流量顾问",
        "quantity": 1.0
    },
    {
        "item": "产品设计",
        "quantity": 1.0
    },
    {
        "item": "室外设计顾问",
        "quantity": 1.0
    },
    {
        "item": "Shoring",
        "quantity": 1.0
    },
    {
        "item": "污水处理厂设计",
        "quantity": 1.0
    },
    {
        "item": "dRMM  团队",
        "quantity": 1.0
    },
    {
        "item": "德州伙伴",
        "quantity": 1.0
    },
    {
        "item": "当地合作团队",
        "quantity": 1.0
    },
    {
        "item": "土力工程师",
        "quantity": 1.0
    },
    {
        "item": "实践团队",
        "quantity": 1.0
    },
    {
        "item": "顾问/施工",
        "quantity": 1.0
    },
    {
        "item": "采光、照明、能源咨询",
        "quantity": 1.0
    },
    {
        "item": "领导公司",
        "quantity": 1.0
    },
    {
        "item": "估价",
        "quantity": 1.0
    },
    {
        "item": "结构及环境工程",
        "quantity": 1.0
    },
    {
        "item": "2004 2005设计主管",
        "quantity": 1.0
    },
    {
        "item": "运动表皮设计",
        "quantity": 1.0
    },
    {
        "item": "设计师 &  建筑者",
        "quantity": 1.0
    },
    {
        "item": "MEP指导",
        "quantity": 1.0
    },
    {
        "item": "砌砖艺术性板",
        "quantity": 1.0
    },
    {
        "item": "项目员工",
        "quantity": 1.0
    },
    {
        "item": "花销顾问",
        "quantity": 1.0
    },
    {
        "item": "屋顶绿化顾问",
        "quantity": 1.0
    },
    {
        "item": "第一阶段项目预算",
        "quantity": 1.0
    },
    {
        "item": "Interior Designers",
        "quantity": 1.0
    },
    {
        "item": "开发人员和助理经理",
        "quantity": 1.0
    },
    {
        "item": "工业厨房设计办公室",
        "quantity": 1.0
    },
    {
        "item": "多功能厅 & 图书馆主要合作方",
        "quantity": 1.0
    },
    {
        "item": "以前的结构建议",
        "quantity": 1.0
    },
    {
        "item": "设计、建筑团队",
        "quantity": 1.0
    },
    {
        "item": "森林梦幻景观",
        "quantity": 1.0
    },
    {
        "item": "规划指导",
        "quantity": 1.0
    },
    {
        "item": "设备报价",
        "quantity": 1.0
    },
    {
        "item": "观众席结构设计",
        "quantity": 1.0
    },
    {
        "item": "建筑年代",
        "quantity": 1.0
    },
    {
        "item": "Reconstruction Phase 1, Trafospace",
        "quantity": 1.0
    },
    {
        "item": "公共空间室内设计师",
        "quantity": 1.0
    },
    {
        "item": "合同价格",
        "quantity": 1.0
    },
    {
        "item": "施工技术员/项目经理",
        "quantity": 1.0
    },
    {
        "item": "电厂",
        "quantity": 1.0
    },
    {
        "item": "桌面出版 ",
        "quantity": 1.0
    },
    {
        "item": "水暖设施",
        "quantity": 1.0
    },
    {
        "item": "服务调查",
        "quantity": 1.0
    },
    {
        "item": "装置协调者",
        "quantity": 1.0
    },
    {
        "item": "自然屋顶",
        "quantity": 1.0
    },
    {
        "item": "音频/ 视觉",
        "quantity": 1.0
    },
    {
        "item": "可视化身份及视觉项目",
        "quantity": 1.0
    },
    {
        "item": "3D团队",
        "quantity": 1.0
    },
    {
        "item": "锌加工",
        "quantity": 1.0
    },
    {
        "item": "责任总编",
        "quantity": 1.0
    },
    {
        "item": "地板承包商",
        "quantity": 1.0
    },
    {
        "item": "材料分析",
        "quantity": 1.0
    },
    {
        "item": "工作设计",
        "quantity": 1.0
    },
    {
        "item": "主管合伙人",
        "quantity": 1.0
    },
    {
        "item": "总包商 ",
        "quantity": 1.0
    },
    {
        "item": "建筑商/承包商",
        "quantity": 1.0
    },
    {
        "item": "实践建筑师",
        "quantity": 1.0
    },
    {
        "item": "配套服务",
        "quantity": 1.0
    },
    {
        "item": "船舶工程师",
        "quantity": 1.0
    },
    {
        "item": "管理主管",
        "quantity": 1.0
    },
    {
        "item": "展览设计负责人",
        "quantity": 1.0
    },
    {
        "item": "Triptyque,总协调",
        "quantity": 1.0
    },
    {
        "item": "状况",
        "quantity": 1.0
    },
    {
        "item": "客户/所有者",
        "quantity": 1.0
    },
    {
        "item": "White Arkitekter 建筑事务所的建筑师团队",
        "quantity": 1.0
    },
    {
        "item": "施工测算师",
        "quantity": 1.0
    },
    {
        "item": "电力、水与燃气",
        "quantity": 1.0
    },
    {
        "item": "2层面积",
        "quantity": 1.0
    },
    {
        "item": "玻璃屋顶承包商",
        "quantity": 1.0
    },
    {
        "item": "安全设施",
        "quantity": 1.0
    },
    {
        "item": "L&B测量师",
        "quantity": 1.0
    },
    {
        "item": "印刷品",
        "quantity": 1.0
    },
    {
        "item": "设计师、建筑师和艺术家",
        "quantity": 1.0
    },
    {
        "item": "奥方",
        "quantity": 1.0
    },
    {
        "item": "项目和现场经理",
        "quantity": 1.0
    },
    {
        "item": "电气和电信",
        "quantity": 1.0
    },
    {
        "item": "Work Directors",
        "quantity": 1.0
    },
    {
        "item": "甲烷研究",
        "quantity": 1.0
    },
    {
        "item": "所有楼层面积",
        "quantity": 1.0
    },
    {
        "item": "基坑保护",
        "quantity": 1.0
    },
    {
        "item": "高级设计助理",
        "quantity": 1.0
    },
    {
        "item": "声/学音响/视觉顾问",
        "quantity": 1.0
    },
    {
        "item": "智慧系统",
        "quantity": 1.0
    },
    {
        "item": "建筑环境顾问",
        "quantity": 1.0
    },
    {
        "item": "消防策略",
        "quantity": 1.0
    },
    {
        "item": "设备电气工程师",
        "quantity": 1.0
    },
    {
        "item": "安全控制",
        "quantity": 1.0
    },
    {
        "item": "可持续建造",
        "quantity": 1.0
    },
    {
        "item": "Building area ",
        "quantity": 1.0
    },
    {
        "item": "采暖工程",
        "quantity": 1.0
    },
    {
        "item": "防火和生命‘安全",
        "quantity": 1.0
    },
    {
        "item": "公共空间和景观建筑",
        "quantity": 1.0
    },
    {
        "item": "参开文献",
        "quantity": 1.0
    },
    {
        "item": "项目组教授",
        "quantity": 1.0
    },
    {
        "item": "采暖通风与空调",
        "quantity": 1.0
    },
    {
        "item": "设计院",
        "quantity": 1.0
    },
    {
        "item": "发展",
        "quantity": 1.0
    },
    {
        "item": "受益人",
        "quantity": 1.0
    },
    {
        "item": "项目责任建筑师",
        "quantity": 1.0
    },
    {
        "item": "展厅",
        "quantity": 1.0
    },
    {
        "item": "项目主任建筑师",
        "quantity": 1.0
    },
    {
        "item": "土木设计师",
        "quantity": 1.0
    },
    {
        "item": "现场团队 ",
        "quantity": 1.0
    },
    {
        "item": "城市景观",
        "quantity": 1.0
    },
    {
        "item": "风力",
        "quantity": 1.0
    },
    {
        "item": "桥梁",
        "quantity": 1.0
    },
    {
        "item": "合作监督总监",
        "quantity": 1.0
    },
    {
        "item": " 声学家",
        "quantity": 1.0
    },
    {
        "item": "可持续认证",
        "quantity": 1.0
    },
    {
        "item": "桥梁, coupure, Barak Y",
        "quantity": 1.0
    },
    {
        "item": "一期承包商",
        "quantity": 1.0
    },
    {
        "item": "V",
        "quantity": 1.0
    },
    {
        "item": "隐形展厅面积",
        "quantity": 1.0
    },
    {
        "item": "景观咨询师",
        "quantity": 1.0
    },
    {
        "item": "Allies and Morrison 合伙人",
        "quantity": 1.0
    },
    {
        "item": "Mechanical/Electrical Engineers",
        "quantity": 1.0
    },
    {
        "item": "室内结构",
        "quantity": 1.0
    },
    {
        "item": "流体设计",
        "quantity": 1.0
    },
    {
        "item": "通气工程师",
        "quantity": 1.0
    },
    {
        "item": "外请合作者",
        "quantity": 1.0
    },
    {
        "item": "安全 /电子交流",
        "quantity": 1.0
    },
    {
        "item": "空调和消防工程师",
        "quantity": 1.0
    },
    {
        "item": "预算霍隆市",
        "quantity": 1.0
    },
    {
        "item": "厨房方案",
        "quantity": 1.0
    },
    {
        "item": "展览统筹",
        "quantity": 1.0
    },
    {
        "item": "图书馆室内建筑师",
        "quantity": 1.0
    },
    {
        "item": "表面外观",
        "quantity": 1.0
    },
    {
        "item": "纽约环境保护部门",
        "quantity": 1.0
    },
    {
        "item": "项目建筑师  ",
        "quantity": 1.0
    },
    {
        "item": "静电",
        "quantity": 1.0
    },
    {
        "item": "艺术建议",
        "quantity": 1.0
    },
    {
        "item": "厨房安装",
        "quantity": 1.0
    },
    {
        "item": "Lot Coverage Area",
        "quantity": 1.0
    },
    {
        "item": "城市建筑师",
        "quantity": 1.0
    },
    {
        "item": "标记系统",
        "quantity": 1.0
    },
    {
        "item": "基本住宅",
        "quantity": 1.0
    },
    {
        "item": "图腾设计",
        "quantity": 1.0
    },
    {
        "item": "扩大住宅面积",
        "quantity": 1.0
    },
    {
        "item": "结构设计单位",
        "quantity": 1.0
    },
    {
        "item": "基本套房面积",
        "quantity": 1.0
    },
    {
        "item": "特定场地设计",
        "quantity": 1.0
    },
    {
        "item": "Curtail wall Consultants",
        "quantity": 1.0
    },
    {
        "item": "所有者/开发商",
        "quantity": 1.0
    },
    {
        "item": "负责管理合伙人",
        "quantity": 1.0
    },
    {
        "item": "建筑记录师",
        "quantity": 1.0
    },
    {
        "item": "绿色屋顶承包商和户外空间",
        "quantity": 1.0
    },
    {
        "item": "园林师",
        "quantity": 1.0
    },
    {
        "item": "现场施工管理",
        "quantity": 1.0
    },
    {
        "item": "室内挂板承包商",
        "quantity": 1.0
    },
    {
        "item": "CAD 绘图员",
        "quantity": 1.0
    },
    {
        "item": "用法",
        "quantity": 1.0
    },
    {
        "item": "储存能力",
        "quantity": 1.0
    },
    {
        "item": "合伙伴",
        "quantity": 1.0
    },
    {
        "item": "Rockwell集团设计团队",
        "quantity": 1.0
    },
    {
        "item": "调研人员",
        "quantity": 1.0
    },
    {
        "item": "竣工年份",
        "quantity": 1.0
    },
    {
        "item": "暖气",
        "quantity": 1.0
    },
    {
        "item": "承办商",
        "quantity": 1.0
    },
    {
        "item": "供稿人 / 客户",
        "quantity": 1.0
    },
    {
        "item": "所有者/客户",
        "quantity": 1.0
    },
    {
        "item": "温室专家",
        "quantity": 1.0
    },
    {
        "item": "规范杜撰",
        "quantity": 1.0
    },
    {
        "item": "业主咨询",
        "quantity": 1.0
    },
    {
        "item": "机/电/给排水工程师",
        "quantity": 1.0
    },
    {
        "item": "技术审查",
        "quantity": 1.0
    },
    {
        "item": "设计时期",
        "quantity": 1.0
    },
    {
        "item": "Tectoniks Team",
        "quantity": 1.0
    },
    {
        "item": "地方设计院",
        "quantity": 1.0
    },
    {
        "item": "灯光顾问 ",
        "quantity": 1.0
    },
    {
        "item": "附加面积",
        "quantity": 1.0
    },
    {
        "item": "植物种植",
        "quantity": 1.0
    },
    {
        "item": "建造承包商",
        "quantity": 1.0
    },
    {
        "item": "通风顾问",
        "quantity": 1.0
    },
    {
        "item": "Local Knowledge",
        "quantity": 1.0
    },
    {
        "item": "建筑技术文件",
        "quantity": 1.0
    },
    {
        "item": "合作建筑师 (A i B )",
        "quantity": 1.0
    },
    {
        "item": "室内设计（大堂）",
        "quantity": 1.0
    },
    {
        "item": "实验室和临床设计",
        "quantity": 1.0
    },
    {
        "item": "施工和安装",
        "quantity": 1.0
    },
    {
        "item": "Design Director",
        "quantity": 1.0
    },
    {
        "item": "联营建筑师",
        "quantity": 1.0
    },
    {
        "item": "水力模型",
        "quantity": 1.0
    },
    {
        "item": "Steel Structure",
        "quantity": 1.0
    },
    {
        "item": "建筑照明",
        "quantity": 1.0
    },
    {
        "item": "管理执行团队",
        "quantity": 1.0
    },
    {
        "item": "景观设计顾问  ",
        "quantity": 1.0
    },
    {
        "item": "学员",
        "quantity": 1.0
    },
    {
        "item": "木材加工",
        "quantity": 1.0
    },
    {
        "item": "建筑工程师 ",
        "quantity": 1.0
    },
    {
        "item": "项目贷款",
        "quantity": 1.0
    },
    {
        "item": "来自",
        "quantity": 1.0
    },
    {
        "item": "整体承包人",
        "quantity": 1.0
    },
    {
        "item": "Plot surface",
        "quantity": 1.0
    },
    {
        "item": "电器机械工程师",
        "quantity": 1.0
    },
    {
        "item": "建筑时间",
        "quantity": 1.0
    },
    {
        "item": "Racking",
        "quantity": 1.0
    },
    {
        "item": "建设机械+电气安装",
        "quantity": 1.0
    },
    {
        "item": "主要负责人 ",
        "quantity": 1.0
    },
    {
        "item": "Cedar提供者",
        "quantity": 1.0
    },
    {
        "item": "机/电/水暖工程师",
        "quantity": 1.0
    },
    {
        "item": "视频音乐及声音设计",
        "quantity": 1.0
    },
    {
        "item": "建筑基地",
        "quantity": 1.0
    },
    {
        "item": "Cultural Heritage",
        "quantity": 1.0
    },
    {
        "item": "暖通空调系统+电力",
        "quantity": 1.0
    },
    {
        "item": "经费",
        "quantity": 1.0
    },
    {
        "item": "Ceramics",
        "quantity": 1.0
    },
    {
        "item": "Local Architect",
        "quantity": 1.0
    },
    {
        "item": "全能工程师",
        "quantity": 1.0
    },
    {
        "item": "技术工程",
        "quantity": 1.0
    },
    {
        "item": "负责伙伴",
        "quantity": 1.0
    },
    {
        "item": "胶合板用量",
        "quantity": 1.0
    },
    {
        "item": "负责人 ",
        "quantity": 1.0
    },
    {
        "item": "Infrastructure Design",
        "quantity": 1.0
    },
    {
        "item": "Mep工程师",
        "quantity": 1.0
    },
    {
        "item": "视觉、色彩环境",
        "quantity": 1.0
    },
    {
        "item": "给排水顾问",
        "quantity": 1.0
    },
    {
        "item": "建筑师（阿根廷注册建筑师）",
        "quantity": 1.0
    },
    {
        "item": "楼梯设计",
        "quantity": 1.0
    },
    {
        "item": "高压交流电工程师",
        "quantity": 1.0
    },
    {
        "item": "Furniture and juicebar",
        "quantity": 1.0
    },
    {
        "item": "场地项目经理",
        "quantity": 1.0
    },
    {
        "item": "机械 电气工程师",
        "quantity": 1.0
    },
    {
        "item": "土木工程/环境",
        "quantity": 1.0
    },
    {
        "item": "遗产",
        "quantity": 1.0
    },
    {
        "item": "Bca / Pca",
        "quantity": 1.0
    },
    {
        "item": "完成",
        "quantity": 1.0
    },
    {
        "item": "公共设施",
        "quantity": 1.0
    },
    {
        "item": "建筑面积（四栋建筑之一）",
        "quantity": 1.0
    },
    {
        "item": "奖项",
        "quantity": 1.0
    },
    {
        "item": "Leed鉴定",
        "quantity": 1.0
    },
    {
        "item": "车道与步道",
        "quantity": 1.0
    },
    {
        "item": "温控与电",
        "quantity": 1.0
    },
    {
        "item": "窗帘",
        "quantity": 1.0
    },
    {
        "item": "研究",
        "quantity": 1.0
    },
    {
        "item": "Co-Autora",
        "quantity": 1.0
    },
    {
        "item": "保护与更新咨询",
        "quantity": 1.0
    },
    {
        "item": "水暖消防",
        "quantity": 1.0
    },
    {
        "item": "基座建筑结构工程师",
        "quantity": 1.0
    },
    {
        "item": "一楼面积",
        "quantity": 1.0
    },
    {
        "item": "项目年",
        "quantity": 1.0
    },
    {
        "item": "结构与机电工程师",
        "quantity": 1.0
    },
    {
        "item": "自动化项目",
        "quantity": 1.0
    },
    {
        "item": "机电安装",
        "quantity": 1.0
    },
    {
        "item": "扎哈事务所项目建筑师 ",
        "quantity": 1.0
    },
    {
        "item": "技术审核",
        "quantity": 1.0
    },
    {
        "item": "结构，土木，水利工程师",
        "quantity": 1.0
    },
    {
        "item": "阶段2",
        "quantity": 1.0
    },
    {
        "item": "项目助理设计师",
        "quantity": 1.0
    },
    {
        "item": "机械和管道",
        "quantity": 1.0
    },
    {
        "item": "占地面积1",
        "quantity": 1.0
    },
    {
        "item": "建构系统",
        "quantity": 1.0
    },
    {
        "item": "照明概念",
        "quantity": 1.0
    },
    {
        "item": "人行步道概念及方案设计",
        "quantity": 1.0
    },
    {
        "item": "Voronoïds图案设计",
        "quantity": 1.0
    },
    {
        "item": "负责董事会",
        "quantity": 1.0
    },
    {
        "item": "GRC",
        "quantity": 1.0
    },
    {
        "item": " 合作者",
        "quantity": 1.0
    },
    {
        "item": "Cdm合作者",
        "quantity": 1.0
    },
    {
        "item": "结构工程师   混凝土",
        "quantity": 1.0
    },
    {
        "item": "木板",
        "quantity": 1.0
    },
    {
        "item": "产家",
        "quantity": 1.0
    },
    {
        "item": "预算工程",
        "quantity": 1.0
    },
    {
        "item": "项目经理和宗教协调员",
        "quantity": 1.0
    },
    {
        "item": "设计&施工周期",
        "quantity": 1.0
    },
    {
        "item": "Project Leaders",
        "quantity": 1.0
    },
    {
        "item": "总技术指导",
        "quantity": 1.0
    },
    {
        "item": "结构概念",
        "quantity": 1.0
    },
    {
        "item": "设计团队领导",
        "quantity": 1.0
    },
    {
        "item": "工程师与建造经理",
        "quantity": 1.0
    },
    {
        "item": "项目设计小组",
        "quantity": 1.0
    },
    {
        "item": "土木和机电管道工程",
        "quantity": 1.0
    },
    {
        "item": "人类学",
        "quantity": 1.0
    },
    {
        "item": "声学视觉系统",
        "quantity": 1.0
    },
    {
        "item": "原理设计",
        "quantity": 1.0
    },
    {
        "item": "预案",
        "quantity": 1.0
    },
    {
        "item": "立面维护工程师",
        "quantity": 1.0
    },
    {
        "item": "音响和照明",
        "quantity": 1.0
    },
    {
        "item": "料测量师",
        "quantity": 1.0
    },
    {
        "item": "设备工程设计",
        "quantity": 1.0
    },
    {
        "item": "工业卫生",
        "quantity": 1.0
    },
    {
        "item": "玻璃选择",
        "quantity": 1.0
    },
    {
        "item": "艺术家和主设计师",
        "quantity": 1.0
    },
    {
        "item": "特殊处理",
        "quantity": 1.0
    },
    {
        "item": "雕塑师",
        "quantity": 1.0
    },
    {
        "item": "Vertical Forest Landscape Design",
        "quantity": 1.0
    },
    {
        "item": "促进",
        "quantity": 1.0
    },
    {
        "item": "设计议员工程师",
        "quantity": 1.0
    },
    {
        "item": "静力学",
        "quantity": 1.0
    },
    {
        "item": "合作设计／系统团队",
        "quantity": 1.0
    },
    {
        "item": "建成日期",
        "quantity": 1.0
    },
    {
        "item": "DDA ",
        "quantity": 1.0
    },
    {
        "item": "流线",
        "quantity": 1.0
    },
    {
        "item": "贵宾室家具",
        "quantity": 1.0
    },
    {
        "item": "Kristine Jensens Tegnestue团队",
        "quantity": 1.0
    },
    {
        "item": "材料/产品使用",
        "quantity": 1.0
    },
    {
        "item": "中承包商",
        "quantity": 1.0
    },
    {
        "item": "挂毯",
        "quantity": 1.0
    },
    {
        "item": "詹姆斯·科纳 ，菲尔德景观设计事务所 ",
        "quantity": 1.0
    },
    {
        "item": "环境图画",
        "quantity": 1.0
    },
    {
        "item": "环境艺术家",
        "quantity": 1.0
    },
    {
        "item": "委托客户",
        "quantity": 1.0
    },
    {
        "item": "智利团队",
        "quantity": 1.0
    },
    {
        "item": "土木/结构/电气顾问",
        "quantity": 1.0
    },
    {
        "item": "装置，工程，照明",
        "quantity": 1.0
    },
    {
        "item": "风雪环境设计",
        "quantity": 1.0
    },
    {
        "item": "特殊设备",
        "quantity": 1.0
    },
    {
        "item": "基金",
        "quantity": 1.0
    },
    {
        "item": "庭院设计师",
        "quantity": 1.0
    },
    {
        "item": "拥有者",
        "quantity": 1.0
    },
    {
        "item": "Arteks合作者",
        "quantity": 1.0
    },
    {
        "item": "S.L 设备",
        "quantity": 1.0
    },
    {
        "item": "景观、市政、设备设计",
        "quantity": 1.0
    },
    {
        "item": "结构面积",
        "quantity": 1.0
    },
    {
        "item": "结构负责人",
        "quantity": 1.0
    },
    {
        "item": "结构/立面工工程师",
        "quantity": 1.0
    },
    {
        "item": "主要建造材料",
        "quantity": 1.0
    },
    {
        "item": "编码顾问",
        "quantity": 1.0
    },
    {
        "item": "结构元素及系统",
        "quantity": 1.0
    },
    {
        "item": "施工总包",
        "quantity": 1.0
    },
    {
        "item": "参赛",
        "quantity": 1.0
    },
    {
        "item": "工程建筑师",
        "quantity": 1.0
    },
    {
        "item": "数量测量师 建筑安全经理",
        "quantity": 1.0
    },
    {
        "item": "电工工程师",
        "quantity": 1.0
    },
    {
        "item": "D3 Team",
        "quantity": 1.0
    },
    {
        "item": "灭火装置设计",
        "quantity": 1.0
    },
    {
        "item": "水策略",
        "quantity": 1.0
    },
    {
        "item": "道路的宽度",
        "quantity": 1.0
    },
    {
        "item": "构架",
        "quantity": 1.0
    },
    {
        "item": "外部玻璃",
        "quantity": 1.0
    },
    {
        "item": "铝合金压铸",
        "quantity": 1.0
    },
    {
        "item": "勘查员",
        "quantity": 1.0
    },
    {
        "item": "室内准备",
        "quantity": 1.0
    },
    {
        "item": "当地结构工程师",
        "quantity": 1.0
    },
    {
        "item": "核心及立面设计",
        "quantity": 1.0
    },
    {
        "item": "通信和数据顾问",
        "quantity": 1.0
    },
    {
        "item": "展品顾问",
        "quantity": 1.0
    },
    {
        "item": "开发商 / 业主",
        "quantity": 1.0
    },
    {
        "item": "MEP/结构、市政顾问",
        "quantity": 1.0
    },
    {
        "item": "地形表面",
        "quantity": 1.0
    },
    {
        "item": "竣工年",
        "quantity": 1.0
    },
    {
        "item": "交通规划",
        "quantity": 1.0
    },
    {
        "item": "Students from Aalto University",
        "quantity": 1.0
    },
    {
        "item": "水体设计和顾问",
        "quantity": 1.0
    },
    {
        "item": "总监建筑师",
        "quantity": 1.0
    },
    {
        "item": "合作社",
        "quantity": 1.0
    },
    {
        "item": "竞赛日期（第一名）",
        "quantity": 1.0
    },
    {
        "item": "影院设备供应",
        "quantity": 1.0
    },
    {
        "item": "室内大厅设计",
        "quantity": 1.0
    },
    {
        "item": "Atelier central arquitectos",
        "quantity": 1.0
    },
    {
        "item": "项目协调员",
        "quantity": 1.0
    },
    {
        "item": "哥本哈根",
        "quantity": 1.0
    },
    {
        "item": "Tag Architects设计团队",
        "quantity": 1.0
    },
    {
        "item": "Kpmb 团队设计人员",
        "quantity": 1.0
    },
    {
        "item": "宇璇",
        "quantity": 1.0
    },
    {
        "item": "立面顾问工程师",
        "quantity": 1.0
    },
    {
        "item": "结构设计（方案）",
        "quantity": 1.0
    },
    {
        "item": "夯土墙施工",
        "quantity": 1.0
    },
    {
        "item": "Gagnon Letellier Cyr 团队设计人员",
        "quantity": 1.0
    },
    {
        "item": "Smith Carter 事务所主创人员",
        "quantity": 1.0
    },
    {
        "item": "施工商",
        "quantity": 1.0
    },
    {
        "item": "机械及电力工程师",
        "quantity": 1.0
    },
    {
        "item": "三维效果图",
        "quantity": 1.0
    },
    {
        "item": "安全协调",
        "quantity": 1.0
    },
    {
        "item": "内饰设计师",
        "quantity": 1.0
    },
    {
        "item": "地板材料",
        "quantity": 1.0
    },
    {
        "item": "艺术家作品",
        "quantity": 1.0
    },
    {
        "item": "广场总面积",
        "quantity": 1.0
    },
    {
        "item": "概念/ 主建筑师",
        "quantity": 1.0
    },
    {
        "item": "结构/土建工程师",
        "quantity": 1.0
    },
    {
        "item": "Mechanical Installer",
        "quantity": 1.0
    },
    {
        "item": "环境研究",
        "quantity": 1.0
    },
    {
        "item": "Building Certifier/Access/ DDA Consultant",
        "quantity": 1.0
    },
    {
        "item": "员工宿舍",
        "quantity": 1.0
    },
    {
        "item": "景观美化工程",
        "quantity": 1.0
    },
    {
        "item": "MX_SI合作人",
        "quantity": 1.0
    },
    {
        "item": "保护设计师",
        "quantity": 1.0
    },
    {
        "item": "总负责",
        "quantity": 1.0
    },
    {
        "item": "机械电器",
        "quantity": 1.0
    },
    {
        "item": "内部合作",
        "quantity": 1.0
    },
    {
        "item": "AZC 团队",
        "quantity": 1.0
    },
    {
        "item": "技术检查",
        "quantity": 1.0
    },
    {
        "item": "灯饰设计",
        "quantity": 1.0
    },
    {
        "item": "投资建设商",
        "quantity": 1.0
    },
    {
        "item": "联合体成员",
        "quantity": 1.0
    },
    {
        "item": "选稿",
        "quantity": 1.0
    },
    {
        "item": "文化遗产",
        "quantity": 1.0
    },
    {
        "item": "土壤植被顾问",
        "quantity": 1.0
    },
    {
        "item": "宣传商",
        "quantity": 1.0
    },
    {
        "item": "展览设计设计和项目总监",
        "quantity": 1.0
    },
    {
        "item": "消防和生命安全",
        "quantity": 1.0
    },
    {
        "item": "树木代理",
        "quantity": 1.0
    },
    {
        "item": "水生顾问",
        "quantity": 1.0
    },
    {
        "item": "卫生/供暖项目",
        "quantity": 1.0
    },
    {
        "item": "席尔瓦电池安装设计",
        "quantity": 1.0
    },
    {
        "item": "客户、管理者",
        "quantity": 1.0
    },
    {
        "item": "Leed 认证顾问",
        "quantity": 1.0
    },
    {
        "item": "原住民社区顾问",
        "quantity": 1.0
    },
    {
        "item": "用户代表",
        "quantity": 1.0
    },
    {
        "item": "项目发展",
        "quantity": 1.0
    },
    {
        "item": "景观设计及深化团队",
        "quantity": 1.0
    },
    {
        "item": "建筑楼面面积",
        "quantity": 1.0
    },
    {
        "item": "标识导向顾问",
        "quantity": 1.0
    },
    {
        "item": "机械和给排水工程师",
        "quantity": 1.0
    },
    {
        "item": "开发商产业",
        "quantity": 1.0
    },
    {
        "item": "建筑师/室内设计师/负责人",
        "quantity": 1.0
    },
    {
        "item": "听觉工程师",
        "quantity": 1.0
    },
    {
        "item": "Co-Authors",
        "quantity": 1.0
    },
    {
        "item": "灯光系统",
        "quantity": 1.0
    },
    {
        "item": "实验室规划和设计",
        "quantity": 1.0
    },
    {
        "item": "参数化设计",
        "quantity": 1.0
    },
    {
        "item": "从政治角度研究水",
        "quantity": 1.0
    },
    {
        "item": "金属工程",
        "quantity": 1.0
    },
    {
        "item": "Equipo de diseño",
        "quantity": 1.0
    },
    {
        "item": "项目管理者",
        "quantity": 1.0
    },
    {
        "item": "装置供应商／制作者",
        "quantity": 1.0
    },
    {
        "item": "高度安全",
        "quantity": 1.0
    },
    {
        "item": "灯光设计咨询",
        "quantity": 1.0
    },
    {
        "item": "管理经济顾问",
        "quantity": 1.0
    },
    {
        "item": "内部建筑师",
        "quantity": 1.0
    },
    {
        "item": "室内合作者",
        "quantity": 1.0
    },
    {
        "item": "建筑总年份",
        "quantity": 1.0
    },
    {
        "item": "防火安全",
        "quantity": 1.0
    },
    {
        "item": "诊所建筑年份",
        "quantity": 1.0
    },
    {
        "item": "项目范围",
        "quantity": 1.0
    },
    {
        "item": "网址",
        "quantity": 1.0
    },
    {
        "item": "室内造型",
        "quantity": 1.0
    },
    {
        "item": "佣金类型 ",
        "quantity": 1.0
    },
    {
        "item": "室内&景观设计顾问",
        "quantity": 1.0
    },
    {
        "item": "Http://www groupea qc ca/",
        "quantity": 1.0
    },
    {
        "item": "承包商 / 建造管理",
        "quantity": 1.0
    },
    {
        "item": "阳光房设计师",
        "quantity": 1.0
    },
    {
        "item": "第一集团",
        "quantity": 1.0
    },
    {
        "item": "建筑师和工程师的记录",
        "quantity": 1.0
    },
    {
        "item": "现存教堂修复",
        "quantity": 1.0
    },
    {
        "item": "技术与舞台设计整合",
        "quantity": 1.0
    },
    {
        "item": "博物馆雕塑花园",
        "quantity": 1.0
    },
    {
        "item": "工程设计团队",
        "quantity": 1.0
    },
    {
        "item": "模架承包商",
        "quantity": 1.0
    },
    {
        "item": "项目质量监测",
        "quantity": 1.0
    },
    {
        "item": "建筑客户",
        "quantity": 1.0
    },
    {
        "item": "主持负责人",
        "quantity": 1.0
    },
    {
        "item": "工程监理 (甲方代表)",
        "quantity": 1.0
    },
    {
        "item": "科技与动态设计",
        "quantity": 1.0
    },
    {
        "item": "中央空调工程",
        "quantity": 1.0
    },
    {
        "item": "热机械系统",
        "quantity": 1.0
    },
    {
        "item": "室内及灯光设计",
        "quantity": 1.0
    },
    {
        "item": "建造监理",
        "quantity": 1.0
    },
    {
        "item": "环境方案",
        "quantity": 1.0
    },
    {
        "item": "当地设计部门",
        "quantity": 1.0
    },
    {
        "item": "陈设",
        "quantity": 1.0
    },
    {
        "item": "实施保障",
        "quantity": 1.0
    },
    {
        "item": "责任结构师",
        "quantity": 1.0
    },
    {
        "item": "单元面积",
        "quantity": 1.0
    },
    {
        "item": "建造年代",
        "quantity": 1.0
    },
    {
        "item": "现有面积",
        "quantity": 1.0
    },
    {
        "item": "里面顾问",
        "quantity": 1.0
    },
    {
        "item": "管道设计师",
        "quantity": 1.0
    },
    {
        "item": "石材制造商",
        "quantity": 1.0
    },
    {
        "item": "规划与建设管理",
        "quantity": 1.0
    },
    {
        "item": " 总承包人",
        "quantity": 1.0
    },
    {
        "item": "建筑合作方",
        "quantity": 1.0
    },
    {
        "item": "各层面积",
        "quantity": 1.0
    },
    {
        "item": "志愿者 调研者",
        "quantity": 1.0
    },
    {
        "item": "最大高度",
        "quantity": 1.0
    },
    {
        "item": "光水暖电工程师",
        "quantity": 1.0
    },
    {
        "item": "工作室主任",
        "quantity": 1.0
    },
    {
        "item": "种植",
        "quantity": 1.0
    },
    {
        "item": "M/E/P 工程师",
        "quantity": 1.0
    },
    {
        "item": "合同类型",
        "quantity": 1.0
    },
    {
        "item": "能源顾问 / Hers评级",
        "quantity": 1.0
    },
    {
        "item": "Urban Economist",
        "quantity": 1.0
    },
    {
        "item": "特派建筑师",
        "quantity": 1.0
    },
    {
        "item": "电话、安保、声学",
        "quantity": 1.0
    },
    {
        "item": "室内精装",
        "quantity": 1.0
    },
    {
        "item": "LDI ",
        "quantity": 1.0
    },
    {
        "item": "混凝土构建",
        "quantity": 1.0
    },
    {
        "item": "成本管理咨询",
        "quantity": 1.0
    },
    {
        "item": "项目团队 (LM Architectural Group)",
        "quantity": 1.0
    },
    {
        "item": "电气设备工程师",
        "quantity": 1.0
    },
    {
        "item": "效果图渲染",
        "quantity": 1.0
    },
    {
        "item": "Sustainability Coordinator",
        "quantity": 1.0
    },
    {
        "item": "工程监察及安全",
        "quantity": 1.0
    },
    {
        "item": "空气处理",
        "quantity": 1.0
    },
    {
        "item": "救生",
        "quantity": 1.0
    },
    {
        "item": "业主/委托人",
        "quantity": 1.0
    },
    {
        "item": "电器安装",
        "quantity": 1.0
    },
    {
        "item": "纽约创始人兼院长",
        "quantity": 1.0
    },
    {
        "item": "建筑承包",
        "quantity": 1.0
    },
    {
        "item": "机电设计顾问",
        "quantity": 1.0
    },
    {
        "item": "土木/岩土工程",
        "quantity": 1.0
    },
    {
        "item": "监管建筑师",
        "quantity": 1.0
    },
    {
        "item": "织物设计",
        "quantity": 1.0
    },
    {
        "item": "技术辅助",
        "quantity": 1.0
    },
    {
        "item": "展陈及景观平面设计 ",
        "quantity": 1.0
    },
    {
        "item": "安全服务承包商",
        "quantity": 1.0
    },
    {
        "item": "计划主管 ",
        "quantity": 1.0
    },
    {
        "item": "博物馆领导",
        "quantity": 1.0
    },
    {
        "item": "客户代理",
        "quantity": 1.0
    },
    {
        "item": "当地建筑师/项目经理",
        "quantity": 1.0
    },
    {
        "item": "服务 & ESD",
        "quantity": 1.0
    },
    {
        "item": "Estructuras",
        "quantity": 1.0
    },
    {
        "item": "餐厅项目",
        "quantity": 1.0
    },
    {
        "item": "施工日期",
        "quantity": 1.0
    },
    {
        "item": "举办单位",
        "quantity": 1.0
    },
    {
        "item": "视听承包商 ",
        "quantity": 1.0
    },
    {
        "item": "2006 2013 展览项目",
        "quantity": 1.0
    },
    {
        "item": "Interior architect",
        "quantity": 1.0
    },
    {
        "item": "集团首脑",
        "quantity": 1.0
    },
    {
        "item": "燃气",
        "quantity": 1.0
    },
    {
        "item": "玻璃装配顾问",
        "quantity": 1.0
    },
    {
        "item": "验收",
        "quantity": 1.0
    },
    {
        "item": "停车顾问",
        "quantity": 1.0
    },
    {
        "item": "德州团队",
        "quantity": 1.0
    },
    {
        "item": "I室内与景观设计",
        "quantity": 1.0
    },
    {
        "item": "展览设计与媒体内容",
        "quantity": 1.0
    },
    {
        "item": "地基和结构",
        "quantity": 1.0
    },
    {
        "item": "建造协助",
        "quantity": 1.0
    },
    {
        "item": "平均面积",
        "quantity": 1.0
    },
    {
        "item": "编外顾问",
        "quantity": 1.0
    },
    {
        "item": "设计和工程主管",
        "quantity": 1.0
    },
    {
        "item": "承包商/建筑商",
        "quantity": 1.0
    },
    {
        "item": "视频材料",
        "quantity": 1.0
    },
    {
        "item": "听觉设计师",
        "quantity": 1.0
    },
    {
        "item": "每平方米造价",
        "quantity": 1.0
    },
    {
        "item": "预算部门",
        "quantity": 1.0
    },
    {
        "item": "计算者",
        "quantity": 1.0
    },
    {
        "item": "Principal-in-Charge",
        "quantity": 1.0
    },
    {
        "item": "房间内装饰品",
        "quantity": 1.0
    },
    {
        "item": "委托建筑师",
        "quantity": 1.0
    },
    {
        "item": "工程师团队",
        "quantity": 1.0
    },
    {
        "item": "电力供应",
        "quantity": 1.0
    },
    {
        "item": "建造总价",
        "quantity": 1.0
    },
    {
        "item": "程序设计师",
        "quantity": 1.0
    },
    {
        "item": "Electric Instalations",
        "quantity": 1.0
    },
    {
        "item": "标识/制图",
        "quantity": 1.0
    },
    {
        "item": "Fondazione 建筑面积 ",
        "quantity": 1.0
    },
    {
        "item": "操场安全顾问",
        "quantity": 1.0
    },
    {
        "item": "木工工程",
        "quantity": 1.0
    },
    {
        "item": "Students From Aalto University",
        "quantity": 1.0
    },
    {
        "item": "内部伙伴",
        "quantity": 1.0
    },
    {
        "item": "水泥基面设计",
        "quantity": 1.0
    },
    {
        "item": "Team Leaders (Professors)",
        "quantity": 1.0
    },
    {
        "item": "生态生产",
        "quantity": 1.0
    },
    {
        "item": "设计和项目主管",
        "quantity": 1.0
    },
    {
        "item": "建筑师领导",
        "quantity": 1.0
    },
    {
        "item": "细部设计顾问",
        "quantity": 1.0
    },
    {
        "item": "医务指导",
        "quantity": 1.0
    },
    {
        "item": "多媒体与音效设计",
        "quantity": 1.0
    },
    {
        "item": "承包价值",
        "quantity": 1.0
    },
    {
        "item": "混凝土工程承包商/生产商",
        "quantity": 1.0
    },
    {
        "item": "流体与热工程",
        "quantity": 1.0
    },
    {
        "item": "项目进度",
        "quantity": 1.0
    },
    {
        "item": "Geothecnic",
        "quantity": 1.0
    },
    {
        "item": "酒店结构",
        "quantity": 1.0
    },
    {
        "item": "车库结构",
        "quantity": 1.0
    },
    {
        "item": "城设合作",
        "quantity": 1.0
    },
    {
        "item": "展品制作人",
        "quantity": 1.0
    },
    {
        "item": "机械、液压和消防工程设计",
        "quantity": 1.0
    },
    {
        "item": "微桩",
        "quantity": 1.0
    },
    {
        "item": "三维渲染",
        "quantity": 1.0
    },
    {
        "item": "结构、立面与参数设计",
        "quantity": 1.0
    },
    {
        "item": "Assisting Architect",
        "quantity": 1.0
    },
    {
        "item": "景观生态设计师",
        "quantity": 1.0
    },
    {
        "item": "景观项目设计师",
        "quantity": 1.0
    },
    {
        "item": "照明装置",
        "quantity": 1.0
    },
    {
        "item": "建筑基底面积",
        "quantity": 1.0
    },
    {
        "item": "动物园技术顾问",
        "quantity": 1.0
    },
    {
        "item": "机械 / 电气工程师",
        "quantity": 1.0
    },
    {
        "item": "心理学顾问",
        "quantity": 1.0
    },
    {
        "item": "商店概念生成及创意指导",
        "quantity": 1.0
    },
    {
        "item": "服务咨询",
        "quantity": 1.0
    },
    {
        "item": "合作负责人",
        "quantity": 1.0
    },
    {
        "item": "外墙施工",
        "quantity": 1.0
    },
    {
        "item": "墙画设计",
        "quantity": 1.0
    },
    {
        "item": "服装设计师",
        "quantity": 1.0
    },
    {
        "item": "电子设备工程师",
        "quantity": 1.0
    },
    {
        "item": "酒店客房家具提供",
        "quantity": 1.0
    },
    {
        "item": "木框架结构",
        "quantity": 1.0
    },
    {
        "item": "砖瓦工",
        "quantity": 1.0
    },
    {
        "item": "Sharon工作室团队",
        "quantity": 1.0
    },
    {
        "item": "业主和资助人",
        "quantity": 1.0
    },
    {
        "item": "FRENTE / RVDG 团队",
        "quantity": 1.0
    },
    {
        "item": "引用",
        "quantity": 1.0
    },
    {
        "item": "热及流体",
        "quantity": 1.0
    },
    {
        "item": "校长",
        "quantity": 1.0
    },
    {
        "item": "项目建设费",
        "quantity": 1.0
    },
    {
        "item": "混凝土结构工程",
        "quantity": 1.0
    },
    {
        "item": "监管与测量站",
        "quantity": 1.0
    },
    {
        "item": "设计和项目团队",
        "quantity": 1.0
    },
    {
        "item": "LAVA",
        "quantity": 1.0
    },
    {
        "item": "保安",
        "quantity": 1.0
    },
    {
        "item": "防火工程师 ",
        "quantity": 1.0
    },
    {
        "item": " 制作人",
        "quantity": 1.0
    },
    {
        "item": "来源",
        "quantity": 1.0
    },
    {
        "item": "标志建造",
        "quantity": 1.0
    },
    {
        "item": "项目经理／设计人",
        "quantity": 1.0
    },
    {
        "item": "说明",
        "quantity": 1.0
    },
    {
        "item": "葡萄牙事务所",
        "quantity": 1.0
    },
    {
        "item": "国标顾问",
        "quantity": 1.0
    },
    {
        "item": "管道和电气工程师",
        "quantity": 1.0
    },
    {
        "item": "物理专家",
        "quantity": 1.0
    },
    {
        "item": "气候环境咨询",
        "quantity": 1.0
    },
    {
        "item": "Caixilharia",
        "quantity": 1.0
    },
    {
        "item": "集合储藏",
        "quantity": 1.0
    },
    {
        "item": "设计合作伙伴负责人",
        "quantity": 1.0
    },
    {
        "item": "工地工程师",
        "quantity": 1.0
    },
    {
        "item": "共同筹资",
        "quantity": 1.0
    },
    {
        "item": "结构工程师 / BLAST",
        "quantity": 1.0
    },
    {
        "item": "统筹协调和可持续性",
        "quantity": 1.0
    },
    {
        "item": "游戏场设计",
        "quantity": 1.0
    },
    {
        "item": "支撑顾问",
        "quantity": 1.0
    },
    {
        "item": "城市项目开发",
        "quantity": 1.0
    },
    {
        "item": "表皮工程",
        "quantity": 1.0
    },
    {
        "item": "工头",
        "quantity": 1.0
    },
    {
        "item": "刚劲混凝土结构工程师",
        "quantity": 1.0
    },
    {
        "item": "ICT 工程",
        "quantity": 1.0
    },
    {
        "item": "首席赞助商",
        "quantity": 1.0
    },
    {
        "item": "机电管道塑料工程",
        "quantity": 1.0
    },
    {
        "item": "能效及立面工程",
        "quantity": 1.0
    },
    {
        "item": "电力和机械",
        "quantity": 1.0
    },
    {
        "item": "技术架构师",
        "quantity": 1.0
    },
    {
        "item": "生物气候系统",
        "quantity": 1.0
    },
    {
        "item": "热学工程师",
        "quantity": 1.0
    },
    {
        "item": "电子工程顾问",
        "quantity": 1.0
    },
    {
        "item": "舞台",
        "quantity": 1.0
    },
    {
        "item": "设计合作者和施工监督",
        "quantity": 1.0
    },
    {
        "item": "一楼接待处",
        "quantity": 1.0
    },
    {
        "item": "建筑及设计师",
        "quantity": 1.0
    },
    {
        "item": "项目采用的产品",
        "quantity": 1.0
    },
    {
        "item": "设计故责人",
        "quantity": 1.0
    },
    {
        "item": "娱乐和酒店负责人",
        "quantity": 1.0
    },
    {
        "item": "咨询商",
        "quantity": 1.0
    },
    {
        "item": "水泵",
        "quantity": 1.0
    },
    {
        "item": "形式",
        "quantity": 1.0
    },
    {
        "item": "BIM 协调员",
        "quantity": 1.0
    },
    {
        "item": "Principle Architect",
        "quantity": 1.0
    },
    {
        "item": "玻璃制造商",
        "quantity": 1.0
    },
    {
        "item": "给排水/电力",
        "quantity": 1.0
    },
    {
        "item": "Installationa Engineer",
        "quantity": 1.0
    },
    {
        "item": "机械和管道工程师",
        "quantity": 1.0
    },
    {
        "item": "凤梨科植物捐款",
        "quantity": 1.0
    },
    {
        "item": "艺术管理",
        "quantity": 1.0
    },
    {
        "item": "室内装饰合作者",
        "quantity": 1.0
    },
    {
        "item": "Date design",
        "quantity": 1.0
    },
    {
        "item": "水文服务",
        "quantity": 1.0
    },
    {
        "item": "专家",
        "quantity": 1.0
    },
    {
        "item": "项目＋工作指导",
        "quantity": 1.0
    },
    {
        "item": "二层平面面积",
        "quantity": 1.0
    },
    {
        "item": "评委访客",
        "quantity": 1.0
    },
    {
        "item": "John Lewis",
        "quantity": 1.0
    },
    {
        "item": "Asociados",
        "quantity": 1.0
    },
    {
        "item": "Electrical Consultant",
        "quantity": 1.0
    },
    {
        "item": "能源/标题24",
        "quantity": 1.0
    },
    {
        "item": "建造咨询",
        "quantity": 1.0
    },
    {
        "item": "力学电力咨询",
        "quantity": 1.0
    },
    {
        "item": "建造以及地产",
        "quantity": 1.0
    },
    {
        "item": "主任合作者",
        "quantity": 1.0
    },
    {
        "item": "客户/发起人",
        "quantity": 1.0
    },
    {
        "item": "Text by",
        "quantity": 1.0
    },
    {
        "item": "开发商/设计施工总承包",
        "quantity": 1.0
    },
    {
        "item": "声效顾问",
        "quantity": 1.0
    },
    {
        "item": "实验室咨询师",
        "quantity": 1.0
    },
    {
        "item": "运营团队",
        "quantity": 1.0
    },
    {
        "item": "使用者 \t",
        "quantity": 1.0
    },
    {
        "item": "顾问计划师",
        "quantity": 1.0
    },
    {
        "item": "项目室内面积",
        "quantity": 1.0
    },
    {
        "item": "LEED ",
        "quantity": 1.0
    },
    {
        "item": "主建筑师, Architect SAFA, 合伙人",
        "quantity": 1.0
    },
    {
        "item": "建筑协调员",
        "quantity": 1.0
    },
    {
        "item": "设计师、建筑师与艺术家",
        "quantity": 1.0
    },
    {
        "item": "总体规划与建筑",
        "quantity": 1.0
    },
    {
        "item": "外立面设计",
        "quantity": 1.0
    },
    {
        "item": "排水工程",
        "quantity": 1.0
    },
    {
        "item": "场地主管",
        "quantity": 1.0
    },
    {
        "item": "建造合作",
        "quantity": 1.0
    },
    {
        "item": "工作管理",
        "quantity": 1.0
    },
    {
        "item": "计划咨询",
        "quantity": 1.0
    },
    {
        "item": "出资人",
        "quantity": 1.0
    },
    {
        "item": "管理与监理",
        "quantity": 1.0
    },
    {
        "item": "地质",
        "quantity": 1.0
    },
    {
        "item": "视听教具",
        "quantity": 1.0
    },
    {
        "item": "独立审计师",
        "quantity": 1.0
    },
    {
        "item": "[\"Casey Chua\", \"Casey Chua\"]",
        "quantity": 1.0
    },
    {
        "item": "展览设计师",
        "quantity": 1.0
    },
    {
        "item": "无障碍环境",
        "quantity": 1.0
    },
    {
        "item": "建筑覆盖率",
        "quantity": 1.0
    },
    {
        "item": "Stayokay 室内",
        "quantity": 1.0
    },
    {
        "item": "设计合作事务所",
        "quantity": 1.0
    },
    {
        "item": "建筑容积率",
        "quantity": 1.0
    },
    {
        "item": "主承包商/施工单位",
        "quantity": 1.0
    },
    {
        "item": "照明和家庭自动化系统",
        "quantity": 1.0
    },
    {
        "item": "Construction Economist",
        "quantity": 1.0
    },
    {
        "item": "主创建筑师 ",
        "quantity": 1.0
    },
    {
        "item": "可行性研究工作人员",
        "quantity": 1.0
    },
    {
        "item": "概念设计——设计开发",
        "quantity": 1.0
    },
    {
        "item": "责任设计师",
        "quantity": 1.0
    },
    {
        "item": "管理工程师",
        "quantity": 1.0
    },
    {
        "item": "音响视屏",
        "quantity": 1.0
    },
    {
        "item": "室内设计和家具设计",
        "quantity": 1.0
    },
    {
        "item": "金属结构建造方",
        "quantity": 1.0
    },
    {
        "item": "动画合作",
        "quantity": 1.0
    },
    {
        "item": "热工系统",
        "quantity": 1.0
    },
    {
        "item": "钢结构顾问",
        "quantity": 1.0
    },
    {
        "item": "施工现场监督",
        "quantity": 1.0
    },
    {
        "item": "联合事务所",
        "quantity": 1.0
    },
    {
        "item": "Students from The Corcoran College of Art & Design",
        "quantity": 1.0
    },
    {
        "item": "历史学家",
        "quantity": 1.0
    },
    {
        "item": "纽约项目团队经理",
        "quantity": 1.0
    },
    {
        "item": "改造面积",
        "quantity": 1.0
    },
    {
        "item": "Project Team of Project Mingde",
        "quantity": 1.0
    },
    {
        "item": "机械和混凝土结构工程师",
        "quantity": 1.0
    },
    {
        "item": "土地测量",
        "quantity": 1.0
    },
    {
        "item": "总承包商/项目经理",
        "quantity": 1.0
    },
    {
        "item": "石结构",
        "quantity": 1.0
    },
    {
        "item": "ZHA项目团队",
        "quantity": 1.0
    },
    {
        "item": "铝节点",
        "quantity": 1.0
    },
    {
        "item": "社区协商和短暂发展",
        "quantity": 1.0
    },
    {
        "item": "覆盖室外面积",
        "quantity": 1.0
    },
    {
        "item": "设计助理/项目经理",
        "quantity": 1.0
    },
    {
        "item": "廊架面积",
        "quantity": 1.0
    },
    {
        "item": "土木及结构",
        "quantity": 1.0
    },
    {
        "item": "预算 & 管理顾问",
        "quantity": 1.0
    },
    {
        "item": "服务范围",
        "quantity": 1.0
    },
    {
        "item": "机械／电子工程",
        "quantity": 1.0
    },
    {
        "item": "扎哈·哈迪德设计团队",
        "quantity": 1.0
    },
    {
        "item": "运行地址",
        "quantity": 1.0
    },
    {
        "item": "电",
        "quantity": 1.0
    },
    {
        "item": "住宅公寓1 (首层+第二层)",
        "quantity": 1.0
    },
    {
        "item": "外观设计和施工",
        "quantity": 1.0
    },
    {
        "item": "项目考古",
        "quantity": 1.0
    },
    {
        "item": "客户/项目",
        "quantity": 1.0
    },
    {
        "item": "室内完成",
        "quantity": 1.0
    },
    {
        "item": "声学顾问，吸音板供应",
        "quantity": 1.0
    },
    {
        "item": "金属建筑工程",
        "quantity": 1.0
    },
    {
        "item": "项目检验",
        "quantity": 1.0
    },
    {
        "item": "Leed顾问",
        "quantity": 1.0
    },
    {
        "item": "主建筑师与创意总监",
        "quantity": 1.0
    },
    {
        "item": "防水工程师",
        "quantity": 1.0
    },
    {
        "item": "现场施工指导",
        "quantity": 1.0
    },
    {
        "item": "Lights",
        "quantity": 1.0
    },
    {
        "item": "艺术顾问(展览设计) 和制图",
        "quantity": 1.0
    },
    {
        "item": "结构承包商",
        "quantity": 1.0
    },
    {
        "item": "材料预算",
        "quantity": 1.0
    },
    {
        "item": "Lead-glass Restorer",
        "quantity": 1.0
    },
    {
        "item": "保温设计",
        "quantity": 1.0
    },
    {
        "item": "玻璃纤维结构",
        "quantity": 1.0
    },
    {
        "item": "竞赛员工",
        "quantity": 1.0
    },
    {
        "item": "洁具设施",
        "quantity": 1.0
    },
    {
        "item": "扶手与护栏",
        "quantity": 1.0
    },
    {
        "item": "所有者代表",
        "quantity": 1.0
    },
    {
        "item": "玻璃设计",
        "quantity": 1.0
    },
    {
        "item": "城市遗产规划者",
        "quantity": 1.0
    },
    {
        "item": "内部装修",
        "quantity": 1.0
    },
    {
        "item": "AV/安全",
        "quantity": 1.0
    },
    {
        "item": "分承包商",
        "quantity": 1.0
    },
    {
        "item": "设计&施工",
        "quantity": 1.0
    },
    {
        "item": "委托方  ",
        "quantity": 1.0
    },
    {
        "item": "法规咨询",
        "quantity": 1.0
    },
    {
        "item": "检验工程师",
        "quantity": 1.0
    },
    {
        "item": "施工队顾问",
        "quantity": 1.0
    },
    {
        "item": "服务工程  ",
        "quantity": 1.0
    },
    {
        "item": "C＆S工程师",
        "quantity": 1.0
    },
    {
        "item": "主持建筑师（建筑设计、室内设计）",
        "quantity": 1.0
    },
    {
        "item": "建筑管理系统",
        "quantity": 1.0
    },
    {
        "item": "声学工程  ",
        "quantity": 1.0
    },
    {
        "item": "设计咨询商",
        "quantity": 1.0
    },
    {
        "item": "创始合伙人",
        "quantity": 1.0
    },
    {
        "item": "展示",
        "quantity": 1.0
    },
    {
        "item": "维护工程师",
        "quantity": 1.0
    },
    {
        "item": "结构构造",
        "quantity": 1.0
    },
    {
        "item": "景观设计单位",
        "quantity": 1.0
    },
    {
        "item": "策略顾问",
        "quantity": 1.0
    },
    {
        "item": "合作中方建筑师",
        "quantity": 1.0
    },
    {
        "item": "项目背景",
        "quantity": 1.0
    },
    {
        "item": "室外材料",
        "quantity": 1.0
    },
    {
        "item": "预算租用",
        "quantity": 1.0
    },
    {
        "item": "Shell Arquitectos Shell Arquitectos Shell Arquitectos Shell Arquitectos Shell Arquitectos Shell Arquitectos Shell Arquitectos Shell Arquitectos Shell Arquitectos",
        "quantity": 1.0
    },
    {
        "item": "基本设计",
        "quantity": 1.0
    },
    {
        "item": "景观工程监理",
        "quantity": 1.0
    },
    {
        "item": "重木结构工程师",
        "quantity": 1.0
    },
    {
        "item": "一层建筑面积",
        "quantity": 1.0
    },
    {
        "item": "造价预算师",
        "quantity": 1.0
    },
    {
        "item": "室外完成",
        "quantity": 1.0
    },
    {
        "item": "面积: 山地自行车奥林匹克公园",
        "quantity": 1.0
    },
    {
        "item": "装配公司",
        "quantity": 1.0
    },
    {
        "item": "搭建技术",
        "quantity": 1.0
    },
    {
        "item": "大致建筑价格",
        "quantity": 1.0
    },
    {
        "item": "项目占地",
        "quantity": 1.0
    },
    {
        "item": "精细木工",
        "quantity": 1.0
    },
    {
        "item": "3D 模型师",
        "quantity": 1.0
    },
    {
        "item": "室内设计 (客人房间)",
        "quantity": 1.0
    },
    {
        "item": "系统化",
        "quantity": 1.0
    },
    {
        "item": "设计和执行团队",
        "quantity": 1.0
    },
    {
        "item": "金属天花板系统",
        "quantity": 1.0
    },
    {
        "item": "外观设计与优化顾问",
        "quantity": 1.0
    },
    {
        "item": "设计与施工",
        "quantity": 1.0
    },
    {
        "item": "建筑事务所合伙人",
        "quantity": 1.0
    },
    {
        "item": "木料胶合板",
        "quantity": 1.0
    },
    {
        "item": "液压喷播",
        "quantity": 1.0
    },
    {
        "item": "结构机械",
        "quantity": 1.0
    },
    {
        "item": "总经理建筑师",
        "quantity": 1.0
    },
    {
        "item": "Mobiliario",
        "quantity": 1.0
    },
    {
        "item": "图形标示设计师",
        "quantity": 1.0
    },
    {
        "item": "环境标识设计 ",
        "quantity": 1.0
    },
    {
        "item": "屋顶工程师",
        "quantity": 1.0
    },
    {
        "item": "Team Members",
        "quantity": 1.0
    },
    {
        "item": "金额",
        "quantity": 1.0
    },
    {
        "item": "可用面积",
        "quantity": 1.0
    },
    {
        "item": "新表面积",
        "quantity": 1.0
    },
    {
        "item": "平面设计，标志和艺术品",
        "quantity": 1.0
    },
    {
        "item": "结构与植物",
        "quantity": 1.0
    },
    {
        "item": "结构和基础设计",
        "quantity": 1.0
    },
    {
        "item": "能源效率",
        "quantity": 1.0
    },
    {
        "item": "海水",
        "quantity": 1.0
    },
    {
        "item": "胶合木",
        "quantity": 1.0
    },
    {
        "item": "场地规模",
        "quantity": 1.0
    },
    {
        "item": "产品团队",
        "quantity": 1.0
    },
    {
        "item": "微弱电流",
        "quantity": 1.0
    },
    {
        "item": "原始面积",
        "quantity": 1.0
    },
    {
        "item": "土木建设",
        "quantity": 1.0
    },
    {
        "item": "质量检验员",
        "quantity": 1.0
    },
    {
        "item": "三维技术",
        "quantity": 1.0
    },
    {
        "item": "设计 施工承包商",
        "quantity": 1.0
    },
    {
        "item": "主管系统结构设计师",
        "quantity": 1.0
    },
    {
        "item": "制造和材料开发",
        "quantity": 1.0
    },
    {
        "item": "高级室内设计师",
        "quantity": 1.0
    },
    {
        "item": "结构设计助理",
        "quantity": 1.0
    },
    {
        "item": "比赛战队 ",
        "quantity": 1.0
    },
    {
        "item": "屋顶建造",
        "quantity": 1.0
    },
    {
        "item": "主管负责人",
        "quantity": 1.0
    },
    {
        "item": "合作外观设计",
        "quantity": 1.0
    },
    {
        "item": "设备承包商",
        "quantity": 1.0
    },
    {
        "item": "外部设计",
        "quantity": 1.0
    },
    {
        "item": "建筑／室内设计／景观",
        "quantity": 1.0
    },
    {
        "item": "建筑物理，消防，声学顾问",
        "quantity": 1.0
    },
    {
        "item": "项目价值",
        "quantity": 1.0
    },
    {
        "item": "MEP Design",
        "quantity": 1.0
    },
    {
        "item": "协调方",
        "quantity": 1.0
    },
    {
        "item": "机械/水暖工程师",
        "quantity": 1.0
    },
    {
        "item": "走过建筑面积",
        "quantity": 1.0
    },
    {
        "item": "Total Cost ",
        "quantity": 1.0
    },
    {
        "item": "竹子工程",
        "quantity": 1.0
    },
    {
        "item": "制图学家",
        "quantity": 1.0
    },
    {
        "item": "区域",
        "quantity": 1.0
    },
    {
        "item": "初步构想方案",
        "quantity": 1.0
    },
    {
        "item": "Architecture Team",
        "quantity": 1.0
    },
    {
        "item": "合规顾问",
        "quantity": 1.0
    },
    {
        "item": "安全咨询",
        "quantity": 1.0
    },
    {
        "item": "加热制冷及电力",
        "quantity": 1.0
    },
    {
        "item": "结构施工",
        "quantity": 1.0
    },
    {
        "item": "设计体验",
        "quantity": 1.0
    },
    {
        "item": "建筑服务公司",
        "quantity": 1.0
    },
    {
        "item": "窗户框架",
        "quantity": 1.0
    },
    {
        "item": "土木、机械和电气工程师",
        "quantity": 1.0
    },
    {
        "item": "建筑师／室内设计",
        "quantity": 1.0
    },
    {
        "item": "土木/景观工程哈斯",
        "quantity": 1.0
    },
    {
        "item": "外壳面积",
        "quantity": 1.0
    },
    {
        "item": "餐厅顾问",
        "quantity": 1.0
    },
    {
        "item": "结构工程师 (公司名称)",
        "quantity": 1.0
    },
    {
        "item": "资金支持",
        "quantity": 1.0
    },
    {
        "item": "主要承包人(公司名称)",
        "quantity": 1.0
    },
    {
        "item": "市政与结构工程",
        "quantity": 1.0
    },
    {
        "item": "MEP 工程 ",
        "quantity": 1.0
    },
    {
        "item": "能源模型",
        "quantity": 1.0
    },
    {
        "item": "音响通讯设计",
        "quantity": 1.0
    },
    {
        "item": "基地建筑师",
        "quantity": 1.0
    },
    {
        "item": "家具制作者",
        "quantity": 1.0
    },
    {
        "item": "木作(公司名称) ",
        "quantity": 1.0
    },
    {
        "item": "北侧办公区域面积",
        "quantity": 1.0
    },
    {
        "item": "项目领导 (Agence Frédéric Nicolas)",
        "quantity": 1.0
    },
    {
        "item": "可丽耐",
        "quantity": 1.0
    },
    {
        "item": "预制钢结构",
        "quantity": 1.0
    },
    {
        "item": "事务所",
        "quantity": 1.0
    },
    {
        "item": "电动",
        "quantity": 1.0
    },
    {
        "item": "项目完成",
        "quantity": 1.0
    },
    {
        "item": "机电设计顾问 ",
        "quantity": 1.0
    },
    {
        "item": "学生宿舍",
        "quantity": 1.0
    },
    {
        "item": "景观与庭院设计",
        "quantity": 1.0
    },
    {
        "item": "结构与土木工程",
        "quantity": 1.0
    },
    {
        "item": "Accessibility",
        "quantity": 1.0
    },
    {
        "item": "工程/能源服务",
        "quantity": 1.0
    },
    {
        "item": "三维可视化",
        "quantity": 1.0
    },
    {
        "item": "里维拉风景设计",
        "quantity": 1.0
    },
    {
        "item": "机械、电力、消防",
        "quantity": 1.0
    },
    {
        "item": "合伙方",
        "quantity": 1.0
    },
    {
        "item": "预制板",
        "quantity": 1.0
    },
    {
        "item": "声学和剧场顾问",
        "quantity": 1.0
    },
    {
        "item": "BIM 经理",
        "quantity": 1.0
    },
    {
        "item": "估计师",
        "quantity": 1.0
    },
    {
        "item": "Costructive Company",
        "quantity": 1.0
    },
    {
        "item": "地段总管",
        "quantity": 1.0
    },
    {
        "item": "人行道",
        "quantity": 1.0
    },
    {
        "item": "室内地板， 纳米漆, 环氧树脂",
        "quantity": 1.0
    },
    {
        "item": "建造类型",
        "quantity": 1.0
    },
    {
        "item": "防御设计师",
        "quantity": 1.0
    },
    {
        "item": "集装箱系统",
        "quantity": 1.0
    },
    {
        "item": "合作牵头设计师",
        "quantity": 1.0
    },
    {
        "item": "当地团队",
        "quantity": 1.0
    },
    {
        "item": "结构安装",
        "quantity": 1.0
    },
    {
        "item": "可行性项目",
        "quantity": 1.0
    },
    {
        "item": "建筑承建商",
        "quantity": 1.0
    },
    {
        "item": "摄像师",
        "quantity": 1.0
    },
    {
        "item": "Cooper Robertson 设计团队",
        "quantity": 1.0
    },
    {
        "item": "预算评估",
        "quantity": 1.0
    },
    {
        "item": "Sructural Engineer",
        "quantity": 1.0
    },
    {
        "item": "总占地面积（四栋建筑之一）",
        "quantity": 1.0
    },
    {
        "item": "架构师负责",
        "quantity": 1.0
    },
    {
        "item": "水电设备",
        "quantity": 1.0
    },
    {
        "item": "声学研究部门",
        "quantity": 1.0
    },
    {
        "item": "景观项目负责人",
        "quantity": 1.0
    },
    {
        "item": "建设面积",
        "quantity": 1.0
    },
    {
        "item": "电器以及卫浴配备",
        "quantity": 1.0
    },
    {
        "item": "装置工程师",
        "quantity": 1.0
    },
    {
        "item": "路径总长度",
        "quantity": 1.0
    },
    {
        "item": "建筑工程副秘书长",
        "quantity": 1.0
    },
    {
        "item": "室内总承包",
        "quantity": 1.0
    },
    {
        "item": "安装工程 ",
        "quantity": 1.0
    },
    {
        "item": "声学研究办公室",
        "quantity": 1.0
    },
    {
        "item": "Coordinadores de Proyecto",
        "quantity": 1.0
    },
    {
        "item": "负责合作者",
        "quantity": 1.0
    },
    {
        "item": "主任联合",
        "quantity": 1.0
    },
    {
        "item": "表皮工程师",
        "quantity": 1.0
    },
    {
        "item": "承包商/Cmar",
        "quantity": 1.0
    },
    {
        "item": "延伸综合体面积",
        "quantity": 1.0
    },
    {
        "item": "砌体",
        "quantity": 1.0
    },
    {
        "item": "项目联络人",
        "quantity": 1.0
    },
    {
        "item": "大保屯统筹人员",
        "quantity": 1.0
    },
    {
        "item": "传播、IT、安防与特殊系统",
        "quantity": 1.0
    },
    {
        "item": "建设合伙人",
        "quantity": 1.0
    },
    {
        "item": "公众健康服务",
        "quantity": 1.0
    },
    {
        "item": "Theatre Planning",
        "quantity": 1.0
    },
    {
        "item": "冷却",
        "quantity": 1.0
    },
    {
        "item": "舞台帷幔",
        "quantity": 1.0
    },
    {
        "item": "加热",
        "quantity": 1.0
    },
    {
        "item": "操作跟踪",
        "quantity": 1.0
    },
    {
        "item": "技术研究团队",
        "quantity": 1.0
    },
    {
        "item": "RA-DA 设计团队",
        "quantity": 1.0
    },
    {
        "item": "职业设计师",
        "quantity": 1.0
    },
    {
        "item": "结构经理",
        "quantity": 1.0
    },
    {
        "item": "专业灯具照明",
        "quantity": 1.0
    },
    {
        "item": "电气/机械工程师",
        "quantity": 1.0
    },
    {
        "item": "机/电/水工程师",
        "quantity": 1.0
    },
    {
        "item": "机械、电气、水暖",
        "quantity": 1.0
    },
    {
        "item": "博物馆功能顾问",
        "quantity": 1.0
    },
    {
        "item": "电气/机械/管道工程师",
        "quantity": 1.0
    },
    {
        "item": "喷泉分包商",
        "quantity": 1.0
    },
    {
        "item": "3D设计",
        "quantity": 1.0
    },
    {
        "item": "设计架构师",
        "quantity": 1.0
    },
    {
        "item": "大楼控制系统",
        "quantity": 1.0
    },
    {
        "item": "建筑架构",
        "quantity": 1.0
    },
    {
        "item": "室内标识顾问",
        "quantity": 1.0
    },
    {
        "item": "工程监督",
        "quantity": 1.0
    },
    {
        "item": "雨水工程",
        "quantity": 1.0
    },
    {
        "item": "意见书建筑师",
        "quantity": 1.0
    },
    {
        "item": "图片来源(建造)",
        "quantity": 1.0
    },
    {
        "item": "Marin + Trottin团队",
        "quantity": 1.0
    },
    {
        "item": "Civil And Structural Engineer",
        "quantity": 1.0
    },
    {
        "item": "工程电缆网和及结构",
        "quantity": 1.0
    },
    {
        "item": "设备项目",
        "quantity": 1.0
    },
    {
        "item": "项目经理 & 施工监理",
        "quantity": 1.0
    },
    {
        "item": "窗帘设计",
        "quantity": 1.0
    },
    {
        "item": "SpaceMatters设计团队",
        "quantity": 1.0
    },
    {
        "item": "技术架构工程师 ",
        "quantity": 1.0
    },
    {
        "item": "追加结构规划\t",
        "quantity": 1.0
    },
    {
        "item": "项目/指导",
        "quantity": 1.0
    },
    {
        "item": "M.E.P.设计",
        "quantity": 1.0
    },
    {
        "item": "生态设计 ",
        "quantity": 1.0
    },
    {
        "item": "工程师（原理图设计，设计开发）",
        "quantity": 1.0
    },
    {
        "item": "Civil and Structural Engineers",
        "quantity": 1.0
    },
    {
        "item": "室内设计及家具",
        "quantity": 1.0
    },
    {
        "item": "Technical consultants",
        "quantity": 1.0
    },
    {
        "item": "第三方调试",
        "quantity": 1.0
    },
    {
        "item": "施工安全",
        "quantity": 1.0
    },
    {
        "item": "Supervision",
        "quantity": 1.0
    },
    {
        "item": "经营者",
        "quantity": 1.0
    },
    {
        "item": "景观与室内设计",
        "quantity": 1.0
    },
    {
        "item": "Project Coordinator",
        "quantity": 1.0
    },
    {
        "item": "固态废弃物",
        "quantity": 1.0
    },
    {
        "item": "健康安全计划",
        "quantity": 1.0
    },
    {
        "item": "玻璃装配",
        "quantity": 1.0
    },
    {
        "item": "香味顾问",
        "quantity": 1.0
    },
    {
        "item": "移动表皮",
        "quantity": 1.0
    },
    {
        "item": "固定表皮",
        "quantity": 1.0
    },
    {
        "item": "设计方",
        "quantity": 1.0
    },
    {
        "item": "建筑系统工程",
        "quantity": 1.0
    },
    {
        "item": "Mechanical / Electrical",
        "quantity": 1.0
    },
    {
        "item": "Water and Sewerage",
        "quantity": 1.0
    },
    {
        "item": "建筑灯光",
        "quantity": 1.0
    },
    {
        "item": "记录",
        "quantity": 1.0
    },
    {
        "item": "热效率工程师",
        "quantity": 1.0
    },
    {
        "item": "机场建筑师",
        "quantity": 1.0
    },
    {
        "item": "副总建筑师 ",
        "quantity": 1.0
    },
    {
        "item": "进度计划",
        "quantity": 1.0
    },
    {
        "item": "特种结构设计",
        "quantity": 1.0
    },
    {
        "item": "工程专家",
        "quantity": 1.0
    },
    {
        "item": "立面评估工程",
        "quantity": 1.0
    },
    {
        "item": "气候，声学和安全",
        "quantity": 1.0
    },
    {
        "item": "模块化系统",
        "quantity": 1.0
    },
    {
        "item": "一期",
        "quantity": 1.0
    },
    {
        "item": "生态工程",
        "quantity": 1.0
    },
    {
        "item": "文献参考",
        "quantity": 1.0
    },
    {
        "item": "建筑师工程师（项目总监）",
        "quantity": 1.0
    },
    {
        "item": "安装 (电气，水力，空调系统）",
        "quantity": 1.0
    },
    {
        "item": "项目和成本管理",
        "quantity": 1.0
    },
    {
        "item": "Civil Engineering",
        "quantity": 1.0
    },
    {
        "item": "团队主要成员",
        "quantity": 1.0
    },
    {
        "item": "升学顾问",
        "quantity": 1.0
    },
    {
        "item": "剧场与声效顾问",
        "quantity": 1.0
    },
    {
        "item": "喷泉",
        "quantity": 1.0
    },
    {
        "item": "承包单位",
        "quantity": 1.0
    },
    {
        "item": "建筑平面",
        "quantity": 1.0
    },
    {
        "item": "设计发展建筑师",
        "quantity": 1.0
    },
    {
        "item": "刚要",
        "quantity": 1.0
    },
    {
        "item": "房屋承包商",
        "quantity": 1.0
    },
    {
        "item": "表面处理",
        "quantity": 1.0
    },
    {
        "item": "绿色屋顶顾问",
        "quantity": 1.0
    },
    {
        "item": "自动控制",
        "quantity": 1.0
    },
    {
        "item": "混凝土结构设计",
        "quantity": 1.0
    },
    {
        "item": "供热",
        "quantity": 1.0
    },
    {
        "item": "主任领导",
        "quantity": 1.0
    },
    {
        "item": "理念",
        "quantity": 1.0
    },
    {
        "item": "湖",
        "quantity": 1.0
    },
    {
        "item": "项目经济",
        "quantity": 1.0
    },
    {
        "item": "工程 ",
        "quantity": 1.0
    },
    {
        "item": "景观美化",
        "quantity": 1.0
    },
    {
        "item": "层压木",
        "quantity": 1.0
    },
    {
        "item": "创意原创",
        "quantity": 1.0
    },
    {
        "item": "检验师",
        "quantity": 1.0
    },
    {
        "item": "Iredale Pedersen Hook Architects事务所团队",
        "quantity": 1.0
    },
    {
        "item": "自动系统",
        "quantity": 1.0
    },
    {
        "item": "Chef de chantier",
        "quantity": 1.0
    },
    {
        "item": "日光分析",
        "quantity": 1.0
    },
    {
        "item": "工地监理",
        "quantity": 1.0
    },
    {
        "item": "理念设计师",
        "quantity": 1.0
    },
    {
        "item": "合作者 － S",
        "quantity": 1.0
    },
    {
        "item": "平面设计 ",
        "quantity": 1.0
    },
    {
        "item": "总外部面积",
        "quantity": 1.0
    },
    {
        "item": "特殊顾问",
        "quantity": 1.0
    },
    {
        "item": "效果图绘制",
        "quantity": 1.0
    },
    {
        "item": "制造年份",
        "quantity": 1.0
    },
    {
        "item": "场地覆盖率",
        "quantity": 1.0
    },
    {
        "item": "电气卫生服务",
        "quantity": 1.0
    },
    {
        "item": "结构和地基",
        "quantity": 1.0
    },
    {
        "item": "设备建筑师",
        "quantity": 1.0
    },
    {
        "item": "商店建筑顾问",
        "quantity": 1.0
    },
    {
        "item": "金属材料顾问",
        "quantity": 1.0
    },
    {
        "item": "生命安全顾问",
        "quantity": 1.0
    },
    {
        "item": "外部勘测与设计",
        "quantity": 1.0
    },
    {
        "item": "占地率",
        "quantity": 1.0
    },
    {
        "item": "观众席设计",
        "quantity": 1.0
    },
    {
        "item": "表现力",
        "quantity": 1.0
    },
    {
        "item": "副总监",
        "quantity": 1.0
    },
    {
        "item": "204 0 Sqm",
        "quantity": 1.0
    },
    {
        "item": "多功能厅 & 图书馆团队",
        "quantity": 1.0
    },
    {
        "item": "能源评定师",
        "quantity": 1.0
    },
    {
        "item": "树艺师",
        "quantity": 1.0
    },
    {
        "item": "岩土工程师 ",
        "quantity": 1.0
    },
    {
        "item": "钛合金屋顶",
        "quantity": 1.0
    },
    {
        "item": "项目学生团队",
        "quantity": 1.0
    },
    {
        "item": "外观工程与调试安装",
        "quantity": 1.0
    },
    {
        "item": "App设计",
        "quantity": 1.0
    },
    {
        "item": "电讯工程师",
        "quantity": 1.0
    },
    {
        "item": "暖通空调和管道安装",
        "quantity": 1.0
    },
    {
        "item": "项目人员",
        "quantity": 1.0
    },
    {
        "item": "气候设计",
        "quantity": 1.0
    },
    {
        "item": "气垫 ",
        "quantity": 1.0
    },
    {
        "item": "暖通&自动灭火装置",
        "quantity": 1.0
    },
    {
        "item": "入口通道设计",
        "quantity": 1.0
    },
    {
        "item": "咨询结构工程师",
        "quantity": 1.0
    },
    {
        "item": "施工建议方",
        "quantity": 1.0
    },
    {
        "item": "阳光房设计团队",
        "quantity": 1.0
    },
    {
        "item": "共同项目面积",
        "quantity": 1.0
    },
    {
        "item": "CGI /数据可视化",
        "quantity": 1.0
    },
    {
        "item": "水力学顾问",
        "quantity": 1.0
    },
    {
        "item": "丛林大火、动植物防护",
        "quantity": 1.0
    },
    {
        "item": "木材顾问",
        "quantity": 1.0
    },
    {
        "item": "图像渲染",
        "quantity": 1.0
    },
    {
        "item": "Video",
        "quantity": 1.0
    },
    {
        "item": "结构工程公司",
        "quantity": 1.0
    },
    {
        "item": "Triptyque, 参与团队",
        "quantity": 1.0
    },
    {
        "item": "家具木工",
        "quantity": 1.0
    },
    {
        "item": "来自Schjelderup Trondahl事务所的设计团队",
        "quantity": 1.0
    },
    {
        "item": "结构及系统工程",
        "quantity": 1.0
    },
    {
        "item": "合约预算 ",
        "quantity": 1.0
    },
    {
        "item": "可用建筑面积",
        "quantity": 1.0
    },
    {
        "item": "毕业建筑师",
        "quantity": 1.0
    },
    {
        "item": "额外项目团队",
        "quantity": 1.0
    },
    {
        "item": "参赛团队",
        "quantity": 1.0
    },
    {
        "item": "其他空间室内设计师",
        "quantity": 1.0
    },
    {
        "item": "液压装置",
        "quantity": 1.0
    },
    {
        "item": "剧院工程师",
        "quantity": 1.0
    },
    {
        "item": "指导原则",
        "quantity": 1.0
    },
    {
        "item": "脚手架",
        "quantity": 1.0
    },
    {
        "item": "岩土顾问",
        "quantity": 1.0
    },
    {
        "item": "停车位",
        "quantity": 1.0
    },
    {
        "item": "木材结构工程师叫",
        "quantity": 1.0
    },
    {
        "item": "参与设计建筑师",
        "quantity": 1.0
    },
    {
        "item": "Manufacturer",
        "quantity": 1.0
    },
    {
        "item": "液体、电气、热学设计",
        "quantity": 1.0
    },
    {
        "item": "Kanco 钢结构",
        "quantity": 1.0
    },
    {
        "item": "公众咨询",
        "quantity": 1.0
    },
    {
        "item": "执行监督助理",
        "quantity": 1.0
    },
    {
        "item": "拱板",
        "quantity": 1.0
    },
    {
        "item": "Structural engineer",
        "quantity": 1.0
    },
    {
        "item": "End construction",
        "quantity": 1.0
    },
    {
        "item": "实行公司",
        "quantity": 1.0
    },
    {
        "item": "其它合作伙伴",
        "quantity": 1.0
    },
    {
        "item": "承包负责人",
        "quantity": 1.0
    },
    {
        "item": "合作工程方",
        "quantity": 1.0
    },
    {
        "item": "金属结构计算",
        "quantity": 1.0
    },
    {
        "item": "建筑估价",
        "quantity": 1.0
    },
    {
        "item": "维修",
        "quantity": 1.0
    },
    {
        "item": "机械管工",
        "quantity": 1.0
    },
    {
        "item": "建造调查人",
        "quantity": 1.0
    },
    {
        "item": "地下室停车",
        "quantity": 1.0
    },
    {
        "item": "暖通咨询",
        "quantity": 1.0
    },
    {
        "item": "室内/家具",
        "quantity": 1.0
    },
    {
        "item": "占地面积 ",
        "quantity": 1.0
    },
    {
        "item": "单元数量",
        "quantity": 1.0
    },
    {
        "item": "DOH",
        "quantity": 1.0
    },
    {
        "item": "树木学家/树木研究",
        "quantity": 1.0
    },
    {
        "item": "生态学家 ",
        "quantity": 1.0
    },
    {
        "item": "Rockwell集团董事会",
        "quantity": 1.0
    },
    {
        "item": "试听顾问",
        "quantity": 1.0
    },
    {
        "item": "围墙设计",
        "quantity": 1.0
    },
    {
        "item": "总平面&教育设施施工项目负责人",
        "quantity": 1.0
    },
    {
        "item": "本地顾问",
        "quantity": 1.0
    },
    {
        "item": "Bauherr",
        "quantity": 1.0
    },
    {
        "item": "Stucture, MEP",
        "quantity": 1.0
    },
    {
        "item": "建筑用材",
        "quantity": 1.0
    },
    {
        "item": "Site supervision",
        "quantity": 1.0
    },
    {
        "item": "可持续发展",
        "quantity": 1.0
    },
    {
        "item": "家庭自动化系统",
        "quantity": 1.0
    },
    {
        "item": "”鲸鱼体“施工",
        "quantity": 1.0
    },
    {
        "item": "围墙",
        "quantity": 1.0
    },
    {
        "item": "修剪",
        "quantity": 1.0
    },
    {
        "item": "设计伙伴负责人",
        "quantity": 1.0
    },
    {
        "item": "本地合作伙伴",
        "quantity": 1.0
    },
    {
        "item": "结构/机械工程师",
        "quantity": 1.0
    },
    {
        "item": "驻场管理",
        "quantity": 1.0
    },
    {
        "item": "特殊技术设施",
        "quantity": 1.0
    },
    {
        "item": "SD阶段结构顾问",
        "quantity": 1.0
    },
    {
        "item": "Main Project Architect",
        "quantity": 1.0
    },
    {
        "item": "水电设计",
        "quantity": 1.0
    },
    {
        "item": "Building Coverage",
        "quantity": 1.0
    },
    {
        "item": "金属顶棚",
        "quantity": 1.0
    },
    {
        "item": "场地勘察",
        "quantity": 1.0
    },
    {
        "item": "建筑项目协调",
        "quantity": 1.0
    },
    {
        "item": "景观/场地部分",
        "quantity": 1.0
    },
    {
        "item": "福斯特团队",
        "quantity": 1.0
    },
    {
        "item": "建筑合作者与设计协调",
        "quantity": 1.0
    },
    {
        "item": "展陈及景观",
        "quantity": 1.0
    },
    {
        "item": "展陈及景观项目协调",
        "quantity": 1.0
    },
    {
        "item": "展陈及景观合作者 ",
        "quantity": 1.0
    },
    {
        "item": "Diseño Interior",
        "quantity": 1.0
    },
    {
        "item": "GEA",
        "quantity": 1.0
    },
    {
        "item": "Ingenieros",
        "quantity": 1.0
    },
    {
        "item": "推广者",
        "quantity": 1.0
    },
    {
        "item": "Façade Construction",
        "quantity": 1.0
    },
    {
        "item": "Solución alternativa de energía",
        "quantity": 1.0
    },
    {
        "item": "葡萄酒顾问",
        "quantity": 1.0
    },
    {
        "item": "木结构/外观设计",
        "quantity": 1.0
    },
    {
        "item": "可再生能源",
        "quantity": 1.0
    },
    {
        "item": "团体竞赛",
        "quantity": 1.0
    },
    {
        "item": "开发",
        "quantity": 1.0
    },
    {
        "item": "城市顾问",
        "quantity": 1.0
    },
    {
        "item": "引导标示",
        "quantity": 1.0
    },
    {
        "item": "给排水与暖通空调",
        "quantity": 1.0
    },
    {
        "item": "河流流域管理",
        "quantity": 1.0
    },
    {
        "item": "水资源有效性研究",
        "quantity": 1.0
    },
    {
        "item": "农学加",
        "quantity": 1.0
    },
    {
        "item": "项目评估",
        "quantity": 1.0
    },
    {
        "item": "发起人 /业主及建筑公司",
        "quantity": 1.0
    },
    {
        "item": "信用评级研究",
        "quantity": 1.0
    },
    {
        "item": "通讯",
        "quantity": 1.0
    },
    {
        "item": "视频与模型",
        "quantity": 1.0
    },
    {
        "item": "Mep 工程",
        "quantity": 1.0
    },
    {
        "item": "社区合作伙伴",
        "quantity": 1.0
    },
    {
        "item": "FR|SCH 项目",
        "quantity": 1.0
    },
    {
        "item": "浆叶",
        "quantity": 1.0
    },
    {
        "item": "Landscape Architecture",
        "quantity": 1.0
    },
    {
        "item": "执行合伙人",
        "quantity": 1.0
    },
    {
        "item": "气候系统承包商",
        "quantity": 1.0
    },
    {
        "item": "项目经理、主管",
        "quantity": 1.0
    },
    {
        "item": "活动",
        "quantity": 1.0
    },
    {
        "item": "道路标识",
        "quantity": 1.0
    },
    {
        "item": "行李操作",
        "quantity": 1.0
    },
    {
        "item": "设备机电顾问",
        "quantity": 1.0
    },
    {
        "item": "钢结构作业",
        "quantity": 1.0
    },
    {
        "item": "玻璃供应商",
        "quantity": 1.0
    },
    {
        "item": "土木与结构工程师",
        "quantity": 1.0
    },
    {
        "item": "机电工程师，消防设施",
        "quantity": 1.0
    },
    {
        "item": "视听，音响设备",
        "quantity": 1.0
    },
    {
        "item": "合作艺术家 2",
        "quantity": 1.0
    },
    {
        "item": "水上项目顾问",
        "quantity": 1.0
    },
    {
        "item": "Colleen@mergearchitects com",
        "quantity": 1.0
    },
    {
        "item": "建筑成本 ",
        "quantity": 1.0
    },
    {
        "item": "Cooper Robertson 项目建筑师",
        "quantity": 1.0
    },
    {
        "item": "幕墙/窗",
        "quantity": 1.0
    },
    {
        "item": "Cooper Robertson 内饰设计",
        "quantity": 1.0
    },
    {
        "item": "Cooper Robertson 项目管理",
        "quantity": 1.0
    },
    {
        "item": "顾问服务",
        "quantity": 1.0
    },
    {
        "item": "室内动态模型",
        "quantity": 1.0
    },
    {
        "item": "Project Client",
        "quantity": 1.0
    },
    {
        "item": "结构助理",
        "quantity": 1.0
    },
    {
        "item": "室内设计书",
        "quantity": 1.0
    },
    {
        "item": "Project management advertiser",
        "quantity": 1.0
    },
    {
        "item": "Design Team Leaders",
        "quantity": 1.0
    },
    {
        "item": "机械、管道工程",
        "quantity": 1.0
    },
    {
        "item": "卫生装置",
        "quantity": 1.0
    },
    {
        "item": "高环境质量援助",
        "quantity": 1.0
    },
    {
        "item": "建筑工地",
        "quantity": 1.0
    },
    {
        "item": "Lighting Design Consultant",
        "quantity": 1.0
    },
    {
        "item": "自动灌溉",
        "quantity": 1.0
    },
    {
        "item": "Type/program",
        "quantity": 1.0
    },
    {
        "item": "地形勘测",
        "quantity": 1.0
    },
    {
        "item": "企业网站",
        "quantity": 1.0
    },
    {
        "item": "项目合作阶段",
        "quantity": 1.0
    },
    {
        "item": "委托任务",
        "quantity": 1.0
    },
    {
        "item": "电脑信息/视频顾问",
        "quantity": 1.0
    },
    {
        "item": "废水管承包商",
        "quantity": 1.0
    },
    {
        "item": "LEED 绿色建筑",
        "quantity": 1.0
    },
    {
        "item": "主要供应商/制造商",
        "quantity": 1.0
    },
    {
        "item": "技术总监/建筑师记录",
        "quantity": 1.0
    },
    {
        "item": "1999年竞赛合作设计师",
        "quantity": 1.0
    },
    {
        "item": "展览设计图形导演",
        "quantity": 1.0
    },
    {
        "item": "艺术指导，枝形吊灯与家具设计",
        "quantity": 1.0
    },
    {
        "item": "范围",
        "quantity": 1.0
    },
    {
        "item": "展览设计主管生产",
        "quantity": 1.0
    },
    {
        "item": "户外区",
        "quantity": 1.0
    },
    {
        "item": "外部评论",
        "quantity": 1.0
    },
    {
        "item": "项目管理顾问",
        "quantity": 1.0
    },
    {
        "item": "导演作品",
        "quantity": 1.0
    },
    {
        "item": "温控工程师",
        "quantity": 1.0
    },
    {
        "item": "景观组",
        "quantity": 1.0
    },
    {
        "item": "电气，液压和消防",
        "quantity": 1.0
    },
    {
        "item": "机械工程师与安装",
        "quantity": 1.0
    },
    {
        "item": "贵宾厅吊灯",
        "quantity": 1.0
    },
    {
        "item": "目的",
        "quantity": 1.0
    },
    {
        "item": "结构计算和基础",
        "quantity": 1.0
    },
    {
        "item": "LEED灯光设计",
        "quantity": 1.0
    },
    {
        "item": "总表面积",
        "quantity": 1.0
    },
    {
        "item": "HVAC顾问 ",
        "quantity": 1.0
    },
    {
        "item": "厨房设计师",
        "quantity": 1.0
    },
    {
        "item": "HPAC 设计",
        "quantity": 1.0
    },
    {
        "item": "消防，舒适，音响，安全",
        "quantity": 1.0
    },
    {
        "item": "项目首席设计师",
        "quantity": 1.0
    },
    {
        "item": "环境问题",
        "quantity": 1.0
    },
    {
        "item": "土木，气候，机械工程师",
        "quantity": 1.0
    },
    {
        "item": "家庭住所",
        "quantity": 1.0
    },
    {
        "item": "维修工程",
        "quantity": 1.0
    },
    {
        "item": "专业金属加工",
        "quantity": 1.0
    },
    {
        "item": "园艺景观",
        "quantity": 1.0
    },
    {
        "item": "坐席",
        "quantity": 1.0
    },
    {
        "item": "风力研究",
        "quantity": 1.0
    },
    {
        "item": "设计建造师",
        "quantity": 1.0
    },
    {
        "item": "Metal work",
        "quantity": 1.0
    },
    {
        "item": "现场监督",
        "quantity": 1.0
    },
    {
        "item": "技师",
        "quantity": 1.0
    },
    {
        "item": "Client (Masterplan)",
        "quantity": 1.0
    },
    {
        "item": "PT 混凝土结构",
        "quantity": 1.0
    },
    {
        "item": "进深",
        "quantity": 1.0
    },
    {
        "item": "分区",
        "quantity": 1.0
    },
    {
        "item": "混凝土顾问",
        "quantity": 1.0
    },
    {
        "item": "项目建筑协调人",
        "quantity": 1.0
    },
    {
        "item": "合作开发",
        "quantity": 1.0
    },
    {
        "item": "构造评估",
        "quantity": 1.0
    },
    {
        "item": "建材商",
        "quantity": 1.0
    },
    {
        "item": "材料设计",
        "quantity": 1.0
    },
    {
        "item": "防水材料",
        "quantity": 1.0
    },
    {
        "item": "智能卫浴和空调系统组装",
        "quantity": 1.0
    },
    {
        "item": "建筑场地",
        "quantity": 1.0
    },
    {
        "item": "园林美化",
        "quantity": 1.0
    },
    {
        "item": "玻璃建材供应商",
        "quantity": 1.0
    },
    {
        "item": "单元数目",
        "quantity": 1.0
    },
    {
        "item": "摄影师 ",
        "quantity": 1.0
    },
    {
        "item": "设计领导",
        "quantity": 1.0
    },
    {
        "item": "展览会建设",
        "quantity": 1.0
    },
    {
        "item": "照明设计&剧院规划",
        "quantity": 1.0
    },
    {
        "item": "多媒体建设",
        "quantity": 1.0
    },
    {
        "item": "设备与防火工程师",
        "quantity": 1.0
    },
    {
        "item": "电缆结构施工",
        "quantity": 1.0
    },
    {
        "item": "Illustrations",
        "quantity": 1.0
    },
    {
        "item": "Adv  工程造价",
        "quantity": 1.0
    },
    {
        "item": "BRT工程",
        "quantity": 1.0
    },
    {
        "item": "Feltrinelli Porta Volta 建筑面积",
        "quantity": 1.0
    },
    {
        "item": " 施工管理",
        "quantity": 1.0
    },
    {
        "item": "斯图加特项目团队",
        "quantity": 1.0
    },
    {
        "item": "建筑室内装饰",
        "quantity": 1.0
    },
    {
        "item": "合同/采购形式",
        "quantity": 1.0
    },
    {
        "item": "模块施工",
        "quantity": 1.0
    },
    {
        "item": "委托人代表",
        "quantity": 1.0
    },
    {
        "item": "Glass Provider",
        "quantity": 1.0
    },
    {
        "item": "木结构施工",
        "quantity": 1.0
    },
    {
        "item": "SC 制造商",
        "quantity": 1.0
    },
    {
        "item": "科技支持",
        "quantity": 1.0
    },
    {
        "item": "安保",
        "quantity": 1.0
    },
    {
        "item": "居民参与",
        "quantity": 1.0
    },
    {
        "item": "空房设计",
        "quantity": 1.0
    },
    {
        "item": "酒店运营商",
        "quantity": 1.0
    },
    {
        "item": "EllisDon (建设)",
        "quantity": 1.0
    },
    {
        "item": "市政投资",
        "quantity": 1.0
    },
    {
        "item": "Bat 顾问",
        "quantity": 1.0
    },
    {
        "item": "2006 2013技术助理合作者",
        "quantity": 1.0
    },
    {
        "item": "Trinity Wood 制品",
        "quantity": 1.0
    },
    {
        "item": "DJ 工程师 & 合伙人",
        "quantity": 1.0
    },
    {
        "item": "艺术统筹",
        "quantity": 1.0
    },
    {
        "item": "原项目时间",
        "quantity": 1.0
    },
    {
        "item": "纽约大学的相互作用的科学部门",
        "quantity": 1.0
    },
    {
        "item": "项目主持建筑师",
        "quantity": 1.0
    },
    {
        "item": " Architects in charge",
        "quantity": 1.0
    },
    {
        "item": "展示顾问",
        "quantity": 1.0
    },
    {
        "item": "健康网络延伸",
        "quantity": 1.0
    },
    {
        "item": "办公室",
        "quantity": 1.0
    },
    {
        "item": "模型、网络平台和应用程序",
        "quantity": 1.0
    },
    {
        "item": "试音员",
        "quantity": 1.0
    },
    {
        "item": "建筑设计事务所",
        "quantity": 1.0
    },
    {
        "item": "作曲家",
        "quantity": 1.0
    },
    {
        "item": "道路设计\t",
        "quantity": 1.0
    },
    {
        "item": "纸板供应",
        "quantity": 1.0
    },
    {
        "item": "Planning Principal",
        "quantity": 1.0
    },
    {
        "item": "设计/竣工时间",
        "quantity": 1.0
    },
    {
        "item": "钢板",
        "quantity": 1.0
    },
    {
        "item": "BET VRD",
        "quantity": 1.0
    },
    {
        "item": "项目概念经理",
        "quantity": 1.0
    },
    {
        "item": "特殊功能",
        "quantity": 1.0
    },
    {
        "item": "项目建设经理",
        "quantity": 1.0
    },
    {
        "item": "门的施工与安装",
        "quantity": 1.0
    },
    {
        "item": "管子展厅面积",
        "quantity": 1.0
    },
    {
        "item": "AREP",
        "quantity": 1.0
    },
    {
        "item": "Groupe 3 建筑师",
        "quantity": 1.0
    },
    {
        "item": "主要室内建筑师",
        "quantity": 1.0
    },
    {
        "item": "地方法规，模范，施工监理",
        "quantity": 1.0
    },
    {
        "item": "合作者 － M",
        "quantity": 1.0
    },
    {
        "item": "环境艺术设计",
        "quantity": 1.0
    },
    {
        "item": "管理合作事务所",
        "quantity": 1.0
    },
    {
        "item": "2000 2001初级设计",
        "quantity": 1.0
    },
    {
        "item": "客户伙伴",
        "quantity": 1.0
    },
    {
        "item": "其他顾问 ",
        "quantity": 1.0
    },
    {
        "item": "电顾问",
        "quantity": 1.0
    },
    {
        "item": "环境和声学",
        "quantity": 1.0
    },
    {
        "item": "完成团队",
        "quantity": 1.0
    },
    {
        "item": "混凝土顾问和设计师",
        "quantity": 1.0
    },
    {
        "item": "基座建筑 LEED 顾问",
        "quantity": 1.0
    },
    {
        "item": "行李管理",
        "quantity": 1.0
    },
    {
        "item": "热、通风、电气设计",
        "quantity": 1.0
    },
    {
        "item": "防火结构",
        "quantity": 1.0
    },
    {
        "item": "媒体计划",
        "quantity": 1.0
    },
    {
        "item": "楼梯制造商",
        "quantity": 1.0
    },
    {
        "item": "室内施工方",
        "quantity": 1.0
    },
    {
        "item": "美术设计",
        "quantity": 1.0
    },
    {
        "item": "项目负责人 ",
        "quantity": 1.0
    },
    {
        "item": "二期设计和总负责",
        "quantity": 1.0
    },
    {
        "item": "环境等级",
        "quantity": 1.0
    },
    {
        "item": "造价，工程，结构、排水、声学设计",
        "quantity": 1.0
    },
    {
        "item": "内部装饰设计师",
        "quantity": 1.0
    },
    {
        "item": "3D 建模",
        "quantity": 1.0
    },
    {
        "item": "设计组长",
        "quantity": 1.0
    },
    {
        "item": "合伙负责人，主建筑师",
        "quantity": 1.0
    },
    {
        "item": "公司名称",
        "quantity": 1.0
    },
    {
        "item": "室内与景观",
        "quantity": 1.0
    },
    {
        "item": "当地景观顾问",
        "quantity": 1.0
    },
    {
        "item": "AMEP顾问",
        "quantity": 1.0
    },
    {
        "item": "Structural / Civil",
        "quantity": 1.0
    },
    {
        "item": "Rockwell集团创始人兼总裁",
        "quantity": 1.0
    },
    {
        "item": "室内家具协调",
        "quantity": 1.0
    },
    {
        "item": "Arquitectos a Cargo",
        "quantity": 1.0
    },
    {
        "item": "盆景设计",
        "quantity": 1.0
    },
    {
        "item": "项目主任 (Atelier Michel Rémon)",
        "quantity": 1.0
    },
    {
        "item": "专业规划师",
        "quantity": 1.0
    },
    {
        "item": "设计建造着",
        "quantity": 1.0
    },
    {
        "item": "系统工程是",
        "quantity": 1.0
    },
    {
        "item": "人形通道总承包商",
        "quantity": 1.0
    },
    {
        "item": "可持续发展技术",
        "quantity": 1.0
    },
    {
        "item": "预算和计划",
        "quantity": 1.0
    },
    {
        "item": "色彩顾问",
        "quantity": 1.0
    },
    {
        "item": "设计合作者",
        "quantity": 1.0
    },
    {
        "item": "博物馆馆长",
        "quantity": 1.0
    },
    {
        "item": "基础结构系统",
        "quantity": 1.0
    },
    {
        "item": "夯土",
        "quantity": 1.0
    },
    {
        "item": "薄膜展厅面积",
        "quantity": 1.0
    },
    {
        "item": "环保性能",
        "quantity": 1.0
    },
    {
        "item": "Saleable Surface",
        "quantity": 1.0
    },
    {
        "item": "建筑技术和工料测量师",
        "quantity": 1.0
    },
    {
        "item": "生产",
        "quantity": 1.0
    },
    {
        "item": "自然光研究",
        "quantity": 1.0
    },
    {
        "item": "通讯系统",
        "quantity": 1.0
    },
    {
        "item": "土木和结构顾问",
        "quantity": 1.0
    },
    {
        "item": "电工顾问",
        "quantity": 1.0
    },
    {
        "item": "视觉艺术",
        "quantity": 1.0
    },
    {
        "item": "淋浴门拱玻璃",
        "quantity": 1.0
    },
    {
        "item": "数学运算",
        "quantity": 1.0
    },
    {
        "item": "服务设计",
        "quantity": 1.0
    },
    {
        "item": "ESD顾问",
        "quantity": 1.0
    },
    {
        "item": "投影工程",
        "quantity": 1.0
    },
    {
        "item": "Hqe 工程师",
        "quantity": 1.0
    },
    {
        "item": "航空工程",
        "quantity": 1.0
    },
    {
        "item": "Landscape Consultant",
        "quantity": 1.0
    },
    {
        "item": "Heating and Ventilating Engineer",
        "quantity": 1.0
    },
    {
        "item": "水供应和污水处理",
        "quantity": 1.0
    },
    {
        "item": "总平面&教育设施建设团队",
        "quantity": 1.0
    },
    {
        "item": "建筑物理&声学",
        "quantity": 1.0
    },
    {
        "item": "机械工程 ",
        "quantity": 1.0
    },
    {
        "item": "LEED 能源评估顾问",
        "quantity": 1.0
    },
    {
        "item": "模块建造",
        "quantity": 1.0
    },
    {
        "item": "ESD (环境的可持续性设计) 顾问",
        "quantity": 1.0
    },
    {
        "item": "制作人",
        "quantity": 1.0
    },
    {
        "item": "二期承包商",
        "quantity": 1.0
    },
    {
        "item": "工程硕士",
        "quantity": 1.0
    },
    {
        "item": "2000 2001 初级设计合作者",
        "quantity": 1.0
    },
    {
        "item": "电、安全、消防工程师",
        "quantity": 1.0
    },
    {
        "item": "2006 2013技术助理",
        "quantity": 1.0
    },
    {
        "item": "3D模型设计：",
        "quantity": 1.0
    },
    {
        "item": "施工技术员合伙人",
        "quantity": 1.0
    },
    {
        "item": "生物处理系统",
        "quantity": 1.0
    },
    {
        "item": "燃气工程",
        "quantity": 1.0
    },
    {
        "item": "Architectural Assistants",
        "quantity": 1.0
    },
    {
        "item": "安全与健康",
        "quantity": 1.0
    },
    {
        "item": "宣传和建设方",
        "quantity": 1.0
    },
    {
        "item": "艺术工作，彩色玻璃，马赛克",
        "quantity": 1.0
    },
    {
        "item": "传统木作设计",
        "quantity": 1.0
    },
    {
        "item": "工程质量检查",
        "quantity": 1.0
    },
    {
        "item": "客户场地主管",
        "quantity": 1.0
    },
    {
        "item": "土地机械",
        "quantity": 1.0
    },
    {
        "item": "风洞顾问",
        "quantity": 1.0
    },
    {
        "item": "房屋面积",
        "quantity": 1.0
    },
    {
        "item": "结构研究",
        "quantity": 1.0
    },
    {
        "item": "设计原则",
        "quantity": 1.0
    },
    {
        "item": "二期",
        "quantity": 1.0
    },
    {
        "item": "面积:登山自行车奥林匹克中心",
        "quantity": 1.0
    },
    {
        "item": "总体规划 及协调",
        "quantity": 1.0
    },
    {
        "item": "照明和音频设计",
        "quantity": 1.0
    },
    {
        "item": "项目开发合作伙伴",
        "quantity": 1.0
    },
    {
        "item": "能源",
        "quantity": 1.0
    },
    {
        "item": "结构组装",
        "quantity": 1.0
    },
    {
        "item": "装置固定",
        "quantity": 1.0
    },
    {
        "item": "TGA",
        "quantity": 1.0
    },
    {
        "item": "竞争团队",
        "quantity": 1.0
    },
    {
        "item": "岩石工程",
        "quantity": 1.0
    },
    {
        "item": "机械+管道",
        "quantity": 1.0
    },
    {
        "item": "建造师负责人",
        "quantity": 1.0
    },
    {
        "item": "舞台机械咨询",
        "quantity": 1.0
    },
    {
        "item": "总项目工程师",
        "quantity": 1.0
    },
    {
        "item": "项目负责合伙人",
        "quantity": 1.0
    },
    {
        "item": "协作人员",
        "quantity": 1.0
    },
    {
        "item": "天花板",
        "quantity": 1.0
    },
    {
        "item": "计划与协调",
        "quantity": 1.0
    },
    {
        "item": "机械工程与调试安装",
        "quantity": 1.0
    },
    {
        "item": "保存记录",
        "quantity": 1.0
    },
    {
        "item": "影音、舞台和项目管理",
        "quantity": 1.0
    },
    {
        "item": "执行主持",
        "quantity": 1.0
    },
    {
        "item": "其它顾问照明设计",
        "quantity": 1.0
    },
    {
        "item": "音频视频",
        "quantity": 1.0
    },
    {
        "item": "Dirección de Proyecto",
        "quantity": 1.0
    },
    {
        "item": "Equipe",
        "quantity": 1.0
    },
    {
        "item": "总施工方",
        "quantity": 1.0
    },
    {
        "item": "模型1",
        "quantity": 1.0
    },
    {
        "item": "场地洁具工程师",
        "quantity": 1.0
    },
    {
        "item": "建筑设备工程",
        "quantity": 1.0
    },
    {
        "item": "景观设计咨询",
        "quantity": 1.0
    },
    {
        "item": "花园和生态系统",
        "quantity": 1.0
    },
    {
        "item": "一楼夹层面积",
        "quantity": 1.0
    },
    {
        "item": "利益相关者",
        "quantity": 1.0
    },
    {
        "item": "艺术家 陶瓷结构",
        "quantity": 1.0
    },
    {
        "item": "酒店面积",
        "quantity": 1.0
    },
    {
        "item": "总施工公司",
        "quantity": 1.0
    },
    {
        "item": "Construction Site Management",
        "quantity": 1.0
    },
    {
        "item": "电气和管道工程师",
        "quantity": 1.0
    },
    {
        "item": "自动化系统",
        "quantity": 1.0
    },
    {
        "item": "历史建筑顾问",
        "quantity": 1.0
    },
    {
        "item": "合作者 － E",
        "quantity": 1.0
    },
    {
        "item": "水源管理",
        "quantity": 1.0
    },
    {
        "item": "建筑系统顾问",
        "quantity": 1.0
    },
    {
        "item": "Panel Construction/Facade Construction",
        "quantity": 1.0
    },
    {
        "item": "竞赛设计团队",
        "quantity": 1.0
    },
    {
        "item": "成立这",
        "quantity": 1.0
    },
    {
        "item": "泳池建造商",
        "quantity": 1.0
    },
    {
        "item": "室内（酒吧）",
        "quantity": 1.0
    },
    {
        "item": "淋浴面板",
        "quantity": 1.0
    },
    {
        "item": "展览（画廊）",
        "quantity": 1.0
    },
    {
        "item": "服务、防静电、垂直运输、声学、外观、环境和消防工程师",
        "quantity": 1.0
    },
    {
        "item": "尺度",
        "quantity": 1.0
    },
    {
        "item": "体感游戏",
        "quantity": 1.0
    },
    {
        "item": "客户代表",
        "quantity": 1.0
    },
    {
        "item": "传统建筑师",
        "quantity": 1.0
    },
    {
        "item": "建筑师工程师（建设）",
        "quantity": 1.0
    },
    {
        "item": "建设总成本(总平方英尺)",
        "quantity": 1.0
    },
    {
        "item": "图表和物体设计 ",
        "quantity": 1.0
    },
    {
        "item": "土建结构",
        "quantity": 1.0
    },
    {
        "item": "董事会负责人",
        "quantity": 1.0
    },
    {
        "item": "先进科技",
        "quantity": 1.0
    },
    {
        "item": "开发商 / 产权拥有者 / 客户",
        "quantity": 1.0
    },
    {
        "item": "景观设计师顾问",
        "quantity": 1.0
    },
    {
        "item": "Restricciones",
        "quantity": 1.0
    },
    {
        "item": "声学/IT",
        "quantity": 1.0
    },
    {
        "item": "活动策划和施工经理",
        "quantity": 1.0
    },
    {
        "item": "滑板运动场地设计",
        "quantity": 1.0
    },
    {
        "item": "机电、防火、暖通工程",
        "quantity": 1.0
    },
    {
        "item": "暖通空调承包商",
        "quantity": 1.0
    },
    {
        "item": "橡胶地板",
        "quantity": 1.0
    },
    {
        "item": "安全系统设计",
        "quantity": 1.0
    },
    {
        "item": "细木工和总建造",
        "quantity": 1.0
    },
    {
        "item": "现场建筑师",
        "quantity": 1.0
    },
    {
        "item": "交通工程顾问",
        "quantity": 1.0
    },
    {
        "item": "MEP/FP",
        "quantity": 1.0
    },
    {
        "item": "建筑土地比",
        "quantity": 1.0
    },
    {
        "item": "Propietario",
        "quantity": 1.0
    },
    {
        "item": "门面顾问工程师",
        "quantity": 1.0
    },
    {
        "item": "外部设施顾问",
        "quantity": 1.0
    },
    {
        "item": "停车场建设和总体规划的建筑概念",
        "quantity": 1.0
    },
    {
        "item": "博物馆设计顾问",
        "quantity": 1.0
    },
    {
        "item": "羡慕建筑师",
        "quantity": 1.0
    },
    {
        "item": "艾松（艺术），李豪（建筑）",
        "quantity": 1.0
    },
    {
        "item": "技术说明和执行",
        "quantity": 1.0
    },
    {
        "item": "玻璃建筑设计",
        "quantity": 1.0
    },
    {
        "item": "静态设计",
        "quantity": 1.0
    },
    {
        "item": "Client ",
        "quantity": 1.0
    },
    {
        "item": "海堤长度",
        "quantity": 1.0
    },
    {
        "item": "施工经济学",
        "quantity": 1.0
    },
    {
        "item": "配套工程",
        "quantity": 1.0
    },
    {
        "item": "Ingeniería Hidrosanitaria",
        "quantity": 1.0
    },
    {
        "item": "细木工匠",
        "quantity": 1.0
    },
    {
        "item": "费用/平米",
        "quantity": 1.0
    },
    {
        "item": "锌承包商",
        "quantity": 1.0
    },
    {
        "item": "施工阶段协调工作",
        "quantity": 1.0
    },
    {
        "item": "Diseño de iluminación",
        "quantity": 1.0
    },
    {
        "item": "组织结构/气体力学",
        "quantity": 1.0
    },
    {
        "item": "图书馆设计团队",
        "quantity": 1.0
    },
    {
        "item": "Team Member",
        "quantity": 1.0
    },
    {
        "item": "图书馆面积",
        "quantity": 1.0
    },
    {
        "item": "室内，窗帘",
        "quantity": 1.0
    },
    {
        "item": "图书馆预算",
        "quantity": 1.0
    },
    {
        "item": "FR-EE 团队",
        "quantity": 1.0
    },
    {
        "item": "展览照明",
        "quantity": 1.0
    },
    {
        "item": "Steel Structure Contractor",
        "quantity": 1.0
    },
    {
        "item": "客户及建造者",
        "quantity": 1.0
    },
    {
        "item": "土木及结构工程师",
        "quantity": 1.0
    },
    {
        "item": "工程总造价",
        "quantity": 1.0
    },
    {
        "item": "屋宇装备工程师",
        "quantity": 1.0
    },
    {
        "item": "建筑师 / 协调员",
        "quantity": 1.0
    },
    {
        "item": "风水设计",
        "quantity": 1.0
    },
    {
        "item": "电力水利",
        "quantity": 1.0
    },
    {
        "item": "物流顾问",
        "quantity": 1.0
    },
    {
        "item": "一期结构",
        "quantity": 1.0
    },
    {
        "item": "研究所电气",
        "quantity": 1.0
    },
    {
        "item": "承包商玻璃建设",
        "quantity": 1.0
    },
    {
        "item": "电气安装承包商",
        "quantity": 1.0
    },
    {
        "item": "合作架构师",
        "quantity": 1.0
    },
    {
        "item": "机械装置承办商",
        "quantity": 1.0
    },
    {
        "item": "专业木工",
        "quantity": 1.0
    },
    {
        "item": "Reducteur",
        "quantity": 1.0
    },
    {
        "item": "国家博物馆顾问",
        "quantity": 1.0
    },
    {
        "item": "计算",
        "quantity": 1.0
    },
    {
        "item": "数字技术",
        "quantity": 1.0
    },
    {
        "item": "总导演",
        "quantity": 1.0
    },
    {
        "item": "基础结构",
        "quantity": 1.0
    },
    {
        "item": "总基地面积",
        "quantity": 1.0
    },
    {
        "item": "总承包商/施工经理",
        "quantity": 1.0
    },
    {
        "item": "建筑师和工程师",
        "quantity": 1.0
    },
    {
        "item": "活动年限",
        "quantity": 1.0
    },
    {
        "item": "M＆E工程师",
        "quantity": 1.0
    },
    {
        "item": "Bathroom, Kitchen and Cabinetry Works",
        "quantity": 1.0
    },
    {
        "item": "电气工程设计",
        "quantity": 1.0
    },
    {
        "item": "学校",
        "quantity": 1.0
    },
    {
        "item": "知识搭档",
        "quantity": 1.0
    },
    {
        "item": "业主/赞助商",
        "quantity": 1.0
    },
    {
        "item": "消防安全工程师",
        "quantity": 1.0
    },
    {
        "item": "当地材料咨询公司",
        "quantity": 1.0
    },
    {
        "item": "BIM管理",
        "quantity": 1.0
    },
    {
        "item": "主要制造商",
        "quantity": 1.0
    },
    {
        "item": "当地照明顾问",
        "quantity": 1.0
    },
    {
        "item": "协助景观建筑",
        "quantity": 1.0
    },
    {
        "item": "金属材料",
        "quantity": 1.0
    },
    {
        "item": "铝合金框架",
        "quantity": 1.0
    },
    {
        "item": "机构工程师",
        "quantity": 1.0
    },
    {
        "item": "构造工程师",
        "quantity": 1.0
    },
    {
        "item": "木材结构",
        "quantity": 1.0
    },
    {
        "item": "立面构造和顾问",
        "quantity": 1.0
    },
    {
        "item": "机械工程顾问",
        "quantity": 1.0
    },
    {
        "item": "休息室与套间的室内设计",
        "quantity": 1.0
    },
    {
        "item": "HWS工程师",
        "quantity": 1.0
    },
    {
        "item": "中国合作伙伴",
        "quantity": 1.0
    },
    {
        "item": "Interiors Staff",
        "quantity": 1.0
    },
    {
        "item": "机电管道 & 空调系统顾问",
        "quantity": 1.0
    },
    {
        "item": "金属结构设计",
        "quantity": 1.0
    },
    {
        "item": "石材结构设计",
        "quantity": 1.0
    },
    {
        "item": "结构与可持续发展",
        "quantity": 1.0
    },
    {
        "item": "合伙人及项目负责",
        "quantity": 1.0
    },
    {
        "item": "游泳池设计",
        "quantity": 1.0
    },
    {
        "item": "台湾忠泰建筑艺术文化基金合作人",
        "quantity": 1.0
    },
    {
        "item": "Diller Scofidio + Renfro 团队",
        "quantity": 1.0
    },
    {
        "item": "Gensler 团队",
        "quantity": 1.0
    },
    {
        "item": "玻璃，幕墙",
        "quantity": 1.0
    },
    {
        "item": "领导",
        "quantity": 1.0
    },
    {
        "item": "数控铣床",
        "quantity": 1.0
    },
    {
        "item": "舞台机械设计",
        "quantity": 1.0
    },
    {
        "item": "De Botella （瓶子）设计",
        "quantity": 1.0
    },
    {
        "item": "座位数:登山自行车奥林匹克中心",
        "quantity": 1.0
    },
    {
        "item": "行政部门",
        "quantity": 1.0
    },
    {
        "item": "Gensler",
        "quantity": 1.0
    },
    {
        "item": "施工执行管理",
        "quantity": 1.0
    },
    {
        "item": "Construction Team",
        "quantity": 1.0
    },
    {
        "item": "设计合作伙伴 ",
        "quantity": 1.0
    },
    {
        "item": "规划与项目管理",
        "quantity": 1.0
    },
    {
        "item": "Use",
        "quantity": 1.0
    },
    {
        "item": "功能区",
        "quantity": 1.0
    },
    {
        "item": "施工现场经理 ",
        "quantity": 1.0
    },
    {
        "item": "植物选择",
        "quantity": 1.0
    },
    {
        "item": "其他项目成员",
        "quantity": 1.0
    },
    {
        "item": "发起人和项目开发",
        "quantity": 1.0
    },
    {
        "item": "项目团队（施工文件）",
        "quantity": 1.0
    },
    {
        "item": "圆顶面积",
        "quantity": 1.0
    },
    {
        "item": "项目赞助",
        "quantity": 1.0
    },
    {
        "item": "制图团队",
        "quantity": 1.0
    },
    {
        "item": "投资成本",
        "quantity": 1.0
    },
    {
        "item": "人为因素",
        "quantity": 1.0
    },
    {
        "item": "Senior Associate - Product Design",
        "quantity": 1.0
    },
    {
        "item": "道路设计",
        "quantity": 1.0
    },
    {
        "item": "保温层设计",
        "quantity": 1.0
    },
    {
        "item": "能源指标 ",
        "quantity": 1.0
    },
    {
        "item": "模型照片",
        "quantity": 1.0
    },
    {
        "item": "电力和电信 ",
        "quantity": 1.0
    },
    {
        "item": "机械、水暖、结构设计",
        "quantity": 1.0
    }
];

def deleteNoContainMlhFieldItem():
    mongoclient = MongoSupport()
    mongoclient.db["scrapy_dimensions"].insert_many(dimensions)

if __name__ == '__main__':
    deleteNoContainMlhFieldItem()