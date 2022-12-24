from django.contrib import admin
from coursetable.models import CourseTable
class CourseTableAdmin(admin.ModelAdmin):
    list_display = ('course_code', 'course_title', 'course_core_elective', 'course_marks', 'course_owner', 'course_reviewer', 'course_mode', 'course_instructor')

admin.site.register(CourseTable, CourseTableAdmin)

# Register your models here.
