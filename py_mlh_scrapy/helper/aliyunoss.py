import oss2


class AliOss(object):

    ALI_OSS_ACCESS_KEY_ID = "LPiVTOXcxFD295jw"
    ALI_OSS_ACCESS_KEY_SECRET = "SVChnXgjJiv7b83o6Awbcr4bVZeDfh"
    ALI_OSS_ENDPOINT = "http://oss-cn-hangzhou.aliyuncs.com"
    ALI_OSS_BUCKET_NAME = "mlhangtest"

    def __init__(self):
        auth = oss2.Auth(self.ALI_OSS_ACCESS_KEY_ID, self.ALI_OSS_ACCESS_KEY_SECRET)
        self.bucket = oss2.Bucket(auth, self.ALI_OSS_ENDPOINT, self.ALI_OSS_BUCKET_NAME)