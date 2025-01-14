# Generated by Django 5.0.6 on 2024-06-13 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('bio', models.TextField()),
                ('phone', models.CharField(max_length=15, unique=True)),
                ('address', models.TextField()),
                ('github', models.URLField()),
                ('linkedin', models.URLField(null=True)),
                ('instagram', models.URLField(null=True)),
                ('telegram', models.URLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('reason', models.TextField()),
                ('notes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.DecimalField(decimal_places=0, max_digits=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ContactUsMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('subject', models.CharField(max_length=100, null=True)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalHistory',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('notes', models.TextField()),
                ('files', models.FileField(upload_to='documents/<django.db.models.fields.related.ForeignKey>-<django.db.models.fields.related.ForeignKey>')),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('drugs', models.TextField()),
                ('recipe', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10, unique=True)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('count', models.IntegerField()),
                ('active_email', models.IntegerField()),
                ('module', models.IntegerField()),
                ('automatic_scan', models.IntegerField()),
                ('parallel_scan', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15, unique=True)),
                ('nick_name', models.CharField(max_length=50, unique=True)),
                ('position', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='images/')),
                ('instagram', models.URLField(blank=True, null=True)),
                ('telegram', models.URLField(blank=True, null=True)),
                ('github', models.URLField(blank=True, null=True)),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('site', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
