#import modules
from flask import Flask, render_template, request, redirect
from dataBase import AudioFiles

app = Flask(__name__)
#for home page
@app.route('/')
def home():
    return render_template('index.html')

#to get option to do nect step
@app.route('/nextstep',methods = ['POST'])
def nextstep():
    if request.method == 'POST':
        operation = request.form["operation"]
        if operation =="create":
            AudioType = request.form['AudioType']
            tab=AudioFiles()
            try:
                ms = tab.create_table(AudioType)
            except Exception as e:
                data=e
            return render_template('index.html', data1=[ms,data])
        elif operation =="Insert":
            return render_template('insertrecords.html')
        elif operation =="Update":
            return render_template('updatesrecords.html')
        elif operation =="delete":
            return render_template('deleteRecords.html')
        elif operation =="get":
            return render_template('/getrecord.html')

#for inserting record in the respective tables  
@app.route('/insertrecord',methods = ['POST', 'GET'])
def insertrecord():
    if request.method == 'POST':
        AudioType = request.form["option"]
        id = request.form['ID']
        title = request.form['Title']
        duration = request.form['Duration']
        Uploaded = request.form['Uploaded']
        Host = request.form['Host']
        Participants = request.form['Participants']
        AuthorOfTitle = request.form['AuthorOfTitle']
        Narrator = request.form['Narrator']
        tab=AudioFiles()
        if AudioType =="Audio":
            row= tab.insertAudio(id, title, duration, Uploaded)
        elif AudioType=="Podcast":
            row= tab.insertPodcast(id, title, duration, Uploaded, Host, Participants)
        else:
            row= tab.insertAudioBook(id, title,AuthorOfTitle, Narrator, duration, Uploaded)
        return render_template('insertrecords.html', data1=row) 

#to delete record   
@app.route('/deleterecord',methods = ['POST', 'GET'])
def deleterecord():
    if request.method == 'POST':
        operation = request.form["option"]
        AudioType = request.form['ID']
        tab=AudioFiles()
        try:
            row=tab.deleteRecords(operation,AudioType)
        except Exception as e:
            row=e
    return render_template('deleteRecords.html', data1= row)
#records
@app.route('/updaterecord',methods = ['POST', 'GET'])
def updaterecord():
    if request.method == 'POST':
        AudioType = request.form["option"]
        id = request.form['ID']
        Column = request.form['Column']
        NewValue = request.form['NewValue']
        tab=AudioFiles()
        row= tab.UpdateRecords(AudioType, Column, NewValue, id)
    return render_template('updatesrecords.html', data1=row)

@app.route('/getrecord',methods = ['POST'])
def getrecord():
    if request.method == 'POST':
        operation = request.form["option"]
        AudioType = request.form['ID']
        tab=AudioFiles()
        try:
            row=tab.records(operation,AudioType)
        except Exception as e:
            row=e
    return render_template('getrecord.html',data1=row)

if __name__== "__main__":
    app.run(debug=True)
