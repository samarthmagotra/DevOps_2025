import json
from pprint import pprint
from json import JSONEncoder

# A basic python dictionary 
py_object = [{"c": 0, "b": 0, "a": 0},'samarth','magotra',('x','y',1),['u',2,3,4]]

# Encoding 
json_string = json.dumps(py_object)
print("Encoding")
pprint(json_string)
print(type(json_string)) 

# Decoding JSON 
py_obj = json.loads(json_string) 
print("Decoding")
pprint(py_obj)
print(type(py_obj))


class Student:
    def __init__(self, name, roll_no, address):
        self.name = name
        self.roll_no = roll_no
        self.address = address

    def to_json(self):
        '''
        convert the instance of this class to json
        '''
        return json.dumps(self, indent=4, default=lambda o: o.__dict__)


class Address:
    def __init__(self, city, street, pin):
        self.city = city
        self.street = street
        self.pin = pin


address = Address("Bulandshahr", "Adarsh Nagar", "203001")
student = Student("Raju", 53, address)

# Encoding
student_json = student.to_json()
print(student_json)
print(type(student_json))

# Decoding
student = json.loads(student_json)
print(student)
print(type(student))

"""
class Student:
    def __init__(self, name, roll_no, address):
        self.name = name
        self.roll_no = roll_no
        self.address = address


class Address:
    def __init__(self, city, street, pin):
        self.city = city
        self.street = street
        self.pin = pin


class EncodeStudent(JSONEncoder):
    def default(self, o):
        return o.__dict__


address = Address("Bulandshahr", "Adarsh Nagar", "203001")
student = Student("Raju", 53, address)

# Encoding custom object to json
# using cls(class) argument of
# dumps method
student_JSON = json.dumps(student, indent=4,
                          cls=EncodeStudent)
print(student_JSON)
print(type(student_JSON))

# Decoding
student = json.loads(student_JSON)
print()
print(student)
print(type(student))

"""