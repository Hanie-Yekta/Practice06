
class Time:
    def __init__(self, h = 0, m = 0, s = 0):
        self.hour = h
        self.minute = m
        self.second = s

    def add(self, other):
        sum = Time()
        sum.hour = self.hour + other.hour
        sum.minute = self.minute + other.minute
        sum.second = self.second + other.second
        sum.Correction1()
        return sum


    def sub(self, other):
        subm = Time()
        self.Correction2(other)
        subm.second = self.second - other.second
        subm.minute = self.minute - other.minute
        subm.hour = self.hour - other.hour
        return subm
    
    def convert_to_sec(self):
        s = self.hour * 3600 + self.minute * 60 + self.second
        return s

    #tabe tashih maqadir bad az mohasebat
    def Correction1(self):
        while self.second >= 60:
            self.second -= 60
            self.minute += 1

        while self.minute >= 60:
            self.minute -= 60
            self.hour += 1

    #tabe tashih maqadie dar zaman vorud
    def Correction2(self, other):
        if self.second < other.second:
            self.second += 60
            self.minute -= 1

        if self.minute < other.minute:
            self.minute += 60
            self.hour -= 1


    def show(self):
            print(self.hour, ":", self.minute, ":", self.second)

    

#tabe vorud saat
def get_hour():
    print("Enter the hour:")
    input_hour = int(input("--> "))
    return input_hour

#tabe vorud daqiqe
def get_minute():
    print("Enter the minute:")
    input_minute = int(input("--> "))
    return input_minute

#tabe vorud sanie
def get_second():
    print("Enter the second:")
    input_second = int(input("--> "))
    return input_second

#################

print("Enter the operation:\n1.Sum\n2.Sub\n3.Convert the second to time\n4.Convert the time to second")
choice = int(input("--> "))

#jam
if choice == 1:
    obj1 = Time(get_hour(), get_minute(), get_second())
    obj2 = Time(get_hour(), get_minute(), get_second())
    result = obj1.add(obj2)
    result.show()

#tafriq
elif choice == 2:
    obj1 = Time(get_hour(), get_minute(), get_second())
    obj2 = Time(get_hour(), get_minute(), get_second())
    result = obj1.sub(obj2)
    result.show()

#tabdil sanie be zaman
elif choice == 3:
    obj1 = Time(s = get_second())
    obj1.show()

#tabdil zaman be sanie
elif choice == 4:
    obj1 = Time(get_hour(), get_minute(), get_second())
    print("Second =", obj1.convert_to_sec())

