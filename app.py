import pymysql

# Replace placeholders with your database credentials
credentials



def connect_to_database():
    """Connects to the MySQL database and returns a connection object."""
    try:
        conn = pymysql.connect(host=host, user=user, password=password, database=database)
        print("Connected to database successfully")
        return conn
    except pymysql.Error as e:
        print("Error connecting to database:", e)
        return None


def insert_student(name, email, age, gender, address, city, state, country):
    """Inserts a new student record into the 'students_data' table."""
    conn = connect_to_database()
    cursor = conn.cursor()
    sql = """
        INSERT INTO student_data (name, email, age, gender, address, city, state, country)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    try:
        cursor.execute(sql, (name, email, age, gender, address, city, state, country))
        conn.commit()
        print("Student data inserted successfully")
    except pymysql.Error as e:
        print("Error inserting student data:", e)
    finally:
        cursor.close()
        conn.close()


def update_student(id, name=None, email=None, age=None, gender=None, address=None, city=None, state=None, country=None):
    conn = connect_to_database()
    cursor = conn.cursor()
    sql = "UPDATE student_data SET "
    update_params = []
    update_values = []
    if name:
        update_params.append("name = %s")
        update_values.append(name)
    if email:
        update_params.append("email = %s")
        update_values.append(email)
    # ... (similar logic for other fields)
    if not update_params:
        print("No update parameters provided")
        return
    sql += ", ".join(update_params)
    sql += " WHERE id = %s"
    update_values.append(id)  # Add ID to the parameter list
    try:
        cursor.execute(sql, update_values)
        conn.commit()
        print("Student data updated successfully")
    except pymysql.Error as e:
        print("Error updating student data:", e)
    finally:
        cursor.close()
        conn.close()

def select_students():
    """Fetches all student records from the 'student_data' table and prints them."""
    conn = connect_to_database()
    cursor = conn.cursor()
    sql = "SELECT * FROM student_data"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        if results:
            print("Student data:")
            for row in results:
                print(row)
        else:
            print("No student data found in the table")
    except pymysql.Error as e:
        print("Error fetching student data:", e)
    finally:
        cursor.close()
        conn.close()


# Example usage
insert_student("Alice", "alice@example.com", 20, "Female", "123 Main St", "Anytown", "CA", "USA")
update_student(1, city="Newtown")  # Update city for student with ID 1
select_students()

# Use a SQL client like MySQL Workbench to view the table contents directly for verification.
print("Connect to your MySQL database using a SQL client to view the 'student_data' table.")
