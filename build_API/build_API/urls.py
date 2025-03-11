"""
URL configuration for build_API project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apis import views 
from apis.views import (
    StudentIssuesList, StudentIssuesDetail,
    CourseIssuesList, CourseIssuesDetail,
    DepartmentCoursesList, DepartmentCoursesDetail
)

router = DefaultRouter()
router.register(r'departments', views.DepartmentViewSet)
router.register(r'courses', views.CourseViewSet)
router.register(r'students', views.StudentViewSet)
router.register(r'lecturers', views.LecturerViewSet)
router.register(r'registrars', views.CollegeRegistrarViewSet)
router.register(r'issues', views.IssueViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
        # Student nested routes
    path('students/<int:student_pk>/issues/', StudentIssuesList.as_view(), name='student-issues-list'),
    path('students/<int:student_pk>/issues/<int:pk>/', StudentIssuesDetail.as_view(), name='student-issues-detail'),
    
    # Course nested routes
    path('courses/<int:course_pk>/issues/', CourseIssuesList.as_view(), name='course-issues-list'),
    path('courses/<int:course_pk>/issues/<int:pk>/', CourseIssuesDetail.as_view(), name='course-issues-detail'),
    
    # Department nested routes
    path('departments/<int:department_pk>/courses/', DepartmentCoursesList.as_view(), name='department-courses-list'),
    path('departments/<int:department_pk>/courses/<int:pk>/', DepartmentCoursesDetail.as_view(), name='department-courses-detail'),
    
    # Include existing router URLs
    path('', include(router.urls)),
]
