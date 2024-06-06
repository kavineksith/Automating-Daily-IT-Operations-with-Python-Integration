from datetime import datetime, timedelta
import sys

class DateTimeInput:
    @staticmethod
    def get_custom_date_time(prompt):
        while True:
            try:
                # Get date input from user
                date_str = input(prompt + " date (YYYY-MM-DD): ")
                # Parse date string into a datetime object
                date = datetime.strptime(date_str, "%Y-%m-%d")
                
                # Get time input from user
                time_str = input(prompt + " time (HH:MM:SS): ")
                # Parse time string into a datetime object
                time = datetime.strptime(time_str, "%H:%M:%S")
                
                # Combine date and time into a single datetime object
                custom_datetime = datetime.combine(date.date(), time.time())
                return custom_datetime
            except ValueError:
                print("Invalid input. Please enter date in format YYYY-MM-DD and time in format HH:MM:SS.")
            except KeyboardInterrupt:
                print("Process interrupted by the user.")
                sys.exit(1)
            except Exception as e:
                print(f"An error occurred: {e}")

class TimeDifferenceCalculator(DateTimeInput):
    def __init__(self):
        super().__init__()

    def calculate_time_difference(self):
        start_datetime = self.get_custom_date_time("Start")
        end_datetime = self.get_custom_date_time("End")

        # Calculate difference of datetime
        time_difference = end_datetime - start_datetime

        # Separate into days and remaining time
        days = time_difference.days
        remaining_time = time_difference - timedelta(days=days)
        
        return days, remaining_time

class DisplayTimeDifference:
    @staticmethod
    def display(days, remaining_time):
        print("Time difference: {} days and {}".format(days, remaining_time))

def main():
    calculator = TimeDifferenceCalculator()
    days, remaining_time = calculator.calculate_time_difference()
    DisplayTimeDifference.display(days, remaining_time)

if __name__ == "__main__":
    main()
