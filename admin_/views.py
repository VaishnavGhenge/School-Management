from django.shortcuts import render, redirect
from . forms import (StaffForm, AdminForm, CreateUserForm, contactus_form, ExamForm, ExamClassForm,
 CreateExamForm, QuestionForm)
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group
from . models import Teacher_details, School_details, contact_us, Exam_details, Variables, Exam_question_paper_questions
from django.core.mail import send_mail 
from django.core.mail import EmailMultiAlternatives 
from django.template.loader import get_template 
from django.template import Context
from django.http import HttpResponse
from django.forms import modelformset_factory

#Accounts
##########################################################################################################################
#staff-login
@unauthenticated_user
def teacher_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('staff-home')
        else:
            messages.info(request, 'username or password is incorrect')

    context = {}
    return render(request, 'admin panel/teachers/teacher_login.html', context)


#admin-login
@unauthenticated_user
def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('admin-home')
        else:
            messages.info(request, 'username or password is incorrect')

    context = {}
    return render(request, 'admin panel/admin/admin_login.html', context)

#staff-signup
@login_required(login_url='admin-login')
@admin_only
def signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():

            user = form.save()
            group = Group.objects.get(name='teachers')
            user.groups.add(group)

            username = form.cleaned_data.get('username')
            messages.success(request, 'Account is created for '+username)
            return redirect('signup')

    context = {'form': form}
    return render(request, 'signup.html', context)

#admin-Logout
@login_required(login_url='staff-login')
def logoutAdmin(request):
    logout(request)
    return redirect('admin-login')

#staff-Logout
@login_required(login_url='staff-login')
def logoutStaff(request):
    logout(request)
    return redirect('staff-login')

