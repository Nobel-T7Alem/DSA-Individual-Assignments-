class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def getTitle(self):
        return self.title

    def getDescription(self):
        return self.description

    def isCompleted(self):
        return self.completed

    def markCompleted(self):
        self.completed = True


class Node:
    def __init__(self, task):
        self.task = task
        self.next = None


class ToDoList:
    def __init__(self):
        self.head = None

    def addToDo(self, task):
        new_node = Node(task)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def markToDoAsCompleted(self, title):
        current = self.head
        while current:
            if current.task.getTitle() == title:
                current.task.markCompleted()
                return True
            current = current.next
        return False

    def viewToDoList(self):
        current = self.head
        while current:
            task = current.task
            status = "Completed" if task.isCompleted() else "Incomplete"
            print(f"Title: {task.getTitle()}, Description: {task.getDescription()}, Status: {status}")
            current = current.next


# Testing the implementation
if __name__ == "__main__":
    todo_list = ToDoList()

    # Adding tasks
    todo_list.addToDo(Task("Task 1", "Description for Task 1"))
    todo_list.addToDo(Task("Task 2", "Description for Task 2"))
    todo_list.addToDo(Task("Task 3", "Description for Task 3"))

    # Viewing tasks
    print("To-Do List:")
    todo_list.viewToDoList()

    # Marking a task as completed
    print("\nMarking 'Task 2' as completed.")
    todo_list.markToDoAsCompleted("Task 2")

    # Viewing tasks again to see the change
    print("\nUpdated To-Do List:")
    todo_list.viewToDoList()
