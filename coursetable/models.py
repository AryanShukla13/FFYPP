from django.db import models
class CourseTable(models.Model):
    course_code = models.CharField(max_length= 7)
    course_title = models.CharField(max_length= 50)
    course_core_elective = models.CharField(max_length= 10)
    course_marks = models.IntegerField()
    course_owner = models.CharField(max_length= 40)
    course_reviewer = models.CharField(max_length= 40)
    course_mode = models.CharField(max_length= 10)
    course_instructor = models.CharField(max_length= 40)
    
    def __str__(self):
        return self.course_title
# Create your models here.
