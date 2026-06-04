import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuhasc', '0003_member'),
    ]

    operations = [
        migrations.CreateModel(
            name='QResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=20)),
                ('scale', models.CharField(max_length=50)),
                ('value', models.PositiveSmallIntegerField()),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                             related_name='qresults', to='cuhasc.member')),
            ],
            options={
                'unique_together': {('member', 'item')},
            },
        ),
    ]
