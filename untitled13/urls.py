"""untitled13 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from mysite import views
from django.contrib.auth import views as auth_views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('test/', views.test),
                  path('test_t/', views.test_1, name='test'),
                  path('', views.main),
                  path('accounts/', include('django.contrib.auth.urls')),
                  path('project_menage/', views.project_menage, name='project_menage'),
                  path('project_menage/create_measure_item/<str:id>', views.create_measure_item,
                       name='project_item_create'),
                  path('project_menage/create/', views.project_create, name='project_create'),
                  path('project_menage/create/delet_item/<str:id>', views.project_item_delet_js,
                       name='project_item_delet'),
                  path('project_menage/create/update_item/<str:id>', views.project_measure_item_update_js,
                       name='update_project_item'),
                  path('work_order/', views.work_order_display),
                  path('work_order/delet_js/<str:id>', views.work_order_delet, name='work_order_delet'),
                  path('work_order/update_js/<str:id>', views.work_order_update, name='work_order_update'),
                  path('update/work_order/<str:id>', views.update_work_order, name='update_work_order'),
                  path('work_order/measure_item/<str:id>', views.work_measure_item_display,
                       name='work_order_item_display'),
                  path('work_order/measure_item_delet/<str:id>', views.work_order_item_delet_js,
                       name='work_order_item_delet'),
                  path('work_order/measure_item_update/<str:id>', views.work_order_measure_item_update,
                       name='work_order_item_update'),
                  path('measure_work_order_data_display/', views.measure_work_order_data_display),  # 顯示工單所量測完成的數據。
                  path('measure_work_order_data_display/update_js/<str:id>', views.work_order_form_update_parts_remake, name='work_order_form_update_parts_remake'),
                  path('measure_work_order_data_display/<str:id>', views.work_order_measure_data_form, name='work_data_display'),
                  path('form_measure_tool/', views.measure_tool),
                  path('form_measure_item/', views.measure_item),
                  path('project_display/project/', views.project_display_project),
                  path('project_display/work_order/', views.project_display_work_order),
                  path('project_display/tool/', views.project_display_tool),
                  path('project_display/item/', views.project_display_item),
                  # path('delet/<str:id>', views.delet),
                  path('delet/project/<str:id>', views.delet_project, name='project_delet'),
                  path('update/project/<str:id>', views.update_project, name='update_project'),
                  # path('delet/work_order/<str:id>', views.delet_work_order, name='work_order_delet'),
                  # path('update/work_order/<str:id>', views.update_work_order, name='update_work_order'),
                  path('delet/measure_tool/<str:id>', views.delet_tool, name='tool_delet'),
                  path('update/measure_tool/<str:id>', views.update_tool, name='update_tool'),
                  path('delet/measure_item/<str:id>', views.delet_item, name='item_delet'),
                  path('update/v/<str:id>', views.update_item, name='update_item'),
                  path('item_image/<str:id>', views.measure_item_image_show, name='items_image_show'),
                  path('measure_data_display/', views.data_display_project),
                  path('measure_data_display/<str:id>', views.measure_data_display_show, name='measuredata_display'),
                  path('measure_data_display/display_all/<str:id>', views.display_all_measure_data_chart),
                  path('measure_data_display/timely/<str:id>', views.display_data_timely),
                  path('measure_data_display/report/<str:id>', views.display_all_report),
                  # path('measure_data_display/display_all/<str:id>', views.display_all_measure_data_chart),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
