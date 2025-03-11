from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Department, Course, Student, Lecturer, CollegeRegistrar, Issue

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['student_id', 'full_name', 'gender', 'profile_pic', 'email', 
                  'password', 'courses', 'year_of_study', 'semester']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        return super().update(instance, validated_data)

class LecturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecturer
        fields = ['lecturer_id', 'full_name', 'gender', 'profile_pic', 'email', 
                  'password', 'department', 'college', 'office']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        return super().update(instance, validated_data)

class CollegeRegistrarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollegeRegistrar
        fields = ['registrar_id', 'full_name', 'gender', 'profile_pic', 'email', 
                  'password', 'college', 'office']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        return super().update(instance, validated_data)

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = '__all__'

# serializers.py (additional serializers)
class StudentIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        exclude = ['student']  # Student is auto-set from URL

class CourseIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        exclude = ['course']  # Course is auto-set from URL

class DepartmentCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        exclude = ['department']  # Department is auto-set from URL        