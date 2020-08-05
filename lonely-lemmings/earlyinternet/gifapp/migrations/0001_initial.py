# Generated by Django 3.0.9 on 2020-08-05 18:46

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_type', models.CharField(choices=[('GIF', 'gif project'), ('IMG', 'image project')], max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('profile_picture', models.ImageField(upload_to='profile/')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('preview_version', models.ImageField(upload_to='images/')),
                ('upload_version', models.ImageField(upload_to='images/')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gifapp.User')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=50)),
                ('image_data', models.ImageField(upload_to='images/')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_last_modified', models.DateTimeField(auto_now=True)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gifapp.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('parent_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gifapp.Comment')),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gifapp.Project')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gifapp.User')),
            ],
        ),
    ]