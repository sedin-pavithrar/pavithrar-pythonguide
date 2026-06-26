Summary: Virtual Environment & Dependency Management Project

You set up a modern Python project using venv, pip, requirements.txt, pyproject.toml, and importlib.

1. Created and Activated a Virtual Environment

You created an isolated Python environment so project dependencies don't affect other projects.

python -m venv myenv

Activated it in PowerShell:

.\myenv\Scripts\Activate.ps1

Your prompt changed to:

(myenv) PS D:\python\Day7\app_check>

This confirms the virtual environment is active.

2. Installed Project Dependencies

You installed the required packages:

pip install requests pandas numpy

Installed packages:

requests
pandas
numpy

Along with their dependencies:

urllib3
certifi
charset-normalizer
idna
python-dateutil
six
tzdata

Verified installation using:

pip list
3. Learned About Multiple Virtual Environments

You discovered you had two environments:

D:\python\.venv
D:\python\Day7\app_check\myenv

You accidentally tried to use:

/d:/python/.venv/Scripts/python.exe

This failed because:

The path syntax was incorrect for PowerShell.
You already had myenv activated.

Key takeaway:

When a virtual environment is activated, simply use python or pip.

4. Generated requirements.txt

You created a snapshot of the exact installed packages:

pip freeze > requirements.txt

Purpose:

Recreate the same environment later.

Example:

pip install -r requirements.txt

5. Understood pyproject.toml

You learned that pyproject.toml is the modern Python project configuration file.

Unlike requirements.txt, it is created manually because it describes your project.

Example:

[build-system]
requires = ["setuptools>=68", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "my-app"
version = "1.0.0"
requires-python = ">=3.10"

dependencies = [
    "requests>=2.28",
    "pandas>=2.0",
    "numpy>=1.24"
]

It defines:

Build tool
Project name
Version
Supported Python versions
Required dependencies


6. Created the Project Structure

Your project should look like:

app_check/
├── myenv/
├── requirements.txt
├── pyproject.toml
└── src/
    └── my_app/
        ├── __init__.py
        └── checker.py
7. Wrote a Dependency Checker

You created checker.py using:

import importlib

The script checks whether required packages are installed dynamically:

importlib.import_module("requests")

This approach is used by many frameworks to validate dependencies.

Expected output:

✓ OK   requests
✓ OK   pandas
✓ OK   numpy
✗ MISS nonexistent

Installed : 3
Missing   : 1
Total     : 4

Key Concepts You Learned
Tool/File	Purpose
venv	Creates isolated Python environments
pip	Installs and manages packages
requirements.txt	Stores exact installed versions
pyproject.toml	Defines project metadata and dependencies
importlib.import_module()	Dynamically imports modules
pip freeze	Generates requirements.txt
Final Workflow

python -m venv myenv

.\myenv\Scripts\Activate.ps1

pip install requests pandas numpy

pip freeze > requirements.txt

python src\my_app\checker.py

