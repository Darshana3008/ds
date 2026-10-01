"""
Life Skills Personal Wellness & Habit Tracker
Author: Darshana Sharma
Description: A simple command-line tool to log and review daily wellness habits.
"""

import datetime

def display_menu():
    print("\n--- Life Skills Daily Tracker ---")
    print("1. Log Today's Habits")
    print("2. View Wellness Tips")
    print("3. Exit")

def log_habits():
    today = datetime.date.today().strftime("%B %d, %Y")
    print(f"\n--- Logging for {today} ---")
    
    try:
        water = float(input("Enter water intake (in liters, e.g., 2.5): "))
        study = float(input("Enter focused study time (in hours): "))
        mindfulness = int(input("Enter mindfulness/meditation time (in minutes): "))
        
        # Simple evaluation logic
        print("\n[Summary]")
        print(f"Hydration: {'Great job!' if water >= 2.0 else 'Try to drink more water.'}")
        print(f"Productivity: {'Excellent focus!' if study >= 4.0 else 'Keep building consistent study habits.'}")
        print(f"Mental Well-being: {mindfulness} minutes of mindfulness logged. Namaste!")
        
        # Save to a local log file
        with open("habit_log.txt", "a") as file:
            file.write(f"{today} | Water: {water}L | Study: {study}h | Mindfulness: {mindfulness}m\n")
        print("Progress successfully saved to habit_log.txt!")
        
    except ValueError:
        print("Invalid input! Please enter numerical values where required.")

def show_tips():
    print("\n--- Life Skills & Bio-Wellness Tips ---")
    print("* Hydration supports cellular function and cognitive focus.")
    print("* The Pomodoro Technique (50 mins study, 10 mins break) prevents burnout.")
    print("* Brief breathing exercises help regulate stress levels during exams.")

if __name__ == "__main__":
    while True:
        display_menu()
        choice = input("Select an option (1-3): ")
        if choice == '1':
            log_habits()
        elif choice == '2':
            show_tips()
        elif choice == '3':
            print("Exiting tracker. Keep building great habits!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")