public class Main {
    public static void main(String[] args) {
        ToDoList toDoList = new ToDoList();

        Task task1 = new Task("Buy groceries", "Buy milk, eggs, and bread");
        Task task2 = new Task("Clean house", "Vacuum and dust all rooms");
        Task task3 = new Task("Finish project", "Complete the Java project by the end of the week");

        toDoList.addToDo(task1);
        toDoList.addToDo(task2);
        toDoList.addToDo(task3);

        System.out.println("To-Do List:");
        toDoList.viewToDoList();

        System.out.println("Marking 'Clean house' as completed.");
        toDoList.markToDoAsCompleted("Clean house");

        System.out.println("To-Do List after marking a task as completed:");
        toDoList.viewToDoList();
    }
}
