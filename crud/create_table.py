import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from db import get_db_connection

def create_user_table():
    try:
        conn = get_db_connection()
        if conn is not None:
            cursor = conn.cursor()
            query = '''
                CREATE TABLE IF NOT EXISTS STUDENTS(
                    ID SERIAL PRIMARY KEY,
                    NAME VARCHAR(100),
                    AGE INTEGER
                );
            '''
            cursor.execute(query)
            conn.commit()
            print("Table created successfully")
    except:
        print("Error occured")
    finally:
        cursor.close()
        conn.close()

def create_teacher_table():
    try:
        conn = get_db_connection()
        if conn is not None:
            cursor = conn.cursor()
            teacherQuery = '''
                CREATE TABLE IF NOT EXISTS TEACHER(
                    EMPID INTEGER PRIMARY KEY,
                    NAME VARCHAR(100),
                    SUBJECT VARCHAR(100)
                );
            '''
            cursor.execute(teacherQuery)
            conn.commit()
            print("Teacher table created.")
    except:
        print("error occured")
    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    #create_user_table()
    create_teacher_table()