# Generated by Django 4.2 on 2023-04-07 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Menu',
                'verbose_name_plural': 'Menus',
            },
        ),
        migrations.CreateModel(
            name='MenuBranch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='maximum 100 characters', max_length=100, verbose_name='Branch name')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tree_menu.menu', verbose_name='Menu')),
                ('parent', models.ForeignKey(blank=True, help_text='Leave the field blank if attached to the menu', null=True, on_delete=django.db.models.deletion.CASCADE, to='tree_menu.menubranch', verbose_name='Parent branch')),
            ],
            options={
                'verbose_name': 'Branch',
                'verbose_name_plural': 'Branches',
            },
        ),
    ]
