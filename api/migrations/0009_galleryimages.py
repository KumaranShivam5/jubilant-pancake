# Generated by Django 5.0.6 on 2024-06-22 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_memberprofile_address_memberprofile_school_college'),
    ]

    operations = [
        migrations.CreateModel(
            name='galleryImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.FileField(blank=True, null=True, upload_to='gallery_photo')),
                ('show_on_homepage', models.BooleanField(blank=True, default=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
