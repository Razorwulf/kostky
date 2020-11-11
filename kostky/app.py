from flask import Flask, render_template,session
from random import choice
 
app = Flask(__name__)
#v produkci smazat!
app.debug = True
app.secret_key='ajksdnkdasdfsd'

def nahodny():
    return choice([1, 2, 3,4,5,6])
    
    
    


   
      
     
def vyhra(hrac, pocitac):
    if not 'scorev' in session:
        session['scorev'] = 0
        session['scorep'] = 0

    if hrac ==  pocitac :
        return  "Remíza"

    if hrac > pocitac:
        session['scorev'] = session['scorev'] + 1
        
        return "výhra"

    
    if hrac < pocitac :
        
        session['scorep'] = session['scorep'] + 1
        return "prohra"
        
   

@app.route("/")
def vyber():

    return render_template ("index.html")
@app.route('/h')


@app.route('/hra')
def hra():
   
    hrac=nahodny()
    pocitac = nahodny()
    obrazek=hrac
    obrazekpc = pocitac
    vyhra2 = vyhra(hrac,pocitac)
    scorev = session['scorev'] 
    scorep = session['scorep'] 
   
    return render_template ("hra.html",scorep=scorep,scorev=scorev, pocitac=pocitac, hrac=hrac, vyhra=vyhra2,obrazek=obrazek,obrazekpc=obrazekpc)









 

if __name__ == '__main__':
    app.run()