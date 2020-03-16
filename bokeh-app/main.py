import pandas as pd
import numpy as np

from bokeh.io import curdoc
from bokeh.layouts import column, widgetbox, row, gridplot
from bokeh.models import ColumnDataSource, Slider
from bokeh.plotting import figure

x = np.linspace(-np.pi, np.pi, 201)
y = np.sin(x)

source=ColumnDataSoucrce(data={'x':x,'y':y})

plot=figure(x_axis_label = 'x')

plot.line=('x','y', source=source, color='red')

slider=Slider(start = 1, end = 10, step = 1, value = 1)

def callback(attr, old, new):
  c=slider.value
  new_y=c*np.sin(x)
  
  source.data={'x':x,'y':new_y}

slider.on_change('value',callback)

layout=row(widgetbox(slider)),plot

curdoc.add_root(layout)

