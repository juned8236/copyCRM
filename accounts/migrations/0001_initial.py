# Generated by Django 2.1.2 on 2019-01-28 07:07

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
                ('email', models.EmailField(max_length=254)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True)),
                ('industry', models.CharField(blank=True, choices=[('ADVERTISING', 'ADVERTISING'), ('AGRICULTURE', 'AGRICULTURE'), ('APPAREL & ACCESSORIES', 'APPAREL & ACCESSORIES'), ('AUTOMOTIVE', 'AUTOMOTIVE'), ('BANKING', 'BANKING'), ('BIOTECHNOLOGY', 'BIOTECHNOLOGY'), ('BUILDING MATERIALS & EQUIPMENT', 'BUILDING MATERIALS & EQUIPMENT'), ('CHEMICAL', 'CHEMICAL'), ('COMPUTER', 'COMPUTER'), ('EDUCATION', 'EDUCATION'), ('ELECTRONICS', 'ELECTRONICS'), ('ENERGY', 'ENERGY'), ('ENTERTAINMENT & LEISURE', 'ENTERTAINMENT & LEISURE'), ('FINANCE', 'FINANCE'), ('FOOD & BEVERAGE', 'FOOD & BEVERAGE'), ('GROCERY', 'GROCERY'), ('HEALTHCARE', 'HEALTHCARE'), ('INSURANCE', 'INSURANCE'), ('LEGAL', 'LEGAL'), ('MANUFACTURING', 'MANUFACTURING'), ('PUBLISHING', 'PUBLISHING'), ('REAL ESTATE', 'REAL ESTATE'), ('SERVICE', 'SERVICE'), ('SOFTWARE', 'SOFTWARE'), ('SPORTS', 'SPORTS'), ('TECHNOLOGY', 'TECHNOLOGY'), ('TELECOMMUNICATIONS', 'TELECOMMUNICATIONS'), ('TELEVISION', 'TELEVISION'), ('TRANSPORTATION', 'TRANSPORTATION'), ('VENTURE CAPITAL', 'VENTURE CAPITAL')], max_length=255, null=True, verbose_name='Industry Type')),
                ('website', models.URLField(blank=True, null=True, verbose_name='Website')),
                ('description', models.TextField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
