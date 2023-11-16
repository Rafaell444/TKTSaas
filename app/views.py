from django.db import connection
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django_tenants.utils import get_tenant_model, get_tenant_domain_model

from .forms import ClientRegistrationForm


def index(request):
    return HttpResponse("<h1>Public მთავარი გვერდი</h1>")


from django.shortcuts import render, redirect
from .forms import ClientRegistrationForm


def register_client(request):
    if request.method == 'POST':
        form = ClientRegistrationForm(request.POST)
        if form.is_valid():
            # Create a new tenant (client)
            tenant = get_tenant_model()(schema_name=form.cleaned_data['schema_name'], name=form.cleaned_data['name'])
            tenant.save()
            domain = get_tenant_domain_model()(domain=form.cleaned_data['schema_name'] + ".localhost", tenant=tenant,
                                               is_primary=True)
            domain.save()

            redirect_url = f"http://{form.cleaned_data['schema_name']}.localhost:8000"
            # Redirect or do other actions as needed
            return redirect(redirect_url)
    else:
        form = ClientRegistrationForm()

    return render(request, 'register_client.html', {'form': form})
