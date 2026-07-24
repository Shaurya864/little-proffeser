# Write a program to fetch system information using os and sys modules.
import os
import sys

print("Operating System:", os.name)               
print("Current Working Directory:", os.getcwd())
print("Python Version:", sys.version)
print("Platform:", sys.platform)
print("Executable Path:", sys.executable)