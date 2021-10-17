
from django.urls import path
from .views import Index,Home_page, dtl_view
app_name = 'dtl'
urlpatterns = [

    path('call/', Index.as_view(),name='index'),
    path('dtl/', Home_page.as_view(),name='home_page'),
    path('dtlv/', dtl_view,name='dtl_view'),
    path('api/', index_api,name='index_api'),


]
