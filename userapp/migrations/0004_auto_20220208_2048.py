# Generated by Django 3.2.9 on 2022-02-08 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0003_alter_profileuser_forget_pass_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileuser',
            name='forget_pass_token',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='profileuser',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userapp.registertable'),
        ),
    ]
