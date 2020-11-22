import sqlite3
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
        cur.execute(sql, task)
        conn.commit()
        return cur.lastrowid

    def update_task(self, conn, task):
        sql = ''' UPDATE tasks
                  SET desc = ?
                  WHERE id = ?'''
        cur = conn.cursor()
        cur.execute(sql, task)
        conn.commit()

    def view_tasks(self, conn):
        cur = conn.cursor()
        cur.execute("SELECT * FROM tasks")
        rows = cur.fetchall()

        print(len(rows))
        for row in rows:
            print(row)

    def delete_task(self, conn, taskID):
        # Should probably reset taskIDs?  Not sure if that's a smart move
        sql = 'DELETE FROM tasks WHERE id=?'
        cur = conn.cursor()
        cur.execute(sql, taskID)
        conn.commit()

        self.updateIDs(conn, taskID)


        #view_tasks(conn)  < doesn't work

    def mark_task_as_done(self, conn, idAndText):
        sql = ''' UPDATE tasks
                      SET complete = ?
                      WHERE id = ?'''
        cur = conn.cursor()
        cur.execute(sql, idAndText)
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
