import sqlite3
from tkinter import messagebox


class Database :
    def __init__(self,db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS student(
        id text Primary Key ,
        reg_no text,
        name text,
        course text,
        dept text,
        year text,
        sec text,
        quota text,
        gender text,
        dob text,
        blood_group text,
        email text,
        student_ph_no text,
        parent_ph_no text,
        address text
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    # Insert Function
    def insert(self, id, reg_no , name, course, dept, year, sec, quota, gender, dob, blood_group, email, student_ph_no, parent_ph_no, address ):
        try:
            self.cur.execute("""insert into student values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                             (id, reg_no, name, course, dept, year, sec, quota, gender, dob, blood_group, email,
                              student_ph_no, parent_ph_no, address))
            self.con.commit()
            messagebox.showinfo("Success", "Record Inserted")
        except Exception as ex:
            messagebox.showerror("Error", f"Due to: {ex}")


    # fetch all data from DB
    def fetch(self):
        self.cur.execute("SELECT * from student")
        rows = self.cur.fetchall()
        # print(rows)
        return rows

    # delete a record from DB
    def remove(self,id):
        self.cur.execute("""delete from student where id=?""", (id,))
        self.con.commit()

    # update a record in DB
    def update(self, id, reg_no , name, course, dept, year, sec, quota, gender, dob, blood_group, email, student_ph_no, parent_ph_no, address ):
        self.cur.execute("""update student set reg_no=?, name=?, course=? , dept=?, year=?, sec=?, quota=?, gender=?, dob=?, blood_group=?, email=?, student_ph_no=?, parent_ph_no=?, address=? where id=?""",
                         (reg_no, name, course, dept, year, sec, quota, gender, dob, blood_group, email, student_ph_no, parent_ph_no, address, id))
        self.con.commit()

    def search(self, option1, option2):
        self.cur.execute("""select * from student where  ? =  ? """, (option1, option2) )
        global data
        data = self.cur.fetchall()
        return data