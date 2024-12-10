from WorkoutLinkedList import WorkoutLinkedList

class HashTableCalendar:
    def __init__(self):
        self.table = {}

    def addToDay(self, month, day, name, exerciseType):
        if month not in self.table:
            self.table[month] = {}
        if day not in self.table[month]:
            self.table[month][day] = WorkoutLinkedList()
        self.table[month][day].addExercise(name, exerciseType)
        print("Added " + name + " to " + month + " " + day + "'s workout")

    def removeFromDay(self, month, day, name):
        if month in self.table and day in self.table[month]:
            removed = self.table[month][day].removeExercise(name)
            if removed:
                print("Removed " + name + " from " + month + " " + day + "'s workout")
                return
            print(name + " not found in " + month + " " + day + "'s workout.")
            return
        print("No workouts found for " + month + " " + day + ".")

    def removeDay(self, month, day):
        if month in self.table and day in self.table[month]:
            del self.table[month][day]
            print("Removed all workouts for " + month + " " + day + ".")
            return
        print("No workouts found for " + month + " " + day + ".")

    def getExerciseType(self, month, day, exerciseName):
        if month in self.table and day in self.table[month]:
            workoutList = self.table[month][day]
            current = workoutList.head
            while current:
                if current.name == exerciseName:
                    return current.exerciseType
                current = current.next
        print("Exercise " + exerciseName + " not found in " + month + " " + day)

    def getDayExercises(self, month, day):
        if month in self.table and day in self.table[month]:
            workoutList = self.table[month][day]
            current = workoutList.head
            exercises = []
            while current:
                exercises.append(current.name)
                current = current.next
            return exercises

    def displayMonthDay(self, month, day):
        if month in self.table and day in self.table[month]:
            print("Workouts for " + month + " " + day + ":")
            self.table[month][day].displayWorkout()
            return
        print("No workouts were scheduled for " + month + " " + day + ".")
    
    def displayCalendar(self):
        if not self.table:
            print("No workouts are currently scheduled.")
            return
        print("Workout Calendar:")
        for month, days in self.table.items():
            for day, workoutList in days.items():
                print(month + " " + day + ", Exercises:")
                current = workoutList.head
                while current:
                    print("    - " + current.name + " (" + current.exerciseType + ")")
                    current = current.next


#calendar = HashTableCalendar()

#calendar.addToDay("December", "25", "Push-ups", "Strength")
#calendar.addToDay("December", "25", "Plank", "Core")
#calendar.addToDay("December", "31", "Running", "Cardio")
#calendar.displayCalendar()

#calendar.removeFromDay("December", "25", "Plank")
#calendar.displayCalendar()

