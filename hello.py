from os import name

import openpyxl
from openpyxl import workbook

print("Hello Koyo!")
print("Hello Ryan!")

def greet(name):
    print(f"Hello, {name}")

def main():
    name = input("What is your name? ")
    greet(name)
    
    # Example: Create and save an Excel file
    try:
        workbook = openpyxl.load_workbook('greeting.xlsx')
    except FileNotFoundError:
        workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.append([f"Hello, {name}!"])
    workbook.save('greeting.xlsx')
    print(f"Greeting saved to greeting.xlsx")
if __name__ == "__main__":
    main()