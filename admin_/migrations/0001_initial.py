# Generated by Django 3.0.6 on 2020-07-04 15:53

import admin_.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Academic_session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='contact_us',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('msg', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Exam_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_name', models.CharField(max_length=100)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('status', models.IntegerField(choices=[(1, 'Active'), (2, 'Disable')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Exam_paper_subject_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniquo', models.CharField(max_length=255, null=True, unique=True)),
                ('creator', models.CharField(max_length=200, null=True)),
                ('exam_date', models.DateField()),
                ('exam_time', models.TimeField()),
                ('exam_duration', models.FloatField()),
                ('total_marks', models.PositiveIntegerField(choices=[(20, '20'), (70, '70')], default=20)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('status', models.IntegerField(choices=[(1, 'Active'), (2, 'Disable')], default=1)),
                ('exam_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='admin_.Exam_details')),
            ],
        ),
        migrations.CreateModel(
            name='Location_city',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Location_country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Location_state',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='School_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('logo', models.ImageField(default='', upload_to='school_logo/')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('contact_person_name', models.CharField(max_length=100)),
                ('contact_person_mobile_no', models.CharField(help_text='Ten Digit Mobile No.', max_length=100, validators=[admin_.models.validate_mobile])),
                ('office_mobile_no', models.CharField(help_text='Ten Digit Mobile No.', max_length=100, validators=[admin_.models.validate_mobile])),
                ('pincode', models.PositiveIntegerField()),
                ('address', models.TextField()),
                ('last_login', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('status', models.IntegerField(choices=[(1, 'Active'), (2, 'Disable')], default=1)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='admin_.Location_city')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='admin_.Location_country')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='admin_.Location_state')),
            ],
        ),
        migrations.CreateModel(
            name='Variables',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniquo', models.CharField(default=0, max_length=200, null=True)),
                ('count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=100, null=True)),
                ('image', models.ImageField(default='', upload_to='teacher_image/', verbose_name='Photo')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mobile_no', models.CharField(help_text='Ten Digit Mobile No.', max_length=100, validators=[admin_.models.validate_mobile])),
                ('qualification', models.CharField(max_length=100)),
                ('experience', models.FloatField(help_text='In Year')),
                ('address', models.TextField(max_length=100)),
                ('pincode', models.PositiveIntegerField()),
                ('last_login', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('status', models.IntegerField(choices=[(1, 'Active'), (2, 'Disable')], default=1)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='admin_.Location_city')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='admin_.Location_country')),
                ('school_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='admin_.School_details')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='admin_.Location_state')),
            ],
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover_image', models.ImageField(upload_to='subject_cover')),
                ('subject_name', models.CharField(max_length=100)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('status', models.IntegerField(choices=[(1, 'Active'), (2, 'Disable')], default=1)),
                ('school_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='admin_.School_details')),
            ],
        ),
        migrations.CreateModel(
            name='School_terms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term_name', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('status', models.IntegerField(choices=[(1, 'Active'), (2, 'Disable')], default=2)),
                ('academic_session_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='admin_.Academic_session', verbose_name='Select academic session')),
                ('school_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='admin_.School_details')),
            ],
        ),
        migrations.CreateModel(
            name='Group_classes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='class name')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('status', models.IntegerField(choices=[(1, 'Active'), (2, 'Disable')], default=1)),
                ('academic_term_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='admin_.School_terms', verbose_name='Current session term')),
                ('class_teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='admin_.Teacher_details', verbose_name='Select class teacher')),
                ('school_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='admin_.School_details')),
            ],
        ),
        migrations.CreateModel(
            name='Group_class_subject_teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('status', models.IntegerField(choices=[(1, 'Active'), (2, 'Disable')], default=1)),
                ('group_class_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='admin_.Group_classes')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='admin_.Subjects', verbose_name='Select subject')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='admin_.Teacher_details', verbose_name='Select teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Exam_question_paper_questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500)),
                ('question_mark', models.PositiveIntegerField(default=2)),
                ('answer', models.TextField(null=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('status', models.IntegerField(choices=[(1, 'Active'), (2, 'Disable')], default=1)),
                ('exam_subject_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='admin_.Exam_paper_subject_details')),
            ],
        ),
        migrations.AddField(
            model_name='exam_details',
            name='academic_term_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='admin_.School_terms', verbose_name='Current session term'),
        ),
        migrations.AddField(
            model_name='exam_details',
            name='school_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='admin_.School_details'),
        ),
        migrations.CreateModel(
            name='Exam_class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('status', models.IntegerField(choices=[(1, 'Active'), (2, 'Disable')], default=1)),
                ('exam_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='admin_.Exam_details')),
                ('group_class_id', models.ManyToManyField(to='admin_.Group_classes')),
            ],
        ),
    ]
