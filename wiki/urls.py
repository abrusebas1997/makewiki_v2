from django.urls import path, include
from wiki.views import PageListView, PageDetailView, PageCreateView


urlpatterns = [
    path('', PageListView.as_view(), name='wiki-list-page'),
    path('new_page/', PageCreateView.as_view(), name='wiki-create-page'),
    path('<str:slug>/', PageDetailView.as_view(), name='wiki-details-page'),

    # path('accounts/', include('django.contrib.auth.urls')),
]
