from functools import reduce

# Define a list of student grades
grades = [85, 92, 78, 90, 88, 76, 95, 89, 84, 91]

# Function to calculate the average grade
def calculate_average(grades):
    return sum(grades) / len(grades)

# Function to find the highest grade
def find_highest_grade(grades):
    return max(grades)

# Function to find the lowest grade
def find_lowest_grade(grades):
    return min(grades)

# Function to count the number of students with grades above a certain threshold
def count_above_threshold(grades, threshold):
    return len(list(filter(lambda grade: grade > threshold, grades)))

# Main function to perform the calculations
def main():
    print(f"Grades: {grades}")
    average_grade = calculate_average(grades)
    highest_grade = find_highest_grade(grades)
    lowest_grade = find_lowest_grade(grades)
    threshold = 85
    count_above = count_above_threshold(grades, threshold)
    
    print(f"Average grade: {average_grade:.2f}")
    print(f"Highest grade: {highest_grade}")
    print(f"Lowest grade: {lowest_grade}")
    print(f"Number of students with grades above {threshold}: {count_above}")

if __name__ == "__main__":
    main()
