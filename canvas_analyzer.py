import matplotlib.pyplot as plt
import canvas_requests
import datetime
"""
Project 4C
Canvas Analyzer
CISC108 Honors
Fall 2019

Access the Canvas Learning Management System and process learning analytics.

Edit this file to implement the project.
To test your current solution, run the `test_my_solution.py` file.
Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: HARITIMA MANCHANDA
"""
__version__ = 7

# 1) main
# 2) print_user_info
# 3) filter_available_courses
# 4) print_courses
# 5) get_course_ids
# 6) choose_course
# 7) summarize_points
# 8) summarize_groups
# 9) plot_scores
# 10) plot_grade_trends

#user_info_dict={"name":"Hermione","title":"student","email":"haritima@udel.edu","bio":"freshman"}
# Keep any function tests inside this IF statement to ensure
# that your `test_my_solution.py` does not execute it.


def print_user_info (user):
    print("Name: ",user["name"])
    print("Title: ",user["title"])
    print("Email: ",user["primary_email"])
    print("Bio: ",user["bio"])

def filter_available_courses(courses: list) -> list:
    list2=[]
    for dictionary in courses:
        if dictionary["workflow_state"]=="available":
            list2.append(dictionary)
    print(list2)
    return list2

def print_courses(courses):
    print("ID","\t","Course")
    for dictionary in courses:
        print(dictionary["id"],"\t",dictionary["name"])

def get_course_ids(courses: list) ->[int]:
    list2=[]
    for dictionary in courses:
        list2.append(dictionary["id"])
    print(list2)
    return list2

def choose_course(course_ids: list) -> int :
    while True:
        course_id=int(input("Enter the course ID of the course you want to chose. Enter a valid course ID: "))
        if (course_id not in course_ids) :
            print("Not a valid ID. Please enter a valid ID.")
            continue
        else:
            break
    return (course_id)

def summarize_points(a_list):
    sum1=sum2=0
    for submission in a_list:
        if submission["score"]!= None :
            sum1+=submission["assignment"]["points_possible"]*submission["assignment"]["group"]["group_weight"]
            sum2+=submission["score"]*submission["assignment"]["group"]["group_weight"]
    print("Points possible so far: ",sum1)
    print("Points Obtained: ",sum2)
    print("Current grade: ",round((sum2/sum1)*100))

def summarize_groups(a_list):
    counts={}
    total_score={}
    for submission in a_list:
        if submission["score"]!=None:
            if submission["assignment"]["group"]["name"] in counts:
                counts[submission["assignment"]["group"]["name"]]+=1
            else:
                counts[submission["assignment"]["group"]["name"]]=1
    for key,value in counts.items():
        score=points_possible=0
        for submission in a_list:
            if key==submission["assignment"]["group"]["name"] and submission["score"]!=None:
                score+=submission["score"]
                points_possible+=submission["assignment"]["points_possible"]
        unweighted_grade=round(((score*value)/(points_possible*value))*100)
        print(key,":",unweighted_grade)

def plot_scores(a_list):
    submission_grade=[]
    for submission in a_list:
        if submission["score"]!=None and submission["assignment"]["points_possible"]>0:
            grade=(submission["score"]*100)/submission["assignment"]["points_possible"]
            submission_grade.append(grade)
    plt.hist(submission_grade)
    plt.title("Distribution of Grades")
    plt.xlabel("Grades")
    plt.ylabel("Number of Assignments")
    plt.show()

def plot_grade_trends(a_list):
    list_max_points=[]
    list_low_points=[]
    list_high_points=[]

    # Calculating max,low,high points of each submission and storing in separate lists

    for submission in a_list:
        max_points_of_a_submission=100*submission["assignment"]["points_possible"]*submission["assignment"]["group"]["group_weight"]
        if submission["score"]!=None:
            low_points_of_submission=100*submission["score"]*submission["assignment"]["group"]["group_weight"]
            high_points_of_submission=100*submission["score"]*submission["assignment"]["group"]["group_weight"]
        else:
            low_points_of_submission=0
            high_points_of_submission=100*submission["assignment"]["points_possible"]*submission["assignment"]["group"]["group_weight"]
        list_max_points.append(max_points_of_a_submission)
        list_low_points.append(low_points_of_submission)
        list_high_points.append(high_points_of_submission)

    # Running sum pattern for max, low, high points of submission

    running_max_sum=0
    running_max_sums=[]
    for points in list_max_points:
        running_max_sum+=points
        running_max_sums.append(running_max_sum)
    max_points=running_max_sum/100

    running_low_sum=0
    running_low_sums=[]
    for low_score in list_low_points:
        running_low_sum+=low_score
        running_low_sums.append(running_low_sum)

    running_high_sum=0
    running_high_sums=[]
    for high_score in list_high_points:
        running_high_sum+=high_score
        running_high_sums.append(running_high_sum)

    # Due dates on the X axis
    list_date=[]
    for submission in a_list:
        due_at = datetime.datetime.strptime(submission["assignment"]["due_at"], "%Y-%m-%dT%H:%M:%SZ")
        list_date.append(due_at)
    #Dividing each element of running sums by the max_points to get the points for plotting

    final_list_maxes=[]
    final_list_lows=[]
    final_list_highs=[]
    for y_data1 in running_max_sums:
        maxes=y_data1/max_points
        final_list_maxes.append(maxes)

    for y_data2 in running_low_sums:
        lows=y_data2/max_points
        final_list_lows.append(lows)


    for y_data3 in running_high_sums:
        highs=y_data3/max_points
        final_list_highs.append(highs)

    plt.title("Grade Trends")
    plt.plot(list_date,final_list_maxes,label="Maximum")
    plt.plot(list_date,final_list_lows, label="Minimum")
    plt.plot(list_date,final_list_highs, label="Highest")
    plt.legend()
    plt.show()

def main(user_id):
    user = canvas_requests.get_user(user_id)
    print_user_info(user)
    courses = canvas_requests.get_courses(user_id)
    list_courses = filter_available_courses(courses)
    print_courses(courses)
    list_course_ids = get_course_ids(courses)
    user_chosen_id = choose_course(list_course_ids)
    a_list = canvas_requests.get_submissions(user_id, user_chosen_id)
    summarize_points(a_list)
    summarize_groups(a_list)
    plot_scores(a_list)
    plot_grade_trends(a_list)

if __name__ == "__main__":
    main('hermione')
    # main('ron')
    # main('harry')

    # https://community.canvaslms.com/docs/DOC-10806-4214724194
    # main('YOUR OWN CANVAS TOKEN (You know, if you want)')

































