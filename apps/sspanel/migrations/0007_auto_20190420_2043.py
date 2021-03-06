# Generated by Django 2.1.7 on 2019-04-20 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("sspanel", "0006_user_sub_type")]

    operations = [
        migrations.AlterField(
            model_name="donate",
            name="money",
            field=models.DecimalField(
                blank=True,
                db_index=True,
                decimal_places=2,
                default=0,
                max_digits=10,
                null=True,
                verbose_name="捐赠金额",
            ),
        ),
        migrations.AlterField(
            model_name="donate",
            name="time",
            field=models.DateTimeField(
                auto_now_add=True, db_index=True, verbose_name="捐赠时间"
            ),
        ),
    ]
