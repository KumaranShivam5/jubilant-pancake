# Generated by Django 5.0.6 on 2024-05-12 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_member_name_memberprofile_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactMsg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=50)),
                ('message', models.TextField(max_length=1000)),
                ('reply_pending', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='newsAndHighlight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=200)),
                ('details', models.TextField(blank=True, max_length=1000, null=True)),
                ('links', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='news_photo')),
                ('date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='memberprofile',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to='member_photo'),
        ),
    ]