#home contents
####################################################################################################################
@login_required(login_url='staff-login')
@allowed_users(allowed_roles=['admin'])
@admin_only
def teacher_details_signup(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = StaffForm()
        else:
            teacher = Teacher_details.objects.get(pk=id)
            form = StaffForm(instance=teacher)
        return render(request, 'admin panel/teachers/teacher_details_signup.html', {'form': form})
    else:
        if id == 0:
            form = StaffForm(request.POST, request.FILES)       
            messages.error(request, form.errors)
            if form.is_valid():            
                form.save()
                username = form.cleaned_data.get('username')
                email = form.cleaned_data.get('email')
                school = form.cleaned_data.get('school_id')
                password = form.cleaned_data.get('password')
                ############ mail system ##############################################
                htmly = get_template('Email.html') 
                d = { 'username': username, 'school': school, 'password': password } 
                subject, from_email, to = 'Welcome', 'gpaonline9@gmail.com', email 
                html_content = htmly.render(d) 
                msg = EmailMultiAlternatives(subject, html_content, from_email, [to]) 
                msg.attach_alternative(html_content, "text / html") 
                msg.send()
                ######################################################################## 
                messages.success(request, 'Registered successfully!')
                return redirect('signup')
            else:
                messages.error(request, 'Please check Entered information!')
                form = StaffForm()
        else:
            teacher = Teacher_details.objects.get(pk=id)
            form = StaffForm(request.POST, instance=teacher)
            messages.success(request, 'Details updated successfully')

    return render(request, 'admin panel/teachers/teacher_details_signup.html', {'form': form})

#Admin-Edit School Details
@login_required(login_url='admin-login')
@allowed_users(allowed_roles=['admin'])
@admin_only
def school_details(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = AdminForm()
        else:
            school = School_details.objects.get(pk=id)
            form = AdminForm(instance=school)
        return render(request, 'edit_school_details.html', {'form': form})
    else:
        if id == 0:
            form = AdminForm(request.POST, request.FILES)
            messages.error(request, form.errors)
            #print(form.errors)
            if form.is_valid():            
                form.save()
                username = form.cleaned_data.get('username') 
                email = form.cleaned_data.get('email')
                name = form.cleaned_data.get('name')
                ############ mail system ##############################################
                htmly = get_template('EmailAdmin.html') 
                d = { 'username': username , 'name': name} 
                subject, from_email, to = 'Welcome', 'gpaonline9@gmail.com', email 
                html_content = htmly.render(d) 
                msg = EmailMultiAlternatives(subject, html_content, from_email, [to]) 
                msg.attach_alternative(html_content, "text / html") 
                msg.send()
                ########################################################################
                messages.success(request, 'Registered successfully!')
                return redirect('school-details')
            else:
                messages.error(request, 'Please check Entered information!')
                form = AdminForm()
        else:
            school = School_details.objects.get(pk=id)
            form = AdminForm(request.POST,request.FILES, instance=school)
            if form.is_valid():
                form.save()
                messages.success(request, 'Details updated successfully')
            else:
                messages.error(request, form.errors)

    return render(request, 'edit_school_details.html', {'form': form})

#admin-home
@login_required(login_url='admin-login')
@allowed_users(allowed_roles=['admin'])
@admin_only
def admin_home(request):
    context = {
        'school': School_details.objects.all(),
    }
    return render(request, 'admin panel/dashboard/dashboard.html', context)




#Staff-Home
@login_required(login_url='staff-login')
@allowed_users(allowed_roles=["teachers"])
def staff_home(request):
    active_exams = Exam_details.objects.filter(status=1)
    return render(request, 'admin panel/teachers/teacher_home.html', {'active_exams': active_exams})

@login_required(login_url="admin-login")
@allowed_users(allowed_roles=["admin"])
@admin_only
#admin-edit_exam
def exam(request, id=0):
    if request.method == 'GET':
        form2 = ExamClassForm()
        if id == 0:
            form1 = ExamForm()
        else:
            exam = Exam_details.objects.get(pk=id)
            form1 = ExamForm(instance=exam)
        context = {
            'form1': form1,
            'form2': form2,
            'exam_list': Exam_details.objects.all(),
        }  
        return render(request, 'admin panel/exams/create_exam.html', context)
    else:
        form2 = ExamClassForm()
        form1 = ExamForm()
        if id == 0:
            if 'create' in request.POST:
                form = ExamForm(request.POST)
            elif 'add' in request.POST:
                form = ExamClassForm(request.POST)

            messages.error(request, form.errors)
            if form.is_valid():
                form.save()
                if 'create' in request.POST:
                    messages.success(request, 'Exam creation successfull')
                elif 'add' in request.POST:
                    messages.success(request, 'Standards added successfully')
            else:
                form2 = ExamClassForm()
                form1 = ExamForm()
                messages.error(request, 'Please enter valid information')
        else:
            exam = Exam_details.objects.get(pk=id)
            form1 = ExamForm(request.POST, instance=exam)
            messages.success(request, 'Exam updated successfully')

    context = {
        'form1': form1,
        'form2': form2,
        'exam_list': Exam_details.objects.all(),
    }
    return render(request, 'admin panel/exams/create_exam.html', context)

#admin-staff_list
@login_required(login_url="admin-login")
@allowed_users(allowed_roles=['admin'])
@admin_only
def teachers_details(request):
    context = {
        'teachers_details': Teacher_details.objects.all(),
    }
    return render(request, 'admin panel/teachers/teachers_details.html', context)

#admin-inbox for contact us messages
@login_required(login_url="admin-login")
@allowed_users(allowed_roles=["admin"])
@admin_only
def inbox(request):
    context = {
        'mails': contact_us.objects.all(),
        'schools': School_details.objects.all(),
    }
    return render(request, 'admin panel/inbox/inbox.html', context)

@login_required(login_url="admin-login")
@allowed_users(allowed_roles=["admin"])
@admin_only
#admin-delete message in inbox
def delete(request, id):
    mail = contact_us.objects.get(pk=id)
    mail.delete()
    return redirect('inbox')

@login_required(login_url="admin-login")
@allowed_users(allowed_roles=["admin"])
@admin_only
#admin-to make exam active in status
def make_active(request, id):
    Exam_details.objects.filter(id=id).update(status=1)
    return redirect('exam')

@login_required(login_url="admin-login")
@allowed_users(allowed_roles=["admin"])
@admin_only
#admin-to make exam disable in status
def make_disable(request, id):
    Exam_details.objects.filter(id=id).update(status=2)
    return redirect('exam')


#home
#################################################################################################################
def home(request):
    return render(request,'main site/home_page.html')

def main_nav(request):
    return render(request,'main site/main_nav.html')

def about_us(request):
    return render(request,'main site/about_us.html')

def disclaimer(request):
    return render(request,'main site/disclaimer.html')

def test(request):
    return render(request,'main site/test.html')

def contactus(request):
    form = contactus_form()
    if request.method == "POST":
        form = contactus_form(request.POST)
        messages.error(request, form.errors)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form submission successful')
            form = contactus_form()
            return render(request, "main site/test.html", {'form': form})

        else:
            return render(request, "main site/contact_us.html", {'form': form})
    else:
        form = contactus_form()
        return render(request, "main site/contact_us.html", {'form': form})

##################################################################################################################
#exam paper creation
@login_required(login_url='staff-login')
@allowed_users(allowed_roles=["teachers"])
def exam_paper(request):
    fi = 0
    obj = Variables.objects.get(pk=1)
    count = obj.count
    #print("count= ",count)

    form = CreateExamForm(initial={'creator': request.user,})
    QueFormset = modelformset_factory(Exam_question_paper_questions, fields=('exam_subject_id', 'question', 'question_mark', 'answer'), extra=0, 
    labels = {'exam_subject_id': 'Select exam subject', 'question': 'Write question','question_mark': 'Question marks', 'answer': 'Write answer'})

    formset = QueFormset(queryset=Exam_question_paper_questions.objects.none())
    if request.method == 'POST':
        if 'paper' in  request.POST:
            form = CreateExamForm(request.POST)
            messages.error(request, form.errors)
            if form.is_valid():
                form.save()
                uniquo = form.cleaned_data.get('uniquo')
                Variables.objects.filter(id=1).update(uniquo=uniquo)
                #print("uniquo= ",uniquo)
                marks = form.cleaned_data.get('total_marks')
                if marks == 70:
                    Variables.objects.filter(id=1).update(count=35)

                    QueFormset = modelformset_factory(Exam_question_paper_questions, fields=('exam_subject_id', 'question', 'question_mark', 'answer'), extra=35, 
                    labels = {'exam_subject_id': 'Select exam subject', 'question': 'Write question','question_mark': 'Question marks', 'answer': 'Write answer'})
                else:
                    Variables.objects.filter(id=1).update(count=10)

                    QueFormset = modelformset_factory(Exam_question_paper_questions, fields=('exam_subject_id', 'question', 'question_mark', 'answer'), extra=10, 
                    labels = {'exam_subject_id': 'Select exam subject', 'question': 'Write question','question_mark': 'Question marks', 'answer': 'Write answer'})

                formset = QueFormset(queryset=Exam_question_paper_questions.objects.none())
                fi = 1
                context = {
                    'formset': formset,
                    'fi': fi,
                }
                messages.success(request, 'Exam paper created successfully')
                return render(request, 'admin panel/exams/exam_paper.html', context)
            else:
                messages.success(request, 'Please enter valid information')
                form = CreateExamForm(initial={'creator': request.user,})

        if 'question' in request.POST:
            formset = QueFormset(request.POST)
            messages.error(request, formset.errors)
            if formset.is_valid():
               formset.save()
               Variables.objects.filter(id=1).update(uniquo="")
               Variables.objects.filter(id=1).update(count=0)
               messages.success(request, 'Submitted successfully')
               return redirect('staff-home')
            else:
                uniquo = obj.uniquo

                QueFormset = modelformset_factory(Exam_question_paper_questions, fields=('exam_subject_id', 'question', 'question_mark', 'answer'), extra=obj.count, 
                labels = {'exam_subject_id': 'Select exam subject', 'question': 'Write question','question_mark': 'Question marks', 'answer': 'Write answer'})
                formset = QueFormset(queryset=Exam_question_paper_questions.objects.none())

                messages.error(request, 'Please enter valid information')
                fi = 1
                context = {'formset': formset, 'fi': fi,}
                return render(request, 'admin panel/exams/exam_paper.html', context)
    
    context = {
        'form': form,
        'formset': formset,
        'fi': fi,
    }
    return render(request, 'admin panel/exams/exam_paper.html', context)

#to show list of questions
@login_required(login_url='staff-login')
@allowed_users(allowed_roles=["teachers"])
def question_paper_details(request):
    context = {
        'question_paper_details': Exam_question_paper_questions.objects.all(),
    }
    return render(request, 'admin panel/exams/question_paper_details.html', context)

#to updatethe individual question
@login_required(login_url='staff-login')
@allowed_users(allowed_roles=["teachers"])
def question_paper_update(request, exam_subject_id, id):
    if request.method == 'GET':
        question = Exam_question_paper_questions.objects.get(pk=id)
        form = QuestionForm(instance=question)
        return render(request, 'admin panel/exams/question_paper_update.html', {'form': form})
    else:
        question = Exam_question_paper_questions.objects.get(pk=id)
        form = QuestionForm(request.POST, instance=question)
        messages.success(request, 'Question updated successfully')
    return render(request, 'admin panel/exams/question_paper_update.html', {'form': form})

@unauthenticated_user
def sessionEndResponse(request):
    return HttpResponse('<h3>Session End</h3>')

@login_required(login_url='sessionError')
@allowed_users(allowed_roles=['teachers', 'admin'])
def dashboard(request):
    return render(request, "admin panel/dashboard/dashboard.html")
