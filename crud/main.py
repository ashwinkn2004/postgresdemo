from create_table import create_user_table,create_teacher_table
from insert_student import insert_student
from update_student import update_student
from delete_student import delete_student
from select_student import select_student

if __name__ == '__main__':
    print("Creating Table for student and teacher")
    print("\n")
    create_user_table()
    create_teacher_table()
    print("Tables created successfully")
    print("\n")

    print("Inserting data to student table")
    print("\n")
    insert_student()
    print("Data inserted successfully")
    print("\n")

    print("Reading data from student table")
    print("\n")
    select_student()
    print("Data read successfully")
    print("\n")

    print("Updating data in student table")
    update_student()
    print("Data updated successfully")

    print("Deleting data from student table")
    delete_student()
    print("Data deleted successfully")

