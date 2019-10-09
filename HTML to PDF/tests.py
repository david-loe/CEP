#HTML to PDF
#09.10.2019

#Available formats
#16:9 // Beamer
#4:3 //  Beamer 
#A4 //   Normal

#Libarys
from Html2Pdf import pisa as htmlconv #HTMlConverter

#Grab the Data


path_html = open("index.html","r") #read only
html_source = path_html.read()     #extract the HTMl data in a String


output_name = "final.pdf"           
output_path ="C:/Users/Dominik\Documents/CEP/CEP/HTML to PDF/teeest/"
output_path_name = output_path+output_name


class HTMLconv_error():             #class for errors
    def htmlconv_path_error():
        if output_path == "":
            print("no filepath, the file will create in the local path")


def convertHTMLtoPDF(html_source, output_path_name):
    result_pdf_file = open(output_path_name, "w+b")   #open/create ouptutfile to write in it
    #convert HTML to PDF                                               
    htmlconvStatus = htmlconv.CreatePDF(html_source, #the HTML to convert e.g index.html
    dest=result_pdf_file)                            #dest = destination // outputfile
    result_pdf_file.close()                          #close after writing the HTML in it
    return htmlconvStatus.err

# Main program
if __name__ == "__main__":
    htmlconv.showLogging()
    convertHTMLtoPDF(html_source,output_path_name)
    HTMLconv_error.htmlconv_path_error()


