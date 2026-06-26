Documented Library -- Sphinx Docstrings
docstrings Google style help() pydoc doctest
Real-world App
Open-source Python packages
Overview
Adds Google-style docstrings (Args, Returns, Raises, Example) to every public function. The 
Example section doubles as a doctest -- run with python -m doctest module.py. help(module) 
renders the docs in terminal. python -m pydoc -w generates a standalone HTML page. This is the 
documentation standard used by requests, pandas, and Django.
Problem
Add Sphinx-compatible docstrings to every function in a module from this course. Verify with 
help() and python -m doctest.
Google-Style Template
def calculate_fare(distance: float, vehicle: str) -> float:
    """Calculate cab fare by distance and vehicle type.
    Args:
        distance (float): Trip distance in km.
        vehicle (str): "car", "bike", or "auto".
    Returns:
        float: Calculated fare in Indian Rupees.
    Raises:
        ValueError: If vehicle type is unsupported.
    Example:
        >>> calculate_fare(10.0, "car")
        200.0
    """
Constraints
•  Args, Returns, Raises, Example in every function
•  All doctests pass: python -m doctest module.py
•  Bonus: Generate HTML with: python -m pydoc -w module_name