# ​‌‍‌⁡⁣⁣⁢𝗖𝗔𝗦𝗘 𝟭⁡​

# Introduction to concept.
# Defining the year, month and day of birth
year_of_birth = int(input("Key in your year of birth in numbers e.g 2000: \n"))
month_of_birth = int(input("Key in your month of birth in numbers e.g 01 for January: \n"))
day_of_birth = int(input("Key in your day of birth in numbers e.g 1: \n"))


# Defining the current year,month and date
todays_year = int(input("Key in the current year e.g 2022: \n"))
todays_month = int(input("Key in the current month e.g 01 for january: \n"))
todays_date = int(input("Key in the current date e.g 23: \n"))

# Performing the difference to establish the year,month and day difference
current_years = todays_year - year_of_birth
current_month = todays_month - month_of_birth
current_day = todays_date - day_of_birth

'''if (current_month < month_of_birth) or (current_month == month_of_birth and todays_date < day_of_birth):
    current_years -= 1
'''
# age test
if (current_years < 18):
    print(
        f"You are not eligible to vote since you are {current_years} years old:")
else:
    print(f"You are eligible to vote since you are {current_years} years old")

# Print the actual age in Years, Months and days.
print(f"You are {current_years} years, {current_month} months and {current_day} years old")

'''
​‌‍‌⁡⁣⁢⁡⁣⁣⁢𝗟𝗜𝗠𝗜𝗧𝗔𝗧𝗜𝗢𝗡𝗦 𝗧𝗢 𝗧𝗛𝗜𝗦 𝗔𝗣𝗣𝗥𝗢𝗔𝗖𝗛⁡⁡
​
1.  Age estimation cannot be done accurately using months or days; it requires the year of birth.
2.  We face difficulties in handling negative outputs for the day of birth, 
    especially when the day of birth is greater than the current date.

​‌‍‌⁡⁣⁣⁢𝗦𝗢𝗟𝗨𝗧𝗜𝗢𝗡⁡​

To address these limitations, it is necessary to incorporate a Python module called "datetime"
to simplify our tasks. For further details on how to implement it, please refer to the documentation 
provided at https://docs.python.org/3/library/datetime.html.
Let's proceed with working on this solution.⁡
'''

# ⁡⁣⁣⁡⁣⁣⁢​‌‍‌𝗖𝗔𝗦𝗘 𝟮​⁡⁡


# Importing the module
from datetime import date

# Get the current date
current_date = date.today()

# Get the day, month, and year from the user
birth_day = int(input("Key in your date of birth e.g. 23:\n "))
birth_month = int(input("Key in your month of birth e.g. 01 for January: \n "))
birth_year = int(input("Key in your year of birth e.g 2000: \n "))

# Calculate the user's age
age = current_date.year - birth_year

if (
    current_date.month < birth_month
    or (current_date.month == birth_month and current_date.day < birth_day)
):
    age -= 1

# Check the eligibility based on age
if age >= 18:
    print("You are eligible to vote!")
else:
    print("You are not eligible to vote.")

# ⁡⁣⁣⁢​‌‍‌𝗖𝗔𝗦𝗘 𝟯​⁡

'''
Remember, all of the above cases, we have been playing around the terminal. 
Now, what if we want to display it in a graphical interface.'''

import tkinter as tk #library for grahical representation in python
from datetime import date # Module that helps in date calculations in python

def check_voter_eligibility():
    current_year = date.today().year
    birth_year = int(entry.get())
    age = current_year - birth_year
    if (age >= 18):
        message = "You are eligible to vote!"
    else:
        message = "You are not eligible to vote."
    label.config(text=message)

# Let's create the main window where our content will be assigned to
window = tk.Tk()  #TK or TCL is a framework provided by the tkinter library

# Setting the window title (Optional though)
window.title("Check Your Eligibility Here")

# Creating an entry widget for birth year (textbox where our values go)
entry = tk.Entry(window)
entry.pack()

# Creating a button widget to check our person's eligibility to vote
button = tk.Button(window, text="Check Eligibility", command=check_voter_eligibility)
button.pack()

# Creating a label widget for displaying the result in a new concept now "GUI (Graphical User Interface)"
label = tk.Label(window, text="")
label.pack()

# Run the main event loop
window.mainloop()

# Enjoy
