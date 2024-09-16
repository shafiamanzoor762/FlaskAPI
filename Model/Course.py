from config import db
class Course(db.Model):
    __tablename__ = "course"
    id = db.Column(db.Integer, primary_key=True)
    course_code = db.Column(db.String(10), unique=True, nullable=False)
    course_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    credits = db.Column(db.Integer, nullable=False)
    semester_id = db.Column(db.Integer, db.ForeignKey('semester.id'), nullable=False)
    status=db.Column(db.String(15),nullable=True)
    material=db.Column(db.String(45),nullable=True)
    semester = db.relationship("Semester", back_populates="courses")