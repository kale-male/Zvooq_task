from flask import Flask, render_template,url_for, request
import logging
from model import Students, Journal, Subjects
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def stud_list():
    if request.method == 'POST':
        Students.insert(request.form['name'],
                       request.form['surname'])
    return render_template('index.html', students = Students.get_all())

@app.route('/journal', methods = ['GET', 'POST'])
def journal():
    #app.logger.info("message")
    if request.method == 'POST':
        #app.logger.info('Post smth')
        Journal.insert(request.form['student'],
                       request.form['subject'],
                       request.form['mark'])
    return render_template('journal.html',
                           jrnl = Journal.get_all(),
                           students = Students.get_all(),
                           subjects = Subjects.get_all())

@app.route('/statistics', methods = ['GET', 'POST'])
def stat():
    studid = 1
    subjid = 1
    if request.method == 'POST':
        studid = int(request.form['student'])
        subjid = int(request.form['subject'])
        #app.logger.info("%s %s" %( studavg, subjavg))
    #else: studid = subjid =None
    studavg = Journal.st_avg(studid)
    subjavg = Journal.disc_avg(subjid)
    return render_template('stat.html',
                           students = Students.get_all(),
                           subjects = Subjects.get_all(),
                           studavg = studavg,
                           subjavg = subjavg,
                           studid = studid,
                           subjid = subjid)

if __name__ == '__main__':
    handler = RotatingFileHandler('foo.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run(debug = True)
