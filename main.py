import sqlite3 as lite 

class DatabaseManage(object):

    def __init__(self):
        # A global variable can be called multipletimes
        # and can be accessible from anywhere in the file
        global conn
        try:
            conn = lite.connect('courses.db')
            with conn: 
                cur = conn.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS course(Id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT, price TEXT, is_private BOOLEAN NOT NULL DEFAULT 1)")
        # so whatever error is gonna come is gonna come 
        # in the exception/except part
        except Exception:
            print("Unable to create DB!")
    
    # some member functions to add, remove and fetch the data

    # TODO: insert the data
    def insert_data(self, data):
        try:
            with conn:
                cur = conn.cursor()
                sql = "INSERT INTO course(name, description, price, is_private) VALUES(?,?,?,?)"
                cur.execute(sql, data)
                return True
        except Exception:
            print("Something went wrong!")
            return False
    
    # TODO: fetching the data 
    def fetch_data(self):
        try:
            with conn:
                cur = conn.cursor()
                sql = "SELECT * FROM course"
                cur.execute(sql)
                return cur.fetchall()
        except Exception:
            print("Something went wrong!")
            return False

    # TODO: delete the data 
    def delete_data(self, id):
        try:
            with conn:
                cur = conn.cursor()
                sql = "DELETE FROM course WHERE id = ?"
                cur.execute(sql, [id])
                return True
        except Exception:
            print("Something went wrong!")
            return False


# TODO: provide user interface 

def main():
    print("*" * 40);
    print("\n:: COURSE MANAGEMENT :: \n");
    print("*" * 40);
    print("\n")

    db = DatabaseManage()

    print("#"*40)
    print("\n :: User Manual :: \n")
    print("#"*40)

    print('1. Insert a new course')
    print('2. Show all courses')
    print('3. Delete a course (NEED ID OF COURSE)')

    choice = input("\n Enter a choice: ")

    if choice == "1":
        name = input("\n Enter course name : ")
        description = input("\n Enter course description : ")
        price = input("\n Enter course price : ")
        private = input("\n Is this course private? (0/1) : ")

        if db.insert_data([name, description, price, private]):
            print("Course was inserted successfully")
        else:
            print("Something went wrong")
        
    elif choice == "2":
        print("\n :: Course List ::")

        for index, item in enumerate(db.fetch_data()):
            print ("\n Sl no : " + str(index + 1))
            print ("Course ID : " + str(item[0]))
            print ("Course Name : " + str(item[1]))
            print ("Course description : " + str(item[2]))
            print ("Course Price : " + str(item[3]))
            print ("Course Price : " + str(item[3]))
            private = 'Yes' if item[4] else 'NO'
            print ("Is course private? : " + private)
            print("\n")

    elif choice == "3":
        course_id = input("\n :: Enter the course id that you wanted to delete :: ")

        if db.delete_data(course_id):
            print("Course was deleted successfully...!")
        else:
            print("Something went wrong")

    else:
        print("\n Wrong Choice enter a vaild one...!")


if __name__ == '__main__':
    main()







