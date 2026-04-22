from operator import index

from setuptools.command.easy_install import sys_executable


class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self,index):
        points = self.scores[index]
        system = {"A":range(90,101),"B":range(80,90),"C":range(70,80),"D":range(60,70),"E":range(50,60),"F":range(0,50)}
        grade = ""
        for key in system.keys():
            if points in system[key]:
                grade = key
        return grade

    def find(self,scored):
        idx_list = []
        list = self.scores
        for i,score in enumerate(list):
            if  score == scored:
                idx_list.append(i)
        return idx_list

    def get_sorted(self):
        scores = self.scores.copy()
        for j in range(len(scores)):
            swapped = False
            for i in range(0, len(scores) - j - 1):

                if scores[i] > scores[i + 1]:
                    scores[i], scores[i + 1] = scores[i + 1], scores[i]
                    swapped = True
            if swapped is False:
                return scores
        return scores

if __name__ == "__main__":
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    i = 0
    while i < results.count():
        print(f"Student {i}: {results.scores[i]} points - {results.get_grade(i)}")
        i += 1




    # print(results.count())  # 9
    # print(results.get_by_index(2))  # 91
    # print(results.scores)  # [85, 42, 91, 67, 50, 73, 100, 38, 58]
    # print(results.get_grade(7))
    # print(results.find(100))  # [6]
    # print(results.get_sorted())  # [38, 42, 50, 58, 67, 73, 85, 91, 100]
    # print(results.scores)