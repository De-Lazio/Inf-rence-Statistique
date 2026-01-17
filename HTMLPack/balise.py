class Balise():
    
    balise_name = ""
    attribute = ""
    content_txt = ""
    
    items: list = []
    
    def __init__(self, balise_name, attribute, content_txt):
        
        self.balise_name = balise_name
        self.attribute = attribute
        self.content_txt = content_txt
        
    def setAttribute(self, attribute):
        self.attribute = attribute
    
    def appendAttribute(self, new_attribute):
        self.attribute ="{} {}".format(self.attribute, new_attribute)
        
        
    def setContentTxt(self, content_txt):
        self.content_txt = content_txt
        
    def appendContentTxt(self, new_content_txt):
        self.content_txt = "{} {}".format(self.content_txt, new_content_txt)
        
    def setItems(self, items: list):
        self.items = items
    
    def appendItem(self, item):
        self.items.append(item)
    def appendItems(self, items: list):
        self.items.append(items)
    
    def fattribut(name, value):
        return "{} = \"{}\" ".format(name, value)
        
    def getBaliseToString(self):
        
        content = self.content_txt
        for element in self.items:
            content = "{} {}".format(content, element)
        return "<{} {}>{}</{}>".format(self.balise_name, self.attribute, content, self.balise_name)
        
        
if __name__ == '__main__':
    mabalise = Balise("HTML", "color= 'black'", "Nous somme les meilleurs")
    
    print(mabalise.attribute)
    mabalise.appendAttribute("font-size= '16'")
    print(mabalise.attribute)
    
    mabalise.appendAttribute("font-family= 'Century'")
    print(mabalise.attribute)
    
    print(mabalise.getBaliseToString())
    
    