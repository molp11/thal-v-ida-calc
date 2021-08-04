from os.path import join, dirname
import pandas as pd
from bokeh.io import curdoc
from bokeh.layouts import row, column, layout
from bokeh.models import ColumnDataSource, Div
from bokeh.models.widgets import TextInput, DataTable, TableColumn, HTMLTemplateFormatter
from bokeh.plotting import figure

def callback(attrname, old, new):
    
    update()
    
def update():
    try:
        ef = round(float(mcv.value) - float(rbc.value) - 5*float(hb.value) - 3.4, 2)
        rbci = round(float(rbc.value), 2)
        mentzer = round(float(mcv.value) / float(rbc.value), 2)
        rivastava = round(float(mch.value) / float(rbc.value), 2)
        sl = round(float(mcv.value)**2 * float(mch.value) / 100, 2)
        bessman = round(float(rdw.value), 2)
        ricerca = round(float(rdw.value) / float(rbc.value), 2)
        gk = round(float(mcv.value)**2 * float(rdw.value) / (100 * float(hb.value)), 2)
        jayabose = round(float(mcv.value) * float(rdw.value) / (float(rbc.value)), 2)
        sirdah = round(float(mcv.value) - float(rbc.value) - 3*float(hb.value), 2)
        ehsani = round(float(mcv.value) - 10*float(rbc.value), 2)
        values = [ef, mentzer, rivastava, sl, bessman, ricerca, gk, jayabose, sirdah, ehsani]

        source.data = pd.DataFrame(dict(index=index,
                                        calculation=calculation,
                                        cutoff=cutoff,
                                        value=values)) 
    except:
        pass

rbc = TextInput(value='', title="RBC (10¹²/L)", width=200, height=50)
rbc.on_change('value', callback)

hb = TextInput(value='', title="Hb (g/dL)", width=200, height=50)
hb.on_change('value', callback)

mcv = TextInput(value='', title="MCV (fL)", width=200, height=50)
mcv.on_change('value', callback)

mch = TextInput(value='', title="MCH (pg)", width=200, height=50)
mch.on_change('value', callback)

rdw = TextInput(value='', title="RDW (fL)", width=200, height=50)
rdw.on_change('value', callback)

cutoff = [0, 13, 3.8, 1530, 15, 4.4, 65, 220, 27.0, 15]
index = ['England and Fraser (E&F)', 'Mentzer', 'Srivastava', 'Shine and Lal (S&L)', 'Bessman', 'Ricerca', 
                                           'Green and King (G&K)', 'Jayabose (RDW index)', 'Sirdah', 'Ehsani']
calculation = ['MCV - RBC - (5 Hb) - 3.4', 'MCV / RBC', 'MCH / RBC', 'MCV² x MCH / 100', 'RDW', 'RDW / RBC', 
                                                 'MCV² x RDW / 100 Hb', 'MCV x RDW / RBC', 'MCV - RBC - (3 Hb)', 'MCV - (10 RBC)']
value = ['', '', '', '', '', '', '', '', '', '']
source = ColumnDataSource(data=dict(index=index,
                                    calculation=calculation,
                                    cutoff = cutoff,
                                    value=value)) 

template="""                
            <p style="color:<%= 
                (function colorfromint(){
                    if (0 < cutoff - value)
                        {return('blue')}
                    else if (0 > cutoff - value)
                        {return('red')}
                    else if (0 == cutoff - value)
                        {return('black')}
                    else 
                        {return('grey')}
                    }()) %>; padding-top: 0px; border: 0px; line-height: 0px;"> 
                <%= value %>
            </p>
            """
formatter =  HTMLTemplateFormatter(template=template)

columns = [
    TableColumn(field='index', title='Discriminant index'),
    TableColumn(field='calculation', title='Calculation'),
    TableColumn(field='cutoff', title='Cut-off value'),
    TableColumn(field='value', title='Value', formatter=formatter),
]

table = DataTable(source=source, columns=columns, width=700,
                        height=700, selectable=True, editable=True)

desc = Div(text=open(join(dirname(__file__), "description.html")).read(), width=1000)

sizing_mode = 'scale_width'
l = layout([
    [desc],
    [row(column(rbc, hb, mcv, mch, rdw), table)]
], sizing_mode=sizing_mode)

update()

curdoc().add_root(l)
curdoc().title = "thal_v_ida_calc"