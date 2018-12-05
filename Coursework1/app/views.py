from flask import render_template,request,flash,redirect,url_for
from app import app,db
from .forms import AddIssueForm
from .models import db,toDo,doctor,ExpertLogin,StudentLogin
from .forms import SearchForm,AddDoctorForm,loginform

@app.route('/', methods=['GET', 'POST'])
def login():
    form=loginform(request.form)
    if request.method == 'POST':
        username=request.form['username']
        password=request.form['password']
        if (db.session.query(ExpertLogin.expertid).filter_by(expertid=username).first()):
            if (db.session.query(ExpertLogin.expertpassword).filter_by(expertpassword=password).first()):
                return render_template('expert.html')
            else:
                flash("Invalid Username or Password")
        elif (db.session.query(StudentLogin.studentid).filter_by(studentid=username).first()):
            if (db.session.query(StudentLogin.studentpassword).filter_by(studentpassword=password).first()):
                return redirect(url_for("search"))
            else:
                flash("Invalid Username or Password")
        else:
            flash("Invalid Username or Password")

    return render_template('home.html', title='Login Page',form=form)


# alltasks route, shows alltasks.html view
@app.route('/alldoctors')
def alldoctors():
    alldoctors=doctor.query.all()

    return render_template('alldoctors.html',theDoctors=alldoctors)

# alltasks route, shows alltasks.html view
@app.route('/allissues')
def allissues():
    allissues=toDo.query.all()

    return render_template('allissues.html',theIssues=allissues)

@app.route('/search', methods=['GET', 'POST'])
def search():
    search=SearchForm(request.form)
    if request.method=='POST':
        return search_results(search)
    
    return render_template('search.html',form=search)


@app.route('/results/')
def search_results(search):
    results = []
    search_string = search.data['search'].lower()
    

    if search.data['search'] == '':
        results =toDo.query.all()
   
    elif search.data['search']!='':
        results=toDo.query.filter(toDo.issue.contains(search_string)).all()
        
    if not results:
        
        return redirect('/alldoctors')
        flash('No results found!')
    else:
        # display results
        return render_template('results.html', theResults=results)

# createtask route, shows createtask.html view
@app.route('/addissue',methods=['GET', 'POST'])
def addissue():
    #collects data from textboxes and input to database
    form=AddIssueForm(request.form)
    if request.method == 'POST' and form.validate():
        x=toDo()
        issue=request.form['issue']
        solution=request.form['solution']
        x.issue=issue
        x.solution=solution
        db.session.add(x)
        db.session.commit()
        flash('Issue Added: ' + issue)
    else:
            flash('Error: All the form fields are required. ')
            
    return render_template("addissue.html",issue='Issue', form=form)

@app.route('/adddoctor',methods=['GET', 'POST'])
def adddoctor():
    #collects data from textboxes and input to database
    form=AddDoctorForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        x=doctor()
        name=request.form['name']
        surname=request.form['surname']
        telephone=request.form['telephone']
        x.name=name
        x.surname=surname
        x.telephone=telephone
        db.session.add(x)
        db.session.commit()
        flash('Doctor added ' + name)
    else:
            flash('Error: All the form fields are required. ')
            
    return render_template("addDoctor.html",name='Name', form=form)

    
