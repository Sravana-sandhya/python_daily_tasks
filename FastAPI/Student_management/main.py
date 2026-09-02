from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app = FastAPI()
students = []

#Student model:
class Student(BaseModel):
    name : str
    age : int
    course : str
    marks : int

#......Q1 : Create FastAPI Application........
@app.get("/")
def home():
    return {"message": "Student Management System is started"} 

#.......Q2. Create API – Add Student..........
@app.post("/students")
def add_student(student: Student):
    new_student = {
        "id": len(students) + 1,
        "name": student.name,
        "age": student.age,
        "course": student.course,
        "marks": student.marks
    }
    students.append(new_student)
    return{"message" : "Student added sucessfully"}

#......Q3. Create API – Get All Students..........   
@app.get("/students")
def get_all_students():
    return students

#.....Q4. Create API – Get Student by ID..........
@app.get("/students/{id}")
def get_student_by_id(id: int):
    for student in students:
        if student["id"] == id:
            return student
    raise HTTPException(status_code = 404, detail = "Student not found")

#.....Q5. Create API – Update Student...........
@app.put("/students/{id}")
def update_student(id: int, updated_student: Student):
    for student in students:
        if student["id"] == id:
            student["name"] = updated_student.name
            student["age"] = updated_student.age
            student["course"] = updated_student.course
            student["marks"] = updated_student.marks
            return {"message": "Student updated successfully"}
    raise HTTPException(status_code = 404, detail = "Student not found")

#.....Q6. Create API – Delete Student...........
@app.delete("/students/{id}")
def delete_student(id: int):
    for student in students:
        if student["id"] == id:
            students.remove(student)
            return {"message": "Student deleted successfully"}
    raise HTTPException(status_code = 404, detail = "Student not found")

#.........Run the server using the command: uvicorn filename:app --reload........
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app",reload = True)