# from pydantic import BaseModel

# class Student(BaseModel):
#     name:str

# new_student={'name':'Ashish'}

# student=Student(**new_student)

# print(student)

# print(type(student))


# --------------<use optional field (eg:age)<----------------
# from pydantic import BaseModel
# from typing import Optional

# class Student(BaseModel):
#     name:str
#     age:Optional[int]=None

# new_student={'name':'Ashish','age':19}

# student=Student(**new_student)

# print(student)

# print(type(student))



# -----------<also uderstand the typeCasting(eg:age -->is string )bydefault string age para ko int me output de diya <-------------------
# from pydantic import BaseModel
# from typing import Optional

# class Student(BaseModel):
#     name:str
#     age:Optional[int]=None

# new_student={'name':'Ashish','age':'19'}

# student=Student(**new_student)

# print(student)

# print(type(student))




# ---------------------------<vadidation perform (like email)<------------------

# from pydantic import BaseModel,EmailStr
# from typing import Optional

# class Student(BaseModel):
#     name:str
#     age:Optional[int]=None
#     email:EmailStr


# # new_student={'name':'Ashish','age':'19','email':'abc'}  #ye aumatic error dega qki gmail proper formate me nhi hai 
# new_student={'name':'Ashish','age':19,'email':'abc@gmail.com'}

# student=Student(**new_student)

# print(student)




# -------------------<apply Findfunction (apply sonstraints like-(cgpa))<-------------------

# from pydantic import BaseModel,EmailStr,Field
# from typing import Optional

# class Student(BaseModel):
#     name:str
#     age:Optional[int]=None
#     email:EmailStr
#     cgpa:float=Field(gt=0,lt=10)
    
#     # cgpa:float=Field(gt=0,lt=10,default=5,description="A decimal val rep the cgpa of student") #all same kaam yaha v hoga 

# # new_student={'name':'Ashish','age':19,'email':'abc@gmail.com','cgpa':12}  #cgpta hmne (1-10)apply kiya hai esliye yaha error aayega qki hm range se jyada value le rhe hai 
# new_student={'name':'Ashish','age':19,'email':'abc@gmail.com','cgpa':5} 

# student=Student(**new_student)

# print(student)




# -------------------<print selected value<-------------------------
from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):
    name:str
    age:Optional[int]=None
    email:EmailStr
    cgpa:float=Field(gt=0,lt=10)
    
new_student={'name':'Ashish','age':19,'email':'abc@gmail.com','cgpa':5} 

student=Student(**new_student)

student_dict=dict(student)
print(student_dict['age'])

# convert into json 
student_json=student.model_dump_json()