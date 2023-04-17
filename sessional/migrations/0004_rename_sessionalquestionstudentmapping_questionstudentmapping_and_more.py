# Generated by Django 4.1.3 on 2022-12-24 13:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sessional', '0003_question_sessional_sessionalquestionstudentmapping_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SessionalQuestionStudentMapping',
            new_name='QuestionStudentMapping',
        ),
        migrations.AddField(
            model_name='question',
            name='sessional',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sessional.sessional'),
        ),
    ]
