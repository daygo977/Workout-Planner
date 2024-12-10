from ExerciseDBAPI import ExerciseDBAPI
from ExerciseTree import ExerciseTree
from ExerciseGraph import ExerciseGraph
from HashTableCalendar import HashTableCalendar
from ExerciseQueue import ExerciseQueue


class PlannerController:
    def __init__(self):
        self.api = ExerciseDBAPI()
        self.tree = ExerciseTree()
        self.graph = ExerciseGraph()
        self.calendar = HashTableCalendar()
        self.exerciseQueue = ExerciseQueue()
        self.treeFilled = False
        self.graphFilled = False

    def fillTree(self):
        if not self.treeFilled:
            bodyParts = self.api.fetchBodyPartList()
            for bodyPart in bodyParts:
                self.tree.addType(bodyPart)
                exercises = self.api.fetchBodyPart(bodyPart)
                for exercise in exercises:
                    self.tree.addExercise(bodyPart, exercise["name"])
            self.treeFilled = True

    def fillGraph(self):
        if not self.graphFilled:
            bodyParts = self.api.fetchBodyPartList()
            for bodyPart in bodyParts:
                exercises = self.api.fetchBodyPart(bodyPart)
                self.graph.determineConnection(exercises)
            self.graphFilled = True

    def fillCalendar(self, month, day, bodyPart):
        exercises = self.api.fetchBodyPart(bodyPart)
        for exercise in exercises[:3]:
            self.calendar.addToDay(month, day, exercise["name"], bodyPart)

    def queueExercisesFromDay(self, month, day):
        if month in self.calendar.table and day in self.calendar.table[month]:
            self.exerciseQueue = ExerciseQueue()
            workoutList = self.calendar.table[month][day]
            current = workoutList.head
            while current:
                self.exerciseQueue.enqueue(current.name)
                current = current.next
            print("Queued exercises from " + month + " " + day)
            return
        print("No exercises were found for " + month + " " + day)

    def enqueueExercise(self, month, day, exerciseName, exerciseType):
        self.exerciseQueue.enqueue(exerciseName)
        if month in self.calendar.table and day in self.calendar.table[month]:
            self.calendar.addToDay(month, day, exerciseName, exerciseType)
            print("Enqueued and added " + exerciseName + " to linked list for " + month + " " + day)
            return
        print(month + " " + day + " not found in calendar")

    def dequeueExercise(self, month, day):
        exerciseName = self.exerciseQueue.dequeue()
        if exerciseName:
            if month in self.calendar.table and day in self.calendar.table[month]:
                self.calendar.removeFromDay(month, day, exerciseName)
                print("Dequeued and removed " + exerciseName + " from the linked list for " + month + " " + day)
                return
            print("Failed to find " + day + " and " + month + " in the calendar for exercise " + exerciseName)
            return
        print("Queue is empty. Cannot dequeue.")


example = PlannerController()
example.fillTree()
example.tree.displayTreeTerminal()
#example.fillGraph()
#example.graph.displayGraph()
#print("Connections for Deadlift:", example.graph.getConnection("Deadlift"))

#example.fillCalendar("December", "25", "back")
#example.calendar.displayCalendar()
#example.calendar.removeFromDay("December", "25", "assisted pull-up")
#example.calendar.displayCalendar()

#example.queueExercisesFromDay("December", "25")
#example.exerciseQueue.display()
#example.dequeueExercise("December", "25")
#example.exerciseQueue.display()




