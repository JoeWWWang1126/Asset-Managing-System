import time
class TimeDemo:


    def ppp(self):
        localtime = time.asctime(time.localtime(time.time()))
        return localtime
# print(isinstance(TimeDemo.ppp(),str))