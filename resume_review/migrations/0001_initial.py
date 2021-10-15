# Generated by Django 3.2.7 on 2021-10-01 06:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('major', models.CharField(max_length=255)),
                ('department', models.CharField(max_length=255)),
                ('academic', models.CharField(choices=[('F', 'Freshmen'), ('S', 'Sophomore'), ('J', 'Junior'), ('C', 'Senior'), ('G', 'Graduate')], max_length=1)),
                ('phone', models.CharField(max_length=12)),
                ('create_at', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reviewer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('specialized_field', models.CharField(max_length=255)),
                ('self_intro', models.TextField()),
                ('comment', models.TextField(null=True)),
                ('rate', models.SmallIntegerField(null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume_review.account')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now=True)),
                ('state', models.CharField(choices=[('P', 'Pending'), ('A', 'Accept'), ('R', 'Reject'), ('D', 'Complete')], max_length=1)),
                ('resume', models.TextField(null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='resume_review.account')),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='resume_review.reviewer')),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='resume_review.account')),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='resume_review.reviewer')),
            ],
        ),
    ]