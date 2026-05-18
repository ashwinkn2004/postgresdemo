import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from db import get_db_connection

def insert_student():
    try:
        conn = get_db_connection()
        if conn is not None:
            cursor = conn.cursor()
            query = '''
                INSERT INTO STUDENTS(NAME, AGE)
                VALUES('Ashwin', 21);
                INSERT INTO STUDENTS(NAME, AGE)
                VALUES('Alphonse', 23);
            '''
            cursor.execute(query)
            conn.commit()
            print("Data inserted successfully")
    except:
        print("Error occured")
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    insert_student()