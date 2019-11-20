from django.urls import path, include
from wiki.views import PageListView, PageDetailView, PageCreateView


urlpatterns = [
    path('', PageListView.as_view(), name='wiki-list-page'),
    path('<str:slug>/', PageDetailView.as_view(), name='wiki-details-page'),
    path('new_page.html', PageCreateView.as_view(), name='wiki-create-page'),
    # path('accounts/', include('django.contrib.auth.urls')),
]
