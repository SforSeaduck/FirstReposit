import sqlite3

def create_database():
    conn = sqlite3.connect('school_database.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Schools (
        school_id INTEGER PRIMARY KEY,
        address TEXT NOT NULL,
        floors INTEGER CHECK(floors >= 1) NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Students (
        last_name TEXT NOT NULL,
        first_name TEXT NOT NULL,
        specialization TEXT,
        school_id INTEGER,
        FOREIGN KEY (school_id) REFERENCES Schools (school_id)
    )
    ''')

    conn.commit()
    conn.close()

def insert_data():

    conn = sqlite3.connect('school_database.db')
    cursor = conn.cursor()

    schools = [
        ('123 Main St', 3),
        ('456 Oak Ave', 2),
        ('789 Pine Rd', 4)
    ]
    cursor.executemany('INSERT INTO Schools (address, floors) VALUES (?, ?)', schools)

    students = [
        ('Smith', 'John', 'Mathematics', 1),
        ('Doe', 'Jane', 'Science', 1),
        ('Brown', 'Mike', 'History', 2),
        ('White', 'Emily', 'Mathematics', 2),
        ('Black', 'Anna', 'Science', 3),
        ('Green', 'Tom', 'History', 3),
        ('Gray', 'Sue', 'Mathematics', 1),
        ('Adams', 'Paul', 'Science', 2),
        ('Nelson', 'Lisa', 'History', 3),
        ('Wilson', 'Anna', 'Mathematics', 2)
    ]
    cursor.executemany('INSERT INTO Students (last_name, first_name, specialization, school_id) VALUES (?, ?, ?, ?)', students)

    conn.commit()
    conn.close()

def fetch_data():

    conn = sqlite3.connect('school_database.db')
    cursor = conn.cursor()

    cursor.execute('''
    SELECT last_name, first_name, specialization, address
    FROM Students
    JOIN Schools ON Students.school_id = Schools.school_id
    ''')

    students = cursor.fetchall()
    for student in students:
        print(student)

    conn.close()

if __name__ == "__main__":
    create_database()
    insert_data()
    fetch_data()
