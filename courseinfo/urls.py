"""wu_meg_ezu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from courseinfo.views import (
    InstructorList,
    SectionList,
    CourseList,
    SemesterList,
    StudentList,
    RegistrationList,
)

urlpatterns = [
    path('instructor/',
         InstructorList.as_view(),
         name='courseinfo_instructor_list_urlpattern'),
    path('section/',
         SectionList.as_view(),
         name='courseinfo_section_list_urlpattern'),
    path('course/',
         CourseList.as_view(),
         name='courseinfo_course_list_urlpattern'),
    path('semester/',
         SemesterList.as_view(),
         name='courseinfo_semester_list_urlpattern'),
    path('student/',
         StudentList.as_view(),
         name='courseinfo_student_list_urlpattern'),
    path('registration/',
         RegistrationList.as_view(),
         name='courseinfo_registration_list_urlpattern'),
]
