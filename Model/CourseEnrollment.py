from config import db
class CourseEnrollment(db.Model):
    __tablename__="courseenrollment"
    id=db.Column(db.Integer,primary_key=True)
    student_id=db.Column(db.Integer,db.ForeignKey("student.id"),nullable=False)
    course_id=db.Column(db.Integer,db.ForeignKey("course.id"),nullable=False)
    enrollment_date=db.Column(db.Date,nullable=False)
    grade=db.Column(db.Integer,nullable=True)

    student=db.relationship("Student")
    course=db.relationship("Course")