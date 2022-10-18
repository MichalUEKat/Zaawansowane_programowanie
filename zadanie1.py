import statistics as s
class Student:
    def __init__(self,name:str, marks:list[int]) -> None:
        self.name = name
        self.marks= marks
    def is_passed(self):
        number_mean = s.mean(self.marks)
        if(number_mean>50):
            return True
        return False


obj1= Student('Janek',[50,10000,240])
ob2 = Student('Jan',[1,1,1])

print(obj1.is_passed())
print(ob2.is_passed())