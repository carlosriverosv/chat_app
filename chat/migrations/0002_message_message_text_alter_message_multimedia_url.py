# Generated by Django 4.2.8 on 2023-12-17 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='message_text',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='multimedia_url',
            field=models.CharField(max_length=2048, null=True),
        ),
    ]