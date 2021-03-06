# Generated by Django 3.1.2 on 2020-11-27 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20201102_0551'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoContacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoCon', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ContactoFinal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('asunto', models.CharField(max_length=50)),
                ('mensaje', models.CharField(max_length=200)),
                ('tipoCon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tipocontacto')),
            ],
        ),
    ]
