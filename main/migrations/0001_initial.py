# Generated by Django 3.2 on 2022-04-21 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auth',
            fields=[
                ('auth_id', models.IntegerField(db_column='Auth_id', primary_key=True, serialize=False)),
                ('auth_name', models.CharField(db_column='Auth_name', max_length=10)),
            ],
            options={
                'db_table': 'auth',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthBoard',
            fields=[
                ('ab_num', models.IntegerField(db_column='Ab_num', primary_key=True, serialize=False)),
                ('ab_title', models.CharField(db_column='Ab_title', max_length=255)),
                ('ab_content', models.CharField(db_column='Ab_content', max_length=3000)),
                ('ab_reg_date', models.DateTimeField(db_column='Ab_reg_date')),
                ('ab_reply_yn', models.IntegerField(db_column='Ab_reply_YN')),
                ('user_id', models.IntegerField(db_column='User_id')),
            ],
            options={
                'db_table': 'auth_board',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(db_column='User_id')),
                ('store_id', models.IntegerField(db_column='Store_id')),
            ],
            options={
                'db_table': 'bookmark',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cafepicture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_id', models.IntegerField(db_column='Store_id')),
                ('cafepictrue_url', models.CharField(db_column='Cafepictrue_url', max_length=1000)),
            ],
            options={
                'db_table': 'cafepicture',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('reply_id', models.IntegerField(db_column='Reply_id', primary_key=True, serialize=False)),
                ('reply_content', models.CharField(db_column='Reply_content', max_length=300)),
                ('reply_date', models.DateTimeField(db_column='Reply_date')),
                ('user_id', models.IntegerField(db_column='User_id')),
                ('ab_num', models.IntegerField(db_column='Ab_num')),
            ],
            options={
                'db_table': 'reply',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('review_id', models.IntegerField(db_column='Review_id', primary_key=True, serialize=False)),
                ('user_id', models.IntegerField(db_column='User_id')),
                ('store_id', models.IntegerField(db_column='Store_id')),
                ('review_content', models.CharField(db_column='Review_content', max_length=300)),
                ('review_reg_date', models.DateTimeField(blank=True, db_column='Review_reg_date', null=True)),
                ('review_mod_date', models.DateTimeField(blank=True, db_column='Review_mod_date', null=True)),
            ],
            options={
                'db_table': 'review',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('store_id', models.IntegerField(db_column='Store_id', primary_key=True, serialize=False)),
                ('store_name', models.CharField(db_column='Store_name', max_length=50)),
                ('store_content', models.CharField(blank=True, db_column='Store_content', max_length=1000, null=True)),
                ('store_businesshour', models.CharField(blank=True, db_column='Store_businesshour', max_length=50, null=True)),
                ('store_sinum', models.CharField(db_column='Store_sinum', max_length=10)),
                ('store_sggnum', models.CharField(db_column='Store_sggnum', max_length=10)),
                ('store_emdnum', models.CharField(db_column='Store_emdnum', max_length=10)),
                ('store_roadnum', models.CharField(db_column='Store_roadnum', max_length=10)),
            ],
            options={
                'db_table': 'store',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StoreAuth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(db_column='User_id')),
                ('store_id', models.IntegerField(db_column='Store_id')),
            ],
            options={
                'db_table': 'store_auth',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StoreTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_id', models.IntegerField(db_column='Store_id')),
                ('tag_id', models.IntegerField(db_column='Tag_id')),
            ],
            options={
                'db_table': 'store_tag',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('tag_id', models.IntegerField(db_column='Tag_id', primary_key=True, serialize=False)),
                ('tag_name', models.CharField(db_column='Tag_name', max_length=20)),
            ],
            options={
                'db_table': 'tag',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_num', models.IntegerField(db_column='User_num', primary_key=True, serialize=False)),
                ('user_id', models.CharField(db_column='User_id', max_length=20)),
                ('user_password', models.CharField(db_column='User_password', max_length=20)),
                ('user_nickname', models.CharField(db_column='User_nickname', max_length=20)),
                ('user_email', models.CharField(blank=True, db_column='User_email', max_length=50, null=True)),
                ('user_profileurl', models.CharField(blank=True, db_column='User_profileurl', max_length=1000, null=True)),
                ('auth_id', models.IntegerField(db_column='Auth_id')),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
    ]
