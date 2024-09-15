
original_filename = input()

date_string = original_filename[4:12]
year = date_string[:4]
month = date_string[4:6]
day = date_string[6:]

months = {
    "01": "Jan",
    "02": "Feb",
    "03": "Mar",
    "04": "Apr",
    "05": "May",
    "06": "Jun",
    "07": "Jul",
    "08": "Aug",
    "09": "Sep",
    "10": "Oct",
    "11": "Nov",
    "12": "Dec",
}
month_name = months[month]
event_name = "PYTHON_CONFERENCE"
new_filename = f"{year}_{month_name}_{day}_{event_name}.jpg"
print(new_filename)