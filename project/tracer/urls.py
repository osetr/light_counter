from django.urls import path
from .views import IndexView, get_amount

urlpatterns = [
    path(r'', IndexView.as_view(), name='index_v'),
    path(
        r"ajax/get_amount/",
        get_amount,
        name="get_amount_v",
    ),
]
