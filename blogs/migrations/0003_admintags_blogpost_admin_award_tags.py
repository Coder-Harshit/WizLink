# Generated by Django 5.0.6 on 2024-06-29 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_tag_rename_user_comment_author_blogpost_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminTags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='blogpost',
            name='admin_award_tags',
            field=models.ManyToManyField(limit_choices_to={'is_admin': True}, to='blogs.admintags'),
        ),
    ]
