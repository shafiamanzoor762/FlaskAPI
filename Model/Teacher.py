from config import db
class Teacher(db.Model):
    __tablename__="teacher"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    email=db.Column(db.String(100),nullable=False)
    department=db.Column(db.String(100),nullable=False)
    hire_date=db.Column(db.Date,nullable=False)

    # teachers = db.relationship("Course", back_populates="semester")