from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pincode: int

class Patient(BaseModel):
    name: str
    age: int
    gender: str
    address: Address

address_info = {"city": "lucknow", "state": "UP", "pincode": 226020}

address1 = Address(**address_info)

patient_info = {"name": "Ishan", "age": 24, "gender": "male", "address": address1}

patient1 = Patient(**patient_info)

temp = patient1.model_dump()

print(temp)
print(type(temp)) 






