# Habit Tracker App with Expanded Inclusivity Features and Heuristic Explanations
# Created by Keona Abad 

class HabitTrackerApp:
    def __init__(self):
        self.users = {}  # Store user profiles and their habits
        print("Welcome to the Habit Tracker App!")
        # IH#1: Explaining the benefits of the app right from the start
        print("This app helps you track your habits, set reminders, and view progress insights to keep you motivated.")

    def create_user(self, username):
        # IH#1: Explaining benefits - Reinforces the value of creating a user profile
        print(f"\nCreating profile for '{username}' - track your habits and see your progress!")
        self.users[username] = {"habits": {}}
    
    def add_habit(self, username, habit_name, goal):
        # IH#6: Providing an explicit path - Each step is presented clearly to guide the user
        print(f"\nSetting up habit: '{habit_name}' with a goal of {goal} days!")
        self.users[username]["habits"][habit_name] = {
            "goal": goal,
            "progress": 0,
            "reminders": None  # No reminder set initially
        }
        # IH#1: Explaining benefits - Reminds the user of the value of tracking this specific habit
        print("Tracking this habit will help you stay accountable and visualize your progress!")

    def view_habits(self, username):
        # IH#4: Keeping familiar features - Lists habits in a way users expect, enhancing usability
        print(f"\nHabits for {username}:")
        for habit, details in self.users[username]["habits"].items():
            print(f"- {habit}: {details['progress']}/{details['goal']} days completed")

    def update_progress(self, username, habit_name):
        # IH#5: Making undo available - Incrementing progress with a way to undo if needed
        if habit_name in self.users[username]["habits"]:
            self.users[username]["habits"][habit_name]["progress"] += 1
            print(f"\nUpdated progress for '{habit_name}'! Current progress: {self.users[username]['habits'][habit_name]['progress']}")
            print("Keep it up! You're doing great.")
        else:
            print("Habit not found.")

    def undo_progress(self, username, habit_name):
        # IH#5: Undo/Redo functionality - Provides a way for users to correct mistakes by reverting progress
        if habit_name in self.users[username]["habits"] and self.users[username]["habits"][habit_name]["progress"] > 0:
            self.users[username]["habits"][habit_name]["progress"] -= 1
            print(f"\nReverted progress for '{habit_name}'. Current progress: {self.users[username]['habits'][habit_name]['progress']}")
        else:
            print("No progress to undo.")

    def set_reminder(self, username, habit_name, frequency="daily"):
        # IH#7: Supporting experimentation - Allows users to experiment with different reminder frequencies
        if habit_name in self.users[username]["habits"]:
            print(f"\nReminder set for '{habit_name}' every {frequency}. This will help keep you on track!")
            self.users[username]["habits"][habit_name]["reminders"] = frequency
        else:
            print("Habit not found.")

    def edit_goal(self, username, habit_name, new_goal):
        # IH#3: Allowing users control over depth of engagement - Users can modify goals as they progress
        if habit_name in self.users[username]["habits"]:
            self.users[username]["habits"][habit_name]["goal"] = new_goal
            print(f"\nUpdated goal for '{habit_name}' to {new_goal} days!")
        else:
            print("Habit not found.")

    def view_analytics(self, username):
        # IH#8: Encouraging mindful tinkering - Analytics provide a non-intrusive way to reflect on progress
        print(f"\nAnalytics for {username}'s habits:")
        for habit, details in self.users[username]["habits"].items():
            completion_rate = (details["progress"] / details["goal"]) * 100 if details["goal"] > 0 else 0
            bar = "#" * int(completion_rate // 10)  # Creates a simple progress bar
            print(f"{habit}: [{bar:<10}] {completion_rate:.2f}% complete")

    def personalized_insights(self, username):
        # IH#1 and IH#2: Explaining benefits and costs - Provides motivational feedback and nudges
        print(f"\n{username}'s Progress Insights:")
        for habit, details in self.users[username]["habits"].items():
            if details["progress"] == 0:
                print(f"Consider starting '{habit}' today to build momentum!")
            elif details["progress"] > 0:
                print(f"Keep up the good work on '{habit}'! You're on a {details['progress']} day streak.")

    def display_help(self):
        # IH#6: Guiding through tasks - Provides an explicit help menu with command explanations
        print("\nCommands:")
        print("  create user - Create a new user profile")
        print("  add habit - Add a new habit with a goal")
        print("  view habits - View all habits and progress")
        print("  update progress - Increment progress on a habit")
        print("  undo progress - Decrement progress on a habit")
        print("  set reminder - Set a reminder frequency for a habit")
        print("  view analytics - View visual progress and completion percentages")
        print("  edit goal - Change the goal for a habit")
        print("  insights - See personalized habit insights")
        print("  help - Display this help menu")
        print("  quit - Exit the program")

    def run(self):
        # Main interaction loop with clear guidance and options for users
        while True:
            print("\nOptions: Create User | Add Habit | View Habits | Update Progress | Undo Progress | Set Reminder | View Analytics | Edit Goal | Insights | Help | Quit")
            choice = input("Select an option: ").strip().lower()
            
            if choice == "create user":
                username = input("Enter username: ")
                self.create_user(username)
            elif choice == "add habit":
                username = input("Enter username: ")
                habit_name = input("Enter habit name: ")
                goal = int(input("Enter goal days: "))
                self.add_habit(username, habit_name, goal)
            elif choice == "view habits":
                username = input("Enter username: ")
                self.view_habits(username)
            elif choice == "update progress":
                username = input("Enter username: ")
                habit_name = input("Enter habit name to update: ")
                self.update_progress(username, habit_name)
            elif choice == "undo progress":
                username = input("Enter username: ")
                habit_name = input("Enter habit name to undo progress: ")
                self.undo_progress(username, habit_name)
            elif choice == "set reminder":
                username = input("Enter username: ")
                habit_name = input("Enter habit name for reminder: ")
                frequency = input("Enter reminder frequency (daily/weekly): ")
                self.set_reminder(username, habit_name, frequency)
            elif choice == "view analytics":
                username = input("Enter username: ")
                self.view_analytics(username)
            elif choice == "edit goal":
                username = input("Enter username: ")
                habit_name = input("Enter habit name to edit: ")
                new_goal = int(input("Enter new goal days: "))
                self.edit_goal(username, habit_name, new_goal)
            elif choice == "insights":
                username = input("Enter username: ")
                self.personalized_insights(username)
            elif choice == "help":
                self.display_help()
            elif choice == "quit":
                print("\nThank you for using the Habit Tracker App! Stay motivated and keep tracking your progress.")
                break
            else:
                print("Invalid option. Please try again.")

# Instantiate and run the Habit Tracker App
app = HabitTrackerApp()
app.run()
