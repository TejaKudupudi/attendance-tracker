# Attendance Tracker Project

def calculate_attendance():
    subjects = int(input("Enter number of subjects: "))
    
    total_all = 0
    attended_all = 0

    for i in range(subjects):
        print(f"\nSubject {i+1}")
        total = int(input("Total classes: "))
        attended = int(input("Attended classes: "))

        total_all += total
        attended_all += attended

        percent = (attended / total) * 100
        print(f"Subject Attendance: {percent:.2f}%")

    overall = (attended_all / total_all) * 100

    print("\n--- Overall Attendance ---")
    print(f"Overall Percentage: {overall:.2f}%")

    if overall >= 75:
        print("Status: Good Attendance ✅")
    else:
        print("Status: Low Attendance ⚠️")

    # Save to file
    with open("attendance.txt", "a") as file:
        file.write(f"Overall Attendance: {overall:.2f}%\n")

calculate_attendance()