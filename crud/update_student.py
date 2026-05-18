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
                UPDATE STUDENTS SET AGE=22 WHERE NAME='Ashwin';
            '''
            cursor.execute(query)
            conn.commit()
            print("Student updated successfully")
    except:
        print("Error occured")
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    insert_student()