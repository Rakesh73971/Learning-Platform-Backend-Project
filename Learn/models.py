from datetime import timezone
from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,db_column='user_id')
    age = models.PositiveSmallIntegerField(validators=
            [MinValueValidator(15),MaxValueValidator(50)])
    birth_date = models.DateField(null=True,blank=True)
    education = models.CharField(max_length=255,null=True,blank=True)
    phone = models.CharField(max_length=15,unique=True)

    def __str__(self):
        return f"{self.user.username} ({self.age} yrs)"
    
class Teacher(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    qualification = models.TextField()
    experience = models.PositiveSmallIntegerField(help_text='Experience in years')
    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Course(models.Model):
    name = models.CharField(max_length=255)
    fee = models.PositiveBigIntegerField()
    duration_months = models.PositiveSmallIntegerField(default=6)
    vacancies = models.PositiveSmallIntegerField()
    teachers = models.ManyToManyField(Teacher,related_name='courses',blank=True)

    class Meta:
        permissions = [
            ("enroll_course", "Can enroll in a course"),
            ("review_course", "Can review a course"),
        ]


    def __str__(self):
        return self.name
    
class CourseInfo(models.Model):
    course = models.OneToOneField(Course,on_delete=models.CASCADE,related_name='info')
    prerequests = models.TextField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Info for {self.course.name}"

    
class Curriculum(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='curriculum')
    name = models.TextField()
    def __str__(self):
        return f"{self.name} ({self.course.name})"

class Enrollment(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name='enrollments')
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='enrollments')
    enrolled_on = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('student','course')

    def __str__(self):
        return f"{self.student.user.username} enrolled in {self.course.name}"



class Progress(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name='progress')
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='progress')
    progress_per = models.PositiveSmallIntegerField(validators=[
        MinValueValidator(0),MaxValueValidator(100)
    ],help_text='Progress percentage (0-100)')

    class Meta:
        unique_together = ('student','course')

    def __str__(self):
        return f"{self.student.user.username} - {self.course.name}: {self.progress_per}%"


class CourseReview(models.Model):
    student = models.ForeignKey(Student,on_delete=models.PROTECT,related_name='course_reviews')
    course = models.ForeignKey(Course,on_delete=models.PROTECT,related_name='reviews')
    review = models.TextField(blank=True)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1),MaxValueValidator(5)]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.course.name} review by {self.student.user.username}"


class PlatformReview(models.Model):
    student = models.ForeignKey(Student,on_delete=models.PROTECT,related_name='platform_reviews')
    review = models.TextField(blank=True)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1),MaxValueValidator(5)]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Platform review by {self.student.user.username}"
