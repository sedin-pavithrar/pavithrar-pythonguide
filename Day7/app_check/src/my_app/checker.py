import importlib

packages = ["requests", "pandas", "numpy", "nonexistent"]

installed = 0
missing = 0

print("Dependency Check\n")

for pkg in packages:
    try:
        importlib.import_module(pkg)
        print(f"OK   {pkg}")
        installed += 1
    except ImportError:
        print(f" MISS {pkg}")
        missing += 1

print("\nSummary")
print("-" * 20)
print(f"Installed : {installed}")
print(f"Missing   : {missing}")
print(f"Total     : {len(packages)}")