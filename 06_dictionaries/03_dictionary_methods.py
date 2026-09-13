"""
Dictionary Methods

Dictionary methods help us work with dictionary data.
"""

student = {
    "name" : "Ruturajsinh",
    "age" : 21,
    "city" : "Vadodara"
}

#get()
print(student.get("name"))

#keys()
print(student.keys())

#values()
print(student.values())

#items()
print(student.items())

#update()
student.update( {"age": 19,"course":"python"} )
print(student)

#pop()
student.pop("city")
print(student)

#clear()
student.clear()
print(student)