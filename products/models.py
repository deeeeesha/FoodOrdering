from django.db import models
import uuid

# Create your models here.

# use DRY method


class BaseModel(models.Model):
    # A UUID field that automatically generates a unique ID for each instance
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    
    # A timestamp for when the instance is created
    created = models.DateTimeField(auto_now_add=True)
    
    # A timestamp for when the instance is last updated
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        # Indicates that this is an abstract base class
        # Django will not create a database table for this model
        #django will create this as a base class not a model when python manage.py makemigrations is ran
        abstract = True  


class Product(BaseModel):
    product_name = models.CharField(max_length=100)
    
    # A SlugField in Django is a field used to store URL-friendly representations of data. 
    # It is often used for creating readable and SEO-friendly URLs for web pages.
    # A slug is a short, URL-friendly string that represents a specific resource or content.
    product_slug = models.SlugField(unique=True)
    product_description = models.TextField()
    product_price = models.IntegerField(default=0)
    product_promo_price = models.IntegerField(default=0)
    
    

class ProductMetaInformation(BaseModel):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    
    product_quantity = models.CharField(null=True, blank=True)
    
    product_measurement =models.CharField(max_length=100, null=True, blank=True, 
                                          choices=(("KG", "KG"),("ML", "ML"),("L", "L")("None", "None"), ))

    is_restrict= models.BooleanField(default=False)
    quantity_restriction = models.IntegerField()
    

    
    
class ProductImage(BaseModel):
    product = models.ForeignKey(Product, related_name="meta_information", on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to="products_image/")
    
    
