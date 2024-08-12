# Program to calculate GPA for a student given three lists: courseIds_list,
# course_credits and course_grades
separator = "***"*10
POSSIBLE_GRADES = ['A', 'B', 'C', 'D']
POSSIBLE_POINTS = [4, 3, 2, 1]
def print_transcript(courseIds, creds, grades ):
    print("Here's a list of transcription you GPA:")
    print("***"*15)
    points = []
    for grade in grades:
        index=POSSIBLE_GRADES.index(grade)
        point = POSSIBLE_POINTS[index]
        points.append(point)
  
    if courseIds :
        for index in range(len(courseIds)):
            print(index+1, courseIds[index], creds[index], points[index], sep="\t")
    else:
        print("No courses added")
    print("***"*15)
    '''Function to print the transcript showing course Ids,
    credits for the course and grades for the courses entered so far
    if no courses added yet, print "No courses added"'''
    
      

def calc_GPA(courseIds, creds, grades):
    '''Function to calculate the total GPA as per the input lists
    of course Ids, credits and letter grades.
    total_points = Sum of (credits_per_course * points_as_per_grade_for_that_course) for all the courses
    total_credits = sum of all the credits
    GPA = total_points / total_credits
    return GPA rounded to 2 digits.
    if no courses added yet, return 0
    '''
    
    total_points = 0
    for credit, grade in zip(creds, grades):
        total_points += credit * POSSIBLE_POINTS[POSSIBLE_GRADES.index(grade)] 

    total_credits = sum(creds)

    if total_credits == 0:
        return 0

    gpa = total_points / total_credits
    return round(gpa, 2)


def main():
    print("Welcome to BC Transcript Generator")
    courseId_list = [] #list of courseIds of courses entered so far
    credits_list = [] #list of credits of courses entered so far
    grades_list = []#list of letter grades of courses entered so far
    ans = 'y'
    while (ans.startswith('y')) :
        print(separator)
        itemname = input("Enter the item of course: ")    ## Prompt for courseId
        courseId_list.append(itemname)
        while True:
            credits = int(input("Enter credit of course(number between 1 through 5): "))  ## Prompt for the credits for the course and Validate that the number oof credits is integer between 1 through 5
            if (1 <= credits <= 5):
                print("It was valid input")
                break
            else:
                print("Please enter a valid credit rating (1 to 5).")
        credits_list.append(credits)
        while True:
            grade = input("Enter GRADE of your course: ")    ## Prompt for the letter grade. Validate that it is one of the possible grades listed above.
            if grade not in ('A', 'B', 'C', 'D'):
                print("Please enter a valid grade (A, B, C, D)")
                continue
            else:
                print("It was valid input")
                break
        grades_list.append(grade)            
        
        print_transcript(courseId_list, credits_list, grades_list)
        total = calc_GPA(courseId_list,credits_list,grades_list)
        print(f"GPA so far: {calc_GPA(courseId_list,credits_list,grades_list)}")
        ans = input("Enter another course? (y/n) ").lower()
    print(separator)
    print(f"Your final GPA: {calc_GPA(courseId_list,credits_list,grades_list)}")
    print(separator)

if (__name__ == "__main__"):
    main()
