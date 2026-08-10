students=[]
class School():
    def add_student(self,student):
        for s in students:
            if s["id"]==student["id"]:
                 return ("student already exist")
        students.append(student)
        return "student added successfully"

    def get_students(self):
        if students:
            return students
        else:
            return "students not found"
        
    def get_student_by_id(self,id):
         for student in students:
              if student["id"]==id:
                   return student
              else:
                   return "student not found"
              
    def update_student(self,student,id=int,description=str):
         for student in students:
              if student["id"]==id:
                   student["description"]=description
                   return ("student updated successfully")
              else:
                   return "student not updates successfully"


    def delete_student(self,id):
         for student in students:
              if student["id"]==student["id"]:
                   students.remove(student)
                   return "student removed successfully"
              else:
                   return "student not found"
              

    