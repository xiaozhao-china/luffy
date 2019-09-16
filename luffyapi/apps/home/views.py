from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers,models
# Create your views here.



class Home(APIView):
    def get(self,request):
        print(request)
        # return HttpResponse('ok')
        return Response({'s':[1,2,3,4,[3],{'s':'d'}]})


# class BannerAPIView(APIView):
#     def get(self,request,*args,**kwargs):
#         queset = models.Banner.objects.all()
#         serializer = serializers.BannerSerializer(queset,many=True)
#         return Response(serializer.data)

from rest_framework.generics import ListAPIView
from luffyapi.settings import constant
class BannerListAPIView(ListAPIView):
    #设置要返回的数据资源
    queryset = models.Banner.objects.filter(is_delete=False,is_show=True).order_by('-orders')[0:constant.BANNER_LIMIT_COUNT]
    #格式化返回的数据（有哪些字段，数据深度）
    serializer_class = serializers.BannerModelSerializer