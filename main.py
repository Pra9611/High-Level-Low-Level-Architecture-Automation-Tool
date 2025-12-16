from fastapi import FastAPI
from requirement_analyzer import analyze_requirement
from generator import generate_low_level_design

app = FastAPI()

@app.post("/convert")
def convert_requirement(requirement: str):
    modules = analyze_requirement(requirement)
    design = generate_low_level_design(modules)
    return {
        "modules": modules,
        "low_level_design": design
    }
