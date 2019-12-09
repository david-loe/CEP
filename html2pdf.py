from settings import Settings as set
from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration

pdfsize = ["35cm", (str(set.output_ratio[1] * (35 / set.output_ratio[0])) + "cm")]
pdfName = set.name_output + '.pdf'

font = FontConfiguration()
html = HTML(filename=set.path_htmlOutput)
#css_grid = CSS(filename='bootstrap-grid.css', font_config=font)
#css_bootstrap = CSS(filename='bootstrap.css', font_config=font)
css_page = CSS(string='@page {size: ' + pdfsize[0] + ' ' + pdfsize[1] + '; margin = 0cm;}', font_config=font)



#Fehlerbehandlung, damit auch ein PFD erzeugt wird wenn die alte geöffnet ist:
#es wird fortlaufend _0# an den Namen angehängt
try:
    file_output = open(pdfName, 'w')
except:
    for i in range (1,10):
        pdfName = set.name_output + '_0' + str(i) + '.pdf'
        try:
            file_output = open(pdfName, 'w')
        except:
            continue
        else:
            break 

html.write_pdf(target=pdfName, stylesheets=[css_page], font_config=font)
