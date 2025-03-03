# Generated by Django 4.1.7 on 2023-04-12 08:59

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='admins',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adminemail', models.CharField(max_length=250, null=True)),
                ('adminpass', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='categorys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categorys', models.TextField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='cmuser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unames', models.CharField(max_length=250, null=True)),
                ('upass', models.CharField(max_length=250, null=True)),
                ('umail', models.CharField(max_length=250, null=True)),
                ('uphone', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HotProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hname', models.CharField(max_length=250, null=True)),
                ('place', models.CharField(max_length=250, null=True)),
                ('adrss', models.CharField(max_length=250, null=True)),
                ('email', models.CharField(max_length=250, null=True)),
                ('mobs', models.TextField(max_length=10)),
                ('hid', models.TextField(max_length=10)),
                ('password', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.TextField(max_length=10)),
                ('catsgry', models.CharField(max_length=250, null=True)),
                ('price', models.CharField(max_length=250, null=True)),
                ('qtys', models.CharField(max_length=250, null=True)),
                ('hotid', models.CharField(max_length=250, null=True)),
                ('description', models.TextField(max_length=10)),
                ('imgs', models.CharField(max_length=250, null=True)),
                ('sts', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('odrid', models.CharField(max_length=250, null=True)),
                ('odruser', models.CharField(max_length=250, null=True)),
                ('odrrcart', models.CharField(max_length=250, null=True)),
                ('odrpaymet', models.CharField(max_length=250, null=True)),
                ('odrstatus', models.CharField(max_length=250, null=True)),
                ('odrdlvey', models.CharField(max_length=250, null=True)),
                ('odrdanam', models.CharField(max_length=250, null=True)),
                ('oddrmob', models.CharField(max_length=250, null=True)),
                ('odrland', models.CharField(max_length=250, null=True)),
                ('odrcity', models.CharField(max_length=250, null=True)),
                ('odrhotel', models.CharField(max_length=250, null=True)),
                ('odridsa', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='tempcart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catitm', models.CharField(max_length=250, null=True)),
                ('catprice', models.CharField(max_length=250, null=True)),
                ('cathots', models.CharField(max_length=250, null=True)),
                ('cattempid', models.CharField(max_length=250, null=True)),
                ('catuser', models.CharField(max_length=250, null=True)),
                ('catqty', models.CharField(max_length=250, null=True)),
                ('catitids', models.CharField(max_length=250, null=True)),
                ('catstatus', models.CharField(max_length=250, null=True)),
                ('catimng', models.CharField(max_length=250, null=True)),
                ('cathotl', models.CharField(max_length=250, null=True)),
                ('catdelivey', models.CharField(max_length=250, null=True)),
                ('cathtsts', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='userregs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('useremail', models.CharField(max_length=250, null=True)),
                ('userphone', models.CharField(max_length=250, null=True)),
                ('username', models.CharField(max_length=250, null=True)),
                ('userpass', models.CharField(max_length=250, null=True)),
                ('usersts', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_fuduser', models.BooleanField(default=False)),
                ('is_fudhotel', models.BooleanField(default=False)),
                ('is_fudadmin', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
