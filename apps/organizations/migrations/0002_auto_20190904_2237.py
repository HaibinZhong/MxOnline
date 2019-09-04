# Generated by Django 2.2 on 2019-09-04 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='address',
            field=models.CharField(default='无', max_length=150, verbose_name='机构地址'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='students',
            field=models.IntegerField(default=0, verbose_name='学习人数'),
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=20, verbose_name='城市名'),
        ),
        migrations.AlterField(
            model_name='courseorg',
            name='image',
            field=models.ImageField(upload_to='org/%Y/%m', verbose_name='机构logo'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='image',
            field=models.ImageField(upload_to='teacher/%Y/%m', verbose_name='讲师头像'),
        ),
    ]
