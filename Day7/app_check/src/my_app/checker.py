import importlib

#activate env .\myenv\Scripts\Activate.ps1
#D:\python\Day7\app_check> .\myenv\Scripts\Activate.ps1      

packages = ["requests", "pandas", "numpy", "nonexistent"]

installed = 0
missing = 0

print("Dependency Check\n")

for pkg in packages:
    try:
        importlib.import_module(pkg) # importlib.import_module() takes a string and imports the module with that name.
        print(f"OK   {pkg}")
        installed += 1
    except ImportError:
        print(f"MISSING {pkg}")
        missing += 1

print("\nSummary")
print("-" * 20)
print(f"Installed : {installed}")
print(f"Missing   : {missing}")
print(f"Total     : {len(packages)}")


# Know the module name while writing code? → Use import
# Know the module name only while the program is running? → Use importlib.import_module()
# pkg = "requests"
# import pkg
# Python does not look at the value stored in pkg.
# Instead, it treats pkg as the actual module name, exactly as if you had written: