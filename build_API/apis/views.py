from django.shortcuts import render

from rest_framework import viewsets
from .models import (
    Department, Course, Student, Lecturer, CollegeRegistrar, Issue
)
from .serializers import (
    DepartmentSerializer, CourseSerializer, StudentSerializer,
    LecturerSerializer, CollegeRegistrarSerializer, IssueSerializer
)
# views.py (additional views)
from rest_framework import generics
from django.shortcuts import get_object_or_404
from .serializers import *

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class LecturerViewSet(viewsets.ModelViewSet):
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer

class CollegeRegistrarViewSet(viewsets.ModelViewSet):
    queryset = CollegeRegistrar.objects.all()
    serializer_class = CollegeRegistrarSerializer

class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer



# Nested: Student -> Issues
class StudentIssuesList(generics.ListCreateAPIView):
    serializer_class = StudentIssueSerializer  # Uses custom serializer

    def get_queryset(self):
        student_pk = self.kwargs['student_pk']
        return Issue.objects.filter(student_id=student_pk)

    def perform_create(self, serializer):
        student = get_object_or_404(Student, pk=self.kwargs['student_pk'])
        serializer.save(student=student)

class StudentIssuesDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentIssueSerializer

    def get_queryset(self):
        student_pk = self.kwargs['student_pk']
        return Issue.objects.filter(student_id=student_pk)

# Nested: Course -> Issues
class CourseIssuesList(generics.ListCreateAPIView):
    serializer_class = CourseIssueSerializer  # Uses custom serializer

    def get_queryset(self):
        course_pk = self.kwargs['course_pk']
        return Issue.objects.filter(course_id=course_pk)

    def perform_create(self, serializer):
        course = get_object_or_404(Course, pk=self.kwargs['course_pk'])
        serializer.save(course=course)

class CourseIssuesDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CourseIssueSerializer

    def get_queryset(self):
        course_pk = self.kwargs['course_pk']
        return Issue.objects.filter(course_id=course_pk)

# Nested: Department -> Courses
class DepartmentCoursesList(generics.ListCreateAPIView):
    serializer_class = DepartmentCourseSerializer  # Uses custom serializer

    def get_queryset(self):
        department_pk = self.kwargs['department_pk']
        return Course.objects.filter(department_id=department_pk)

    def perform_create(self, serializer):
        department = get_object_or_404(Department, pk=self.kwargs['department_pk'])
        serializer.save(department=department)

class DepartmentCoursesDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DepartmentCourseSerializer

    def get_queryset(self):
        department_pk = self.kwargs['department_pk']
        return Course.objects.filter(department_id=department_pk)    