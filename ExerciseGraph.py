class ExerciseGraph:
    def __init__(self):
        self.graph = {}

    def addExercise(self, exercise):
        if exercise not in self.graph:
            self.graph[exercise] = []

    #Bidirected
    def addConnection(self, exercise1, exercise2):
        if exercise1 not in self.graph:
            self.graph[exercise1] = []
        if exercise2 not in self.graph:
            self.graph[exercise2] = []
        if exercise1 not in self.graph[exercise2]:
            self.graph[exercise2].append(exercise1)
        if exercise2 not in self.graph[exercise1]:
            self.graph[exercise1].append(exercise2)

    def determineConnection(self, exercises):
        for exercise1 in exercises:
            for exercise2 in exercises:
                if exercise1 != exercise2:
                    if exercise1["bodyPart"] == exercise2["bodyPart"] and exercise1["equipment"] == exercise2["equipment"]:
                        self.addConnection(exercise1["name"], exercise2["name"])

    def getConnection(self, exercise):
        if exercise in self.graph:
            return self.graph[exercise]
        return []
    
    def displayGraph(self):
        for exercise, connections in self.graph.items():
            print(exercise + " -> " + ", ".join(connections))
            print(' ')