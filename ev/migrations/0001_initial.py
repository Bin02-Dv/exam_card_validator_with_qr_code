# Generated by Django 4.2.3 on 2023-08-17 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_regis', models.CharField(max_length=10, unique=True)),
                ('exam_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='QRCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_image', models.ImageField(upload_to='qr_codes/')),
                ('exam', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ev.exam')),
            ],
        ),
    ]
