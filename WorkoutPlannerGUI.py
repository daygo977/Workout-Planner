import tkinter as tk
from tkinter import messagebox
from PlannerController import PlannerController

class WorkoutPlannerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Workout Planner")
        self.root.geometry("900x900")
        self.controller = PlannerController()

        self.main_menu()

    def main_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        tk.Label(self.root, text="Workout Planner", font=("Arial", 30)).pack(pady=20)
        
        tk.Button(self.root, text = "View Calendar", command = self.view_calendar, width = 30).pack(pady = 20)
        tk.Button(self.root, text = "Manage Queue", command = self.manage_queue, width = 30).pack(pady = 20)
        tk.Button(self.root, text = "View Exercises", command = self.view_exercises, width = 30).pack(pady = 20)
        tk.Button(self.root, text = "Exit", command = self.root.quit, width = 30).pack(pady = 20)
        tk.Button(self.root, text = "Check API Rate Limit", command = self.check_rate_limit, width = 30).pack(pady = 20)

    def view_calendar(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    
        tk.Label(self.root, text = "Workout Calendar - December 2024", font = ("Arial", 18)).pack(pady = 20)

        calendarFrame = tk.Frame(self.root)
        calendarFrame.pack()

        days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
        for i, day in enumerate(days):
            tk.Label(calendarFrame, text = day, font = ("Arial", 10, "bold"), width = 10, height = 2, borderwidth = 1, relief = "solid").grid(row = 0, column = i)

        from calendar import monthcalendar
        calendar = monthcalendar(2024, 12)
        for r, week in enumerate(calendar, start = 1):
            for c, day in enumerate(week):
                if day != 0:
                    button = tk.Button(calendarFrame, text = str(day), width = 10, height = 2, command = lambda d = day: self.add_exercise_to_day("December", d))
                    button.grid(row = r, column = c)
                else:
                    tk.Label(calendarFrame, text = "", width = 10, height = 2, borderwidth = 1, relief = "solid").grid(row = r, column = c)
        tk.Button(self.root, text = "Back", command = self.main_menu, width = 15).pack(pady = 20)

    def add_exercise_to_day(self, month, day):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.current_month = month
        self.current_day = day

        self.controller.queueExercisesFromDay(month, str(day))

        tk.Label(self.root, text="Add Exercise - " + month + " " + str(day), font=("Arial", 18)).pack(pady=20)
        tk.Label(self.root, text="Select Exercise Type:").pack(pady=5)
        self.selected_body_part = tk.StringVar(self.root)

        body_parts = [child.name for child in self.controller.tree.root.children]
        if not body_parts:
            self.controller.fillTree()
            body_parts = [child.name for child in self.controller.tree.root.children]
        self.selected_body_part.set(body_parts[0])
        tk.OptionMenu(self.root, self.selected_body_part, *body_parts, command=self.update_exercise_list).pack(pady=10)

        tk.Label(self.root, text="Select Exercise:").pack(pady=5)
        self.exercise_listbox = tk.Listbox(self.root, width=50, height=10)
        self.exercise_listbox.pack(pady=10)

        self.update_exercise_list(body_parts[0])

        tk.Button(self.root, text="Add Exercise", command=self.add_selected_exercise, width=20).pack(pady=10)

        # Show linked list for the selected day
        tk.Label(self.root, text="Current Exercises in Queue:").pack(pady=5)

        # Define `queue_text` to fix the error
        self.queue_text = tk.Text(self.root, width=60, height=10)
        self.queue_text.pack(pady=10)

        # Refresh queue display after defining `queue_text`
        self.refresh_queue_display()

        # Back to Calendar
        tk.Button(self.root, text="Back to Calendar", command=self.view_calendar, width=20).pack(pady=20)

    def refresh_day_exercises(self):
        self.day_exercises_text.delete("1.0", tk.END)
        exercises = self.controller.calendar.getDayExercises(self.current_month, str(self.current_day))
        if exercises:
            for exercise in exercises:
                self.day_exercises_text.insert(tk.END, exercise + "\n")
        else:
            self.day_exercises_text.insert(tk.END, "No exercises scheduled for this day.\n")


    def update_exercise_list(self, body_part):
        self.exercise_listbox.delete(0, tk.END)
        exercises = self.controller.tree.displayTree(body_part)
        if exercises:
            for exercise in exercises:
                self.exercise_listbox.insert(tk.END, exercise)

    def add_selected_exercise(self):
        selected_index = self.exercise_listbox.curselection()
        if not selected_index:
            tk.messagebox.showerror("Error", "Please select an exercise.")
            return
        exercise_name = self.exercise_listbox.get(selected_index)
        body_part = self.selected_body_part.get()

        # Add the exercise to the calendar and queue
        self.controller.enqueueExercise(self.current_month, str(self.current_day), exercise_name, body_part)
        tk.messagebox.showinfo("Success", exercise_name + " added to " + self.current_month + " " + str(self.current_day) + " and queued.")

    def refresh_queue_display(self):
        self.queue_text.delete("1.0", tk.END)
        queue = self.controller.exerciseQueue.queue  # Fetch the current queue
        if queue:
            self.queue_text.insert(tk.END, "Exercises in queue:\n")
            for i, exercise in enumerate(queue, start=1):
                self.queue_text.insert(tk.END, str(i) + ". " + exercise + "\n")
        else:
            self.queue_text.insert(tk.END, "No exercises in the queue.")


    def update_exercise_list(self, body_part):
        self.exercise_listbox.delete(0, tk.END)
        exercises = self.controller.tree.displayTree(body_part)
        if exercises:
            for exercise in exercises:
                self.exercise_listbox.insert(tk.END, exercise)

    def add_selected_exercise(self):
        selected_index = self.exercise_listbox.curselection()
        if not selected_index:
            tk.messagebox.showerror("Error", "Please select an exercise.")
            return
        exercise_name = self.exercise_listbox.get(selected_index)
        body_part = self.selected_body_part.get()

        # Add the exercise to the calendar and queue
        self.controller.enqueueExercise(self.current_month, str(self.current_day), exercise_name, body_part)
        tk.messagebox.showinfo("Success", exercise_name + " added to " + self.current_month + " " + str(self.current_day) + " and queued.")
    
        # Refresh the queue display
        self.refresh_queue_display()


    def manage_queue(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    
        tk.Label(self.root, text="Workout Queue", font=("Arial", 18)).pack(pady=20)
    
        queue_text = tk.Text(self.root, width=50, height=10)
        queue_text.pack(pady=10)
        queue_text.insert(tk.END, "1. Push-ups\n2. Pull-ups\n")
    
        tk.Button(self.root, text="Enqueue Exercise", command=lambda: messagebox.showinfo("Enqueue", "Add exercise feature here!"), width=20).pack(pady=5)
        tk.Button(self.root, text="Dequeue Exercise", command=lambda: messagebox.showinfo("Dequeue", "Remove exercise feature here!"), width=20).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.main_menu, width=15).pack(pady=10)


    def view_exercises(self):
        # Clear the current window
        for widget in self.root.winfo_children():
            widget.destroy()
    
        tk.Label(self.root, text="View Exercises by Body Part", font=("Arial", 18)).pack(pady=20)
    
        # Dropdown for selecting a body part
        body_parts = ["Back", "Chest", "Lower Arms", "Lower Legs", "Neck", "Shoulders", "Upper Arms", "Upper Legs", "Waist"]  # Example body parts
        self.selected_body_part = tk.StringVar(self.root)
        self.selected_body_part.set(body_parts[0])  # Default selection

        tk.OptionMenu(self.root, self.selected_body_part, *body_parts).pack(pady=10)

        # Text area to display exercises
        self.exercise_text = tk.Text(self.root, width=60, height=15)
        self.exercise_text.pack(pady=10)

        # Button to fetch exercises
        tk.Button(self.root, text="Show Exercises", command=self.display_exercises, width=20).pack(pady=10)

        # Back button
        tk.Button(self.root, text="Back", command=self.main_menu, width=15).pack(pady=10)


    def display_exercises(self):
        self.exercise_text.delete("1.0", tk.END)

        if not self.controller.treeFilled:  # Ensure tree is only filled once
            self.controller.fillTree()

        body_part = self.selected_body_part.get()
        exercises = self.controller.tree.displayTree(body_part)
        if exercises:
            self.exercise_text.insert(tk.END, "Exercises for " + body_part + ":\n")
            for exercise in exercises:
                self.exercise_text.insert(tk.END, " - " + exercise + "\n")
        else:
            self.exercise_text.insert(tk.END, "No exercises found for " + body_part + ".\n")

    def check_rate_limit(self):
        rate_limit_info = self.controller.api.fetchRateLimit()
        if rate_limit_info:
            messagebox.showinfo("API Rate Limit: " + "\nRemaining Requests: " + str(rate_limit_info['Remaining Requests']) + "\n" + "Rate Limit Resets At: " + str(rate_limit_info['Reset Time']))
        else:
            messagebox.showerror("Error", "Unable to fetch rate limit.")





# Start the Application
if __name__ == "__main__":
    root = tk.Tk()
    app = WorkoutPlannerApp(root)
    root.mainloop()
