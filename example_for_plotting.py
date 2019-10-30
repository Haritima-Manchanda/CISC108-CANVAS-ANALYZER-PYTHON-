import matplotlib.pyplot as plt


grades = [90, 30, 40, 50, 30, 40, 20, 30, 40]

plt.hist(grades)
plt.title("Grade distribution")
plt.xlabel("Possible grades")
plt.ylabel("How many people fall into those grades")
plt.show()

hours_of_sleep = [1, 4, 3, 2, 3, 2, 4, 2, 4]

plt.scatter(grades, hours_of_sleep)
plt.show()


miles_jogged_each_day = [5, 5, 10, 2, 1, 5, 5, 5, 1, 2]

plt.plot(miles_jogged_each_day)
plt.show()

