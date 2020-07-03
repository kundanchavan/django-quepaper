from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from .forms import Conatctform
from .forms import Mark20
from django.views.generic import View
from .utils import render_to_pdf

# Create your views here.



def main(request):
    return render(request, 'main.html')


def contact(request):
    if request.method == 'POST':
        form = Conatctform(request.POST)
        if form.is_valid():
            sub = form.cleaned_data['sub']
            date = form.cleaned_data['date']
            Q1 = form.cleaned_data['Q1']
            Q2 = form.cleaned_data['Q2']
            Q3 = form.cleaned_data['Q3']
            Q4 = form.cleaned_data['Q4']
            Q5 = form.cleaned_data['Q5']
            Q6 = form.cleaned_data['Q6']
            Q2a = form.cleaned_data['Q2a']
            Q2b = form.cleaned_data['Q2b']
            Q3a = form.cleaned_data['Q3a']
            Q3b = form.cleaned_data['Q3b']
            Q4a = form.cleaned_data['Q4a']
            Q4b = form.cleaned_data['Q4b']
            Q5a = form.cleaned_data['Q5a']
            Q5b = form.cleaned_data['Q5b']
            Q5c = form.cleaned_data['Q5c']
            Q5d = form.cleaned_data['Q5d']
            Q5e = form.cleaned_data['Q5e']

            context = {
                'sub': sub,
                'date': date,
                'Q1': Q1,
                'Q2': Q2,
                'Q3': Q3,
                'Q4': Q4,
                'Q5': Q5,
                'Q6': Q6,
                'Q2a': Q2a,
                'Q2b': Q2b,
                'Q3a': Q3a,
                'Q3b': Q3b,
                'Q4a': Q4a,
                'Q4b': Q4b,
                'Q5a': Q5a,
                'Q5b': Q5b,
                'Q5c': Q5c,
                'Q5d': Q5d,
                'Q5e': Q5e
            }
            # return render(request, 'quepaper.html', context)
            template = get_template('quepaper.html')
            html = template.render(context)
            pdf = render_to_pdf('quepaper.html', context)
            return HttpResponse(pdf, content_type='application/pdf')
    form = Conatctform()
    return render(request, 'form.html', {'form': form})

def formmark20(request):
    if request.method == 'POST':
        form = Mark20(request.POST)
        if form.is_valid():
            sub = form.cleaned_data['sub']
            date = form.cleaned_data['date']
            Q1 = form.cleaned_data['Q1']
            Q2 = form.cleaned_data['Q2']
            Q3 = form.cleaned_data['Q3']
            Q4 = form.cleaned_data['Q4']
            Q5 = form.cleaned_data['Q5']
            Q6 = form.cleaned_data['Q6']
            Q2a = form.cleaned_data['Q2a']
            Q2b = form.cleaned_data['Q2b']
            Q2c = form.cleaned_data['Q2c']
            Q2d = form.cleaned_data['Q2d']

            context = {
                'sub': sub,
                'date': date,
                'Q1': Q1,
                'Q2': Q2,
                'Q3': Q3,
                'Q4': Q4,
                'Q5': Q5,
                'Q6': Q6,
                'Q2a': Q2a,
                'Q2b': Q2b,
                'Q2c': Q2c,
                'Q2d': Q2d
            }
            template = get_template('quepaper2.html')
            html = template.render(context)
            pdf = render_to_pdf('quepaper2.html', context)
            return HttpResponse(pdf, content_type='application/pdf')

    form = Mark20()
    return render(request, 'form2.html', {'form': form})