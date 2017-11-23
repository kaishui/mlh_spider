import time

#获取当前时间，精确的毫秒
def getCurTime():
    curTime=round(time.time()*1000)
    return curTime

if __name__ == "__main__":
    print(getCurTime())