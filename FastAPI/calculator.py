
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import math

# Create FastAPI application
app = FastAPI(
    title="Complete Calculator API",
    description="Basic and Scientific Calculator using Python FastAPI",
    version="1.0"
)


# Input model
class CalculatorInput(BaseModel):
    operation: str
    a: float
    b: float | None = None
    digits: int = Field(default=2, ge=0, le=10)


# Helper function to validate second number
def require_b(b: float | None) -> float:

    if b is None:
        raise HTTPException(
            status_code=400,
            detail="Second number is required"
        )

    return b


# Home API
@app.get("/")
def home():
    return {
        "message": "Welcome to Complete Calculator API",
        "documentation": "/docs"
    }


# Calculator API
@app.post("/calculate")
def calculate(data: CalculatorInput):

    operation = data.operation.lower()
    a = data.a
    b = data.b

    # Basic arithmetic operations

    if operation == "add":
        b_value = require_b(b)
        result = a + b_value

    elif operation == "subtract":
        b_value = require_b(b)
        result = a - b_value

    elif operation == "multiply":
        b_value = require_b(b)
        result = a * b_value

    elif operation == "divide":
        b_value = require_b(b)

        if b_value == 0:
            raise HTTPException(
                status_code=400,
                detail="Cannot divide by zero"
            )

        result = a / b_value

    elif operation == "modulus":
        b_value = require_b(b)

        if b_value == 0:
            raise HTTPException(
                status_code=400,
                detail="Cannot calculate modulus by zero"
            )

        result = a % b_value

    elif operation == "floor_divide":
        b_value = require_b(b)

        if b_value == 0:
            raise HTTPException(
                status_code=400,
                detail="Cannot divide by zero"
            )

        result = a // b_value

    elif operation == "power":
        b_value = require_b(b)
        result = a ** b_value

    # Percentage calculation

    elif operation == "percentage":
        b_value = require_b(b)
        result = (a * b_value) / 100

    # Square and cube

    elif operation == "square":
        result = a ** 2

    elif operation == "cube":
        result = a ** 3

    # Square root

    elif operation == "sqrt":

        if a < 0:
            raise HTTPException(
                status_code=400,
                detail="Square root of negative number is not supported"
            )

        result = math.sqrt(a)

    # Factorial

    elif operation == "factorial":

        if a < 0 or not a.is_integer():
            raise HTTPException(
                status_code=400,
                detail="Factorial requires a non-negative integer"
            )

        if a > 170:
            raise HTTPException(
                status_code=400,
                detail="Number is too large for factorial"
            )

        result = math.factorial(int(a))

    # Absolute value

    elif operation == "absolute":
        result = abs(a)

    # Rounding

    elif operation == "round":
        result = round(a, data.digits)

    # Trigonometric functions (input in degrees)

    elif operation == "sin":
        result = math.sin(math.radians(a))

    elif operation == "cos":
        result = math.cos(math.radians(a))

    elif operation == "tan":
        result = math.tan(math.radians(a))

    # Logarithms

    elif operation == "log":

        if a <= 0:
            raise HTTPException(
                status_code=400,
                detail="Log requires a positive number"
            )

        result = math.log(a)

    elif operation == "log10":

        if a <= 0:
            raise HTTPException(
                status_code=400,
                detail="Log10 requires a positive number"
            )

        result = math.log10(a)

    else:
        raise HTTPException(
            status_code=400,
            detail="Invalid operation. Check available operations."
        )

    # Check result

    if isinstance(result, complex):
        raise HTTPException(
            status_code=400,
            detail="Complex results are not supported"
        )

    if isinstance(result, float) and not math.isfinite(result):
        raise HTTPException(
            status_code=400,
            detail="Invalid calculation result"
        )

    # Return API response

    return {
        "operation": operation,
        "number1": a,
        "number2": b,
        "result": result
    }
