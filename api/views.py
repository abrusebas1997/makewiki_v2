# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.shortcuts import get_object_or_404
#
# from wiki.models import Page
# from api.serializers import PageSerializer
#
#
# class PageList(APIView):
#     def get(self, request):
#         pages = Page.objects.all()[:20]
#         data = PageSerializer(pages, many=True).data
#         return Response(data)
#
# class PageDetail(APIView):
#     def get(self, request, pk):
#         page = get_object_or_404(Page, pk=pk)
#         data = PageSerializer(page).data
#         return Response(data)
