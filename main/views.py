import datetime
import locale
import calendar
from django.shortcuts import render, get_object_or_404
from .models import Day

# Set locale to Dutch for correct month names
locale.setlocale(locale.LC_TIME, "nl_NL.UTF-8")

def get_day(request, date_str=None):
    """
    Function to handle both a specific day's memory and today's memory.
    """
    today = datetime.date.today()

    if date_str:
        # Convert string date to date object
        date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
    else:
        # Default to today's date if no date is provided
        date_obj = today

    # Retrieve the day object or return 404 if not found
    day = get_object_or_404(Day, date=date_obj)

    # Determine if we are viewing today's memory
    is_today = (date_obj == today)

    # Format date as "1 Januari"
    formatted_date = date_obj.strftime("%-d %B").title()

    return render(request, 'memory_page.html', {
        'day': day,
        'is_today': is_today,  
        'formatted_date': formatted_date,
    })

def overview(request):
    today = datetime.date.today()
    current_year = today.year

    # Get selected month from GET parameters, default to the current month
    selected_month = request.GET.get('month', today.month)
    try:
        selected_month = int(selected_month)
    except ValueError:
        selected_month = today.month

    # Ensure month is in valid range
    if selected_month < 1 or selected_month > 12:
        selected_month = today.month

    # Get all days for the selected month in the current year
    days = Day.objects.filter(date__year=current_year, date__month=selected_month).order_by('date')

    # First day of the month
    first_day_of_month = datetime.date(current_year, selected_month, 1)
    
    # Get weekday (0 = Monday, 6 = Sunday)
    first_weekday = first_day_of_month.weekday()

    # Calculate total days using the calendar module
    total_days = calendar.monthrange(current_year, selected_month)[1]
    total_cells = first_weekday + total_days
    num_rows = total_cells // 7 + (1 if total_cells % 7 != 0 else 0)

    # Empty slots before the first day
    empty_days = range(first_weekday)

    # List of months in Dutch
    maanden = [(i, datetime.date(2000, i, 1).strftime('%B').capitalize()) for i in range(1, 13)]

    return render(request, 'overview.html', {
        'days': days,
        'selected_month': selected_month,
        'current_year': current_year,
        'maanden': maanden,
        'empty_days': empty_days,
        'num_rows': num_rows
    })
