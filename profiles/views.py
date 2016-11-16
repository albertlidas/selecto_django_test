from django.views.generic import ListView
from .models import Profile
import operator
from django.db.models import Q, Count


class ProfilesListView(ListView):
    model = Profile
    paginate_by = 10
    template_name = 'profiles.html'
    context_object_name = 'profiles'

    def get_queryset(self):
        result = super(ListView, self).get_queryset()

        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            result = result.filter(
                reduce(operator.and_,
                       (Q(first_name__startswith=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(last_name__startswith=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(phone__startswith=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(address__startswith=q) for q in query_list))
            )

        if 'created_asc' == self.request.GET.get('ordering'):
            result = result.order_by('date_created')
        elif 'created_desc' == self.request.GET.get('ordering'):
            result = result.order_by('-date_created')
        elif 'comments_asc' == self.request.GET.get('ordering'):
            result = result.annotate(num_comments=Count('comment')).order_by('num_comments')
        elif 'comments_desc' == self.request.GET.get('ordering'):
            result = result.annotate(num_comments=Count('comment')).order_by('-num_comments')
        return result
