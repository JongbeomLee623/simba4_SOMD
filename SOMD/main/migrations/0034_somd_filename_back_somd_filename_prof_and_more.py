# Generated by Django 4.2.1 on 2023-06-26 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0033_images_filename_alter_images_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='somd',
            name='filename_back',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='somd',
            name='filename_prof',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='images',
            name='filename',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
