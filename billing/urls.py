from django.urls import path

from . import views

urlpatterns = [
    path('tenants/', views.TenantCreateView.as_view(), name = 'create_tenant'),
    path('plans/', views.PlanCreateView.as_view(), name = 'create_plan'),
    path('subscriptions/', views.SubscriptionsCreateView.as_view(), name = 'create_subscription'),
    path('usage/', views.UsageEventListCreateView.as_view(), name = 'usage'),
    path('invoices/generate/', views.InvoiceAPIView.as_view(), name = 'generate_invoices'),
    path('invoices/<int:pk>/pay/', views.InvoicesPay.as_view(), name = 'pay_invoice'),
    path('tenants/me/', views.TenantMeView.as_view(), name = 'tenant_me'),
    path('subscriptions/current/', views.CurrentSubscriptionView.as_view(), name = 'current_subscription'),
    path('invoices/', views.InvoiceListView.as_view(), name = 'list_invoices'),
]
