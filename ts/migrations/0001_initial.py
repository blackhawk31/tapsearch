# Generated by Django 2.2.7 on 2019-11-20 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_id', models.IntegerField()),
                ('key', models.CharField(max_length=120)),
                ('frequency', models.IntegerField()),
            ],
        ),
    ]
