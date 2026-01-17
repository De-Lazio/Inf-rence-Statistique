from .balise import Balise

class HTMLDoc():
    html = Balise("HTML","", "")
    head = Balise("head","", "")
    body = Balise("body","", "")
    
    
    def __init__(self, title, charset, style_sheet):
        self.setHead(title, charset, style_sheet)
    
    def setHead(self, title, charset, style_sheet):
        self.head.setItems(["<meta charset='{}'> <meta http-equiv='X-UA-Compatible' content='IE=edge'><meta name='viewport' content='width=device-width, initial-scale=1.0'><title>{}</title><link rel='stylesheet' type='text/css' href='{}'>".format(charset, title, style_sheet)])
      
    def write(self, file_path, test):
        with open(file_path, "w") as fic:
            fic.write(test)  
            
    def formatHTML(self, test):
        self.html.setItems([self.head.getBaliseToString()])
        self.html.appendItem(self.body.getBaliseToString())
        return test
         
if __name__ == '__main__':
    my_doc = HTMLDoc("Resultats des TEst", "UTF-8", "")
    
    my_doc.body.items.append(Balise("b", "", "Mikpor").getBaliseToString())
    my_doc.write("res.html")
