# Generated by Django 5.0.1 on 2025-01-31 20:45

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('block_no', models.CharField(blank=True, max_length=10, null=True)),
                ('house_flat_no', models.CharField(blank=True, max_length=10, null=True)),
                ('street', models.CharField(blank=True, max_length=150, null=True)),
                ('landmark', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mobile', models.BigIntegerField(blank=True, null=True)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('form_type', models.CharField(blank=True, choices=[('contact us', 'contactus'), ('query', 'query')], max_length=20, null=True)),
                ('reply_remark', models.CharField(blank=True, max_length=100, null=True)),
                ('reply_date', models.DateField(blank=True, null=True)),
                ('reply_by', models.CharField(blank=True, max_length=50, null=True)),
                ('replied', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='client',
        ),
        migrations.RemoveField(
            model_name='ledger',
            name='client',
        ),
        migrations.AddField(
            model_name='category',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='category'),
        ),
        migrations.AddField(
            model_name='product',
            name='gst',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_description',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='vendors',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vendors', to='ecom.vendors'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_type',
            field=models.CharField(blank=True, choices=[('pre_placed', 'PREPLCED'), ('instant', 'Instant'), ('instantorder', 'InstantOrder')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category_product', to='ecom.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('code', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('discount_type', models.CharField(blank=True, choices=[('fixed', 'Fixed'), ('percentage', 'Percentage'), ('firstorder', 'FirstOrder'), ('categorydiscount', 'CategoryDiscout'), ('referraldiscount', 'ReferralDiscount')], max_length=20, null=True)),
                ('discount_value', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('min_order_value', models.DecimalField(blank=True, decimal_places=2, help_text='Minimum order value required to apply the coupon.', max_digits=10, null=True)),
                ('max_discount', models.DecimalField(blank=True, decimal_places=2, help_text='Maximum discount allowed for percentage-based coupons.', max_digits=10, null=True)),
                ('valid_from', models.DateTimeField(blank=True, null=True)),
                ('valid_to', models.DateTimeField(blank=True, null=True)),
                ('usage_limit', models.PositiveIntegerField(default=1, help_text='Total number of times this coupon can be used.')),
                ('used_count', models.PositiveIntegerField(default=0, help_text='Number of times the coupon has been used.')),
                ('is_active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category_coupan', to='ecom.category')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='ecom.coupon'),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('alternate_phone_number', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('gender', models.CharField(blank=True, choices=[('male', 'MALE'), ('female', 'FEMALE'), ('other', 'OTHER')], max_length=10, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('Address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='address', to='ecom.address')),
            ],
        ),
        migrations.AddField(
            model_name='coupon',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_coupan', to='ecom.customer'),
        ),
        migrations.AddField(
            model_name='ledger',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ledger', to='ecom.customer'),
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='ecom.customer'),
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='productimage')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_images', to='ecom.product')),
            ],
        ),
        migrations.DeleteModel(
            name='Client',
        ),
    ]
