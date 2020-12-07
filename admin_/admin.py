# accounts.admin.py

from django.contrib import admin
from . models import *


admin.site.register(School_details)
admin.site.register(School_terms)
admin.site.register(Teacher_details)
admin.site.register(Group_classes)
admin.site.register(Subjects)
admin.site.register(Group_class_subject_teacher)
admin.site.register(Exam_details)
admin.site.register(Exam_class)
admin.site.register(Exam_paper_subject_details)
admin.site.register(Exam_question_paper_questions)
admin.site.register(contact_us)
admin.site.register(Variables)