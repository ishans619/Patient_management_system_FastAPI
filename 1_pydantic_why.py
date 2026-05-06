from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator, computed_field
from typing import List, Dict, Optional

class Patient(BaseModel):
    name: str = Field(max_length = 50)
    age: int = Field(gt = 0, lt = 100)
    email: EmailStr
    weight: float
    height: float
    married: Optional[bool] = None
    allergies: List[str] = Field(max_length = 5)
    contact_details: Dict[str, str]

    @field_validator("email")
    @classmethod
    def email_validator(cls, value):
        
        valid_domains = ["hdfc.com", "icici.com"]
        domain_name = value.split("@")[-1]

        if domain_name not in valid_domains:
            raise ValueError("Not a valid domain")
        
        return value
    
    @model_validator(mode = "after")
    def validate_emergency_contact(cls, model):
        if model.age > 60 and "emergency" not in model.contact_details:
            raise ValueError("Patients older than 60 must have an emergency contact")
        
        return model

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2), 2)
        return bmi


def update_patient_data(patient: Patient):
    print(patient.age)
    print(patient.name)
    print(patient.email)
    print(patient.weight)
    print(patient.height)
    print("BMI", patient.bmi)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)

patient_info = {"name": "nitish", "age": 30, "email": "ishanshukla@hdfc.com", "weight": 70.0, "height": 1.8, "allergies": ["pollen", "dust"], "contact_details": {"email": "abc@gmail.com", "phone": "23456789"}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)
