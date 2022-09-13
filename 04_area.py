class Area:
    def __init__(self, *args) -> None:
        if len(args) == 0:
            self.area = 0
        if len(args) == 1:
            self.area = args[0] * args[0]
        if len(args) == 2:
            self.area = args[0] * args[1]

    def get_time(self):
        return self.area

a = Area()
b = Area(10)
c = Area(12, 4)

print(a.get_time())
print(b.get_time())
print(c.get_time())