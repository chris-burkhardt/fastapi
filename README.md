# Algorithm Solutions API 

A FastAPI-based API for running and measuring the performance of algorithmic solutions. This project demonstrates clean code organization, API design, and performance measurement capabilities.

> **Note**: This is not a dynamic problem-solving platform. It's an exploration of FastAPI's capabilities to:
> - Structure a clean, modular API project
> - Handle requests and responses with type safety
> - Measure solution performance
> - Document code and API endpoints
> 
> The solutions are pre-written and the API simply executes them. This is a demonstration of FastAPI's features rather than a full-featured algorithmic problem platform.

## Virtual Environment Setup (FastAPI)

To isolate project dependencies, use a Python virtual environment.

1. **Create the virtual environment**  
   ```bash
   python -m venv venv
   ```

2. **Activate it**  
   - **macOS/Linux**:  
     ```bash
     source venv/bin/activate
     ```
   - **Windows**:  
     ```bash
     .\venv\Scripts\activate
     ```

3. **Confirm activation**  
   Your terminal prompt should now begin with `(venv)`.

4. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

   Example `requirements.txt`:
   ```
   fastapi[standard,dev]
   watchfiles
   psutil
   pydantic
   ```

## VS Code Integration

1. Open Command Palette: `Cmd+Shift+P` (macOS) or `Ctrl+Shift+P` (Windows/Linux)  
2. Select:
   ```
   Python: Select Interpreter
   ```
3. Choose the one inside your `.venv` folder

> If your environment doesn't appear, activate it in your terminal before opening VS Code.

## Features

- Run algorithmic solutions with performance metrics (time and memory)
- Organized by problem categories (arrays, strings, trees, etc.)
- Interactive API documentation via Swagger UI (`/docs`, and `/redoc`)
- Clean, modular code structure
- Type-safe request/response handling with Pydantic

## Project Structure

```
app/
├── api/                    # API endpoints
│   └── algo.py            # Main algorithm execution endpoint
├── models/                 # Pydantic models for request/response
│   └── algo_models.py     # Solution request/response models
├── solutions/             # Algorithm solutions by category
│   ├── arrays/           # Array-based problems
│   ├── strings/          # String-based problems
│   └── trees/            # Tree-based problems
└── main.py               # FastAPI application setup
```

## How It Works

1. **Adding a Solution**
   - Create a new Python file in the appropriate category directory
   - Implement a `solve` function that takes an `input_data` dictionary
   - Add problem description and solution notes as documentation

2. **Running a Solution**
   - Send a POST request to `/algo/solve` with:
     ```json
     {
         "problem_id": "your_solution_file_name",
         "category": "category_name",
         "input_data": {
             "your_input": "here"
         }
     }
     ```
   - Get back performance metrics and results

3. **Viewing Documentation**
   - Visit `/docs` for interactive API documentation
   - Each solution file contains its own documentation
   - Performance metrics are automatically measured

