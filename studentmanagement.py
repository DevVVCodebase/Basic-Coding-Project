import tkinter as tk
from tkinter import messagebox

FILE_NAME = "attendance.txt"


def mark_attendance():
    name = entry_name.get()
    date = entry_date.get()
    status = status_var.get()

    if name == "" or date == "":
        messagebox.showerror("Error", "Please fill all fields")
        return

    with open(FILE_NAME, "a") as f:
        f.write(name + "," + date + "," + status + "\n")

    messagebox.showinfo("Success", "Attendance marked successfully")
    entry_name.delete(0, tk.END)
    entry_date.delete(0, tk.END)


def view_attendance():
    name = entry_name.get()

    if name == "":
        messagebox.showerror("Error", "Enter student name to view records")
        return

    total = 0
    present = 0
    records = ""

    try:
        with open(FILE_NAME, "r") as f:
            for line in f:
                s_name, date, status = line.strip().split(",")
                if s_name == name:
                    total += 1
                    if status == "Present":
                        present += 1
                    records += f"{date} - {status}\n"
    except FileNotFoundError:
        messagebox.showerror("Error", "No attendance data found")
        return

    if total == 0:
        messagebox.showinfo("Result", "No records found for this student")
    else:
        percentage = (present / total) * 100
        result = records + f"\nAttendance Percentage: {percentage:.2f}%"
        messagebox.showinfo("Attendance Record", result)


# GUI Setup
root = tk.Tk()
root.title("Student Attendance Tracker")
root.geometry("400x350")
root.config(bg="#e6f0ff")

tk.Label(root, text="Student Attendance Tracker",
         font=("Arial", 16, "bold"), bg="#e6f0ff").pack(pady=10)

frame = tk.Frame(root, bg="#e6f0ff")
frame.pack(pady=10)

tk.Label(frame, text="Student Name:", bg="#e6f0ff").grid(row=0, column=0, sticky="w")
entry_name = tk.Entry(frame, width=25)
entry_name.grid(row=0, column=1)

tk.Label(frame, text="Date (DD-MM-YYYY):", bg="#e6f0ff").grid(row=1, column=0, sticky="w")
entry_date = tk.Entry(frame, width=25)
entry_date.grid(row=1, column=1)

tk.Label(frame, text="Status:", bg="#e6f0ff").grid(row=2, column=0, sticky="w")

status_var = tk.StringVar(value="Present")
tk.Radiobutton(frame, text="Present", variable=status_var,
               value="Present", bg="#e6f0ff").grid(row=2, column=1, sticky="w")
tk.Radiobutton(frame, text="Absent", variable=status_var,
               value="Absent", bg="#e6f0ff").grid(row=3, column=1, sticky="w")

tk.Button(root, text="Mark Attendance",
          bg="#4CAF50", fg="white",
          width=20, command=mark_attendance).pack(pady=10)

tk.Button(root, text="View Attendance",
          bg="#2196F3", fg="white",
          width=20, command=view_attendance).pack(pady=5)

root.mainloop()
