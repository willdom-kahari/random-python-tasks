s1 = [('Alice', 'Bio', 1), ('Bob', 'NED', 8), ('Bob', 'Bio', 0), ('Alice', 'LO', 7), ('Alice', 'NED', 9), ('Bob', 'LO', 10)]
v1 = [('Bio', 3), ('NED', 5), ('LO', 2)]

# Get course weight based on course name
def find_course_weight(course):
    for course_index, course_details in enumerate(v1):
        if course in course_details:
            return v1[course_index][1]
    return -1  # Return -1 if the course is not found


def top_student(grades, courses):
    sum_of_all_courses_weight = 0
    student_sum_of_weighted_grades = dict()

    for index, student_details in enumerate(grades):

        # get course weight
        course_weight = find_course_weight(student_details[1])

        # skip current iteration if course is not found
        if course_weight == -1:
            continue

        # calculate the total weight of all courses
        if index < len(courses):
            sum_of_all_courses_weight += courses[index][1]

        # calculate the student's total grade weight
        if student_details[0] not in student_sum_of_weighted_grades:
            student_sum_of_weighted_grades[student_details[0]] = student_details[2] * course_weight
        else:
            student_sum_of_weighted_grades[student_details[0]] += student_details[2] * course_weight

    # divide total student score by the total courses weight
    weighted_averages = dict(map(lambda x: (x[0], x[1] / sum_of_all_courses_weight), student_sum_of_weighted_grades.items()))

    # sort grades by weighted averages in descending order
    sorted_grades = dict(sorted(weighted_averages.items() , key=lambda item: item[1], reverse=True))

    # return first item in the list
    return list(sorted_grades.keys())[0]


top_student = top_student(s1, v1)
print(top_student)
