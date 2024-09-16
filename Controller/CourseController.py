from sqlalchemy import select
from sqlalchemy.orm import session
from flask import jsonify,make_response
from config import db
from Model.Course import Course
from Model.Semester import Semester
from Model.Teacher import Teacher
from Model.CourseAllocation import CourseAllocation
from Model.Student import Student
from Model.CourseEnrollment import CourseEnrollment
from Model.Prerequisite import Prerequisite
# to get current date have to import this
from datetime import date

class CourseController():
     
    #  @staticmethod
    #  def list_semester():
    #      semesters = Semester.query.all()
    #      return [{'id':s.id,'semester_name':s.semester_name} for s in semesters]
     
     @staticmethod
     def list_courses():
        courses = Course.query.all()
        return [{
           'name': c.course_name,
            'code': c.course_code,
            'description': c.description,
            'credits': c.credits,
            'semester': c.semester_id} for c in courses]
     
     @staticmethod
     def get_course_details(id):
        c = Course.query.get_or_404(id)
        return {
            'name': c.course_name,
            'code': c.course_code,
            'description': c.description,
            'credits': c.credits,
            'semester': c.semester.semester_name
        }

     @staticmethod
     def create_course(data):
        # Look up the semester by ID to link it to the course
        semester = Semester.query.get(data.get('semester'))
        if not semester:
            return make_response(jsonify({"error": "Semester not found"}), 404)

        new_course = Course(
            course_name=data.get('name'),
            credits=data.get('credits'),
            course_code=data.get('code'),
            semester=semester,
            description=data.get('description')
        )
        db.session.add(new_course)
        db.session.commit()

        # Return the newly created course details
        response = {
            'name': new_course.course_name,
            'code': new_course.course_code,
            'description': new_course.description,
            'credits': new_course.credits,
            'semester': new_course.semester_id
        }
        return make_response(jsonify(response), 201)
        
     @staticmethod
     def update_course(id, data):
        course = Course.query.get_or_404(id)
        print(course.course_name)
        course.course_name = data.get('name')
        course.credits = data.get('credits')
        course.semester_id = data.get('semester')
        course.description = data.get('description')
        db.session.commit()
        return jsonify({
            'name': course.course_name,
            'code': course.course_code,
            'description': course.description,
            'credits': course.credits,
            'semester': course.semester_id
        }), 200
    
     @staticmethod
     def delete_course(id):
        course = Course.query.get_or_404(id)
        db.session.delete(course)
        db.session.commit()
        return jsonify({
            'name': course.course_name,
            'code': course.course_code,
            'description': course.description,
            'credits': course.credits,
            'semester': course.semester_id
        }), 200
     
     @staticmethod
     def allocate_teacher(data):
        try:
           print(data.get('cid'))
           course=Course.query.get_or_404(data.get('cid'))
           teacher=Teacher.query.get_or_404(data.get('tid'))
           print(f"Course found: {course.id}, Teacher found: {teacher.id}")
           print('-----------------DONE---------------')
           if(course.id and teacher.id):
             courseallocate=CourseAllocation(
                course_id=course.id,
                teacher_id=teacher.id,
                allocation_date=date.today()
             )
             db.session.add(courseallocate)
             db.session.commit()
             return jsonify({
                'course_id':courseallocate.course_id,
                'teacher_id':courseallocate.teacher_id,
                'allocation_date':courseallocate.allocation_date
             }), 200      
        except:
           return jsonify({
                'error':'No Record Found!'
             }), 200 
        
     @staticmethod
     def deallocate_teacher(data):
        try:
           course=Course.query.get_or_404(data.get('cid'))
           teacher=Teacher.query.get_or_404(data.get('tid'))
           print(f">>>>>>>>>>>>Course found: {course.id}, Teacher found: {teacher.id}")
           
           courseallocate = CourseAllocation.query.filter_by(course_id=course.id, teacher_id=teacher.id).first()
           
           if courseallocate:
             print(f"Course found: {courseallocate.course_id}, Teacher found: {courseallocate.teacher_id}")
             db.session.delete(courseallocate)
             db.session.commit()
             return jsonify({
                'course_id':courseallocate.course_id,
                'teacher_id':courseallocate.teacher_id,
                'allocation_date':courseallocate.allocation_date
             }), 200          
        except:
           return jsonify({
                'error':'No Record Found!'
             }), 200  
        
     @staticmethod
     def list_courses_by_teacher(id):
        courses_teacher=db.session.query(CourseAllocation,Course,Teacher).join(Course,Course.id == CourseAllocation.course_id).join(Teacher,Teacher.id == CourseAllocation.teacher_id).filter(Teacher.id==id).all()
        return[{
           'course_name':c.course_name,
           'course_code':c.course_code,
           'allocation_date':ca.allocation_date,
           'teacher_name':t.name
        }
        for ca,c,t in courses_teacher]
     
     @staticmethod
     def  list_courses_by_student(id):
        courses_student=db.session.query(CourseEnrollment,Course,Student).join(Course,Course.id == CourseEnrollment.course_id).join(Student,Student.id == CourseEnrollment.student_id).filter(Student.id==id).all()
        return[{
           'course_name':c.course_name,
           'course_code':c.course_code,
           'enrollment_date':ce.enrollment_date,
           'student_name':s.name
        }
        for ce,c,s in courses_student]
     
     @staticmethod
     def search_courses(str):
        print(str)
        courses=db.session.query(Course).filter(Course.course_name.like(f'%{str}%')).all()
        print(courses)
        return [{
           'name': c.course_name,
            'code': c.course_code,
            'description': c.description,
            'credits': c.credits,
            'semester': c.semester_id} for c in courses]
     
