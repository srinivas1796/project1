from django.db import models

class MerchantModel(models.Model):
    merchant_id = models.IntegerField(primary_key=True)
    merchant_name = models.CharField(max_length=30)
    merchant_contact = models.IntegerField(unique=True)
    merchant_email = models.EmailField(unique=True)
    merchant_password = models.CharField(max_length=10)


class ProductsModel(models.Model):
    p_no=models.IntegerField(primary_key=True)
    p_name=models.CharField(max_length=30)
    p_price=models.FloatField()
    p_quantity=models.IntegerField()
    m_id=models.ForeignKey(MerchantModel,on_delete=models.CASCADE)