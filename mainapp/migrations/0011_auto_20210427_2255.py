# Generated by Django 2.1.7 on 2021-04-27 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_auto_20210427_2208'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartEntity',
            fields=[
                ('no', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='购物车编号')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainapp.UserEntity', verbose_name='账户')),
            ],
            options={
                'verbose_name': '购物车表',
                'verbose_name_plural': '购物车表',
                'db_table': 't_cart',
            },
        ),
        migrations.AlterField(
            model_name='storeentity',
            name='id',
            field=models.UUIDField(default='d21dc4eea7cf493396d499e79c5ea2ff', primary_key=True, serialize=False, verbose_name='店号'),
        ),
    ]
