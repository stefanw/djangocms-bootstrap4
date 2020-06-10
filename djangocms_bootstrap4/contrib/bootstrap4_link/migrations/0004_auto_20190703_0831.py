# Generated by Django 2.2.2 on 2019-07-03 08:31

import django.db.models.deletion
from django.db import migrations, models

import djangocms_link.validators
import filer.fields.file


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0011_auto_20190418_0137'),
        ('bootstrap4_link', '0003_icon_updates'),
    ]

    operations = [
        migrations.AddField(
            model_name='bootstrap4link',
            name='file_link',
            field=filer.fields.file.FilerFileField(blank=True, help_text='If provided links a file from the filer app.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='filer.File', verbose_name='File link'),
        ),
        migrations.AlterField(
            model_name='bootstrap4link',
            name='external_link',
            field=models.CharField(blank=True, help_text='Provide a link to an external source.', max_length=2040, validators=[djangocms_link.validators.IntranetURLValidator(intranet_host_re=None)], verbose_name='External link'),
        ),
    ]