#  11.add_course_prerequisite (POST) - Add a prerequisite to a course.
     @staticmethod
     def add_course_prerequisite(course_id,pre_cid):
        pre=Prerequisite(
           cid=course_id,
           prerequisite_cid=pre_cid
        )
        db.session.add(pre)
        db.session.commit()
        return[{
           'course_prerequisite':'Added Sucessfully!'
        }]

#  12.remove_course_prerequisite (POST) - Remove a prerequisite from a course.
     @staticmethod
     def remove_course_prerequisite(course_id,pre_cid):
        pre=Prerequisite.query.filter(Prerequisite.cid==course_id).filter(Prerequisite.prerequisite_cid==pre_cid).first()
        db.session.delete(pre)
        db.session.commit()
        return[{
           'course_prerequisite':'Deleted Sucessfully!'
        }]
     
#  13.get_course_prerequisites (GET) - Retrieve all prerequisites for a course.
     @staticmethod
     def get_course_prerequisites(course_id):
        pre_courses=Prerequisite.query.filter(Prerequisite.cid==course_id).all()
        return [{
            'prerequisite_cid':pre.prerequisite_cid
            } for pre in pre_courses]
#  14.list_available_courses (GET) - List courses available for enrollment (not full)
     @staticmethod
     def list_available_courses():
        courses=Course.query.filter(Course.status=='active').all()
        return [{
           'name': c.course_name,
            'code': c.course_code,
            'description': c.description,
            'credits': c.credits,
            'semester': c.semester_id} for c in courses]
   
     @staticmethod
     def update_course_credits(cid,credits):
        print(credits)
        course = Course.query.get_or_404(cid)
        print(course.course_name)
        course.credits = credits
        db.session.commit()
        return jsonify({
            'name': course.course_name,
            'code': course.course_code,
            'description': course.description,
            'credits': course.credits,
            'semester': course.semester_id
        }), 200
     
#  16.archive_course (POST) - Archive a course, making it inactive.
     @staticmethod
     def archive_course(cid):
        course=Course.query.get_or_404(cid)
        course.status='inactive'
        db.session.commit()
        return[{
           'course_name':course.course_name,
           'status':course.status
        }]
        
#  17.unarchive_course (POST) - Unarchive a course, making it active again.
     @staticmethod
     def unarchive_course(cid):
        course=Course.query.get_or_404(cid)
        course.status='active'
        db.session.commit()
        return[{
           'course_name':course.course_name,
           'status':course.status
        }]
     
#  18.list_archived_courses (GET) - List all archived courses
     @staticmethod
     def list_archived_courses():
        courses=Course.query.filter(Course.status=='inactive').all()
        return [{
           'name': c.course_name,
            'code': c.course_code,
            'description': c.description,
            'credits': c.credits,
            'semester': c.semester_id,
            'status':c.status} for c in courses]
   
     @staticmethod
     def get_teacher_for_course(cid):
        course_teacher=db.session.query(CourseAllocation,Course,Teacher).join(Course,Course.id==CourseAllocation.course_id).join(Teacher,Teacher.id== CourseAllocation.teacher_id).filter(Course.id==cid).all()
        return[{
           'allocation_date':ca.allocation_date,
           'course_name':c.course_name,
           'teacher_name':t.name
        } for ca,c,t in course_teacher]               

# 20.add_course_materials (POST) - Upload materials (e.g., syllabus, lecture notes) for 
# a course.
     @staticmethod
     def add_course_materials(cid,material):
        course=Course.query.get_or_404(cid)
        course.material=material
        db.session.commit()
        return[{
           'course_name':course.course_name,
           'material':course.material
        }]