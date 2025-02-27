import os
import django
import datetime

# Set up Django environment BEFORE importing models
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Site_Hanna.settings")  # Replace with your project name if different
django.setup()

from main.models import Day

# Automatically use the current year
year = datetime.date.today().year

# Define the start date as January 1st of the current year
start_date = datetime.date(year, 1, 1)

# Determine if it's a leap year
is_leap_year = (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))
days_in_year = 366 if is_leap_year else 365

# Loop over all days in the current year
for i in range(0, days_in_year):
    day_date = start_date + datetime.timedelta(days=i)
    image_filename = f"foto_{i+1:03d}.png"
    text = f"This is the memory of {day_date}."

    # Only insert if the date doesn't already exist
    if not Day.objects.filter(date=day_date).exists():
        Day.objects.create(date=day_date, image_filename=image_filename, text=text)
        print(f"✅ Added {day_date} → {image_filename}")
    else:
        print(f"⚠️ Skipped {day_date}, already exists")

print(f"🎉 Finished adding all days for {year}!")
