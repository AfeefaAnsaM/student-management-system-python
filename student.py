from database import connect_db

class Student:

    @staticmethod
    def add_student(id, name, branch, year):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO students VALUES (?, ?, ?, ?)",
            (id, name, branch, year)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def view_students():
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        conn.close()
        return rows

    @staticmethod
    def delete_student(id):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE id=?", (id,))
        conn.commit()
        conn.close()
        
    
  

