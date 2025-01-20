
# from datetime import datetime, timedelta

# # List of clock-in times
# clock_in_times = ["9:15 AM", "10:15 AM", "11:00 AM", "12:00 PM", "8:00 PM"]

# # Convert times to minutes using the logic past midnight
# minutes = []
# for time in clock_in_times:
#     dt = datetime.strptime(time, "%I:%M %p")
#     total_minutes = dt.hour * 60 + dt.minute
#     minutes.append(total_minutes)

# # Calculate the average time in minutes
# average_minutes = sum(minutes) // len(minutes)

# # Convert the average minutes back to a time
# average_time = (datetime(1, 1, 1) + timedelta(minutes=average_minutes)).time()

# # Display the average clock-in time
# print("Average clock-in time:", average_time.strftime("%I:%M %p"))

from datetime import datetime, timedelta

def calculate_average_clock_in_time(clock_in_times):
    """
    Calculate the average clock-in time from a list of times.
    :param clock_in_times: List of clock-in times in "%I:%M %p" format (e.g., ["9:15 AM", "10:15 AM"])
    :return: Average clock-in time as a string in "%I:%M %p" format.
    """
    if not clock_in_times:
        return "No clock-in times provided."
    
    try:
        # Convert times to minutes past midnight
        minutes = []
        for time in clock_in_times:
            dt = datetime.strptime(time, "%I:%M %p")  # Parse time string
            total_minutes = dt.hour * 60 + dt.minute  # Convert to total minutes
            minutes.append(total_minutes)
        
        # Calculate the average time in minutes
        average_minutes = sum(minutes) // len(minutes)

        # Convert the average minutes back to a time
        average_time = (datetime(1, 1, 1) + timedelta(minutes=average_minutes)).time()

        # Return formatted average clock-in time
        return average_time.strftime("%I:%M %p")
    except ValueError:
        return "Invalid time format detected. Please ensure times are in '%I:%M %p' format."

# Input clock-in times dynamically
print("Enter clock-in times (e.g., 9:15 AM), one per line. Enter 'done' when finished:")

clock_in_times = []
while True:
    time_input = input("Enter time (or 'done' to finish): ").strip()
    if time_input.lower() == 'done':
        break
    clock_in_times.append(time_input)

# Calculate and display the average clock-in time
average_time = calculate_average_clock_in_time(clock_in_times)
print("Average clock-in time:", average_time)
