import sys

print(sys.ps1)
print(sys.ps2)
sys.ps1 = 'C>'

print(sys.ps1)
