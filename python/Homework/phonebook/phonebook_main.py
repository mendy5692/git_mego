class Salary:
    def __init__(self):
        self.h = 0
        self.z = 0
        print(id(self))
    def update(self,h):
        self.h = h

s = Salary()
print(s.h)

s.update(100)
print(s.h)


