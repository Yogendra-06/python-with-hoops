class student:
    name="abc"
    roll_no=6621
    maths=58
    physics=55
    chemistry=40
    
    def total_marks(self):
        total=maths+physics+chemistry
        print("total marks",total)
        
    def average(self):
        avg=(maths+physics+chemistr)/3
        print("average: ",avg)
        
    def grade(self):
        if total>90:
            print("grade : A")
        elif total>=75:
            print("grade : B")
        elif total>=60:
            print("grade : C")
        elif total>=40:
            print("grade : D")
        else:
            print("fail")
        
s=student()
s.total_marks()
s.average()
s.grade()
        
            
    