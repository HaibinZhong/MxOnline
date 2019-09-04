# Generated by Django 2.2 on 2019-09-04 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0002_auto_20190904_2237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='address',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='students',
        ),
        migrations.AddField(
            model_name='courseorg',
            name='address',
            field=models.CharField(default='无', max_length=150, verbose_name='机构地址'),
        ),
        migrations.AddField(
            model_name='courseorg',
            name='course_nums',
            field=models.IntegerField(default=0, verbose_name='课程数'),
        ),
        migrations.AddField(
            model_name='courseorg',
            name='students',
            field=models.IntegerField(default=0, verbose_name='学习人数'),
        ),
    ]
