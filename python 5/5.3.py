class Time:
    def __init__(self, hour,minute,second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __add__(self, other):
        return self.__hour + other.__hour, self.__minute + other.__minute, self.__second + other.__second
t1 = Time(2,10,10)
t2 = Time(4,15,20)
t3 = t1+t2
print(t3)

