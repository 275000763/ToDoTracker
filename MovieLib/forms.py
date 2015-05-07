from MovieLib.models import todo

class MovieMixin(object):
    model = todo
    def get_context_data(self, **kwargs):
        kwargs.update({'object_name':'Movie'})
        return kwargs