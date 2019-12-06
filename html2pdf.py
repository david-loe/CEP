from settings import Settings as set
from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration

pdfsize = ["35cm", (str(set.output_ratio[1] * (35 / set.output_ratio[0])) + "cm")]


font = FontConfiguration()
html = HTML(filename=set.path_htmlOutput)
#css_grid = CSS(filename='bootstrap-grid.css', font_config=font)
#css_bootstrap = CSS(filename='bootstrap.css', font_config=font)
css_page = CSS(string='@page {size: ' + pdfsize[0] + ' ' + pdfsize[1] + '; margin = 0cm;}', font_config=font)


""" 
!TBD: Fehlerbehandlung, damit auch ein PFD erzeugt wird wenn die alte geöffnet ist. 
try:
    file_output = open(set.name_output + '.pdf', 'w')
except:
    for i in range (1,10):
        try:
            file_output = open(set.name_output + '_0' + str(i) + '.pdf', 'w')
        except:
            continue
        break """

html.write_pdf(target=set.name_output + '.pdf', stylesheets=[css_page], font_config=font)
