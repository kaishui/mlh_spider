import oss2


class AliOss(object):

    ALI_OSS_ACCESS_KEY_ID = "LPiVTOXcxFD295jw"
    ALI_OSS_ACCESS_KEY_SECRET = "SVChnXgjJiv7b83o6Awbcr4bVZeDfh"
    # 外网
    # ALI_OSS_ENDPOINT = "http://oss-cn-hangzhou.aliyuncs.com"
    # 阿里云内网
    ALI_OSS_ENDPOINT = "http://oss-cn-hangzhou-internal.aliyuncs.com"
    # oss bucket
    # ALI_OSS_BUCKET_NAME = "mlhangtest"
    ALI_OSS_BUCKET_NAME = "mlhspider"

    def __init__(self):
        auth = oss2.Auth(self.ALI_OSS_ACCESS_KEY_ID, self.ALI_OSS_ACCESS_KEY_SECRET)
        self.bucket = oss2.Bucket(auth, self.ALI_OSS_ENDPOINT, self.ALI_OSS_BUCKET_NAME)