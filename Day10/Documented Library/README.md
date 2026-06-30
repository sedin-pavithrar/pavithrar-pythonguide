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



Step 1: Install Sphinx

If you haven't already:

pip install sphinx

Verify:

sphinx-build --version
Step 2: Go to your project folder

For example:

cd "D:\python\Day10\Documented Library"
Step 3: Create the Sphinx project

Run:

sphinx-quickstart docs

Answer the prompts like this:

Separate source and build directories (y/n) [n]: y

Project name: Transport Fare Calculator

Author name(s): Pavithra Ram

Project release []: 1.0

Project language [en]:

This creates:

docs/
│
├── build/
├── source/
│   ├── conf.py
│   ├── index.rst
│   └── ...
└── Makefile
Step 4: Edit conf.py

Open:

docs/source/conf.py
Add these lines at the very top:
import os
import sys

sys.path.insert(0, os.path.abspath("../.."))

This tells Sphinx where your fare_calculator.py file is located.

Find:
extensions = []

Replace it with:

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
]
Step 5: Create fare_calculator.rst

Inside

docs/source/

create a new file called

fare_calculator.rst

Contents:

Fare Calculator
===============

.. automodule:: fare_calculator
   :members:
   :undoc-members:
   :show-inheritance:

Replace fare_calculator with your module name if it's different.

Step 6: Edit index.rst

Replace everything after the title with:

Welcome to Transport Fare Calculator's documentation!
======================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   fare_calculator
Step 7: Build the HTML

Move into the docs folder:

cd docs
On Windows

Run:

.\make.bat html

or

sphinx-build -b html source build/html
Step 8: Open the documentation

Open this file in your browser:

docs/build/html/index.html

You'll see documentation like:

TransportCalculator

calculate_fare()

estimate_eta()

apply_discount()

trip_summary()

surge_multiplier()

km_to_miles()

validate_distance()

validate_vehicle()

validate_hour()

validate_day_type()

validate_discount()

along with all of your docstrings and examples.

Expected folder structure
Documented Library/
│
├── fare_calculator.py
│
└── docs/
    ├── build/
    │   └── html/
    │       └── index.html
    │
    ├── source/
    │   ├── conf.py
    │   ├── index.rst
    │   └── fare_calculator.rst
    │
    ├── Makefile
    └── make.bat
If you're using Google-style docstrings (with Args:, Returns:, Raises:)

To have those sections rendered nicely instead of as plain text, install the Napoleon extension:

pip install sphinx

Then in conf.py, use:

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.napoleon",
]

The napoleon extension is specifically designed to render Google-style and NumPy-style docstrings cleanly in the generated HTML.