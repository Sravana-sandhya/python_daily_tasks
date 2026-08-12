# Q7 : Student Result Generator (Method Overloading Concept) A school system calculates student results differently depending on available data. Create a Result class where a method can calculate the result using either two subjects or three subjects.
class Result:
    def calculate(self,sub1,sub2,sub3 = None):
        if sub3 is None:
           total = sub1 + sub2
           print("Total Marks=",total)
        else:
            total = sub1 + sub2 + sub3
            print("Total Marks=",total)
r = Result()
r.calculate(60,70)
r.calculate(70,80,90)

