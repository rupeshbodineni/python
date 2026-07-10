class student():
    college="acem"
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    def avg_score(self):
        sum=0
        for mark in self.marks:
            sum+=mark
        print("your avg score is ,",sum/3)

s1=student("rupesh",[50,60,80])
s1.avg_score()