from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# from django.views.generic.create import FormView

from wiki.models import Page


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
# class PageCreateView(FormView):
#     template_name = "page.html"
#     form_class = PageForm
#     success_url = '/'
#
#     def post(self, request):
#         page_form = PageForm(request.POST)
#         page = page_form.save(commit=False)
#         page.author = User.objects.get(id=request.POST('author'))
#         page.save()
#         return redirect(page)
#     def form_valid(self, form):
#         return super().form_valid(form)
