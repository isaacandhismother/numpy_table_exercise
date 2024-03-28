import numpy as np
from tabulate import tabulate
import random


# The main Table class
class Table:
    def __init__(self, student_count: int, subject_count: int):
        self.table = np.empty((student_count + 1, subject_count + 1), dtype='object')
        self.student_count = student_count
        self.subject_count = subject_count

    def __repr__(self):
        return '<Object Table>'

    def __call__(self):
        print(tabulate(self.table, tablefmt='grid'))

    def __getitem__(self, item):
        return self.table[item]

    def fill_table(self, student_list: list, subject_list: list):
        student_count = len(student_list)
        for student in range(student_count):
            self.table[student + 1, 0] = student_list[student]

        subject_count = len(subject_list)
        for subject in range(subject_count):
            self.table[0, subject + 1] = subject_list[subject]

    def fill_marks(self, marks_list: dict):
        for student, marks_dict in marks_list.items():
            student_index = np.where(self.table == student)
            for subject, mark in marks_dict.items():
                subject_index = np.where(self.table == subject)
                self.table[student_index[0], subject_index[1]] = mark

    def get_mark(self, student, subject):
        student_index = np.where(self.table == student)
        student_number = student_index[0][0]
        subject_index = np.where(self.table == subject)
        subject_number = subject_index[1][0]

        mark = self.table[student_number, subject_number]
        if isinstance(mark, int):
            return mark

    def get_marks(self, student) -> list:
        student_index = np.where(self.table == student)
        mark_list = [mark for mark in self.table[student_index[0][0]] if isinstance(mark, int)]
        return mark_list

    def get_highest_mark(self, student):
        mark_list = self.get_marks(student)
        if len(mark_list) != 0:
            return np.max(mark_list)

    def get_lowest_mark(self, student):
        mark_list = self.get_marks(student)
        if len(mark_list) != 0:
            return np.min(mark_list)

    def get_median_mark(self, student):
        mark_list = self.get_marks(student)
        if len(mark_list) != 0:
            return np.median(mark_list)


if __name__ == '__main__':
    def get_highest_mark_from_median(table: Table):
        students_medians = {}
        for student_info in table:
            if isinstance(student_info[0], str):
                student_name = student_info[0]
                median = table.get_median_mark(student_name)
                students_medians[student_name] = median
        medians = list(students_medians.values())
        max_median_index = np.argmax(medians)
        max_median_student = list(students_medians.keys())[max_median_index]

        return max_median_student, medians[max_median_index]

    def get_subject_mark_more_than_median(table: Table, subject: str):
        result = {}
        for student_info in table:
            if isinstance(student_info[0], str):
                student_name = student_info[0]
                median_mark = table.get_median_mark(student_name)
                subject_mark = table.get_mark(student_name, subject)
                if subject_mark > median_mark:
                    result[student_name] = (subject_mark, median_mark)

        return result

    def get_highest_mark_in_subject(table: Table, subject):
        mark_list = {}
        for student_info in table:
            if isinstance(student_info[0], str):
                student_name = student_info[0]
                mark = table.get_mark(student_name, subject)
                mark_list[student_name] = mark
        subject_marks = list(mark_list.values())
        highest_mark_index = np.argmax(subject_marks)
        highest_mark_student = list(mark_list.keys())[highest_mark_index]

        return highest_mark_student, subject_marks[highest_mark_index]

    def get_lowest_mark_in_subject(table: Table, subject):
        mark_list = {}
        for student_info in table:
            if isinstance(student_info[0], str):
                student_name = student_info[0]
                mark = table.get_mark(student_name, subject)
                mark_list[student_name] = mark
        subject_marks = list(mark_list.values())
        highest_mark_index = np.argmin(subject_marks)
        highest_mark_student = list(mark_list.keys())[highest_mark_index]

        return highest_mark_student, subject_marks[highest_mark_index]

    student_names = ['ვენერა', 'თინა', 'თეა', 'სოსო', 'მირანდა', 'ჟენია', 'ტატიანა',
                     'ედუარდ', 'კლარა', 'სიმონ', 'ანზორ', 'სოფია', 'სოსო', 'ნელი',
                     'ბონდო', 'ედუარდ', 'სონია', 'არჩილ', 'მარიამ', 'სოფია', 'ემა',
                     'იზოლდა', 'ომარ', 'ტატიანა', 'ვიქტორ', 'კარინე', 'გუგული',
                     'კახა', 'როზა', 'რუსუდან', 'სიმონ', 'ნელი', 'ბადრი', 'მადონა',
                     'ირინე', 'მინდია', 'ნათია', 'გულნარა', 'კახა', 'ელზა', 'როინ',
                     'ნაირა', 'ლიანა', 'ნინელი', 'მაყვალა', 'რეზო', 'ჟუჟუნა', 'ზინა',
                     'გოჩა', 'მურმან']

    student_surnames = ['ქუთათელაძე', 'მეგრელიშვილი', 'სალუქვაძე', 'ხარაიშვილი',
                        'შელია', 'კევლიშვილი', 'ბუჩუკური', 'ტყებუჩავა', 'მიქაბერიძე',
                        'ურუშაძე', 'ძიძიგური', 'გოგუაძე', 'ანთაძე', 'ვალიევა', 'როგავა',
                        'ნაკაშიძე', 'ღურწკაია', 'გვაზავა', 'გვასალია', 'ზარანდია', 'სხირტლაძე',
                        'ბერაძე', 'ხვიჩია', 'ბასილაშვილი', 'კაკაბაძე', 'მერებაშვილი', 'ნოზაძე',
                        'ხარაბაძე', 'მუსაევა', 'მამულაშვილი', 'ელიზბარაშვილი', 'მამულაშვილი',
                        'ჯოჯუა', 'გულუა', 'ხალვაში', 'ხარატიშვილი', 'დუმბაძე', 'ბერიანიძე',
                        'ჯოხაძე', 'სამხარაძე', 'ლიპარტელიანი', 'იობიძე', 'გაბაიძე', 'ხარაბაძე',
                        'ინასარიძე', 'ბერაძე', 'შენგელია', 'ქობალია', 'მიქავა', 'რევაზიშვილი']

    # Creating random students
    students = []
    for student in range(100):
        name = random.sample(student_names, 1)[0]
        surname = random.sample(student_surnames, 1)[0]
        students.append(f'{name} {surname}')

    # Creating 5 subjects
    subjects = ['Math', 'Chemistry', 'English', 'Georgian', 'History']

    # Creating random marks for all students in all subjects
    marks = {student: {subject: random.randint(1, 100) for subject in subjects} for student in students}

    # Creating the first table

    table1 = Table(100, 5)
    table1.fill_table(students, subjects)
    table1.fill_marks(marks)

    # Printing the first table
    table1()

    # Printing all necessary information
    highest_median_mark = get_highest_mark_from_median(table1)
    print(f'Student that has highest median mark: {highest_median_mark}')

    highest_mark_in_math = get_highest_mark_in_subject(table1, 'Math')
    print(f'Student with the highest mark in math: {highest_mark_in_math}')

    lowest_mark_in_math = get_lowest_mark_in_subject(table1, 'Math')
    print(f'Student with the lowest mark in math:{lowest_mark_in_math}')

    subject_mark_more_than_median = get_subject_mark_more_than_median(table1, 'English')
    print(f'Students with a subject mark more than median: {subject_mark_more_than_median}')
