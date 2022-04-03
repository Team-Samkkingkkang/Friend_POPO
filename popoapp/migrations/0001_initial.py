# Generated by Django 3.2.12 on 2022-04-03 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basket_price', models.IntegerField()),
                ('basket_delivery_fee', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board_title', models.CharField(max_length=200)),
                ('board_content', models.TextField()),
                ('board_date', models.DateTimeField(auto_now=True)),
                ('board_img', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.IntegerField()),
                ('order_price', models.IntegerField()),
                ('order_delivery_fee', models.IntegerField()),
                ('order_username', models.CharField(max_length=200)),
                ('order_user_phone_num', models.CharField(max_length=200)),
                ('order_address_num', models.CharField(max_length=200)),
                ('order_request', models.TextField()),
                ('order_agree', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('product_info', models.CharField(max_length=200)),
                ('product_category', models.CharField(max_length=200)),
                ('product_emotion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.EmailField(max_length=200)),
                ('user_password', models.CharField(max_length=200)),
                ('user_nickname', models.CharField(max_length=200)),
                ('user_profile', models.ImageField(upload_to='')),
                ('user_regi_date', models.DateTimeField(auto_now_add=True)),
                ('user_number', models.IntegerField()),
                ('user_sns_type', models.CharField(max_length=200)),
                ('user_sns_id', models.IntegerField()),
                ('user_auth_type', models.BooleanField()),
                ('user_address_number', models.CharField(max_length=200)),
                ('user_address', models.CharField(max_length=200)),
                ('user_delivery_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Qna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qna_title', models.CharField(max_length=200)),
                ('qna_content', models.TextField()),
                ('qna_date', models.DateTimeField(auto_now=True)),
                ('qna_img', models.ImageField(upload_to='')),
                ('qna_status', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='popoapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='ProductOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_classification', models.TextField()),
                ('option_name', models.CharField(max_length=200)),
                ('option_price', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='popoapp.product')),
            ],
        ),
        migrations.CreateModel(
            name='OrderCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_count_count', models.IntegerField()),
                ('order_count_price', models.IntegerField()),
                ('basket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='popoapp.basket')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='popoapp.order')),
                ('product_option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='popoapp.productoption')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='popoapp.user'),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='popoapp.board')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='popoapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diary_content', models.TextField()),
                ('diary_date', models.DateTimeField(auto_now_add=True)),
                ('diary_img', models.FileField(upload_to='')),
                ('diary_share_state', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='popoapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_content', models.TextField()),
                ('comment_date', models.DateTimeField(auto_now=True)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='popoapp.board')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='popoapp.user')),
            ],
        ),
        migrations.AddField(
            model_name='board',
            name='diary',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='popoapp.diary'),
        ),
        migrations.AddField(
            model_name='board',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='popoapp.user'),
        ),
        migrations.AddField(
            model_name='basket',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='popoapp.user'),
        ),
    ]