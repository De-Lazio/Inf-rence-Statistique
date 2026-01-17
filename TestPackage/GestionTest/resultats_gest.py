from HTMLPack.html_pack import HTMLDoc
from HTMLPack.balise import Balise
from HTMLPack.balise_meta import BaliseMeta


resultPath = "file:///E:/WorkSpace/pycharmeWorkspace/Base/ResultatsDocs/resultats.html"
testIconStr = "images/test.png"
tableaIconStr = "images/table.png"
graphIconStr = "images/histo.png"
camabertIconStr = "images/camabert.png"
testCouter = 1
grahFolder = "ResultatsDocs/graph/"
RDoc = """
<!DOCTYPE html>
<html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel ="stylesheet" href="css/style-sheet-table.css"/>
        <title>Resultats des tests</title>
    </head>
    
    <body>
    
        <!--Div de gauche-->
        <div id="links_div" >
            {}
        </div>
        
        <!--Div de droit-->
        <div id="content_div" >   
            {}
        </div>
        
    </body>
</html>
"""


leftDiv =""
rightDiv = ""


def defRefTestPartie(i: (int)):
    return "ref{}{}".format(testCouter, i)


def formatFloat(value):
    return "{0:.4f}".format(value)

def formatpValue(value):
    return "{0:.5f}".format(value)

#Regeneration
def refreshHtmlResult():
        with open("ResultatsDocs/resultats.html", "w", encoding="UTF-8") as fic:
            fic.write(RDoc.format(leftDiv, rightDiv))

#Formatage des points d'un Teste
def formatTestLeft(testTitle:(str), pointStrList:(str)):
        return """
                <details open="open" >
                    <summary >
                        <img class="lk_t_logo" src="images/test.png" />
                        <a href="#ref{}" class="lk">{}</a>
                    </summary>
                    
                    {}
                    
                </details>
                """.format(testCouter, testTitle, pointStrList)
    
def formatPoint(pointCounter:(int), pointtitle:(str), icon:(str)):
    return """
            <div class="tst_lk" >
                <img class="lk_logo" src="{}" />
                <a href="#ref{}{}" class="lk">{}</a>
            </div>
            """.format(icon, str(testCouter), str(pointCounter), pointtitle)
            
            
def formatImgPartie(partieCounter:(int), partieTitle:(str), partieImg:(str)):
    return """
            <div class="partie" >
                <h3 id="ref{}{}" ><u >{}</u></h3>
                <div class="imgdiv" >
                    <img class="graph" src="graph/{}" />
                </div>
            </div>
            """.format(testCouter, partieCounter, partieTitle, partieImg)
            
def formatTableHPartie(partieCounter:(int), partieTitle:(str), table:(list)):
    
    cells = ""
    cellsTitle = ""
    for cell in table[0]:
        cellsTitle = cellsTitle + "<th >{}</th>".format(cell)
    cellsTitle = "<tr> {} </tr>".format(cellsTitle)
        
    for line in table[1:]:
        for cell in line:
            cells = cells + "<td >{}</td>".format(cell)
        cells = "<tr> {} </tr>".format(cells)
     
    return """
            <div class="partie" >
                <h3 id="ref{}{}" ><u >{}</u></h3>
                <table >
                    <thead > 
                        {} 
                    </thead>
                    
                    <tbody > 
                        {} 
                    </tbody>
                </table>
            </div>
            """.format(testCouter, partieCounter, partieTitle, cellsTitle, cells)
            
def formatTestRight(testTitle:(str), testContent:(str)):
    return """
            <div class="test" >
                <h2 id="ref{}" ><u >{}</u></h2>
                {}
            </div>
            """.format(testCouter, testTitle, testContent)
        
def appendLeftDiv(content):
    leftDiv = leftDiv + content

def appendRightDiv(content):
    rightDiv = rightDiv + content