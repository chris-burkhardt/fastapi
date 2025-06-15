from fastapi import APIRouter, HTTPException
import time
import psutil
import os
from app.models.algo_models import SolutionRequest, SolutionResponse

router = APIRouter(prefix="/algo", tags=["algorithms"])

"""
Example: Expected request format for 1d array sum:
{
    "problem_id": "running_sum_1d",
    "category": "arrays",
    "input_data": {
        "nums": [1, 2, 3, 4]
    }
}
"""

@router.post("/solve", response_model=SolutionResponse)
async def solve_problem(request: SolutionRequest):
    """
    Solve an algorithmic problem with the given input data.
    
    The problem_id should match the filename in the solutions directory.
    For example, if you have a solution in solutions/arrays/two_sum.py,
    the problem_id would be "two_sum".
    """
    try:
        # Import the solution module dynamically (requires you know where the file is for now)
        module_path = f"app.solutions.{request.category}.{request.problem_id}"
        solution_module = __import__(module_path, fromlist=["solve"])
        
        # Get the solve function from the module
        solve_func = getattr(solution_module, "solve")
        
        # Execute the solution and measure performance (memory and time)
        process = psutil.Process(os.getpid())
        start_memory = process.memory_info().rss
        start_time = time.time()
        
        result = solve_func(request.input_data)
        
        end_memory = process.memory_info().rss
        memory_usage = (end_memory - start_memory) / 1024
        execution_time = time.time() - start_time
        
        return SolutionResponse(
            problem_id=request.problem_id,
            result=result,
            execution_time=execution_time,
            memory_usage=memory_usage
        )
        
    except ImportError:
        raise HTTPException(status_code=404, detail=f"Problem {request.problem_id} not found in category {request.category}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 