from model import *
from datetime import date


# Making some test data
Studentss = [
    Students(name = 'Федот', surname = 'Стрелец'),
    Students(name = 'Алиса', surname = 'Чудесная'),
    Students(name = 'Арсений', surname = 'Молодец'),
    Students(name = 'Вероника', surname = 'Трава'),
    Students(name = 'Noname', surname = 'Www')
    ]

sess = Session()
for s in Studentss:
    sess.add(s)
sess.commit()

Subjects = [
    Subjects(subjname = 'алгебра'),
    Subjects(subjname = 'геометрия'),
    Subjects(subjname = 'философия'),
    Subjects(subjname = 'физика'),
    Subjects(subjname = 'история'),
    Subjects(subjname = 'иностранный язык')
    ]
sess = Session()
for sb in Subjects:
    sess.add(sb)


Rows = [
    Journal(student_id = 1, discipline_id = 5, grade = 4, date = date.today()),
    Journal(student_id = 5, discipline_id = 1, grade = 3, date = date.today()),
    Journal(student_id = 2, discipline_id = 4, grade = 5, date = date.today()),
    Journal(student_id = 3, discipline_id = 2, grade = 5, date = date.today()),
    Journal(student_id = 4, discipline_id = 3, grade = 4, date = date.today())]

for r in Rows:
    sess.add(r)
    
j1 = Journal(student_id = 1, discipline_id = 1, grade = 4, date = date.today())
sess.add(j1)
sess.commit()
