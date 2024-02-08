# Generated by Django 5.0.1 on 2024-02-07 21:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_alter_book_category'),
        ('reader', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loan_book', to='book.book'),
        ),
    ]