from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Address(models.Model):
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    locality = models.CharField(max_length=150, verbose_name="Nearest Location")
    city = models.CharField(max_length=150, verbose_name="City")
    state = models.CharField(max_length=150, verbose_name="State")

    def __str__(self):
        return self.locality


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name="Category Title")
    slug = models.SlugField(max_length=55, verbose_name="Category Slug")
    description = models.TextField(blank=True, verbose_name="Category Description")
    category_image = models.ImageField(upload_to='category', blank=True, null=True, verbose_name="Category Image")
    is_active = models.BooleanField(verbose_name="Is Active?")
    is_featured = models.BooleanField(verbose_name="Is Featured?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated Date")

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('-created_at', )

    def __str__(self):
        return self.title


class Product(models.Model):

    def get_default_user(self):
        return User.objects.first().id

    COUNTRIES = (
        ('Kenya', 'Kenya'),
        ('Uganda', 'Uganda'),
        ('Tanzania', 'Tanzania'),
        ('Ghana', 'Ghana'),
        ('Rwanda', 'Rwanda'),
        ('Congo Brazzaville', 'Congo Brazzaville'),
        ('South Africa', 'South Africa'),
        ('Nigeria', 'Nigeria'),
        ('Egypt', 'Egypt'),
        ('S. Sudan', 'S. Sudan'),
        ('Malawi', 'Malawi'),
        ('Senegal', 'Senegal'),
        ('Madagascar', 'Madagascar'),
        ('Mauritius', 'Mauritius'),
    )
    title = models.CharField(max_length=150, verbose_name="Product Title")
    slug = models.SlugField(max_length=160, verbose_name="Product Slug")
    sku = models.CharField(default='default-sku', max_length=255, unique=True, verbose_name="Unique Product ID (SKU)")
    country = models.CharField(choices=COUNTRIES, max_length=255, verbose_name="Country of Origin", default="Kenya")
    location = models.CharField(max_length=255, verbose_name="Location of the seller item", default="Nairobi")
    seller = models.ForeignKey(User, default=None, null=True, on_delete=models.CASCADE, max_length=255, verbose_name="who is selling the item")
    short_description = models.TextField(verbose_name="Short Description")
    detail_description = models.TextField(blank=True, null=True, verbose_name="Detail Description")
    product_image = models.ImageField(upload_to='product', blank=True, null=True, verbose_name="Product Image")
    price = models.DecimalField(max_digits=12, decimal_places=2)
    category = models.ForeignKey(Category, verbose_name="Product Category", on_delete=models.CASCADE)
    is_active = models.BooleanField(verbose_name="Is Active?")
    is_featured = models.BooleanField(verbose_name="Is Featured?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated Date")

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created_at', )

    def __str__(self):
        return self.title


class Cart(models.Model):
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name="Product", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, verbose_name="Quantity")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated Date")

    def __str__(self):
        return str(self.user)
    
    # Creating Model Property to calculate Quantity x Price
    @property
    def total_price(self):
        return self.quantity * self.product.price


STATUS_CHOICES = (
    ('Pending', 'Pending'),
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Cancelled', 'Cancelled')
)

class Order(models.Model):
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    address = models.ForeignKey(Address, verbose_name="Shipping Address", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name="Product", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name="Quantity")
    ordered_date = models.DateTimeField(auto_now_add=True, verbose_name="Ordered Date")
    status = models.CharField(
        choices=STATUS_CHOICES,
        max_length=50,
        default="Pending"
        )

# Dealers Model
# class Dealer(models.Model):
#     company_name = models.CharField(max_length=255)  # Company name
#     contact_email = models.EmailField()  # Dealer's contact email
#     contact_phone = models.CharField(max_length=15, blank=True, null=True)  # Phone number
#     company_address = models.TextField()  # Company address
#     website = models.URLField(blank=True, null=True)  # Dealer's website (optional)
#     created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when created
#     updated_at = models.DateTimeField(auto_now=True)  # Automatically set when modified
#
#     def __str__(self):
#         return self.company_name


