# 1. Name:
#      Mark Van Horn
# 2. Assignment Name:
#      Lab 03 : Calendar Program
# 3. Assignment Description:
#      This program is meant to accept user input for a month and a year and display
#      an accurate calendar of that month.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part for me was calculating the dow of the week. Also, for some reason
#      the month kept getting passed as -1, despite accepting user input, but by using
#      breakpoint debugging I figured out what was going wrong and I was able to get
#      everything working smoothly.
# 5. How long did it take for you to complete the assignment?
#      About 2 hours total.


def leap_year(year):
    return True if year % 400 == 0 or year % 100 != 0 and year % 4 == 0 else False

def get_days(month, year):
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    if month == 2:
        if leap_year(year):
            return 29
        return 28
    return 30

def day_of_week(month, year):
    sum = 0
    for i in range(1752, year):
        if leap_year(i):
            sum += 366
        else:
            sum += 365
    for j in range(1, month):
        sum += get_days(j, year)
    
    sum -= 1
    return sum % 7

def display_table(dow, num_days):
    '''Display a calendar table'''
    assert(type(num_days) == type(dow) == type(0))
    assert(0 <= dow <= 6)
    assert(28 <= num_days <= 31)

    # Display a nice table header
    print("  Su  Mo  Tu  We  Th  Fr  Sa")

    # Indent for the first day of the week
    for indent in range(dow):
        print("    ", end='')

    # Display the days of the month
    for dom in range(1, num_days + 1):
        print(repr(dom).rjust(4), end='')
        dow += 1
        # Newline after Saturdays
        if dow % 7 == 0:
            print("")  # newline

    # We must end with a newline
    if dow % 7 != 0:
        print("")  # newline

# Output
month = -1
while 1 > month or month > 12:
    try:
        month = int(input("Enter the month number: "))
        if 1 > month or month > 12:
            print("Please enter a valid month number.")
    except:
        print("Please enter an integer value.")

year = -1
while 1753 > year:
    try:
        year = int(input("Enter the year number: "))
        if 1753 > year:
            print("Please enter a year after 1753.")
    except:
        print("Please enter an integer value.")

days = get_days(month, year)
dow = day_of_week(month, year)

display_table(dow, days)
