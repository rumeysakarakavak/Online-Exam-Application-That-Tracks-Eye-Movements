# Generated by Django 3.0.7 on 2020-07-02 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Rumeysa KARAKAVAK', 'Rumeysa KARAKAVAK'), ('Busra Nur ALTUNBAS', 'Busra Nur ALTUNBAS'), ('Esra CERAN', 'Esra CERAN')], max_length=300, null=True)),
                ('lectures', models.CharField(choices=[('CSE341', 'CSE341'), ('CSE312', 'CSE312'), ('CSE396', 'CSE396')], max_length=100, null=True)),
            ],
        ),
    ]