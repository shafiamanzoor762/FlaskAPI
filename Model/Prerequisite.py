from config import db
class Prerequisite(db.Model):
    __tablename__= "prerequisite"
    id=db.Column(db.Integer,primary_key=True)
    cid=db.Column(db.Integer,db.ForeignKey("course.id"),nullable=False)
    prerequisite_cid=db.Column(db.Integer,db.ForeignKey("course.id"),nullable=False)

    # course=db.relationship("Course")
    # pre_course=db.relationship("Course")

    course = db.relationship('Course', foreign_keys=[cid],backref='prerequisites')
    prerequisite_course = db.relationship('Course', foreign_keys=[prerequisite_cid], backref='prerequisite_for')