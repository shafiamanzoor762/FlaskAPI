from flask import jsonify,make_response
from config import db
from Model.Student import Student
from Model.Course import Course
from Model.Semester import Semester
from Model.Teacher import Teacher
from Model.CourseAllocation import CourseAllocation
from Model.CourseEnrollment import CourseEnrollment
# to get current date have to import this
from datetime import date

class StudentController():
        
     @staticmethod
     def list_students():
        students = Student.query.all()
        return [{
           'name': s.name,
            'email': s.email,
            'date_of_birth': s.date_of_birth,
            'registration_date': s.registration_date} for s in students]
     
     @staticmethod
     def get_student_details(id):
        s = Student.query.get_or_404(id)
        return {
           'name': s.name,
            'email': s.email,
            'date_of_birth': s.date_of_birth,
            'registration_date': s.registration_date}

     @staticmethod
     def register_student(data):

        new_student = Student(
            name=data.get('name'),
            email=data.get('email'),
            date_of_birth=data.get('date_of_birth'),
            registration_date=data.get('registration_date')
        )
        db.session.add(new_student)
        db.session.commit()

        # Return the newly created course details
        response = {
            'name': new_student.name,
            'email': new_student.email,
            'date_of_birth': new_student.date_of_birth,
            'registration_date': new_student.registration_date
        }
        return make_response(jsonify(response), 201)

     @staticmethod
     def update_student(id, data):
        student = Student.query.get_or_404(id)
        print(student.name)
        student.name=data.get('name'),
        student.email=data.get('email'),
        student.date_of_birth=data.get('date_of_birth'),
        student.registration_date=data.get('registration_date')
        db.session.commit()
        return jsonify({
            'name': student.name,
            'email': student.email,
            'date_of_birth': student.date_of_birth,
            'registration_date': student.registration_date
        }), 200
    
     @staticmethod
     def delete_student(id):
        student = Student.query.get_or_404(id)
        db.session.delete(student)
        db.session.commit()
        return jsonify({
            'name': student.name,
            'email': student.email,
            'date_of_birth': student.date_of_birth,
            'registration_date': student.registration_date
        }), 200
     
     @staticmethod
     def enroll_in_course(cid,sid):
        try:
           print(cid)
           course=Course.query.get_or_404(cid)
           student=Student.query.get_or_404(sid)
           print(f"Course found: {course.id}, Student found: {student.id}")
           print('-----------------DONE---------------')
           if(course.id and student.id):
             courseenrollment=CourseEnrollment(
                course_id=course.id,
                student_id=student.id,
                enrollment_date=date.today()
             )
             db.session.add(courseenrollment)
             db.session.commit()
             return jsonify({
                'course_id':courseenrollment.course_id,
                'student_id':courseenrollment.student_id,
                'allocation_date':courseenrollment.enrollment_date
             }), 200      
        except:
           return jsonify({
                'error':'No Record Found!'
             }), 200

     @staticmethod
     def withdraw_from_course(cid,sid):
           try:
            print(cid)
            course=Course.query.get_or_404(cid)
            student=Student.query.get_or_404(sid)
            print(f"Course found: {course.id}, Student found: {student.id}")
            courseenrollment= CourseEnrollment.query.filter_by(course_id=course.id,student_id=student.id).first()
            db.session.delete(courseenrollment)
            db.session.commit()
            return jsonify({
                'course_id':courseenrollment.course_id,
                'student_id':courseenrollment.student_id,
                'enrollment_date':courseenrollment.enrollment_date
             }), 200      
           except:
            return jsonify({
                'error':'No Record Found!'
             }), 200
           
      # 8. list_courses_for_student is same method as list_courses_by_student in CourseController

     @staticmethod
     def list_courses_for_student(sid):
        stud_courses=db.session.query(CourseEnrollment,Student,Course).join(Student,Student.id==CourseEnrollment.student_id).join(Course,Course.id==CourseEnrollment.course_id).filter(Student.id==sid).all()
        return[{
            'courses': [{
                    'course_code': c.course_code,
                    'course_name': c.course_name,
                    'credits': c.credits,
                    'enrollment_date': ce.enrollment_date,
                    'course_grade': ce.grade
                   }for ce,s,c in stud_courses]
         }]

     @staticmethod
     def  get_student_transcript(sid):
        transcript_data=db.session.query(CourseEnrollment,Student,Course,Semester).join(Student,Student.id==CourseEnrollment.student_id).join(Course,Course.id==CourseEnrollment.course_id).filter(Student.id==sid).join(Semester,Semester.id==Course.semester_id).order_by(Semester.id).all()

        if transcript_data:
           return [{
            'student_name': transcript_data[0][1].name,
            'email': transcript_data[0][1].email,
            'date_of_birth': transcript_data[0][1].date_of_birth,
            'registration_date': transcript_data[0][1].registration_date,
            
            'semesters': [{
                'semester_name': sem.semester_name,
                'courses': [{
                    'course_code': c.course_code,
                    'course_name': c.course_name,
                    'credits': c.credits,
                    'enrollment_date': ce.enrollment_date,
                    'course_grade': ce.grade
                   }]
               }for ce, stu, c,sem in transcript_data]
        }]
      
     @staticmethod
     def search_students(stu_name):
        students=db.session.query(Student).filter(Student.name.like(f'%{stu_name}%')).all()
        return [{
           'name': s.name,
            'email': s.email,
            'date_of_birth': s.date_of_birth,
            'registration_date': s.registration_date
            } for s in students]
     
     @staticmethod
     def add_student_note(sid,note):
        student=db.session.query(Student).get_or_404(sid)
        if student:
           student.note=note
           db.session.commit()
        return jsonify({
            'name': student.name,
            'note': student.note
        }), 200
     
     @staticmethod
     def remove_student_note(sid):
        student=db.session.query(Student).get_or_404(sid)
        if student:
           student.note=None
           db.session.commit()
        return jsonify({
            'name': student.name,
            'note': student.note
        }), 200
     
     @staticmethod
     def list_student_notes(sid):
        student=Student.query.get_or_404(sid)
        return[{
           'note':student.note
        }]
     
     @staticmethod
     def assign_student_advisor(sid,tid):
        student=db.session.query(Student).get_or_404(sid)
        if student:
           student.advisor=tid
           db.session.commit()
        return jsonify({
            'student_name': student.name,
            'advisor_id': student.advisor
        }), 200
     
     @staticmethod
     def remove_student_advisor(sid):
        student=db.session.query(Student).get_or_404(sid)
        if student:
           student.advisor=None
           db.session.commit()
        return jsonify({
            'student_name': student.name,
            'advisor_id': student.advisor
        }), 200
     
     @staticmethod
     def get_student_advisor(sid):
        student=Student.query.get_or_404(sid)
        return[{
           'advisor_id':student.advisor
        }]
     
     @staticmethod
     def update_student_contact(sid,contact):
        student=Student.query.get_or_404(sid)
        student.contact=contact
        db.session.commit()
        return[{
           'name':student.name,
           'contact':student.contact
        }]
     
     @staticmethod
     def list_students_by_course(cid):
        students_by_cources=db.session.query(CourseEnrollment,Student,Course).join(Student,Student.id==CourseEnrollment.student_id).join(Course,Course.id==CourseEnrollment.course_id).filter(Course.id==cid).all()
        return [{
           'name': s.name,
            'email': s.email,
            'date_of_birth': s.date_of_birth,
            'registration_date': s.registration_date
            } for ce,s,c in students_by_cources]
     
     @staticmethod
     def get_student_status(sid):
        student=Student.query.get_or_404(sid)
        return[{
           'name':student.name,
           'status':student.status
        }]
     
     @staticmethod
     def change_student_status(sid,status):
        student=Student.query.get_or_404(sid)
        student.status=status
        db.session.commit()
        return[{
           'name':student.name,
           'contact':student.status
        }]