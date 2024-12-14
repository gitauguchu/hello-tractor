# Generated by Django 3.0.5 on 2024-11-24 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20241124_0127'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dealer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('contact_email', models.EmailField(max_length=254)),
                ('contact_phone', models.CharField(blank=True, max_length=15, null=True)),
                ('company_address', models.TextField()),
                ('website', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operator_category', models.CharField(choices=[('agriculture', 'Agriculture'), ('construction', 'Construction'), ('forestry', 'Forestry'), ('transport', 'Transport'), ('industrial', 'Industrial'), ('maintenance', 'Maintenance'), ('custom_services', 'Custom Services'), ('specialized', 'Specialized Equipment')], max_length=50)),
                ('operator_subcategory', models.CharField(choices=[('crop_farming', 'Crop Farming'), ('livestock_farming', 'Livestock Farming'), ('horticulture', 'Horticulture'), ('aquaculture', 'Aquaculture'), ('organic_farming', 'Organic Farming'), ('earth_moving', 'Earth Moving'), ('demolition', 'Demolition'), ('road_construction', 'Road Construction'), ('landscaping', 'Landscaping'), ('logging', 'Logging'), ('reforestation', 'Reforestation'), ('wildlife_management', 'Wildlife Management'), ('firefighting', 'Firefighting'), ('cargo_transport', 'Cargo Transport'), ('trailer', 'Trailer Operation'), ('market_distribution', 'Market Distribution'), ('factory_transport', 'Factory Transport'), ('warehouse', 'Warehouse Transport'), ('heavy_cargo', 'Heavy Cargo Transport'), ('preventive_maintenance', 'Preventive Maintenance'), ('repair', 'Repair Operations'), ('seasonal_maintenance', 'Seasonal Maintenance'), ('snow_removal', 'Snow Removal'), ('spraying', 'Spraying Operations'), ('land_clearing', 'Land Clearing'), ('emergency_services', 'Emergency Services'), ('gps_guided', 'GPS-Guided Tractors'), ('high_tech', 'High-Tech Tractors'), ('multi_attachment', 'Multi-Attachment Operators'), ('research', 'Research & Development')], max_length=50)),
                ('operator_first_name', models.CharField(max_length=50)),
                ('operator_last_name', models.CharField(max_length=50)),
                ('operator_phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('operator_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('operator_profile_picture', models.ImageField(blank=True, null=True, upload_to='operators/')),
                ('operator_experience_years', models.PositiveIntegerField(default=0)),
                ('operator_tractor_models_operated', models.TextField(blank=True, null=True)),
                ('operator_address', models.TextField(blank=True, null=True)),
                ('operator_created_at', models.DateTimeField(auto_now_add=True)),
                ('operator_updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='RepairWorker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rw_first_name', models.CharField(max_length=50)),
                ('rw_last_name', models.CharField(max_length=50)),
                ('rw_phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('rw_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('rw_profile_picture', models.ImageField(blank=True, null=True, upload_to='repair_workers/')),
                ('rw_expertise', models.TextField(blank=True, null=True)),
                ('rw_certification', models.CharField(blank=True, max_length=255, null=True)),
                ('rw_years_experience', models.PositiveIntegerField(default=0)),
                ('rw_address', models.TextField(blank=True, null=True)),
                ('rw_created_at', models.DateTimeField(auto_now_add=True)),
                ('rw_updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
