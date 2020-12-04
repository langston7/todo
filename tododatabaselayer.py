import sqlite3
import todotask
from sqlite3 import Error


class databaseLayer:
    def __init__(self, databasePath):
        self.conn = self.create_connection(databasePath)

    def create_connection(self, databasePath):
        conn = None
        try:
            conn = sqlite3.connect(databasePath)
        except Error as e:
            print(e)
        return conn

    def new_task(self, conn, task):
        # cursor object https://docs.python.org/2/library/sqlite3.html#sqlite3.Cursor
        sql = ''' INSERT INTO tasks(desc, complete)
                             VALUES(?,?) '''
        cur = conn.cursor()
        cur.execute(sql, (task.description, task.isDone))
        conn.commit()

    def update_task(self, conn, task):
        sql = ''' UPDATE tasks
                  SET desc = ?
                  WHERE id = ?'''
        cur = conn.cursor()
        cur.execute(sql, (task.description, task.id))
        conn.commit()

    def delete_task(self, conn, taskID):
        sql = 'DELETE FROM tasks WHERE id=?'
        cur = conn.cursor()
        cur.execute(sql, taskID)
        conn.commit()

        self.updateIDs(conn, taskID)

    def mark_task_as_done(self, conn, id):
        sql = ''' UPDATE tasks
                          SET complete = ?
                          WHERE id = ?'''
        cur = conn.cursor()
        cur.execute(sql, (1, id))
        conn.commit()

    def updateIDs(self, conn, taskID):
        cur = conn.cursor()
        cur.execute("SELECT * FROM tasks")
        rows = cur.fetchall()
        sql = '''UPDATE tasks SET id = ? WHERE id = ?'''
        i = int(taskID)
        while i <= len(rows):
            cur.execute(sql, (i, (i + 1),))
            i += 1

        conn.commit()

    def get_tasks(self, conn):
        # returns a list of all tasks
        cur = conn.cursor()
        cur.execute("SELECT * FROM tasks")
        rows = cur.fetchall()
        listOfTasks = []
        for row in rows:
            task = todotask.task(row[0], row[1], row[2])
            listOfTasks.append(task)
        return listOfTasks