# Operators Model
class TractorOperator(models.Model):
    # Main category
    CATEGORY_CHOICES = [
        ('agriculture', 'Agriculture'),
        ('construction', 'Construction'),
        ('forestry', 'Forestry'),
        ('transport', 'Transport'),
        ('industrial', 'Industrial'),
        ('maintenance', 'Maintenance'),
        ('custom_services', 'Custom Services'),
        ('specialized', 'Specialized Equipment'),
    ]


    # Subcategory
    SUBCATEGORY_CHOICES = [
        # Agriculture
        ('crop_farming', 'Crop Farming'),
        ('livestock_farming', 'Livestock Farming'),
        ('horticulture', 'Horticulture'),
        ('aquaculture', 'Aquaculture'),
        ('organic_farming', 'Organic Farming'),

        # Construction
        ('earth_moving', 'Earth Moving'),
        ('demolition', 'Demolition'),
        ('road_construction', 'Road Construction'),
        ('landscaping', 'Landscaping'),

        # Forestry
        ('logging', 'Logging'),
        ('reforestation', 'Reforestation'),
        ('wildlife_management', 'Wildlife Management'),
        ('firefighting', 'Firefighting'),

        # Transport
        ('cargo_transport', 'Cargo Transport'),
        ('trailer', 'Trailer Operation'),
        ('market_distribution', 'Market Distribution'),

        # Industrial
        ('factory_transport', 'Factory Transport'),
        ('warehouse', 'Warehouse Transport'),
        ('heavy_cargo', 'Heavy Cargo Transport'),

        # Maintenance
        ('preventive_maintenance', 'Preventive Maintenance'),
        ('repair', 'Repair Operations'),
        ('seasonal_maintenance', 'Seasonal Maintenance'),

        # Custom Services
        ('snow_removal', 'Snow Removal'),
        ('spraying', 'Spraying Operations'),
        ('land_clearing', 'Land Clearing'),
        ('emergency_services', 'Emergency Services'),

        # Specialized Equipment
        ('gps_guided', 'GPS-Guided Tractors'),
        ('high_tech', 'High-Tech Tractors'),
        ('multi_attachment', 'Multi-Attachment Operators'),
        ('research', 'Research & Development'),
    ]
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    operator_category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    operator_subcategory = models.CharField(max_length=50, choices=SUBCATEGORY_CHOICES)
    operator_first_name = models.CharField(max_length=50)
    operator_last_name = models.CharField(max_length=50)
    operator_phone_number = models.CharField(max_length=15, blank=True, null=True)
    operator_email = models.EmailField(blank=True, null=True)  # Optional email
    operator_profile_picture = models.ImageField(upload_to='operators/', blank=True, null=True)  # Profile picture
    operator_experience_years = models.PositiveIntegerField(default=0)  # Years of experience
    operator_tractor_models_operated = models.TextField(blank=True, null=True)  # List or description of tractor models they've operated
    operator_address = models.TextField(blank=True, null=True)  # Operator's address
    operator_created_at = models.DateTimeField(auto_now_add=True)
    operator_updated_at = models.DateTimeField(auto_now=True)
    operator_application_status = models.CharField(choices=STATUS_CHOICES, default="pending", max_length=50)

    def __str__(self):
        return f"{self.operator_first_name} {self.operator_last_name}"


# RepairWorkers Model
# class RepairWorker(models.Model):
#     rw_first_name = models.CharField(max_length=50)
#     rw_last_name = models.CharField(max_length=50)
#     rw_phone_number = models.CharField(max_length=15, blank=True, null=True)
#     rw_email = models.EmailField(blank=True, null=True)  # Optional email
#     rw_profile_picture = models.ImageField(upload_to='repair_workers/', blank=True, null=True)  # Profile picture
#     rw_expertise = models.TextField(blank=True, null=True)  # Expertise or specialization
#     rw_certification = models.CharField(max_length=255, blank=True, null=True)  # Certification details (if any)
#     rw_years_experience = models.PositiveIntegerField(default=0)  # Years of experience
#     rw_address = models.TextField(blank=True, null=True)  # Repair worker's address
#     rw_created_at = models.DateTimeField(auto_now_add=True)
#     rw_updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return f"{self.rw_first_name} {self.rw_last_name}"

class Skill(models.Model):
    skill_name = models.CharField(max_length=50, unique=True, verbose_name="Skill Name")

    def __str__(self):
        return self.skill_name

