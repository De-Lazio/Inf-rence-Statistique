from HTMLPack.html_pack import HTMLDoc
from HTMLPack.balise import Balise
from HTMLPack.balise_meta import BaliseMeta

testIconStr = ""
tableaIconStr = ""
graphIconStr = ""
camabertIconStr = ""

testCouter = 1
RDoc = HTMLDoc("Resultats des Tests", "UTF-8", "ResultatsDocs\css\style-sheet-table.css")
leftDiv = Balise("div", "id = leftDiv", "")
RightDiv = Balise("div", "id = rightDiv", "")

"""
RDoc.body.items.append(Balise("b", "", "Mikpor").getBaliseToString())
RDoc.write("res.html")
"""

def appendToLeftDiv(content:(str)):
    leftDiv.appendContentTxt(content)

def appendToRightDiv(content:(str)):
    RightDiv.appendContentTxt(content)

def defPointRef(i: (int)):
    return "ref{}{}".format(testCouter, i)

def defPartieRef(i: (int)):
    i = i+1
    return "ref{}{}".format(testCouter, (i-1))

def defTestRef():
    return "test{}".format(testCouter)

def creatTest():
    testPoints = Balise("", "", "")
    testContent = Balise("", "", "")
    
def creatPoint(pointTitle, ref, pointIcon):
    point = Balise("div", Balise.fattribut("class", "point"), "")
    
    icon = BaliseMeta("img", "{} {}".format(BaliseMeta.fattribut("class", "sign"), BaliseMeta.fattribut("src", pointIcon)))
    link = Balise("a", BaliseMeta.fattribut("href", "#{}".format(ref)), pointTitle)
    
    point.appendItem(icon.getBaliseToString())
    point.appendItem(link.getBaliseToString())
    
    return point.getBaliseToString()

def creatTestLink(testName, ref, pointStrList):
    details = Balise("details", Balise.fattribut("open", "open"), "")
    summary = Balise("summary", "", "")
    summary.appendItem(creatPoint(testName, ref, testIconStr))
    details.appendItem(summary.getBaliseToString())
    details.appendItems(pointStrList)
    
    return details.getBaliseToString()

def creatPartie(partieName, ref, partieContent):
    div =  Balise("div", Balise.fattribut("class", "partie"), "")
    style = Balise("h3", Balise.fattribut("id", ref), "")
    title = (Balise("u", "", partieName))
    style.appendItem(title.getBaliseToString())
    div.appendItem(style.getBaliseToString())
    div.appendItem(partieContent)
    return div.getBaliseToString()

def creatPartieImg(imgLocation):
    div = Balise("div", Balise.fattribut("class", "imgdiv"), "")
    img = BaliseMeta("img", Balise.fattribut("class", "graph")+ Balise.fattribut("src", imgLocation))
    div.appendItem(img.getBaliseToString())
    return div.getBaliseToString()

def creatPartieLTable(lTable:list):
    if(len(lTable)>1):
        table = Balise("table", "", "")
        thead = Balise("thead", "", "")
        theadRow = Balise("tr", "", "")
        tbody = Balise("tbody", "", "")
        i = 0
        for ligne in lTable:
            tbodyRow = Balise("tr","","")
            for cell in ligne:
                if(i == 0):
                    theadRow.appendItem(Balise("th", "", cell).getBaliseToString())
                    i = 1
                else:
                    tbodyRow.appendItem(Balise("td", "", cell).getBaliseToString())
            tbody.appendItem(tbodyRow.getBaliseToString())
            
        thead.appendItem(theadRow.getBaliseToString())
        table.appendItem(thead.getBaliseToString())
        table.appendItem(tbody.getBaliseToString())
        
        return table.getBaliseToString()
                    
def creatPartieCTable(cTable:list):
    if(len(cTable)>1):
        table = Balise("table", "", "")
        thead = Balise("thead", "", "")
        theadRow = Balise("tr", "", "")
        tbody = Balise("tbody", "", "")
        
        for column in cTable:
            tbodyRow = Balise("tr","","")
            i = 0
            for cell in column:
                if(i == 0):
                    theadRow.appendItem(Balise("th", "", cell).getBaliseToString())
                    i = 1
                else:
                    tbodyRow.appendItem(Balise("td", "", cell).getBaliseToString())
            tbody.appendItem(tbodyRow.getBaliseToString())
            
        thead.appendItem(theadRow.getBaliseToString())
        table.appendItem(thead.getBaliseToString())
        table.appendItem(tbody.getBaliseToString())
        
        return table.getBaliseToString()
            
    else: 
        return "Rien de chez Rien"
    
    
def creatparties(testName, ref, partiesList):
   
    div =  Balise("div", Balise.fattribut("class", "test"),"")
    style = Balise("h2", Balise.fattribut("id", ref), "")
    title = (Balise("u", "", testName))
    style.appendItem(title.getBaliseToString())
    div.appendItem(style.getBaliseToString())
    div.appendItems(partiesList)
    return div.getBaliseToString()
    