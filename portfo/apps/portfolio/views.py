from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView

from portfo.apps.portfolio.models import Image, Portfolio


class HomeView(ListView):
    model = Image
    template_name = 'portfolio/home.html'

    def get_queryset(self):
        return self.model.objects.order_by('-created_at')


class ImageDetailView(DetailView):
    model = Image
    template_name = 'portfolio/image_details.html'


class AddPortfolioView(LoginRequiredMixin, CreateView):
    model = Portfolio
    template_name = 'portfolio/add_portfolio.html'
    fields = ('name', 'description')

    def form_valid(self, form):
        form.instance.owner_id = self.request.user.id
        return super().form_valid(form)


class PortfoliosView(ListView):
    model = Portfolio
    template_name = 'portfolio/portfolio_list.html'
    fields = ('name', 'description', 'created_at')

    def get_queryset(self):
        return self.model.objects.filter(owner_id=self.request.user).order_by('-created_at')


class PortfolioDetailView(DetailView):
    model = Portfolio
    fields = '__all__'
    template_name = 'portfolio/portfolio_details.html'
