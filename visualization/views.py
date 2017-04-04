from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, View



class IndexView(TemplateView):
    template_name = 'visualization/index.html'
# Create your views here.

class Horizontal_bar_View(View):

    def get(self, request, *args, **kwargs):
        plt.rcdefaults()
        fig, ax = plt.subplots()

        # Example data
        people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
        y_pos = np.arange(len(people))
        performance = 3 + 10 * np.random.rand(len(people))
        error = np.random.rand(len(people))

        ax.barh(y_pos, performance, xerr=error, align='center',
                color='green', ecolor='black')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(people)
        ax.invert_yaxis()  # labels read top-to-bottom
        ax.set_xlabel('Performance')
        ax.set_title('How fast do you want to go today?')

        response = HttpResponse(content_type='image/png')
        fig.savefig(response, format='png')
        return response
