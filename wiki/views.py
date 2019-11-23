from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.urls import reverse_lazy


from wiki.forms import PageForm
from wiki.models import Page
from django.http import HttpResponse, HttpResponseRedirect


class PageListView(ListView):
    """ Renders a list of all Pages. """
    model = Page

    def get(self, request):
        """ GET a list of Pages. """
        pages = self.get_queryset().all()
        return render(request, 'list.html', {
          'pages': pages
        })

class PageDetailView(DetailView):
    """ Renders a specific page based on it's slug."""
    model = Page

    def get(self, request, slug):
        """ Returns a specific wiki page by slug. """
        page = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'page.html', {
          'page': page
        })
class PageCreateView(CreateView):
    form_class = PageForm
    # success_url = reverse_lazy('list.html')
    template_name = "new_page.html"

    def post(self, request, *args, **kwargs):
        form = PageForm(request.POST)
        if form.is_valid():
            wiki = form.save()
            wiki.save()
            return HttpResponseRedirect(reverse_lazy("wiki-details-page", args=[wiki.slug]))
    #     page = page_form.save(commit=False)
    #     page.author = User.objects.get(id=request.POST('author'))
    #     page.save()
    #     return redirect(page)
    # def form_valid(self, form):
    #     return super().form_valid(form)
