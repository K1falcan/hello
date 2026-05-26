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
    sheet['A1'] = f"Hello, {name}!"
    workbook.save('greeting.xlsx')
    print(f"Greeting saved to greeting.xlsx")

if __name__ == "__main__":
    main()
