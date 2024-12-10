class ExerciseQueue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, name):
        self.queue.append(name)

    def dequeue(self):
        if self.is_empty():
            print('Queue is empty. Cannot dequeue')
            return
        return self.queue.pop(0)
    
    def peek(self):
        if self.is_empty():
            print('Queue is empty')
            return
        return self.queue[0]
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def display(self):
        if self.is_empty():
            print('Queue is empty')
        else:
            print('Exercise in queue (from start to end):')
            for exercise in self.queue:
                print(exercise)

#queue = ExerciseQueue()

#queue.enqueue("Push-ups")
#queue.enqueue("Plank")
##queue.enqueue("Squats")

#queue.display()

#print("Front exercise:", queue.peek())

#print("Dequeued exercise:", queue.dequeue())

#queue.display()

#rint("Queue empty?", queue.is_empty())#