import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        total = int(total_entry.get())
        attended = int(attended_entry.get())

        if total <= 0:
            messagebox.showerror("Error", "Total classes must be greater than 0")
            return

        if attended > total:
            messagebox.showerror("Error", "Attended cannot be greater than total")
            return

        percentage = (attended / total) * 100

        result_label.config(text=f"{percentage:.2f}%")

        if percentage >= 75:
            status_label.config(text="Good Attendance", fg="#00ff9d")
        else:
            status_label.config(text="Low Attendance", fg="#ff4d4d")

        # Save to file
        with open("attendance.txt", "a") as file:
            file.write(f"{percentage:.2f}%\n")

    except:
        messagebox.showerror("Invalid Input", "Enter valid numbers")

# Window
root = tk.Tk()
root.title("Attendance Tracker")
root.geometry("420x420")
root.configure(bg="#0f172a")  # dark blue theme

# Title
title = tk.Label(root, text="ATTENDANCE TRACKER", font=("Segoe UI", 18, "bold"), bg="#0f172a", fg="#38bdf8")
title.pack(pady=20)

# Frame (for better layout)
frame = tk.Frame(root, bg="#1e293b", padx=20, pady=20)
frame.pack(pady=10)

# Labels + Inputs
tk.Label(frame, text="Total Classes", bg="#1e293b", fg="white").grid(row=0, column=0, pady=10)
total_entry = tk.Entry(frame, width=20)
total_entry.grid(row=0, column=1)

tk.Label(frame, text="Attended Classes", bg="#1e293b", fg="white").grid(row=1, column=0, pady=10)
attended_entry = tk.Entry(frame, width=20)
attended_entry.grid(row=1, column=1)

# Button
calc_btn = tk.Button(root, text="Calculate Attendance", command=calculate,
                     bg="#38bdf8", fg="black", padx=15, pady=8, font=("Segoe UI", 10, "bold"))
calc_btn.pack(pady=20)

# Result
result_label = tk.Label(root, text="", font=("Segoe UI", 20, "bold"), bg="#0f172a", fg="white")
result_label.pack()

status_label = tk.Label(root, text="", font=("Segoe UI", 12), bg="#0f172a")
status_label.pack(pady=10)

# Footer
footer = tk.Label(root, text="Simple Student Project", bg="#0f172a", fg="gray", font=("Segoe UI", 8))
footer.pack(side="bottom", pady=10)

# Run
root.mainloop()
