import csv

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.attendance = {}

    def mark_attendance(self, date, status):
        self.attendance[date] = status

class AttendanceSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name):
        if student_id not in self.students:
            self.students[student_id] = Student(student_id, name)

    def mark_attendance(self, student_id, date, status):
        if student_id in self.students:
            self.students[student_id].mark_attendance(date, status)

    def export_attendance(self):
        with open('attendance.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Student ID', 'Name', 'Date', 'Status'])
            for student in self.students.values():
                for date, status in student.attendance.items():
                    writer.writerow([student.student_id, student.name, date, status])

if __name__ == "__main__":
    attendance_system = AttendanceSystem()

    while True:
        print("Attendance System Menu:")
        print("1. Add Student")
        print("2. Mark Attendance")
        print("3. Export Attendance")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_id = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            attendance_system.add_student(student_id, name)
        elif choice == "2":
            student_id = input("Enter Student ID: ")
            date = input("Enter Date (YYYY-MM-DD): ")
            status = input("Enter Status (Present/Absent): ")
            attendance_system.mark_attendance(student_id, date, status)
        elif choice == "3":
            attendance_system.export_attendance()
            print("Attendance data exported to 'attendance.csv'.")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please select a valid option.")
