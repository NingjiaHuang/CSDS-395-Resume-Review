# Generated by Django 3.2.8 on 2021-11-21 22:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resume_review', '0019_reviewer_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='account',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='resume_review.account'),
        ),
    ]
