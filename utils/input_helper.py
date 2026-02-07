from datetime import datetime

def get_valid_string(prompt, error_msg="Input cannot be empty. Please try again."):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print(error_msg)

def get_valid_integer(prompt, error_msg="Please enter a valid integer."):
    while True:
        value = input(prompt).strip()
        if value.isdigit():
            return int(value)
        print(error_msg)

def get_valid_date(prompt, date_format="%Y-%m-%d", error_msg=None):
    if error_msg is None:
        error_msg = f"Invalid date. Please use format {date_format}."
    while True:
        value = input(prompt).strip()
        try:
            datetime.strptime(value, date_format)
            return value
        except ValueError:
            print(error_msg)

def get_valid_choice(prompt, choices, error_msg=None):
    if error_msg is None:
        error_msg = f"Invalid choice. Please choose from: {', '.join(choices)}"
    while True:
        value = input(prompt).strip()
        if value in choices:
            return value
        print(error_msg)

def get_valid_politician_id(prompt):
    while True:
        value = input(prompt).strip()
        if value.isdigit() and len(value) == 8 and not value.startswith('0'):
            return value
        print("Invalid ID. It must be an 8-digit number and cannot start with 0.")
