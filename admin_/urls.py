from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('accounts/login/staff/', views.teacher_login, name="staff-login"),
    path('accounts/login/admin/', views.admin_login, name="admin-login"),
    path('accounts/logout/admin/', views.logoutAdmin, name="admin-logout"),
    path('accounts/logout/staff/', views.logoutStaff, name="staff-logout"),
    path('accounts/staff-home/', views.staff_home, name="staff-home"),
    path('accounts/school-details/', views.school_details, name="school-details"),
    path('accounts/school-details/your-school/<int:id>/', views.school_details, name="school-detailsn"),
    path('accounts/school-details/<int:id>/', views.school_details, name="school-update"),
    path('accounts/teacher-details/', views.teachers_details, name="teachers-details"),
    path('accounts/teacher/<int:id>/', views.teacher_details_signup, name="teacher-update"),
    path('accounts/admin-home/', views.admin_home, name="admin-home"),
    path('accounts/signup/', views.signup, name="signup"),
    path('accounts/exam/', views.exam, name="exam"),
    path('accounts/teacher-details-signup/', views.teacher_details_signup, name="teacher-details-signup"),

    path('reset_password/',
        auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
        name="reset_password"),
    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), 
        name="password_reset_done"),
    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), 
        name="password_reset_confirm"),
    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), 
        name="password_reset_complete"),

    path('', views.home, name="home"),
    path('main_nav', views.main_nav),
    path('about_us', views.about_us),
    path('disclaimer', views.disclaimer),
    path('contact_us', views.contactus),
    path('test', views.test),


    path('accounts/mail/', views.inbox, name="inbox"),
    path('accounts/mail/<int:id>/', views.delete, name="delete_mail"),

    path('accounts/admin/exam/<int:id>/', views.exam, name="edit-exam"),
    path('accounts/admin/exam/active/<int:id>/', views.make_active, name="make_active"),
    path('accounts/admin/exam/disable/<int:id>/', views.make_disable, name="make_disable"),

    path('accounts/staff/create-exam/', views.exam_paper, name="create-paper"),
    path('accounts/staff-home/question-paper-details/', views.question_paper_details, name="question-paper-details"),
    path('accounts/staff-home/question-paper-details/<str:exam_subject_id>/<int:id>', views.question_paper_update, name="question-paper-update"),

    path("dashboard/", views.dashboard, name="dashboard"),

    path("SessionEnd/", views.sessionEndResponse, name="sessionEnd"),
]

