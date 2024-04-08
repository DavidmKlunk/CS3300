# Generated by Django 4.2 on 2024-04-08 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('functionalStrat', '0003_remove_boss_strategy_bossstrat_boss'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expansion',
            name='raid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='functionalStrat.raid'),
        ),
        migrations.AlterField(
            model_name='raid',
            name='boss',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='functionalStrat.boss'),
        ),
    ]
