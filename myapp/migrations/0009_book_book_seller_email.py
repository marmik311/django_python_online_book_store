# Generated by Django 2.2 on 2020-08-04 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_book_book_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_seller_email',
            field=models.CharField(default='shah.marmik311@gmail.com', max_length=100),
            preserve_default=False,
        ),
    ]
