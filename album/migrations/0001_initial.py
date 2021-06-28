# Generated by Django 3.2.4 on 2021-06-28 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(upload_to='album/photo')),
                ('description', models.TextField()),
                ('creation', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
