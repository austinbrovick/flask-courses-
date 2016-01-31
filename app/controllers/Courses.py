
from system.core.controller import *

class Courses(Controller):
    def __init__(self, action):
        super(Courses, self).__init__(action)
        self.load_model('Course') #must load model before using it
    def index(self):
        print "******************** Made it to index **************"
        courses = self.models['Course'].get_all_courses()
        return self.load_view('index.html', courses = courses)
    def add(self):
        course_details = {
            'course': request.form['course'],
            'description': request.form['description']
        }
        self.models['Course'].add_course(course_details)
        print '************ Made it to add *******************'
        return redirect('/')
    def show(self, id):
        course = self.model['Course'].get_course_by_id(id)
        return self.load_view('show.html', course=course)
    def delete(self, id):
        print '************* Made it to Delete *************'

        course_that_will_be_deleted = self.models['Course'].get_course_by_id(id)
        # print course_that_will_be_deleted['id']
        # print course_that_will_be_deleted['title']
        return self.load_view('delete.html', course=course_that_will_be_deleted)
        # course = self.models['Course'].get_course_by_id(id)
        # print course
        # self.models['Course'].delete_course(id)
        # return redirect('/')
    def yes_delete(self, id):
        print "made it to yes delete"
        # course = self.models['Course'].get_course_by_id(id)
        self.models['Course'].delete_course(id)
        return redirect('/')



    def no_delete(self):
        return redirect('/')


