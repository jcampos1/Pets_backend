# Generated by Django 2.0 on 2017-12-22 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name', max_length=150)),
            ],
        ),
        migrations.AlterField(
            model_name='owner',
            name='name',
            field=models.CharField(help_text='Name', max_length=100),
        ),
    ]
