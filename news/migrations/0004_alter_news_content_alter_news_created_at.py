# Generated by Django 4.2.3 on 2023-11-23 15:39

from django.db import migrations, models
import news.validators


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0003_news"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="content",
            field=models.TextField(
                max_length=200, validators=[news.validators.validate_content]
            ),
        ),
        migrations.AlterField(
            model_name="news",
            name="created_at",
            field=models.DateField(validators=[news.validators.validate_date]),
        ),
    ]