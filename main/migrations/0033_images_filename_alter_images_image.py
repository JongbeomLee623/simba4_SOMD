# Generated by Django 4.2.1 on 2023-06-26 14:06

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_post_is_secret'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='filename',
            field=models.CharField(max_length=64, null=True, verbose_name='첨부파일명'),
        ),
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=main.models.get_file_path),
        ),
    ]
