from config import db
class CourseAllocation(db.Model):
    __tablename__="courseallocation"
    id=db.Column(db.Integer,primary_key=True)
    course_id=db.Column(db.Integer,db.ForeignKey("course.id"),nullable=False)
    teacher_id=db.Column(db.Integer,db.ForeignKey("teacher.id"),nullable=False)
    allocation_date=db.Column(db.Date,nullable=False)
    
    course=db.relationship("Course")
    teacher=db.relationship("Teacher")