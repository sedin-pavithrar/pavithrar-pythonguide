
Day 11  —  Assignment 1
Code Formatter Setup & Cleanup
black
ruff
isort
pyproject.toml
Real-world App
Any Python CI/CD pipeline
Overview
Takes a deliberately badly formatted Python file (missing spaces, import clumping, inconsistent 
style) and applies black (auto-formatter) then ruff check --fix (linter). pyproject.toml configured with 
[tool.black] and [tool.ruff] sections. Optional pre-commit hook runs both on every git commit -- this is 
standard at all professional Python shops.
Problem
Take badly formatted Python, run black and ruff to fix it. Configure pyproject.toml and set up 
pre-commit hooks.


Before
import os,sys
import   json
def calculate_total(items,discount=0,tax=0.18):
    total=0
    for item in items :
        total=total+item["price"]*item["quantity"]
    if discount>0 : total=total-(total*discount/100)
    return   round(total,2)


After black
import json
import os
import sys
def calculate_total(items, discount=0, tax=0.18):
    total = 0
    for item in items:
        total = total + item["price"] * item["quantity"]
    if discount > 0:
        total = total - (total * discount / 100)
    return round(total, 2)
pyproject.toml
[tool.black]
line-length = 88
target-version = ["py310"]
[tool.ruff]
line-length = 88
select = ["E","F","I"]
Constraints
•  Run black and show diff output
•  Run ruff check and list violations
•  Configure pyproject.toml
•  Bonus: .pre-commit-config.yaml with black + ruff hook



Black — the formatter
Black is what we call an "opinionated" formatter. You don't configure how it formats things — it just has one correct way of doing it (spacing, quote style, line breaks, blank lines between functions) and rewrites your file to match. The whole point is removing the debate. You saw it take def calculate_total(items,discount=0,tax=0.18): and turn it into properly spaced, PEP8-compliant code. You ran black --diff first, which is a dry run — it shows you what would change without touching the file, which is good practice so you can review before committing. Then black billing.py actually applies it.
Ruff — the linter
Where black only cares about style (spacing, formatting), ruff checks for actual problems — unused imports, undefined variables, bad import ordering, etc. In our example it caught that os, sys, and json were imported but never used anywhere in the file — that's dead code, and ruff flags it as F401. It also caught import os, sys on one line, which is against PEP8 (E401 — imports should be one per line). Running ruff check --fix doesn't just point these out, it auto-fixes whatever it safely can — in this case it deleted the unused imports entirely.


isort
This one specifically sorts and groups your imports — standard library first, then third-party, then your own project's modules, alphabetically within each group. Ruff can actually do this itself (that's the I001 rule you saw), so in modern setups people often don't even run isort separately anymore — ruff covers it. I kept the isort config in pyproject.toml mostly for completeness / in case someone's still using the standalone tool in their editor.
pyproject.toml
This is just the single config file modern Python projects use to tell all these tools how to behave — instead of having a .flake8 file, a .isort.cfg, a black config buried somewhere else, everything lives in one place under [tool.black], [tool.ruff], etc. Things like line length (we set 88, black's default) and which Python version to target live here.
pre-commit
This is the part that makes all of the above actually enforced rather than optional. The .pre-commit-config.yaml file sets up a git hook — meaning before any commit is allowed to go through, it automatically runs black and ruff on your changed files. If your code isn't formatted correctly, the commit gets blocked (or auto-fixed and you just need to re-stage and commit again). This is what stops badly formatted code from ever reaching the shared repo in the first place — nobody has to manually remember to run these tools, it just happens.




ruff check --fix bill_total.py
black bill_total.py   