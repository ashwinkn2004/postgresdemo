import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from db import get_db_connection

def delete_student():
    try:
        conn = get_db_connection()
        if conn is not None:
            cursor = conn.cursor()
            query = '''
                DELETE FROM STUDENTS WHERE NAME='Alphonse';
            '''
            cursor.execute(query)
            conn.commit()
            print("Student deleted successfully")
    except:
        print("Error occured")
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    delete_student()