import csv

def read_employees(filename):
    with open(filename, mode='r') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        output_list = list(csv_reader)
    return output_list

# Call it

print(read_employees("realpythontest1.txt"))

