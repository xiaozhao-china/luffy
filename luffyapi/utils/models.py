from django.db import models

class BaseModel(models.Model):
    # 共有部分
    orders = models.IntegerField(verbose_name='显示顺序')
    is_show=models.BooleanField(verbose_name="是否上架",default=False)
    is_delete=models.BooleanField(verbose_name="逻辑删除",default=False)
    create_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间',null=True,blank=True)
    update_time= models.DateTimeField(auto_now=True,verbose_name='更新时间',null=True,blank=True)

    class Meta:
        #代表数据库迁移时不会形成一张独立的表
        abstract = True

