from django.db import models
from django.contrib.auth.hashers import make_password

class Department(models.Model):
    department_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.department_name  # Fixed

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=20)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.course_code} - {self.course_name}"  # Fixed

class Person(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    profile_pic = models.CharField(max_length=200, blank=True)
    email = models.EmailField()
    password = models.CharField(max_length=128)  # Changed to CharField
    role = models.CharField(max_length=100)  # Will be overridden in subclasses

    class Meta:
        abstract = True

class Student(Person):
    student_id = models.AutoField(primary_key=True)
    courses = models.ManyToManyField(Course)
    year_of_study = models.CharField(max_length=10)
    semester = models.CharField(max_length=20)
    role = models.CharField(max_length=100, default='Student')  # Auto-set role

    def __str__(self):
        return self.full_name

class Lecturer(Person):
    lecturer_id = models.AutoField(primary_key=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    college = models.CharField(max_length=50)
    office = models.CharField(max_length=50)
    role = models.CharField(max_length=100, default='Lecturer')  # Auto-set role

    def __str__(self):
        return self.full_name

class CollegeRegistrar(Person):
    registrar_id = models.AutoField(primary_key=True)
    college = models.CharField(max_length=50)
    office = models.CharField(max_length=50)
    role = models.CharField(max_length=100, default='Registrar')  # Auto-set role

    def __str__(self):
        return f"Registrar {self.full_name}"

class Issue(models.Model):
    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('IN_PROGRESS', 'In Progress'),
        ('RESOLVED', 'Resolved'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    issue_category = models.CharField(max_length=50)
    issue_description = models.TextField()
    issue_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='OPEN')
    assigned_lecturer = models.ForeignKey(Lecturer, on_delete=models.SET_NULL, null=True, blank=True)
    registrar_receiving = models.ForeignKey(CollegeRegistrar, on_delete=models.SET_NULL, null=True, blank=True)
    attachment = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Issue by {self.student.full_name}"  # Fixed

    class Meta:
        ordering = ['-created_at']