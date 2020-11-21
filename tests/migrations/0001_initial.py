# Generated by Django 2.2.4 on 2020-11-09 20:48

from django.db import migrations, models
import django.db.models.deletion
import tests.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('problems', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('position', models.IntegerField()),
                ('input', models.FileField(upload_to=tests.models.get_encrypted_file_path)),
                ('output', models.FileField(upload_to=tests.models.get_encrypted_file_path)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problems.Problem', to_field='problem_code')),
            ],
        ),
    ]
