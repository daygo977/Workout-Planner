class ExerciseNode:
    def __init__(self, name, exerciseType):
        self.name = name
        self.exerciseType = exerciseType
        self.next = None

    def __str__(self):
        return "{} ({})".format(self.name, self.exerciseType)

class WorkoutLinkedList:
    def __init__(self):
        self.head = None
    
    def addExercise(self, name, exerciseType):
        newNode = ExerciseNode(name, exerciseType)
        if self.head is None:
            self.head = newNode
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = newNode

    def removeExercise(self, name):
        current, prev = self.head, None
        while current is not None:
            if current.name == name:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                return True
            prev, current = current, current.next
        return False
    
    def displayWorkout(self):
        current = self.head
        if current is None:
            print('No exercises in workout')
            return
        print('Workout Exercises:')
        while current:
            print(current)
            current = current.next

#example = WorkoutLinkedList()

#example.addExercise('exercise1', 'type')
#example.displayWorkout()
#example.removeExercise('exercise1')
#example.displayWorkout()