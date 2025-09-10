from django.shortcuts import render
from .models import Student,Teacher,Course,CourseInfo,Curriculum,Enrollment,Progress,PlatformReview,CourseReview
from .serializers import StudentSerializer,TeacherSerializer,CourseSerializer,CourseInfoSerializer,CurriculumSerializer,EnrollmentSerializer,ProgressSerializer,PlatformReviewSerializer,CourseReviewSerializer
from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin,DestroyModelMixin,UpdateModelMixin
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import ModelViewSet,GenericViewSet
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsAdminOrReadOnly,IsAuthenticatedUser
from .filters import CourseFilter
# Create your views here.

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAdminOrReadOnly]


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_class = CourseFilter
    permission_classes = [IsAdminOrReadOnly]    
    

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_class = CourseFilter

    permission_classes = [IsAdminOrReadOnly]
    

class CourseInfoViewSet(ModelViewSet):
    serializer_class = CourseInfoSerializer

    def get_queryset(self):
        return CourseInfo.objects.filter(course_id=self.kwargs['course_pk'])

    def get_serializer_context(self):
        return {'course_id':self.kwargs['course_pk']}
    permission_classes = [IsAdminOrReadOnly]

    
class CurriculumViewSet(ModelViewSet):
    serializer_class = CurriculumSerializer
    def get_queryset(self):
        return Curriculum.objects.filter(course_id=self.kwargs['course_pk'])
    
    def get_serializer_context(self):
        return {'course_id':self.kwargs['course_pk']}
    permission_classes = [IsAdminOrReadOnly]

class EnrollmentViewSet(ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAdminOrReadOnly]

class ProgressViewSet(ModelViewSet):
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer
    permission_classes = [IsAuthenticatedUser]



class CourseReviewViewSet(ModelViewSet):
    serializer_class = CourseReviewSerializer

    def get_queryset(self):
        return CourseReview.objects.filter(course_id=self.kwargs['course_pk'])
    
    def get_serializer_context(self):
        return {'course_id':self.kwargs['course_pk']}
    
    http_method_names = ['get','post']


class PlatformReviewViewSet(ModelViewSet):
    queryset = PlatformReview.objects.all()
    serializer_class = PlatformReviewSerializer
    http_method_names = ['get','post']





    