from os.path import join, dirname
import pandas as pd
from bokeh.io import curdoc
from bokeh.layouts import row, column, layout
from bokeh.models import ColumnDataSource, Div
from bokeh.models.widgets import TextInput, DataTable, TableColumn, HTMLTemplateFormatter
from bokeh.plotting import figure

def mchc(hb, hct):
    
    return hb*100/hct

def callback(attrname, old, new):
    
    update()
    
def update():
    try:
        ef = round(float(mcv.value) - float(rbc.value) - 5*float(hb.value) - 3.4, 2)
        rbci = round(float(rbc.value), 2)
        mentzer = round(float(mcv.value) / float(rbc.value), 2)
        srivastava = round(float(mch.value) / float(rbc.value), 2)
        sl = round(float(mcv.value)**2 * float(mch.value) / 100, 2)
        bessman = round(float(rdw.value), 2)
        ricerca = round(float(rdw.value) / float(rbc.value), 2)
        gk = round(float(mcv.value)**2 * float(rdw.value) / (100 * float(hb.value)), 2)
        dasgupta = round(1.89*float(rbc.value) - 0.33*float(rdw.value) - 3.28) 
        jayabose = round(float(mcv.value) * float(rdw.value) / (float(rbc.value)), 2)
        telmissani_mchd = round(float(mch.value) / float(mcv.value), 2)
        telmissani_mdhl = round(float(mch.value) * float(rbc.value) / float(mcv.value), 2)
        huberherklotz = round((float(mch.value) * float(rdw.value)) / (10 * float(rbc.value)) + float(rdw.value), 2)
        kermani = round(float(mcv.value)*float(mch.value)/float(rbc.value), 2)
        kermanii = round((float(mcv.value)*float(mch.value)*10) / (float(rbc.value)*mchc(float(hb.value), float(hct.value))), 2)
        sirdah = round(float(mcv.value) - float(rbc.value) - 3*float(hb.value), 2)
        ehsani = round(float(mcv.value) - 10*float(rbc.value), 2)
        keikhaei = round((float(hb.value)*float(rdw.value)*100)/(float(rbc.value)**2 * mchc(float(hb.value), float(hct.value))), 2)
        nishad = round(0.615*float(mcv.value) + 0.518*float(mch.value) + 0.446*float(rdw.value), 2)
        wongprachum = round(float(mcv.value)*float(rdw.value)/float(rbc.value) - 10*float(hb.value), 2)
        sehgal = round(float(mcv.value)**2 / float(rbc.value), 2)
        pornprasert = round(mchc(float(hb.value), float(hct.value)), 2)
        sirachainan = round(1.5 * float(hb.value) - 0.05 * float(mcv.value), 2)
        bordbar = round(abs(80 - float(mcv.value)) * abs(27 - float(mch.value)), 2)
        values = [ef, rbci, mentzer, srivastava, sl, bessman, ricerca, gk, dasgupta, jayabose, telmissani_mchd, telmissani_mdhl, 
                  huberherklotz, kermani, kermanii, sirdah, ehsani, keikhaei, nishad, wongprachum, sehgal, pornprasert, sirachainan, bordbar]

        source.data = pd.DataFrame(dict(index=index,
                                        calculation=calculation,
                                        direction=direction,
                                        cutoff=cutoff,
                                        value=values))
    except:
        pass

rbc = TextInput(value='', title="RBC (10¹²/L)", width=200, height=50)
rbc.on_change('value', callback)

hb = TextInput(value='', title="Hb (g/dL)", width=200, height=50)
hb.on_change('value', callback)

hct = TextInput(value='', title="HCT (%)", width=200, height=50)
hct.on_change('value', callback)

mcv = TextInput(value='', title="MCV (fL)", width=200, height=50)
mcv.on_change('value', callback)

mch = TextInput(value='', title="MCH (pg)", width=200, height=50)
mch.on_change('value', callback)

rdw = TextInput(value='', title="RDW (fL)", width=200, height=50)
rdw.on_change('value', callback)

cutoff = [0, 5.0, 13, 3.8, 1530, 15, 4.4, 65, 0, 220, 0.34, 1.75, 20, 300, 85, 27.0, 15, 21, 59, 104, 972, 31, 14, 44.76]
direction = ['<', '>', '<', '<', '<', '<', '<', '<', '>', '<', '<', '>', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '>', '>']
index = ['England and Fraser (E&F)', 'RBC', 'Mentzer', 'Srivastava', 'Shine and Lal (S&L)', 'Bessman', 'Ricerca', 
         'Green and King (G&K)', 'Das Gupta', 'Jayabose (RDW index)', 'Telmissani - MCHD', 'Telmissani - MDHL',
         'Huber-Herklotz', 'Kerman I', 'Kerman II', 'Sirdah', 'Ehsani', 'Keikhaei', 'Nishad', 'Wongprachum', 'Sehgal',
         'Pornprasert', 'Sirachainan', 'Bordbar']
calculation = ['MCV - RBC - (5 Hb) - 3.4', 'RBC', 'MCV / RBC', 'MCH / RBC', 'MCV² x MCH / 100', 'RDW', 'RDW / RBC', 
               'MCV² x RDW / (100 Hb)', '1.89 RBC - 0.33 RDW - 3.28', 'MCV x RDW / RBC', 
               'MCH / MCV', 'MCH x RBC / MCV', '(MCH x RDW / (10 RBC)) + RDW', 'MCV x MCH / RBC', '(MCV x MCH x 10) / (RBC x MCHC)',
               'MCV - RBC - (3 Hb)', 'MCV - (10 RBC)', '(Hb x RDW x 100) / (RBC² x MCHC)', '0.615 MCV + 0.518 MCH + 0.446 RDW',
               '(MCV x RDW / RBC) - 10 Hb', 'MCV² / RBC', 'MCHC', '1.5 Hb - 0.05 MCV', '|80 - MCV| x |27 - MCH|']
value = ['']*len(index)
source = ColumnDataSource(data=dict(index=index,
                                    calculation=calculation,
                                    direction=direction,
                                    cutoff=cutoff,
                                    value=value)) 

template="""                
            <p style="color:<%= 
                (function colorfromint(){
                    if (value - cutoff > 0 && direction == '>')
                        {return('blue')}
                    else if (value - cutoff < 0 && direction == '<')
                        {return('blue')}
                    else if (value - cutoff < 0 && direction == '>')
                        {return('red')}
                    else if (value - cutoff > 0 && direction == '<')
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
    TableColumn(field='direction', title='Thalassemia'),
    TableColumn(field='cutoff', title='Cut-off value'),
    TableColumn(field='value', title='Value', formatter=formatter),
]

table = DataTable(source=source, columns=columns, width=700,
                        height=1000, selectable=True, editable=True)

desc = Div(text=open(join(dirname(__file__), "description.html")).read(), width=1000)

sizing_mode = 'scale_width'
l = layout([
    [desc],
    [row(column(rbc, hb, hct, mcv, mch, rdw), table)]
], sizing_mode=sizing_mode)

update()

curdoc().add_root(l)
curdoc().title = "thal_v_ida_calc"