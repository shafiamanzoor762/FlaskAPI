
from flask import Flask, request,jsonify
from config import app

from Controller.CourseController import CourseController
from Controller.StudentController import StudentController


# @app.route('/list_semester', methods=['GET'])
# def get_all_semester():
#     return jsonify(CourseController.list_semester())

@app.route('/list_courses', methods=['GET'])
def list_courses():
    return jsonify(CourseController.list_courses())

@app.route('/course/<int:course_id>', methods=['GET'])
def get_course_details(course_id):
    return CourseController.get_course_details(course_id)

@app.route('/create_course',methods=['POST'])
def create_course():
    return CourseController.create_course(request.get_json())

@app.route('/update_course/<int:course_id>',methods=['POST'])
def update_course(course_id):
    return CourseController.update_course(course_id, request.get_json())

@app.route('/delete_course/<int:course_id>', methods=['POST'])
def delete_course(course_id):
    return CourseController.delete_course(course_id)

@app.route('/allocate_teacher', methods=['POST'])
def allocate_teacher():
    return CourseController.allocate_teacher(request.get_json())

@app.route('/deallocate_teacher', methods=['POST'])
def deallocate_teacher():
    return CourseController.deallocate_teacher(request.get_json())

@app.route('/courses_by_teacher/<int:teacher_id>', methods=['GET'])
def list_courses_by_teacher(teacher_id):
    return CourseController.list_courses_by_teacher(teacher_id)

@app.route('/courses_by_student/<int:student_id>', methods=['GET'])
def list_courses_by_student(student_id):
    return CourseController.list_courses_by_student(student_id)

@app.route('/search_courses/<string:course_name>', methods=['GET'])
def search_courses(course_name):
    return CourseController.search_courses(course_name)

@app.route('/add_course_prerequisite/<int:course_id>/<int:pre_cid>', methods=['POST'])
def add_course_prerequisite(course_id,pre_cid):
    return CourseController.add_course_prerequisite(course_id,pre_cid)

@app.route('/remove_course_prerequisite/<int:course_id>/<int:pre_cid>', methods=['POST'])
def remove_course_prerequisite(course_id,pre_cid):
    return CourseController.remove_course_prerequisite(course_id,pre_cid)

@app.route('/get_course_prerequisites/<int:course_id>', methods=['GET'])
def get_course_prerequisites(course_id):
    return CourseController.get_course_prerequisites(course_id)

@app.route('/list_available_courses', methods=['GET'])
def list_available_courses():
    return CourseController.list_available_courses()

@app.route('/update_course_credits/<int:course_id>/<int:credits>',methods=['POST'])
def update_course_credits(course_id,credits):
    return CourseController.update_course_credits(course_id, credits)

@app.route('/archive_course/<int:course_id>',methods=['POST'])
def archive_course(course_id):
    return CourseController.archive_course(course_id)

@app.route('/unarchive_course/<int:course_id>',methods=['POST'])
def unarchive_course(course_id):
    return CourseController.archive_course(course_id)

@app.route('/list_archived_courses', methods=['GET'])
def list_archived_courses():
    return CourseController.list_archived_courses()

@app.route('/get_teacher_for_course/<int:course_id>', methods=['GET'])
def get_teacher_for_course(course_id):
    return CourseController.get_teacher_for_course(course_id)

@app.route('/add_course_materials/<int:course_id>/<string:material>',methods=['POST'])
def add_course_materials(course_id,material):
    return CourseController.add_course_materials(course_id, material)

# ---------- STUDENT CONTROLLER-------------

@app.route('/list_students', methods=['GET'])
def list_students():
    return jsonify(StudentController.list_students())

@app.route('/student/<int:student_id>', methods=['GET'])
def get_student_details(student_id):
    return StudentController.get_student_details(student_id)

@app.route('/register_student',methods=['POST'])
def register_student():
    return StudentController.register_student(request.get_json())

@app.route('/update_student/<int:student_id>',methods=['POST'])
def update_student(student_id):
    return StudentController.update_student(student_id, request.get_json())

@app.route('/delete_student/<int:student_id>', methods=['POST'])
def delete_student(student_id):
    return StudentController.delete_student(student_id)

@app.route('/enroll_in_course/<int:course_id>/<int:student_id>',methods=['POST'])
def enroll_in_course(course_id,student_id):
    return StudentController.enroll_in_course(course_id, student_id)

@app.route('/withdraw_from_course/<int:course_id>/<int:student_id>',methods=['POST'])
def withdraw_from_course(course_id,student_id):
    return StudentController.withdraw_from_course(course_id, student_id)

@app.route('/list_courses_for_student/<int:student_id>', methods=['GET'])
def list_courses_for_student(student_id):
    return StudentController.list_courses_for_student(student_id)

@app.route('/get_student_transcript/<int:student_id>', methods=['GET'])
def get_student_transcript(student_id):
    return StudentController.get_student_transcript(student_id)

@app.route('/search_students/<string:student_name>', methods=['GET'])
def search_students(student_name):
    return StudentController.search_students(student_name)

@app.route('/add_student_note/<int:student_id>/<string:note>', methods=['POST'])
def add_student_note(student_id,note):
    return StudentController.add_student_note(student_id,note)

@app.route('/remove_student_note/<int:student_id>', methods=['POST'])
def remove_student_note(student_id):
    return StudentController.remove_student_note(student_id)

@app.route('/list_student_notes/<int:student_id>', methods=['GET'])
def list_student_notes(student_id):
    return StudentController.list_student_notes(student_id)

@app.route('/assign_student_advisor/<int:student_id>/<int:teacher_id>', methods=['POST'])
def assign_student_advisor(student_id,teacher_id):
    return StudentController.assign_student_advisor(student_id,teacher_id)

@app.route('/remove_student_advisor/<int:student_id>', methods=['POST'])
def remove_student_advisor(student_id):
    return StudentController.remove_student_advisor(student_id)

@app.route('/get_student_advisor/<int:student_id>', methods=['GET'])
def get_student_advisor(student_id):
    return StudentController.get_student_advisor(student_id)

@app.route('/update_student_contact/<int:student_id>/<string:contact>', methods=['POST'])
def update_student_contact(student_id,contact):
    return StudentController.update_student_contact(student_id,contact)

@app.route('/list_students_by_course/<int:course_id>',methods=['GET'])
def list_students_by_course(course_id):
    return StudentController.list_students_by_course(course_id)

@app.route('/get_student_status/<int:student_id>',methods=['GET'])
def get_student_status(student_id):
    return StudentController.get_student_status(student_id)

@app.route('/change_student_status/<int:student_id>/<string:status>',methods=['POST'])
def change_student_status(student_id,status):
    return StudentController.change_student_status(student_id,status)

if __name__ == "__main__":
    app.run(debug=True)