class JobPosting(models.Model):
    # Job Details
    title = models.CharField(max_length=100, verbose_name="Job Title")
    description = models.TextField(verbose_name="Job Description")
    location = models.CharField(max_length=100, verbose_name="Job Location")
    JOB_TYPE = [
        ('Full Time', 'Full Time'),
        ('Part-Time', 'Part-Time'),
        ('Contract', 'Contract')
    ]
    CATEGORY_CHOICES = [
        ('operator', 'Tractor Operator'),
        ('mechanic', 'Tractor Mechanic'),
        ('technician', 'Field Technician'),
        ('manager', 'Operations Manager'),
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, verbose_name="Job Category")
    job_type = models.CharField(max_length=20, default='Full Time', choices=JOB_TYPE, verbose_name="Type of job posted")
    salary = models.PositiveIntegerField(default=0)

    # Requirements
    years_of_experience_required = models.PositiveIntegerField(verbose_name="Years of Experience Required")
    certification_required = models.BooleanField(default=False, verbose_name="Certification Required")
    skills_required = models.ManyToManyField(Skill, blank=True, verbose_name="Required Skills")

    # Employer Information
    company_name = models.CharField(max_length=100, verbose_name="Company Name", blank=True, null=True)
    company_email = models.EmailField(verbose_name="Contact Email", blank=True, null=True)
    company_phone = models.CharField(max_length=15, verbose_name="Contact Phone", blank=True, null=True)
    company_website = models.URLField(verbose_name="Company Website", blank=True, null=True)

    # Additional Information
    application_deadline = models.DateField(verbose_name="Application Deadline")
    posted_at = models.DateTimeField(auto_now_add=True, verbose_name="Posted At")

    class Meta:
        verbose_name = "Job Posting"
        verbose_name_plural = "Job Postings"
        ordering = ['-posted_at']

    def __str__(self):
        return f"{self.title} - {self.company_name}"


class JobApplication(models.Model):
    # Personal Information
    applicant_first_name = models.CharField(max_length=50, verbose_name="First Name")
    applicant_last_name = models.CharField(max_length=50, verbose_name="Last Name")
    applicant_email = models.EmailField(verbose_name="Email Address")
    applicant_phone_number = models.CharField(max_length=15, verbose_name="Phone Number")
    applicant_address = models.TextField(verbose_name="Address")

    # Job Preferences
    POSITION_CHOICES = [
        ('operator', 'Tractor Operator'),
        ('mechanic', 'Tractor Mechanic'),
        ('technician', 'Field Technician'),
        ('manager', 'Operations Manager'),
    ]
    applicant_desired_position = models.CharField(max_length=20, choices=POSITION_CHOICES, verbose_name="Desired Position")

    # Experience
    applicant_years_of_experience = models.PositiveIntegerField(verbose_name="Years of Experience")
    applicant_is_certified_operator = models.BooleanField(default=False, verbose_name="Certified Tractor Operator")

    # Qualifications
    applicant_certifications = models.TextField(blank=True, null=True, verbose_name="Relevant Certifications")
    applicant_skills = models.ManyToManyField(Skill, verbose_name="Skills and Expertise")

    # Additional Information
    applicant_resume = models.FileField(upload_to='resumes/', verbose_name="Upload Resume (PDF or DOC)", blank=True, null=True)
    applicant_cover_letter = models.TextField(blank=True, null=True, verbose_name="Cover Letter")

    # Application Metadata
    applicant_submitted_at = models.DateTimeField(auto_now_add=True, verbose_name="Submitted At")

    class Meta:
        verbose_name = "Job Application"
        verbose_name_plural = "Job Applications"
        ordering = ['-applicant_submitted_at']

    def __str__(self):
        return f"{self.applicant_first_name} {self.applicant_last_name} - {self.applicant_desired_position}"


class InAppMessage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="messages")
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_messages")
    content = models.TextField(verbose_name="Message Content")
    timestamp = models.DateTimeField(auto_now_add=True)
    is_reply = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Automatically set the recipient as the product's seller
        if not self.recipient:
            self.recipient = self.product.seller
            self.product = self.product.title
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Message from {self.sender} to {self.recipient} on {self.product.title} at {self.timestamp}"


