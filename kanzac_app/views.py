from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .serilaizers import *


class UserCreateView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserGetView(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "tg_id"


class CategoryListView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ProductListView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        cat_id = self.request.query_params.get('cat_id')
        return Product.objects.filter(category_id=cat_id)


class ProductGetView(RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = "id"


class OrderCreateView(APIView):
    def post(self, request):
        user_id, product_id = request.data['user_id'], request.data['product_id'],
        product = Product.objects.get(id=product_id)
        product.quan -= 1
        product.save()
        user = User.objects.get(tg_id=user_id)
        new_order = Order.objects.create(user=user, product=product)
        return Response(data={"id": new_order.id}, status=status.HTTP_200_OK)


class OrderGetView(APIView):
    def get(self, request):
        user_id = request.query_params.get('tg_id')
        user = User.objects.get(tg_id=user_id)
        res = Order.objects.filter(user=user).exists()
        if res:
            return Response(data={"status": True}, status=status.HTTP_200_OK)
        return Response(data={"status": False}, status=status.HTTP_200_OK)


class VideoListView(RetrieveAPIView):
    serializer_class = VideoSerializer
    lookup_field = "id"
    queryset = Video.objects.all()
