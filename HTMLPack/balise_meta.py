class BaliseMeta():
    
    balise_name = ""
    attribute = ""
    
    items: list = []
    
    def __init__(self, balise_name, attribute):
        
        self.balise_name = balise_name
        self.attribute = attribute
        
    def setAttribute(self, attribute):
        self.attribute = attribute
    
    def appendAttribute(self, new_attribute):
        self.attribute ="{} {}".format(self.attribute, new_attribute)
        
    def setItems(self, items: list):
        self.items = items
    
    def appendItems(self, items: list):
        self.items.append(items)
        
    def fattribut(name, value):
        return "{} = \"{}\"".format(name, value)
    
    def getBaliseToString(self):
        return "<{} {}/>".format(self.balise_name, self.attribute)
        
        
if __name__ == '__main__':
    mabalise = BaliseMeta("HTML", "color= 'black'")
    
    print(mabalise.attribute)
    mabalise.appendAttribute("font-size= '16'")
    print(mabalise.attribute)
    
    mabalise.appendAttribute("font-family= 'Century'")
    print(mabalise.attribute)
    
    print(mabalise.getBaliseToString())
    
    