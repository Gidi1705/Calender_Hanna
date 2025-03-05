import os
import django
import datetime

# Set up Django environment BEFORE importing models
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Site_Hanna.settings")  # Replace with your project name if different
django.setup()

from main.models import Day

# Define the target year
year = 2025

# Define the start date as January 1st of the target year
start_date = datetime.date(year, 1, 1)

# Determine if it's a leap year
days_in_year = 366 if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) else 365

# Clear existing data in the database
Day.objects.all().delete()
print("🗑️ Deleted all existing records from the database.")

# Loop over all days in the target year
for i in range(0, days_in_year):
    day_date = start_date + datetime.timedelta(days=i)
    image_filename = f"foto_{i+1:03d}.jpg"

    # Insert new record
    Day.objects.create(date=day_date, image_filename=image_filename)
    print(f"✅ Added {day_date} → {image_filename}")

print(f"🎉 Finished adding all days for {year}!")