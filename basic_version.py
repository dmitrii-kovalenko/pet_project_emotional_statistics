import datetime
import csv
import os
from typing import List


# Function to get a valid integer input within the range of 1 to 10
def int_input(feeling: str) -> int:
    while True:
        try:
            print(f"Enter your rating for {feeling}:")
            rating = int(input())
            if 1 <= rating <= 10:
                return rating  # If the number is in range, return it
            else:
                print("Oops, the number is out of the range 1 to 10, please try again.")
        except ValueError:
            print("Oops, that's not a number, please try again.")


# Function to collect user input for different metrics
def get_assessment() -> List[int | str]:
    print("Hello! Let's rate your current state on a scale of 1 to 10, where 10 is excellent and 1 is awful.")

    # Get input for various metrics
    mood = int_input("mood")
    mental = int_input("mental state")
    anxiety = int_input("anxiety (anxiety 10 is not anxious at all)")

    # Collect optional comment
    print("If you have a short comment, type it in one line, otherwise just press 'Enter':")
    notion = input("")

    # Return the collected data as a list
    return [mood, mental, anxiety, notion]


# Function to add data to the CSV file
def add_to_file(assessments: List[int | str], now: str, path: str) -> None:
    try:
        # Open the file in append mode
        with open(path, 'a', newline='') as file:
            writer = csv.writer(file)

            # Write the current date/time and the user data to the CSV file
            writer.writerow(now + assessments)

            print("Data successfully saved!")
    except IOError as e:
        print(f"An error occurred while working with the file: {e}")


# Define the relative path to the CSV file
csv_path = 'data/data_storage.csv'

# Get current date and time in the desired format
now = [datetime.datetime.now().strftime("%d.%m.%Y %H:%M")]

# Collect user ratings
assessments = get_assessment()

# Add the collected data to the CSV file
add_to_file(assessments, now, csv_path)