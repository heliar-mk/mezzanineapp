from django.http import HttpResponseRedirect
from mezzanine.pages.page_processors import processor_for
from app.models import Registration
from app.form import RegisterForm


@processor_for(Registration)
def register_form(request, page):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            redirect = request.path + "?sent=1"
            return HttpResponseRedirect(redirect)
    return {"form": form}
