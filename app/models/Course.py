
from system.core.model import Model

class Course(Model):
    def __init__(self):
        super(Course, self).__init__()
    def get_all_courses(self):
        return self.db.query_db("SELECT * FROM courses")
    def get_course_by_id(self, course_id):
        print "******** Made it to get_course_by_id *******"
        query = "SELECT * FROM courses WHERE id = %s"
        data = [course_id]
        print "******** Made it to get_course_by_id after query and data *******"

        return self.db.query_db(query, data)
    def add_course(self, course):
        query = "INSERT INTO courses (title, description, created_at) VALUES (%s, %s, NOW())"
        data = [course['course'], course['description']] #data must be an array
        print '************ Made it to add_course *******************'

        return self.db.query_db(query, data)
    def update_course(self, course):
        query = "UPDATE courses SET title = %s, description = %s WHERE id = %s"
      # we need to pass the necessary data
        data = [course['title'], course['description'], course['id']]
      # run the update
        return self.db.query_db(query, data)
    def delete_course(self, course_id):
        print "made it to delete course"
        # print course['id']
        query = "DELETE FROM courses WHERE id = %s"
        data = [course_id]
        return self.db.query_db(query, data)
