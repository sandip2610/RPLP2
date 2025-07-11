# Generated by Django 5.0.7 on 2024-12-26 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('STUDENT', '0010_admission'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('file', models.FileField(upload_to='notes/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
