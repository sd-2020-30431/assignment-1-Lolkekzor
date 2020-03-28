# Generated by Django 3.0.4 on 2020-03-28 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wasteless', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='listitem',
            name='parent_list',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='wasteless.List'),
            preserve_default=False,
        ),
    ]
