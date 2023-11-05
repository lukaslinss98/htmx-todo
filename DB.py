import sqlite3
from models.Todo import Todo

TODO_DB_NAME = "todo"
TODO_TABLE_TODOS = "todos"

TODO_FIELD_ID = "id"
TODO_FIELD_CONTENT = "content"
TODO_FIELD_STATUS = "status"

def get_todos():
    connection = sqlite3.connect(TODO_DB_NAME)
    
    SELECT_ALL_SQL = f"SELECT * FROM {TODO_TABLE_TODOS}"
    
    try:
        rows = connection.execute(SELECT_ALL_SQL).fetchall()
    except sqlite3.Error as error:
        print('SQLite error: %s' % (' '.join(error.args)))
    
    connection.close()
    
    return [Todo(row[0], row[1], row[2]) for row in rows]


def insert_todo(input_text):
    
    connection = sqlite3.connect(TODO_DB_NAME)
    INSERT_SQL = f"INSERT INTO {TODO_TABLE_TODOS} ('{TODO_FIELD_CONTENT}', '{TODO_FIELD_STATUS}') VALUES(?,?)"
    
    try:
        last_row_id = connection.execute(INSERT_SQL, (input_text, 'In Progress')).lastrowid
        connection.commit()
    except sqlite3.Error as error:
        print('SQLite error: %s' % (' '.join(error.args)))

    connection.close()
    
    return last_row_id
    
def delete_todo(id):
    connection = sqlite3.connect(TODO_DB_NAME)
    DELETE_SQL = f"DELETE FROM {TODO_TABLE_TODOS} WHERE {TODO_FIELD_ID} = ?"
    
    try:
        connection.execute(DELETE_SQL, (id,))
        connection.commit()
    except sqlite3.Error as error:
        print('SQLite error: %s' % (' '.join(error.args)))

    connection.close()
    
def delete_all():
    connection = sqlite3.connect(TODO_DB_NAME)
    DELETE_ALL_SQL = f"DELETE FROM {TODO_TABLE_TODOS}"
    
    try:
        connection.execute(DELETE_ALL_SQL)
        connection.commit()
    except sqlite3.Error as error:
        print('SQLite error: %s' % (' '.join(error.args)))

    connection.close()

def update_todo(id):
    connection = sqlite3.connect(TODO_DB_NAME)
    cursor = connection.cursor()
    UPDATE_TODO_SQL = f"UPDATE {TODO_TABLE_TODOS} set {TODO_FIELD_STATUS} = 'Finished' WHERE {TODO_FIELD_ID} = ? RETURNING *"
    
    try:
        cursor.execute(UPDATE_TODO_SQL,(id,))
        result = next(cursor)
        connection.commit()

    except sqlite3.Error as error:
        print('SQLite error: %s' % (' '.join(error.args)))

    connection.close()
    
    return result