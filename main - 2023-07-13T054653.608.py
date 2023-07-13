import datetime

# Initialize the number of spots available at the dock
spots_available = 10

# Initialize a dictionary to track the number of fill-ups per hour
fillups_per_hour = {}

# Function to check the availability of spots and update fill-up statistics
def check_dock_availability():
    global spots_available
    
    # Get the current date and time
    current_datetime = datetime.datetime.now()
    
    # Check if the current hour is already tracked in the dictionary
    current_hour = current_datetime.strftime('%Y-%m-%d %H')
    if current_hour in fillups_per_hour:
        fillups_per_hour[current_hour] += 1
    else:
        fillups_per_hour[current_hour] = 1
    
    # Decrease the number of spots available
    spots_available -= 1
    
    # Print the current number of spots available
    print(f'Spots available: {spots_available}')
    
# Simulate the availability check every hour for a day
for _ in range(24):
    check_dock_availability()
    
# Print the fill-up statistics
print('Fill-up statistics:')
for hour, count in fillups_per_hour.items():
    print(f'Hour: {hour}, Fill-ups: {count}')

