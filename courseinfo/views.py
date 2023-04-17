from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .utils import PageLinksMixin
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from courseinfo.forms import InstructorForm, SectionForm, CourseForm, SemesterForm, StudentForm, RegistrationForm
from courseinfo.models import (
    Instructor,
    Section,
    Course,
    Semester,
    Student,
    Registration,
)


class InstructorList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 25
    model = Instructor


class InstructorDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Instructor
    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        instructor = self.get_object()
        section_list = instructor.sections.all()
        context['section_list'] = section_list
        return context


class InstructorCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = InstructorForm
    model = Instructor


class InstructorUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = InstructorForm
    model = Instructor
    template_name = 'courseinfo/instructor_form_update.html'


class InstructorDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Instructor
    success_url = reverse_lazy('courseinfo_instructor_list_urlpattern')

    def get(self, request, pk):
        instructor = get_object_or_404(Instructor, pk=pk)
        sections = instructor.sections.all()
        if sections.count() > 0:
            return render(
                request,
                'courseinfo/instructor_refuse_delete.html',
                {'instructor': instructor,
                 'sections': sections,
                 }
            )
        else:
            return render(
                request,
                'courseinfo/instructor_confirm_delete.html',
                {'instructor': instructor}
            )


class SectionList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Section


class SectionDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Section
    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        section = self.get_object()
        semester = section.semester
        course = section.course
        instructor = section.instructor
        registration_list = section.registrations.all()
        context['semester'] = semester
        context['course'] = course
        context['instructor'] = instructor
        context['registration_list'] = registration_list
        return context


class SectionCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = SectionForm
    model = Section


class SectionUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = SectionForm
    model = Section
    template_name = 'courseinfo/section_form_update.html'


class SectionDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Section
    success_url = reverse_lazy('courseinfo_section_list_urlpattern')

    def get(self, request, pk):
        section = get_object_or_404(Section, pk=pk)
        registrations = section.registrations.all()
        if registrations.count() > 0:
            return render(
                request,
                'courseinfo/section_refuse_delete.html',
                {'section': section,
                 'registrations': registrations,
                 }
            )
        else:
            return render(
                request,
                'courseinfo/section_confirm_delete.html',
                {'section': section}
            )


class CourseList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Course


class CourseDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Course
    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        course = self.get_object()
        section_list = course.sections.all()
        context['section_list'] = section_list
        return context


class CourseCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = CourseForm
    model = Course


class CourseUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = CourseForm
    model = Course
    template_name = 'courseinfo/course_form_update.html'


class CourseDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Course
    success_url = reverse_lazy('courseinfo_course_list_urlpattern')

    def get(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        sections = course.sections.all()
        if sections.count() > 0:
            return render(
                request,
                'courseinfo/course_refuse_delete.html',
                {'course': course,
                 'sections': sections,
                 }
            )
        else:
            return render(
                request,
                'courseinfo/course_confirm_delete.html',
                {'course': course}
            )


class SemesterList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Semester


class SemesterDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Semester
    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        semester = self.get_object()
        section_list = semester.sections.all()
        context['section_list'] = section_list
        return context


class SemesterCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = SemesterForm
    model = Semester


class SemesterUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = SemesterForm
    model = Semester
    template_name = 'courseinfo/semester_form_update.html'


class SemesterDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Semester
    success_url = reverse_lazy('courseinfo_semester_list_urlpattern')

    def get(self, request, pk):
        semester = get_object_or_404(Semester, pk=pk)
        sections = semester.sections.all()
        if sections.count() > 0:
            return render(
                request,
                'courseinfo/semester_refuse_delete.html',
                {'semester': semester,
                 'sections': sections,
                 }
            )
        else:
            return render(
                request,
                'courseinfo/semester_confirm_delete.html',
                {'semester': semester}
            )


class StudentList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 25
    model = Student


class StudentDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Student
    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        student = self.get_object()
        registration_list = student.registrations.all()
        context['registration_list'] = registration_list
        return context


class StudentCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = StudentForm
    model = Student


class StudentUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = StudentForm
    model = Student
    template_name = 'courseinfo/student_form_update.html'


class StudentDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Student
    success_url = reverse_lazy('courseinfo_student_list_urlpattern')

    def get(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        registrations = student.registrations.all()
        if registrations.count() > 0:
            return render(
                request,
                'courseinfo/student_refuse_delete.html',
                {'student': student,
                 'registrations': registrations,
                 }
            )
        else:
            return render(
                request,
                'courseinfo/student_confirm_delete.html',
                {'student': student}
            )


class RegistrationList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Registration


class RegistrationDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Registration
    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        return context


class RegistrationCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = RegistrationForm
    model = Registration


class RegistrationUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = RegistrationForm
    model = Registration
    template_name = 'courseinfo/registration_form_update.html'


class RegistrationDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Registration
    success_url = reverse_lazy('courseinfo_registration_list_urlpattern')
