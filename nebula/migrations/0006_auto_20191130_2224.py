# Generated by Django 2.2.7 on 2019-11-30 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nebula', '0005_delete_memberdeploymenttemplate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='deployment',
            field=models.CharField(blank=True, choices=[('amd64_ubuntu_runit', 'Ubuntu runit amd64'), ('amd64_ubuntu_systemd', 'Ubuntu systemd amd64')], max_length=100),
        ),
        migrations.AlterField(
            model_name='member',
            name='expiry_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
