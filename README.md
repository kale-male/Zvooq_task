# Zvooq_task
The task was to create a web application as a recordation of school marks. User can add a student in list, evaluate a student and also know an average grade per student or per subject.  
It was needed to use Flask & SQLAlchemy.  

There are three classes in my lab: Students, Subjects and Journal (description in model.py). We create a schema of database by the classes structure.   

Class Students:  
id - attribute of class (and table field)  
name - attribute of class (and table field)  
surname - attribute of class (and table field)  
get_all - method of class to list all rows in table Students  
get_st - method of class to find a student by name and surname  
insert - method of class to add a student record into table  
  
Class Subjects:  
id - attribute of class (and table field)  
subjname - attribute of class (and table field)  
get_all - method of class to list all rows in table Subjects  
get_d - method of class to find a student by subject name  
  
Class Journal:  
id - attribute of class (and table field)  
student_id - related with Students.id  
discipline_id - related with Subjects.id  
grade - attribute of class (and table field)  
date - attribute of class (and table field)  
get_all - method of class to list all rows in table Journal  
st_avg - method of class to calculate an average mark of a student  
disc_avg - method of class to calculate an average mark of a discipline  
insert - method of class to add a record in Journal table  
  
To create a database with test data, run Create_SCHEMA.py  

To run the application, run Server.py  
