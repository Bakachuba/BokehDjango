from bokeh.embed import components
from bokeh.plotting import figure
from django.shortcuts import render


def home(request):
    # create a plot
    plot = figure(width=400, height=400)

    # add a circle renderer with a size, color, and alpha

    plot.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=20, color="navy", alpha=0.5)

    script, div = components(plot)

    return render(request, 'base.html', {'script': script, 'div': div})
