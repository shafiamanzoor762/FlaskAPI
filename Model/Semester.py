from config import db


class Semester(db.Model):
    __tablename__ = "semester"

    id = db.Column(db.Integer(), primary_key=True)
    semester_name = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)

    # Relationship with Course
    courses = db.relationship("Course", back_populates="semester")