class ExerciseTreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []
    
    def addChild(self, childNode):
        self.children.append(childNode)

    def displayNode(self, level = 0):
        print(" " * level + "- " + self.name)
        for child in self.children:
            child.displayNode(level + 3)

class ExerciseTree:
    def __init__(self):
        self.root = ExerciseTreeNode("Exercises")

    def addType(self, type):
        self.root.addChild(ExerciseTreeNode(type))

    def addExercise(self, type, exercise):
        typeNode = self.searchNode(self.root, type)
        if typeNode:
            typeNode.addChild(ExerciseTreeNode(exercise))
            return
        print("Type " + type + " not found")

    def searchNode(self, node, name):
        if node.name == name:
            return node
        for child in node.children:
            result = self.searchNode(child, name)
            if result:
                return result
        return
    
    #Current display tree method for GUI
    def displayTree(self, bodyPart = None):
        results = []
        for child in self.root.children:
            if child.name.lower() == bodyPart.lower():
                results = [grandchild.name for grandchild in child.children]
                break
        return results
    
    #Old display tree method for terminal
    def displayTreeTerminal(self):
        self.root.displayNode()

#treeExample = ExerciseTree()

#treeExample.addType("Upper Body")
#treeExample.addType("Lower Body")
#treeExample.addType("Core")

#treeExample.addExercise("Upper Body", "Bench Press")
#treeExample.addExercise("Upper Body", "Pull-ups")
#treeExample.addExercise("Lower Body", "Squats")
#treeExample.addExercise("Lower Body", "Deadlifts")
#treeExample.addExercise("Core", "Plank")
#treeExample.addExercise("Core", "Hanging Leg Raises")

#treeExample.displayTree()
