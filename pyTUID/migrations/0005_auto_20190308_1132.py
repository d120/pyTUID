# Generated by Django 2.1.7 on 2019-03-08 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyTUID', '0004_auto_20170903_1902'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tuiduser',
            options={'verbose_name': 'TUID User', 'verbose_name_plural': 'TUID Users'},
        ),
        migrations.AlterField(
            model_name='tuiduser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='email'),
        ),
    ]
