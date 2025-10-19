# first programmer writes
def insert_patient_data(name, age):
    print(name)
    print(age)
    # insert into db
    print("Inserted into db")


# junior programmer writes
insert_patient_data("Rohit", "twentyfive")  # age should be int but passing string

print("=====================================")


# second programmer writes using type hints
def insert_patient_data_v2(name: str, age: int):
    print(name)
    print(age)
    # insert into db
    print("Inserted into db")


# junior programmer writes
insert_patient_data_v2("Rohit", "twentyfive")  # age should be int but passing string
# This will not give any error, as type hints are not enforced at runtime

print("=====================================")


# third way to write this function using if condition
def insert_patient_data_v3(name: str, age: int):
    # use type  check  with == operator
    if type(name) == str and type(age) == int:
        print(name)
        print(age)
        # insert into db
        print("Inserted into db")
    else:
        raise TypeError("Invalid data types")


# junior programmer writes
# insert_patient_data_v3("Rohit", "twentyfive")
insert_patient_data_v3("Rohit", 25)
# This will give error at runtime

print("=====================================")


# insert patient data function with negative age check if another if condition is added in the same function
def insert_patient_data_v4(name: str, age: int):
    # use type check with == operator
    if not (type(name) == str and type(age) == int):
        raise TypeError("Invalid data types")
    if age < 0:
        raise ValueError("Age cannot be negative")
    print(name)
    print(age)
    # insert into db
    print("Inserted into db")


# insert_patient_data_v4("Rohit", -25)  # negative age
print("=====================================")


# fourth way  same function to update the patient  data
def update_patient_data(name: str, age: int):
    if type(name) == str and type(age) == int:
        print(name)
        print(age)
        # update db
        print("Updated in db")
    else:
        raise TypeError("Invalid data types")


# junior programmer writes
# update_patient_data("Rohit", "twentyfive")
update_patient_data("Rohit", 26)

# the above 2 method insert_patient_data_v3 and update_patient_data have same type checking code
# this is code duplication
print("=====================================")


from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional


class Patient(BaseModel):
    name: str = Field(
        max_length=10,
        title="Patient Name",
        description="The name of the patient",
        examples=["Rohit", "Alice"],
    )  # name is required field
    age: int = Field(
        ge=0, lt=120
    )  # age should be greater than or equal to 0 and less than 120
    email: EmailStr  # validate email format
    weight: float = Field(gt=0)  # weight should be greater than 0
    married: bool = False  # make the default value to False
    allergies: Optional[List[str]] = (
        None  # make this optional by using Optional[List[str]]
    )
    contact_details: Dict[str, str]
    linkedin_url: AnyUrl  # validate URL format


# function to insert patient data
def insert_patient(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print((patient.married))
    # insert into db
    print("Inserted into db")


# function to update patient data
def update_patient(patient: Patient):
    print(patient.name)
    print(patient.age)
    # update db
    print("Updated in db")


# patient_info = {"name": "Rohit", "age": "twentyfive"} # age should be int but passing string
# patient_info = {
#     "name": "Rohit",
#     "age": 25,
#     "weight": 70.5,
#     "married": False,
#     "allergies": ["pollen", "nuts"],
#     "contact_details": {"email": "rohit@example.com", "phone": "1234567890"},
# }
# patient = Patient(**patient_info)
# print(patient)
# insert_patient(patient)
# print("=====================================")
# update_patient(patient)


# # make the allergies field optional in the patient model
# patient_info2 = {
#     "name": "Alice",
#     "age": 30,
#     "weight": 60.0,
#     "married": True,
#     "contact_details": {"email": "alice@example.com", "phone": "0987654321"},
# }
# patient2 = Patient(**patient_info2)
# print(patient2)
# insert_patient(patient2)
# print("=====================================")

# # marriage defaults to False and allergies defaults to None
# patient_info3 = {
#     "name": "Bob",
#     "age": 40,
#     "weight": 80.0,
#     "contact_details": {"email": "bob@example.com", "phone": "1122334455"},
# }
# patient3 = Patient(**patient_info3)
# print(patient3)
# insert_patient(patient3)
# print("=====================================")

# invalid email format validation in patient model
patient_info4 = {
    "name": "Charlie",
    "age": 35,
    "email": "charlieexamplegmail.com",  # invalid email format
    "weight": 75.0,
    "married": True,
    "contact_details": {"email": "charlie@example.com", "phone": "6677889900"},
}
# call the function
# patient4 = Patient(**patient_info4)  # this will raise validation error
# print(patient4)
# insert_patient(patient4) # invalid email format
print("=====================================")

# invalid URL format validation in patient model
patient_info5 = {
    "name": "David",
    "age": 28,
    "email": "david@example.com",  # valid email format
    "weight": 68.0,
    "married": False,
    "contact_details": {"email": "david@example.com", "phone": "6677889900"},
    "linkedin_url": "www.linkedin.com/in/david",  # invalid URL format
}
# patient5 = Patient(**patient_info5)  # this will raise validation error
# print(patient5)
# insert_patient(patient5)  # invalid URL format
print("=====================================")

# negative weight validation in patient model
patient_info6 = {
    "name": "Eve",
    "age": 32,
    "email": "eve@example.com",  # valid email format
    "weight": -55.0,  # negative weight
    "married": True,
    "contact_details": {"email": "eve@example.com", "phone": "6677889900"},
    "linkedin_url": "https://www.linkedin.com/in/eve",  # valid URL format
}
# patient6 = Patient(**patient_info6)  # this will raise validation error
# print(patient6)
# insert_patient(patient6)  # negative weight
print("=====================================")


# age less than 0 and greater than 120 validation in patient model
patient_info7 = {
    "name": "Frank",
    "age": 130,  # age greater than 120
    "email": "frank@example.com",  # valid email format
    "weight": 85.0,
    "married": False,
    "contact_details": {"email": "frank@example.com", "phone": "6677889900"},
    "linkedin_url": "https://www.linkedin.com/in/frank",  # valid URL format
}
# patient7 = Patient(**patient_info7)  # this will raise validation error
# print(patient7)
# insert_patient(patient7)  # age greater than 120
print("=====================================")

# name max length validation in patient model
patient_info8 = {
    "name": "Christopher",  # name length greater than 10
    "age": 29,
    "email": "christopher@example.com",  # valid email format
    "weight": 75.0,
    "married": True,
    "contact_details": {"email": "christopher@example.com", "phone": "6677889900"},
    "linkedin_url": "https://www.linkedin.com/in/christopher",  # valid URL format
}
# patient8 = Patient(**patient_info8)  # this will raise validation error
# print(patient8)
# insert_patient(patient8)  # name length greater than 10
print("=====================================")
