# Generated by Django 3.2 on 2022-04-25 01:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adj',
            fields=[
                ('adj_id', models.AutoField(primary_key=True, serialize=False)),
                ('first', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'adj',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Auth',
            fields=[
                ('auth_id', models.AutoField(db_column='Auth_id', primary_key=True, serialize=False)),
                ('auth_name', models.CharField(db_column='Auth_name', max_length=10)),
            ],
            options={
                'db_table': 'auth',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='AuthBoard',
            fields=[
                ('ab_id', models.AutoField(db_column='Ab_id', primary_key=True, serialize=False)),
                ('ab_title', models.CharField(db_column='Ab_title', max_length=255)),
                ('ab_content', models.CharField(db_column='Ab_content', max_length=3000)),
                ('ab_reg_date', models.DateTimeField(db_column='Ab_reg_date')),
                ('ab_reply_yn', models.IntegerField(db_column='Ab_reply_YN')),
            ],
            options={
                'db_table': 'auth_board',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Noun',
            fields=[
                ('noun_id', models.AutoField(primary_key=True, serialize=False)),
                ('second', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'noun',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('store_id', models.AutoField(db_column='Store_id', primary_key=True, serialize=False)),
                ('store_name', models.CharField(db_column='Store_name', max_length=50)),
                ('store_content', models.CharField(blank=True, db_column='Store_content', max_length=1000, null=True)),
                ('store_businesshour', models.CharField(blank=True, db_column='Store_businesshour', max_length=50, null=True)),
                ('store_sinum', models.CharField(db_column='Store_sinum', max_length=10)),
                ('store_sggnum', models.CharField(db_column='Store_sggnum', max_length=10)),
                ('store_emdnum', models.CharField(db_column='Store_emdnum', max_length=10)),
                ('store_roadnum', models.CharField(db_column='Store_roadnum', max_length=50)),
            ],
            options={
                'db_table': 'store',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('tag_id', models.AutoField(db_column='Tag_id', primary_key=True, serialize=False)),
                ('tag_name', models.CharField(db_column='Tag_name', max_length=20)),
            ],
            options={
                'db_table': 'tag',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(db_column='User_id', primary_key=True, serialize=False)),
                ('user_account', models.CharField(db_column='User_account', max_length=20)),
                ('user_password', models.CharField(db_column='User_password', max_length=20)),
                ('user_nickname', models.CharField(db_column='User_nickname', max_length=20)),
                ('user_email', models.CharField(blank=True, db_column='User_email', max_length=50, null=True)),
                ('user_profileurl', models.CharField(blank=True, db_column='User_profileurl', max_length=1000, null=True)),
                ('auth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.auth')),
            ],
            options={
                'db_table': 'user',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='StoreTag',
            fields=[
                ('store_tag_id', models.AutoField(db_column='Store_Tag_id', primary_key=True, serialize=False)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.store')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.tag')),
            ],
            options={
                'db_table': 'store_tag',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='StoreAuth',
            fields=[
                ('store_auth_id', models.IntegerField(db_column='Store_Auth_id', primary_key=True, serialize=False)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.store')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user')),
            ],
            options={
                'db_table': 'store_auth',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('review_id', models.AutoField(db_column='Review_id', primary_key=True, serialize=False)),
                ('review_content', models.CharField(db_column='Review_content', max_length=300)),
                ('review_reg_date', models.DateTimeField(blank=True, db_column='Review_reg_date', null=True)),
                ('review_mod_date', models.DateTimeField(blank=True, db_column='Review_mod_date', null=True)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.store')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user')),
            ],
            options={
                'db_table': 'review',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('reply_id', models.AutoField(db_column='Reply_id', primary_key=True, serialize=False)),
                ('reply_content', models.CharField(db_column='Reply_content', max_length=300)),
                ('reply_date', models.DateTimeField(db_column='Reply_date')),
                ('authboard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.authboard')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user')),
            ],
            options={
                'db_table': 'reply',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Cafepicture',
            fields=[
                ('cafepicture_id', models.AutoField(db_column='Cafepicture_id', primary_key=True, serialize=False)),
                ('cafepicture_url', models.CharField(db_column='Cafepicture_url', max_length=1000)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.store')),
            ],
            options={
                'db_table': 'cafepicture',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('bookmark_id', models.AutoField(db_column='Bookmark_id', primary_key=True, serialize=False)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.store')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user')),
            ],
            options={
                'db_table': 'bookmark',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='authboard',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user'),
        ),
    ]
