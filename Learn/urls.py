from django.urls import path
from rest_framework_nested import routers
from . import views
router = routers.DefaultRouter()
router.register('students',views.StudentViewSet)
router.register('teachers',views.TeacherViewSet)
router.register('courses',views.CourseViewSet)
router.register('enrollments',views.EnrollmentViewSet)
router.register('reviews',views.PlatformReviewViewSet)

courses_router = routers.NestedDefaultRouter(router,'courses',lookup='course')
courses_router.register('info',views.CourseInfoViewSet,basename='info')
courses_router.register('curriculum',views.CurriculumViewSet,basename='curriculum')
courses_router.register('reviews',views.CourseReviewViewSet,basename='reviews')

student_router=routers.NestedDefaultRouter(router,'students',lookup='students')
student_router.register('progress',views.ProgressViewSet,basename='progress')


urlpatterns = router.urls + courses_router.urls + student_router.urls