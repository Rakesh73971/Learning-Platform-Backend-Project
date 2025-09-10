from django.contrib import admin
from . import models

@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['user','birth_date','education','age_status','phone']

    @admin.display(ordering="age")
    def age_status(self, customer):
        if customer.age < 18:
            return "Minor"
        return "Major"

@admin.register(models.Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','qualification','experience']
    list_display = ['qualification','experience']

@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name','fee','duration_months','vacancies']
    list_editable = ['fee','vacancies']
    search_fields = ['name']

@admin.register(models.CourseInfo)
class CourseInfoAdmin(admin.ModelAdmin):
    list_display = ['course','prerequests','description']
    autocomplete_fields = ['course']

@admin.register(models.Curriculum)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['course','name']
    autocomplete_fields = ['course']

@admin.register(models.Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['student','course','enrolled_on']
    autocomplete_fields = ['course']
    
@admin.register(models.Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ['student','course','progress_per']
    autocomplete_fields = ['course']

@admin.register(models.CourseReview)
class CourseReviewAdmin(admin.ModelAdmin):
    list_display = ['student','course','review','rating']
    list_editable = ['rating']
    autocomplete_fields = ['course']

@admin.register(models.PlatformReview)
class PlatformReviewAdmin(admin.ModelAdmin):
    list_display = ['student','review','rating']
    list_editable = ['rating']