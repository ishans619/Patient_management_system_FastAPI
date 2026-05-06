from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)

    return data

@app.get("/")
def hello():
    return {"message" : "Hello world"}

@app.get("/about")
def about():
    return {"message" : "This is an API that helps you maintain patients records."}

@app.get("/view")
def view():
    data = load_data()

    return data

@app.get("/patient/{patient_id}")
def view_patient(patient_id: str = Path(..., description = "This is suppose to be the ID of the patient", example = "P001")):
    data = load_data()

    for patient in data["patients"]:
        if patient["id"] == patient_id:
            return patient
        
    raise HTTPException(status_code = 404, detail = "Patient not found")

@app.get("/sort")
def sort_patients(sort_by: str = Query(..., description = "Sort on the basis of age or id"), 
order: str = Query(..., description = "sort in asc or desc order")):
    
    valid_fields = ["age", "id"]

    if sort_by not in valid_fields:
        raise HTTPException(status_code = 400, detail = f"Invalid field, select from {valid_fields}")
    
    if order not in ["asc", "desc"]:
        raise HTTPException(status_code = 400, detail = "Invalid choice select between asc or desc")
    
    data = load_data()

    if(order == "desc"):
        sort_order = True
    else:
        sort_order = False

    sorted_data = sorted(data["patients"], key = lambda x : x.get(sort_by, 0), reverse = sort_order)

    return sorted_data