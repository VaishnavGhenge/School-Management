from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_mobile(value):
    if not value.isdigit() or not len(value) == 10:
        raise ValidationError(
            _('Enter current mobile number'),
            params={'value': value},
        )

#Missing Models
class Location_city(models.Model):
    city = models.CharField(max_length=50)
    def __str__(self):
        return self.city

class Location_country(models.Model):
    country = models.CharField(max_length=50)
    def __str__(self):
        return self.country

class Location_state(models.Model):
    state = models.CharField(max_length=50)
    def __str__(self):
        return self.state

# specifying choices
STATUS_CHOICES = (
	(1, "Active"),
	(2, "Disable"),
)
EXAM_MARKS_CHOICES = (
    (20, "20"),
    (70, "70"),
)


#Defualt school id
DEFUALT_SCHOOL_ID = 1

class Academic_session(models.Model):
    session = models.CharField(max_length=20)
    def __str__(self):
        return self.session


# Original Models
class School_details(models.Model):
    username = models.CharField(unique=True, max_length=100)
    logo = models.ImageField(default="", upload_to='school_logo/')
    name = models.CharField(max_length = 100)
    email = models.EmailField(unique=True)
    contact_person_name = models.CharField(max_length = 100)
    contact_person_mobile_no = models.CharField(max_length = 100, validators = [validate_mobile], help_text = "Ten Digit Mobile No.")
    office_mobile_no = models.CharField(max_length = 100, validators = [validate_mobile], help_text = "Ten Digit Mobile No.")
    country = models.ForeignKey(Location_country, on_delete=models.PROTECT)
    state = models.ForeignKey(Location_state, on_delete=models.PROTECT)
    city = models.ForeignKey(Location_city, on_delete=models.PROTECT)
    pincode = models.PositiveIntegerField()
    address = models.TextField()
    last_login = models.DateTimeField(auto_now_add=True, null = True)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    status = models.IntegerField(choices = STATUS_CHOICES, default = 1)
    def __str__(self):
        return self.name

class School_terms(models.Model):
    school_id = models.ForeignKey(School_details, on_delete = models.PROTECT, default=DEFUALT_SCHOOL_ID)
    academic_session_id = models.ForeignKey(Academic_session, on_delete = models.PROTECT, verbose_name="Select academic session")
    term_name = models.CharField(max_length = 100)
    start_date = models.DateField()
    end_date = models.DateField()
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    status = models.IntegerField(choices = STATUS_CHOICES, default = 2)
    def __str__(self):
        return self.term_name

class Teacher_details(models.Model):
    username = models.CharField(unique=True, max_length=200)
    password = models.CharField(max_length=100, null=True)
    school_id = models.ForeignKey(School_details, on_delete = models.PROTECT, default=DEFUALT_SCHOOL_ID)
    image = models.ImageField(default="", upload_to = 'teacher_image/', verbose_name = 'Photo')
    name = models.CharField(max_length = 100)
    email = models.EmailField(unique = True)
    mobile_no = models.CharField(max_length = 100, validators = [validate_mobile], help_text = "Ten Digit Mobile No.")
    qualification = models.CharField(max_length = 100)
    experience = models.FloatField(help_text = "In Year")
    country = models.ForeignKey(Location_country, on_delete=models.PROTECT)
    state = models.ForeignKey(Location_state, on_delete=models.PROTECT)
    city = models.ForeignKey(Location_city, on_delete=models.PROTECT)
    address = models.TextField(max_length=100)
    pincode = models.PositiveIntegerField()
    last_login = models.DateTimeField(auto_now_add=True, null = True)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    status = models.IntegerField(choices = STATUS_CHOICES, default = 1)
    def __str__(self):
        return self.username

class Group_classes(models.Model):
    school_id = models.ForeignKey(School_details, on_delete = models.PROTECT, default=DEFUALT_SCHOOL_ID)
    academic_term_id = models.ForeignKey(School_terms, on_delete = models.PROTECT, verbose_name = 'Current session term')
    class_teacher_id = models.ForeignKey(Teacher_details, on_delete = models.PROTECT, verbose_name = 'Select class teacher')
    name = models.CharField(max_length = 100, verbose_name = "class name")
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    status = models.IntegerField(choices = STATUS_CHOICES, default = 1)
    def __str__(self):
        return self.name

class Subjects(models.Model):
    school_id = models.ForeignKey(School_details, on_delete = models.PROTECT, default=DEFUALT_SCHOOL_ID)
    cover_image = models.ImageField(upload_to='subject_cover')
    subject_name = models.CharField(max_length= 100)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    status = models.IntegerField(choices = STATUS_CHOICES, default = 1)
    def __str__(self):
        return self.subject_name

class Group_class_subject_teacher(models.Model):
    group_class_id = models.ForeignKey(Group_classes, on_delete = models.PROTECT)
    teacher_id = models.ForeignKey(Teacher_details, on_delete = models.PROTECT, verbose_name = 'Select teacher')
    subject_id = models.ForeignKey(Subjects, on_delete = models.PROTECT, verbose_name = 'Select subject')
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    status = models.IntegerField(choices = STATUS_CHOICES, default = 1)
    

class Exam_details(models.Model):
    school_id = models.ForeignKey(School_details, on_delete = models.PROTECT, default=DEFUALT_SCHOOL_ID)
    academic_term_id = models.ForeignKey(School_terms, on_delete = models.PROTECT, verbose_name = 'Current session term')
    exam_name = models.CharField(max_length =100)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    status = models.IntegerField(choices = STATUS_CHOICES, default = 1)
    def __str__(self):
        return self.exam_name

class Exam_class(models.Model):
    exam_id = models.ForeignKey(Exam_details, on_delete = models.PROTECT)
    group_class_id = models.ManyToManyField(Group_classes)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    status = models.IntegerField(choices = STATUS_CHOICES, default = 1)

class Exam_paper_subject_details(models.Model):
    exam_id = models.ForeignKey(Exam_details, on_delete = models.PROTECT)
    uniquo = models.CharField(max_length=255, unique = True, null=True)
    creator = models.CharField(max_length=200, null=True)
    exam_date = models.DateField()
    exam_time = models.TimeField()
    exam_duration = models.FloatField() # in Hr
    total_marks = models.PositiveIntegerField(choices = EXAM_MARKS_CHOICES, default = 20)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    status = models.IntegerField(choices = STATUS_CHOICES, default = 1)
    def __str__(self):
        return self.uniquo

class Exam_question_paper_questions(models.Model):
    exam_subject_id = models.ForeignKey(Exam_paper_subject_details, on_delete = models.PROTECT)
    question = models.CharField(max_length = 500)
    question_mark = models.PositiveIntegerField(default = 2)
    answer = models.TextField(null = True)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    status = models.IntegerField(choices = STATUS_CHOICES, default = 1)

class contact_us(models.Model):
    Name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    msg = models.CharField(max_length=200)

    def __str__(self):
        return self.Name

class Variables(models.Model):
    uniquo = models.CharField(max_length=200, null=True, default=0)
    count = models.IntegerField(default=0)
