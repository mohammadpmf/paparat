from time import sleep

class Time():
    def __init__(self, h=0, m=0, s=0):
        self.h=h
        self.m=m
        self.s=s
        if h<0:
            raise ValueError("Hour can not be negative!")
        if m<0:
            raise ValueError("Minute can not be negative!")
        if s<0:
            raise ValueError("Second can not be negative!")
        if self.s>59:
            self.m += self.s//60
            self.s %= 60
        if self.m>59:
            self.h += self.m//60
            self.m %= 60
        if self.h>23:
            self.h %= 24
    
    def __add__(self, other: 'Time'):
        h = self.h+other.h
        m = self.m+other.m
        s = self.s+other.s
        return Time(h, m, s)

    def __sub__(self, other: 'Time'):
        h = self.h-other.h
        m = self.m-other.m
        s = self.s-other.s
        if s<0:
            s+=60
            m-=1
        if m<0:
            m+=60
            h-=1
        if h<0:
            h+=24
        return Time(h, m, s)
    
    def __gt__(self, other: 'Time'):
        if self.h>other.h:
            return True
        if self.m>other.m:
            return True
        if self.s>other.s:
            return True
        return False
    
    def __eq__(self, other: 'Time'):
        if self.h==other.h and self.m==other.m and self.s==other.s:
            return True
        return False
    
    def __ne__(self, other: 'Time'):
        return not self.__eq__(other)
    
    def __ge__(self, other: 'Time'):
        if self.h==other.h and self.m==other.m and self.s==other.s:
            return True
        return self.__gt__(other)

    def __str__(self):
        return f"{self.h:02}:{self.m:02}:{self.s:02}"

class StopWatch(Time):
    def __init__(self, h=0, m=0, s=0):
        super().__init__(h, m, s)
        self.ms = 0

    def count(self):
        while True:
            sleep(0.001)
            self.ms+=1
            if self.ms>999:
                self.ms=0
                self.s+=1
                if self.s>59:
                    self.s=0
                    self.m+=1
                    if self.m>59:
                        self.m=0
                        self.h+=1
                        if self.h>23:
                            self.h=0
            print(self)
    
    def __str__(self):
        return f"{super().__str__()}.{self.ms:03}"


# t1 = Time(17, 22, 30)
# t2 = Time(15, 10, 7)
# t3 = t1-t2
# print(t1==t2)
s1 = StopWatch()
s1.count()