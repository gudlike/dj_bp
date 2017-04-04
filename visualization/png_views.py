#encoding=utf-8
from django.http import HttpResponse
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

def simple(request):
    import random
    import datetime

    from matplotlib.figure import Figure
    from matplotlib.dates import DateFormatter

    fig = Figure()
    ax = fig.add_subplot(111)
    x = []
    y = []
    now = datetime.datetime.now()
    delta = datetime.timedelta(days=1)
    for i in range(10):
        x.append(now)
        now += delta
        y.append(random.randint(0, 1000))
    ax.plot_date(x, y, '-')
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()
    canvas = FigureCanvas(fig)
    response = HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response

def masked_line(request):
    x = np.arange(0, 2 * np.pi, 0.02)
    y = np.sin(x)
    y1 = np.sin(2 * x)
    y2 = np.sin(3 * x)
    ym1 = np.ma.masked_where(y1 > 0.5, y1)
    ym2 = np.ma.masked_where(y2 < -0.5, y2)

    lines = plt.plot(x, y, x, ym1, x, ym2, 'o')
    plt.setp(lines[0], linewidth=4)
    plt.setp(lines[1], linewidth=2)
    plt.setp(lines[2], markersize=10)

    plt.legend(('No mask', 'Masked if > 0.5', 'Masked if < -0.5'),
               loc='upper right')
    plt.title('Masked line demo')
    response = HttpResponse(content_type='image/png')
    plt.savefig(response, format='png')
    return response
