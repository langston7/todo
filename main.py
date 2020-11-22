import sys
import tododatabaselayer


def main():
    databasePath = r"C:\sqlite\db\todo.db"
    database = tododatabaselayer.databaseLayer(databasePath)

    script = sys.argv[0]
    if len(sys.argv) == 1:  # no arguments, so print help message
        print("""Commands are: --new "description", --view, --edit "taskID"
         "description", --delete "taskID", --mark taskID""")
        return
    action = sys.argv[1]

    if action == '--new':
        # By default, set complete column to incomplete
        desc = sys.argv[2]
        task = (desc, 'Incomplete')
        database.new_task(database.conn, task)       # ???

    elif action == '--view':
        # Print rows
        database.view_tasks(database.conn)

    elif action == '--edit':
        # Take ID to edit and new description
        taskID = sys.argv[2]
        desc = sys.argv[3]
        database.update_task(database.conn, (desc, taskID,))

    elif action == '--delete':
        taskID = sys.argv[2]
        database.delete_task(database.conn, (taskID,))

    elif action == '--mark':
        # Create markText variable because I don't know how else to create the tuple
        taskID = sys.argv[2]
        markText = "Done"
        database.mark_task_as_done(database.conn, (markText, taskID))


if __name__ == '__main__':
    main()

