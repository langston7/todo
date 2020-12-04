import sys
import tododatabaselayer
import todotask


def main():
    databasePath = r"C:\sqlite\db\todo.db"
    database = tododatabaselayer.databaseLayer(databasePath)
    conn = database.create_connection(databasePath)

    script = sys.argv[0]
    if len(sys.argv) == 1:  # no arguments, so print help message
        print("""Commands are: --new "description", --view, --edit "taskID"
         "description", --delete "taskID", --mark taskID""")
        return
    action = sys.argv[1]

    if action == '--new':
        # description of task from user
        desc = sys.argv[2]
        # DTO object creation and passing to database layer
        task = todotask.newTask(desc)
        database.new_task(conn, task)
        printTasks(conn, database)

    elif action == '--view':
        printTasks(conn, database)

    elif action == '--edit':
        # Take ID to edit and new description
        taskID = sys.argv[2]
        desc = sys.argv[3]
        # DTO needs a value? so pass 0
        task = todotask.task(taskID, desc, 0)
        database.update_task(conn, task)
        printTasks(conn, database)

    elif action == '--delete':
        taskID = sys.argv[2]
        database.delete_task(conn, taskID)
        printTasks(conn, database)

    elif action == '--mark':
        taskID = sys.argv[2]
        database.mark_task_as_done(conn, taskID)
        printTasks(conn, database)


def printTasks(conn, database):
    listOfTasks = database.get_tasks(conn)
    for task in listOfTasks:
        if task.isDone == 0:
            doneTextToPrint = "Not done"
        else:
            doneTextToPrint = "Done"
        print(f"{task.id}, {task.description}, {doneTextToPrint}")


if __name__ == '__main__':
    main()

