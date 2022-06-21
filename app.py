from cgitb import html
import yfinance as yf # Import Dataset menggunkan library python yfinance #pip install yfinan
from bokeh.models.widgets import Tabs # import Tabs digunakna untuk membuat tab halaman website
from bokeh.io import curdoc # import curdoc 
# Memanggil fungsi Tab Korelasi dan Line 
from Tab_Visualization.Visualization_Corr import Tab_Corellation 
from Tab_Visualization.Visualization_Line import Tab_LinePlot

# Membuat Tab Menu
tab1 = Tab_Corellation(yf)
tab2 = Tab_LinePlot(yf)
tabs = Tabs(tabs = [tab1, tab2])

curdoc().add_root(tabs)
curdoc().title = "Kelompok 7 - Pergerakan Saham Perusahan US"