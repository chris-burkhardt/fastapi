from typing import Any
from pydantic import BaseModel

class SolutionRequest(BaseModel):
    problem_id: str
    category: str  # e.g., "arrays", "strings", "trees"
    input_data: Any

class SolutionResponse(BaseModel):
    problem_id: str
    result: Any
    execution_time: float # would log this typically, not return it
    memory_usage: float # would log this typically, not return it