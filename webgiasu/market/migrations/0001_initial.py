# Generated by Django 3.2.5 on 2022-04-29 13:58

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
            name='subs_market',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_user', models.ManyToManyField(blank=True, default=None, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='marketpost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('describe', models.TextField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=30)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('date_outdate', models.PositiveSmallIntegerField(default=15)),
                ('post_img1', models.ImageField(blank=True, null=True, upload_to='postImg/market/', verbose_name='Ảnh 1:')),
                ('post_img2', models.ImageField(blank=True, null=True, upload_to='postImg/market/', verbose_name='Ảnh 2:')),
                ('post_img3', models.ImageField(blank=True, null=True, upload_to='postImg/market/', verbose_name='Ảnh 3:')),
                ('post_img4', models.ImageField(blank=True, null=True, upload_to='postImg/market/', verbose_name='Ảnh 4:')),
                ('post_img5', models.ImageField(blank=True, null=True, upload_to='postImg/market/', verbose_name='Ảnh 5:')),
                ('author', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('report', models.ManyToManyField(blank=True, default=None, related_name='marketreport_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
