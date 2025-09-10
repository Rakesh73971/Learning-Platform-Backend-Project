from .models import Student,Teacher,Course,CourseInfo,Curriculum,Enrollment,Progress,PlatformReview,CourseReview
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','user','birth_date','age','education','phone']


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id','first_name','last_name','qualification','experience']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id','name','fee','duration_months','vacancies','teachers']

class CourseInfoSerializer(serializers.ModelSerializer):
    course_name = serializers.SerializerMethodField()
    class Meta:
        model = CourseInfo
        fields = ['id','course_name','prerequests','description']

    def get_course_name(self,obj):
        return obj.course.name
    
    def create(self,validated_data):
        course_id = self.context['course_id']
        return CourseInfo.objects.create(course_id=course_id,**validated_data)
        
class CurriculumSerializer(serializers.ModelSerializer):
    course_name = serializers.SerializerMethodField()
    class Meta:
        model = Curriculum
        fields = ['id','course_name','name']

    def get_course_name(self,obj):
        return obj.course.name
    
    def create(self, validated_data):
        course_id = self.context['course_id']
        return Curriculum.objects.create(course_id=course_id,**validated_data)
    


class EnrollmentSerializer(serializers.ModelSerializer):
    course_name = serializers.SerializerMethodField()

    class Meta:
        model = Enrollment
        fields = ['id','student','course_name','enrolled_on']

    def get_course_name(self,obj):
        return obj.course.name

class ProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = ['id','course','progress_per']

class CourseReviewSerializer(serializers.ModelSerializer):
    course_name = serializers.SerializerMethodField()
    class Meta:
        model = CourseReview
        fields = ['id','student','course_name','review','rating','created_at']

    def get_course_name(self,obj):
        return obj.course.name
    
    def create(self,validated_data):
        course_id = self.context['course_id']
        return CourseReview.objects.create(course_id=course_id,**validated_data)

class PlatformReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatformReview
        fields = ['id','student','review','rating','created_at']
