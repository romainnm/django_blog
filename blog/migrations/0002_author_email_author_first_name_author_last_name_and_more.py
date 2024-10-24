# Generated by Django 5.1.2 on 2024-10-22 15:43

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='first_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='last_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='blog.author'),
        ),
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(null=True, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='post',
            name='excerpt',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='caption',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
