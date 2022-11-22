from dataclasses import dataclass

@dataclass
class Student:
    sid : int
    age : int
    name : str
    dept_name : str

@dataclass
class Department:
    dept_id : int
    sid : int
    dept_name : str
    
# function for INNER JOIN     
def inner_join(Student,Department):
    result=[]
    for s in Student:
        for d in Department:
            if(s.sid==d.sid):
                result.append(
                    (s.sid,s.name,d.dept_name))
    return result

# OBJECTS OF STUDENT CLASS
x1=Student(1,20,'A','CSE')   # sid, age, name, dept_name
x2=Student(2,20,'B','EE')
x3=Student(3,20,'C','CIVIL')
x4=Student(4,20,'D','CSE')

# OBJECT OF DEPARTMENT CLASS
y1=Department(10,2,'EE')     # dept_id, sid, name
y2=Department(11,3,'CIVIL')
y3=Department(12,4,'CSE')
y4=Department(13,1,'CSE')

Student=[x1,x2,x3,x4]  # type: ignore
Department=[y1,y2,y3,y4]  # type: ignore
print(inner_join(Student,Department))    