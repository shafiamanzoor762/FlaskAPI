from config import db

class Student(db.Model):
    __tablename__ = "student"
    id=db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable = False)
    email = db.Column(db.String(100), unique=True,nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    registration_date = db.Column(db.Date, nullable=False)
    note=db.Column(db.String(100), nullable=True)
    advisor=db.Column(db.Integer,db.ForeignKey("teacher.id"), nullable=True)
    contact=db.Column(db.String(11),nullable=True)
    status=db.Column(db.String(15),nullable=True)

    teacher=db.relationship("Teacher")