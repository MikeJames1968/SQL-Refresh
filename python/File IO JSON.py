import json
# open file section
def read_employees(filename):
    with open(filename, mode='r') as jsonfile:
        # json.load does the heavy lifting
        jsondata = json.load(jsonfile)
    return jsondata

# Call it
employees = read_employees("employees.json")
print(employees)

# Calculate and print the total no of employees
total = len(employees)
print(f"Number of employees: {total}")

# Print numbered employee list
for i, emp_record in enumerate(employees, start=1):
   print(f'{i}. {emp_record["name"]}')

# Note this only returns the first matching entry, not multiple
def find_employee(employees, name):
    # first time using next() function and a generator...
    target = next((emp for emp in employees if emp["name"] == name), None)
    return target

# Call it
test = find_employee(employees, "John Smith")
print(test)
