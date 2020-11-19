import sys
import sqlite3
from sqlite3 import Error


def create_connection(dbFile):
    conn = None
    try:
        conn = sqlite3.connect(dbFile)
    except Error as e:
        print(e)
    return conn


def new_task(conn, task):
    sql = ''' INSERT INTO tasks(desc, complete)
                  VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid


def update_task(conn, task):
    sql = ''' UPDATE tasks
              SET desc = ?
              WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()


def view_tasks(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")

    rows = cur.fetchall()

    for row in rows:
        print(row)


def delete_task(conn, taskID):
    # Should probably reset taskIDs?  Not sure if that's a smart move
    sql = 'DELETE FROM tasks WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, taskID)
    conn.commit()


def mark_task_as_done(conn, idAndText):
    sql = ''' UPDATE tasks
                  SET complete = ?
                  WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, idAndText)
    conn.commit()


def main():
    database = r"C:\sqlite\db\todo.db"
    conn = create_connection(database)

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
        new_task(conn, task)       # ???

    elif action == '--view':
        # Print rows
        view_tasks(conn)

    elif action == '--edit':
        # Take ID to edit and new description
        taskID = sys.argv[2]
        desc = sys.argv[3]
        update_task(conn, (desc, taskID,))

    elif action == '--delete':
        taskID = sys.argv[2]
        delete_task(conn, (taskID,))

    elif action == '--mark':
        # Create markText variable because I don't know how else to create the tuple
        taskID = sys.argv[2]
        markText = "Done"
        mark_task_as_done(conn, (markText, taskID))


if __name__ == '__main__':
    main()

