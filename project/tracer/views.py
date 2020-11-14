from django.shortcuts import render
from django.views.generic import View
from .models import TrackedUsers
from django.http import Http404, JsonResponse


class IndexView(View):
    def get(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        amount = TrackedUsers.objects.all().count()
        tracked_user, created = TrackedUsers.objects.get_or_create(ip=ip)

        return render(
            request,
            "index.html",
            context={
                'amount': amount
            }
        )


def get_amount(request):
    if request.is_ajax():
        amount = TrackedUsers.objects.all().count()
        return JsonResponse(
            {
                "response": "Success",
                "amount": amount
            }
        )
    else:
        raise Http404