from typing import List

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sort_student: list[str] = sorted(students)
ball = {sort_student[0] : sum(grades[0])/len(grades[0]),
        sort_student[1] : sum(grades[1])/len(grades[1]),
        sort_student[2] : sum(grades[2])/len(grades[2]),
        sort_student[3] : sum(grades[3])/len(grades[3]),
        sort_student[4] : sum(grades[4]) / len(grades[4])
        }
print(ball)




