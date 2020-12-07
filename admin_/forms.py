from django import forms
from . models import (Teacher_details, School_details, contact_us, Exam_details, Exam_class, Exam_paper_subject_details, 
Exam_question_paper_questions)
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

#Module for staff Signup Page
class StaffForm(forms.ModelForm):
    class Meta:
        model = Teacher_details
        fields = ('username', 'school_id', 'image', 'name', 'email', 'mobile_no', 'qualification', 'experience', 'country',
        'state', 'city', 'address', 'pincode', 'status')
        labels = {
            'username': 'Username',
            'school_id': 'School ID',
            'image': 'Uplaod Profile Photo',
            'name': 'Name',
            'email': 'Email',
            'mobile_no': 'Mobile No.',
            'qualification': 'Qualification',
            'experience': 'Experience',
            'country': 'Country',
            'state': 'State',
            'city': 'City',
            'address': 'Address',
            'pincode': 'Pincode',
            'status': 'Status',
        }
    #Function to give combobox select text
    def __init__(self, *args, **kwargs):
        super(StaffForm, self).__init__(*args, **kwargs)
        self.fields['school_id'].empty_label = 'Select'
        self.fields['country'].empty_label = 'Select'
        self.fields['state'].empty_label = 'Select'
        self.fields['city'].empty_label = 'Select'
        self.fields['status'].empty_label = 'Select'

#Module for edit school details form
class AdminForm(forms.ModelForm):
    class Meta:
        model = School_details
        fields = ('username', 'logo', 'name', 'email', 'contact_person_name', 'contact_person_mobile_no', 'office_mobile_no', 'country',
        'state', 'city', 'pincode', 'address', 'status')
        labels = {
            'username': 'Username',
            'logo': 'School Logo',
            'name': 'School Name',
            'email': 'Email',
            'contact_person_name': 'Principal Name',
            'contact_person_mobile_no': 'Principal Mobile No.',
            'office_mobile_no': 'Office Mobile No.',
            'country': 'Country',
            'state': 'State',
            'city': 'city',
            'pincode': 'Pincode',
            'address': 'Address',
            'status': 'Status',
         }
    #Function to give combobox select text
    def __init__(self, *args, **kwargs):
        super(AdminForm, self).__init__(*args, **kwargs)
        self.fields['country'].empty_label = 'Select'
        self.fields['state'].empty_label = 'Select'
        self.fields['city'].empty_label = 'Select'
        self.fields['status'].empty_label = 'Select'

class contactus_form(forms.ModelForm):
    class Meta:
        model = contact_us
        fields = "__all__"

class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam_details
        fields = ('exam_name', 'academic_term_id')
        labels = {
            'exam_name': 'Enter exam name',
        }
    #Function to give combobox select text
    def __init__(self, *args, **kwargs):
        super(ExamForm, self).__init__(*args, **kwargs)
        self.fields['academic_term_id'].empty_label = 'Select'

class ExamClassForm(forms.ModelForm):
    class Meta:
        model = Exam_class
        fields = ('exam_id', 'group_class_id')
        labels = {
            'group_class_id': 'Select standards for exam',
            'exam_id': 'Select exam',
        }
    #Function to give combobox select text
    def __init__(self, *args, **kwargs):
        super(ExamClassForm, self).__init__(*args, **kwargs)
        self.fields['exam_id'].empty_label = 'Select'


class CreateExamForm(forms.ModelForm):
    class Meta:
        model = Exam_paper_subject_details
        fields = ('uniquo', 'exam_id', 'creator', 'exam_date', 'exam_time', 'exam_duration', 'total_marks')
        labels = {
            'exam_id': 'Select exam',
            'creator': 'Who are you',
            'exam_date': 'Select exam date',
            'exam_time': 'Select exam time',
            'exam_duration': 'Select exam duration',
            'total_marks': 'Select total marks',
        }
    #Function to give combobox select text
    def __init__(self, *args, **kwargs):
        super(CreateExamForm, self).__init__(*args, **kwargs)
        self.fields['exam_id'].empty_label = 'Select'
        self.fields['exam_date'].widget.attrs['placeholder'] = 'yyyy-mm-dd'
        self.fields['exam_time'].widget.attrs['placeholder'] = 'hh:mm:ss.000000'
        self.fields['exam_duration'].widget.attrs['placeholder'] = 'in Hr'
        self.fields['total_marks'].widget.attrs['placeholder'] = '1hr/3hr'
        self.fields['uniquo'].widget.attrs['placeholder'] = 'Enter unique id to link the questions to paper'

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Exam_question_paper_questions
        fields = ('exam_subject_id', 'question', 'question_mark', 'answer')
        labels = {
            'exam_subject_id': 'Select exam subject',
            'question': 'Write question',
            'question_mark': 'Question marks',
            'answer': 'Write answer',
        }