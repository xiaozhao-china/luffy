import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'luffyapi.settings.dev')
import django
django.setup()


#测试django的代码
# import logging
# log = logging.getLogger('django')
#
# log.error('订单交易失败')
