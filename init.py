import sqlite3

TODO_DATABASE = "todo"

SQL_CREATE_TABEL_TODOS = """CREATE TABLE IF NOT EXISTS todos (
                                    id integer PRIMARY KEY,
                                    content text NOT NULL,
                                    status integer
                                );"""

def create_db():
    connection = sqlite3.connect(TODO_DATABASE)
    print(f"Database Connection started with {connection.total_changes} changes")
    
    cursor = connection.cursor()
    cursor.execute(SQL_CREATE_TABEL_TODOS)
    
    #cursor.execute("INSERT INTO todos VALUES (?, ?);", ("My first todo", "In Progress"))
    
    print(f"Added initial data. {connection.total_changes} changes were made")
