# Generated by Django 4.1.3 on 2022-12-24 14:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sessional', '0004_rename_sessionalquestionstudentmapping_questionstudentmapping_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='total_marks',
            new_name='maximum_marks',
        ),
        migrations.RenameField(
            model_name='questionstudentmapping',
            old_name='user',
            new_name='student',
        ),
        migrations.CreateModel(
            name='SessionalStudentMapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_marks_student', models.IntegerField()),
                ('sessional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sessional.sessional')),
            ],
        ),
    ]
