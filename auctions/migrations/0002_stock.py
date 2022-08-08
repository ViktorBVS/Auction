# Generated by Django 4.0.6 on 2022-08-06 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_Title', models.CharField(max_length=512)),
                ('s_Img', models.ImageField(upload_to='images/')),
            ],
            options={
                'verbose_name': 'Акции',
                'verbose_name_plural': '13_Акции_Титул',
                'ordering': ('s_Title',),
            },
        ),
    ]