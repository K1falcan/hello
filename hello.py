import openpyxl

print("Hello Koyo!")
print("Hello Ryan!")

def greet(name):
    print(f"Hello, {name}")

def main():
    name = input("What is your name? ")
    greet(name)
    
    # Example: Create and save an Excel file
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    next_row = sheet.max_row + 1
    sheet.cell(row=next_row, column=1).value = f"Hello, {name}!"
    workbook.save('greeting.xlsx')
    print(f"Greeting saved to greeting.xlsx")

if __name__ == "__main__":
    main()
