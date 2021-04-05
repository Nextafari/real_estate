from django.db import models


# Models for the the rent&lease feature

class Properties(models.Model):
    PROPERTY_TYPES = (
        ("01", "RENT"), 
        ("02", "LEASE"),
        ("03", "PURCHASE"))
    class Meta:
        verbose_name = 'Properties'
        verbose_name_plural = 'Properties'
    property_type = models.CharField(max_length=250, choices=PROPERTY_TYPES)
    property_description = models.CharField(max_length=500)
    property_location = models.CharField(max_length=250)
    property_price = models.DecimalField(max_digits=19, decimal_places=2)
    bedroom_desc = models.CharField(max_length=250)
    bathroom_desc = models.CharField(max_length=250)
    toilet_desc = models.CharField(max_length=150)
    property_image = models.ImageField(upload_to="images", default='')

    def __str__(self):
        return self.property_description

