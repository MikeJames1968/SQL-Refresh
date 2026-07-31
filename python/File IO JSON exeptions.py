import json
from pathlib import Path

def read_employees(filename):
    # General error trap
    try:
        # Check path+file exists - note best practice would be to use FileNotFoundError
        file_path = Path(filename)
        if not file_path.is_file():
            print (f"{filename} does not exist")
            return None
        # Open file
        with open(filename, mode='r') as jsonfile:
            jsondata = json.load(jsonfile)
            # Trap malformed JSON data
    except json.JSONDecodeError as e:
        print(f"{filename} contains invalid JSON data")
        return None
    except Exception as e:
        print(f"General error: {e}")
        return None
    return jsondata

# Call it - no errors
employees = read_employees("employees.json")
print(employees)

# Call it - nonexistent file
employees = read_employees("nonexistent.file")
print(employees)

# Call it - bad JSON data
employees = read_employees("employees.badjson")
print(employees)