# Generated by Django 3.2 on 2021-04-29 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Имя', models.CharField(max_length=255)),
                ('E-mail', models.EmailField(max_length=255)),
                ('Текст', models.TextField()),
                ('date_abbed', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.post')),
            ],
            options={
                'ordering': ['-date_abbed'],
            },
        ),
    ]
