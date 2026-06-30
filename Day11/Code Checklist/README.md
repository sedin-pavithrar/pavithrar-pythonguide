PEP 8 Code Review Checklist
PEP 8 naming ruff --select ALL line length

GitHub PRs / GitLab MR

Manual + automated PEP 8 audit using ruff check --select ALL. Identifies all violations by rule code 
and line number across 10 key rules. After fixing all violations, re-runs ruff to confirm zero errors. 
This is exactly the code review checklist used at Python-first companies like Dropbox, Instagram, 
and Notion.
Problem
Audit a Python file for PEP 8 manually, verify with ruff. List and fix all violations.
Key PEP 8 Rules
# Rule ruff Code
1 Max line length: 88 (black) / 79 
(PEP 8)
E501
2 2 blank lines before top-level 
fn/class
E302
3 1 blank line before method in 
class
E301
4 Variable names: snake_case N816
5 Class names: PascalCase N801
6 Imports on separate lines E401
7 Stdlib imports before third-party I001
8 Spaces around operators E225
9 No semicolons to separate 
statements
E702
10 Use "is True" not "== True" E712
Constraints
•  Run ruff check --select ALL on Day 6 or Day 10 code
•  List every violation with code and line number
•  Fix all -- run again until 0 errors
•  Bonus: Run mypy on same file and fix type errors to





Reading the assignment line by line
"PEP 8 naming, ruff --select ALL, line length, Real-world App, GitHub PRs / GitLab MR" — this is just a tag line summarizing the skills being tested: knowing PEP 8's naming conventions, knowing how to run ruff with every rule category enabled (not just the default subset), checking line length specifically, and tying it back to something you'd actually do in industry — code review on a pull request.
"Manual + automated PEP 8 audit using ruff check --select ALL" — this is the actual task. You're meant to do two passes: first read the code yourself and spot violations (the "manual" part, which builds your eye for style issues), then run ruff check --select ALL <file> to catch everything programmatically, including stuff you'd miss by eye. --select ALL matters because ruff's default rule set is a curated subset (mostly pycodestyle/pyflakes); ALL turns on every rule family ruff supports (pep8-naming, flake8-bugbear, isort-style import sorting, etc.), which is why rules like N801 and I001 show up in the table below — those aren't in ruff's default selection.
"Identifies all violations by rule code and line number across 10 key rules" — your output should look like a real linter report: something like myfile.py:14:1: E302 expected 2 blank lines, found 1. The rule code and line number are the two pieces of information a reviewer actually needs to act on a finding.
"After fixing all violations, re-runs ruff to confirm zero errors" — this is the verification loop: fix, re-run, repeat until ruff check --select ALL myfile.py returns nothing. That's your "done" signal — not "I think I fixed it" but "the tool confirms zero findings."
"This is exactly the code review checklist used at Python-first companies" — this is just motivation/context, telling you this isn't busywork; CI pipelines at these companies fail your PR exactly this way.
The 10 rules, why each one exists

E501 (line length 88/79) — long lines are hard to review in a diff view and on split screens. Black defaults to 88, vanilla PEP 8 says 79; ruff is configurable, so you state which you're following.
E302 (2 blank lines before top-level def/class) — visually separates top-level units so your eye can scan a file's structure quickly.
E301 (1 blank line before a method inside a class) — same idea, one level down, to separate methods from each other.
N816 (variable names should be snake_case, this code specifically flags mixedCase module-level/global names) — Python's convention; mixing camelCase in is usually a tell that someone is used to JS/Java.
N801 (class names PascalCase) — distinguishes classes from functions/variables at a glance, e.g. UserAccount vs user_account.
E401 (one import per line) — import os, sys is harder to diff and grep than two separate lines.
I001 (stdlib imports before third-party, properly grouped/sorted) — predictable import ordering avoids merge conflicts and makes it obvious what's a dependency vs what's builtin.
E225 (spaces around operators) — x=1 vs x = 1; missing spaces hurt readability, especially in dense expressions.
E702 (no semicolons to separate statements) — x = 1; y = 2 crams two statements onto one line, which is harder to step through in a debugger and harder to diff.
E712 (is True not == True) — == True is redundant and can misbehave with truthy-but-not-True values; if x: or if x is True: is the idiomatic way to express the comparison precisely.