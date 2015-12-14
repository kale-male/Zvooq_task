from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, aliased
from sqlalchemy.sql import func
from datetime import date

db = create_engine('sqlite:///DATABASE.db', echo = True)

Base = declarative_base()

# Connect to our database.
connection = db.connect()
Session = sessionmaker()
Session.configure(bind=db)

class Students(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    surname = Column(String(50))

    def __repr__(self):
        return "<Students(name='%s', surname='%s')>" % (self.name, self.surname)

    @staticmethod
    def get_all(sess = None):
        sess = sess or Session()        
        return sess.query(Students).all()

    @staticmethod
    def get_st(name, surname, sess = None):
        sess = sess or Session()
        return sess.query(Students).\
               filter(Students.name == name).\
               filter(Students.surname == surname).\
               first()
    @staticmethod
    def insert(name, surname, sess = None):
        sess = sess or Session()
        stud = Students(name = name,
                        surname = surname)
        sess.add(stud)
        sess.commit()

class Subjects(Base):
    __tablename__='subjects'
    id = Column(Integer, primary_key=True)
    subjname = Column(String(100))

    def __repr__(self):
        return "<Subjects(subjname='%s')>" % (self.subjname)

    @staticmethod
    def get_all(sess = None):
        sess = sess or Session()        
        return sess.query(Subjects).all()

    @staticmethod
    def get_d(subject, sess = None):
        sess = sess or Session()
        return sess.query(Subjects).\
               filter(Subjects.subjname == subject).\
               first()

class Journal(Base):
    __tablename__='journal'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    discipline_id =Column(Integer, ForeignKey("subjects.id"), nullable=False)
    grade = Column(Integer)
    date = Column(Date)

    @staticmethod
    def get_all(sess = None):
        sess = sess or Session()
        S = aliased(Students)
        D = aliased(Subjects)
        J = aliased(Journal)
        return sess.query(S.name, S.surname, D.subjname, J.grade, J.date).\
               join(J, J.student_id==S.id).\
               join(D, J.discipline_id==D.id).\
               all()

    @staticmethod
    def st_avg(stid,sess = None):
        sess = sess or Session()
        #stud = Student.get_st(name,surname, sess)
        sid = stid #stud.id
        return sess.query(func.avg(Journal.grade)).\
                          filter(Journal.student_id==sid).\
                          scalar()
    
    #group_by(J.student_id)
    #join(S, J.student_id==S.id).\
    
    @staticmethod
    def insert(userid, subjid, grade, sess = None):
        sess = sess or Session()
        row = Journal(student_id = userid,
                      discipline_id = subjid,
                      grade = grade,
                      date = date.today())
        sess.add(row)
        sess.commit()

    @staticmethod
    def disc_avg(subjectid, sess = None):
        sess = sess or Session()
        #subj = Subjects.get_d(subject, sess)
        sid = subjectid #subj.id
        return sess.query(func.avg(Journal.grade)).\
                          filter(Journal.discipline_id==sid).\
                          scalar()


Base.metadata.create_all(db)


