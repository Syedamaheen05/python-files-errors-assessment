
import csv

# Input and output files
INPUT_FILE = "attendance.txt"
OUTPUT_FILE = "attendance_clean.csv"


# Read and clean student names
def clean_attendance():
    try:
        with open(INPUT_FILE, "r") as file:
            original_names = file.readlines()

    except FileNotFoundError:
        print("Error: attendance.txt file not found.")
        return

    # Clean names using list comprehension
    # Clean names using list comprehension
    cleaned_names: list[str] = [
    " ".join(name.strip().split()).title()
    for name in original_names
    if name.strip()
]

    # Use set to remove duplicate student names
    unique_students = set(cleaned_names)

    # Sort unique students alphabetically
    sorted_students = sorted(unique_students)

    # Save cleaned attendance to CSV
    with open(OUTPUT_FILE, "w", newline="") as file:
        writer = csv.writer(file)

        # Write CSV header
        writer.writerow(["Student Name"])

        # Write sorted student names
        for student in sorted_students:
            writer.writerow([student])

    # Display attendance summary
    print("\n--- Attendance Cleaning Report ---")
    print(f"Original Records: {len(original_names)}")
    print(f"Unique Students: {len(unique_students)}")

    print("\n--- Cleaned Attendance List ---")

    for student in sorted_students:
        print(student)

    print(f"\nCleaned attendance saved to {OUTPUT_FILE}")


# Start the program
if __name__ == "__main__":
    clean_attendance()

