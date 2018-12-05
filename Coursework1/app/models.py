from app import db

class StudentLogin(db.Model):
    __tablename__='student'
    studentid= db.Column(db.String(6),primary_key=True)
    studentpassword= db.Column(db.String(8))

class ExpertLogin(db.Model):
    __tablename__='expert'
    expertid= db.Column(db.String(6), primary_key=True)
    expertpassword= db.Column(db.String(8))

#create the database
class toDo(db.Model):
    __tablename__='list'
    issue = db.Column(db.String(40), index=True, primary_key=True)
    solution = db.Column(db.String(500), index=True, unique=True)
    

#output the database
    def __repr__(self):
        return 'toDo %r' % (self.issue,self.solution)
    
class doctor(db.Model):
    __tablename__='doctors'
    name = db.Column(db.String(40), index=True, unique=True)
    surname = db.Column(db.String(40), index=True, unique=True)
    telephone = db.Column(db.String(40), index=True, primary_key=True)
    
    

#output the database
    def __repr__(self):

        return 'doctor %r' % (self.name,self.surname,self.telephone)
