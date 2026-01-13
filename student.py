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
        @staticmethod
def update_student(id, name=None, branch=None, year=None):
    conn = connect_db()
    cursor = conn.cursor()
    
    # Update name if provided
    if name:
        cursor.execute("UPDATE students SET name=? WHERE id=?", (name, id))
    
    # Update branch if provided
    if branch:
        cursor.execute("UPDATE students SET branch=? WHERE id=?", (branch, id))
    
    # Update year if provided
    if year:
        cursor.execute("UPDATE students SET year=? WHERE id=?", (year, id))
    
    conn.commit()
    conn.close()

