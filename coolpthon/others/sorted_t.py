from operator import itemgetter, attrgetter


class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        return repr((self.name, self.grade, self.age))


def t_sorted():
    print(sorted([5, 2, 3, 1, 4]))

    a = [5, 2, 3, 1, 4]
    a.sort()
    print(a)

    # dict 中重复key会被覆盖
    print(sorted({1: 'D', 4: 'B', 3: 'B', 2: 'E', 5: 'A'}))

    print(sorted("This is a test string from Andrew".split(), key=str.lower))

    student_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'B', 10),
        ]
    print(sorted(student_tuples, key=lambda student: student[2]))
    print(sorted(student_tuples, key=itemgetter(2)))
    # 支持多个排序
    print(sorted(student_tuples, key=itemgetter(1,2)))
    student_objects = [
        Student('john', 'A', 15),
        Student('jane', 'B', 12),
        Student('dave', 'B', 10),
        ]

    print(sorted(student_objects, key=lambda student: student.age))
    print(sorted(student_objects, key=attrgetter('age')))
    print(sorted(student_objects, key=attrgetter('grade', 'age')))


if __name__ == '__main__':
    t_sorted()
