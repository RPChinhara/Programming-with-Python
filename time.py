class Time:
    def __init__(self, *args) -> None:
        if len(args) == 0:
            self.hr = 0
            self.min = 0
        if len(args) == 1:
            self.hr = args[0]//60
            self.min = args[0]%60
        if len(args) == 2:
            self.hr = args[0]
            self.min = args[1]
    
    def get_time(self):
        return (self.hr, self.min)

a = Time()
print(a.get_time())

b = Time(71)
print(b.get_time())

c = Time(1, 18)
print(c.get_time())