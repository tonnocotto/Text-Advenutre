import time
import random
import sys,time,os

soldi = 50.0
nome_gioco = "24:00"
prompt = "> "

def invio(numero):
    separatore(numero)
    raw_input("premi invio per continuare\n" + prompt)
    separatore(numero)
def pausa(testo, tempo):
    testo = str(testo)
    print testo
    tempo = float(tempo)
    time.sleep(tempo)
def animazione(testo,tempo):
    testo = str(testo)
    tempo = float(tempo)
    for char in testo:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(tempo)
def separatore(numero):
    print "=" * numero
def scelta():
    print "scegli un'opzione\n[1] Vai a nord\n[2] Vai a sud\n[3] Vai a est\n[4] Vai a ovest\n[5] Vai al menu'"
    separatore(30)
    opzione = ""

    while opzione != "1" and opzione != "2" and opzione != "3" and opzione != "4" and opzione != "5":
        opzione = raw_input(prompt)
        opzione = str(opzione)

    separatore(30)
    return opzione       

def salva(soldi):
    save = open("salvataggi.txt", "w")
    save.write(str(soldi))
def leggi():
    global soldi
    try:
        f = open("salvataggi.txt", "r")
        codice = f.read()
        if codice == "":
          soldi = 50.0
        else:
          soldi = float(codice)
    except IOError:
        soldi = 50.0
    finally:
        f.close()

def menu():
    separatore(30)
    animazione ("\tMenu'", 0.1)
    separatore(30)

    print "Scegli un'opzione\n[1] Gioca\n[2] Guida\n[3] Carica un capitolo\n[4] Statistiche"
    separatore(30)

    opzione = ""

    while opzione != "1" and opzione != "2" and opzione != "3" and opzione != "4": #input validation  
      opzione = str(raw_input(prompt))

    separatore(30)

    if opzione == "1":
        intro()
        
    if opzione == "2":
        guida()
    
    if opzione == "3":
        pausa("scegli il capitolo da caricare\n[1] Introduzione\n[2] Capitolo 1 - La casa\n[3] Capitolo 2 - Primi ed ultimi ricordi\n[4] Indietro",0.0)
        separatore(30)

        opzione_1 = ""
        while opzione_1 != "1" and opzione_1 != "2" and opzione_1 != "3":
            opzione_1 = str(raw_input(prompt))
        
        if opzione_1 == "2":
            capitolo_1()
            separatore(30)

        if opzione_1 == "1":
            intro()
            separatore(30)

        if opzione_1 == "3":
            capitolo_2
            separatore(30)

        if opzione_1 ==  "4":
            menu()        

    if opzione == "4":
        animazione("Statistiche\nSoldi: %s euro" % soldi, 0.1)
def guida(): # non finito
    separatore(30)
    print "-" * 10 + " Regolamento " + "-" * 10
    separatore(30)
    print "\n\tPagina 1 - azioni\n "
    print "Quando vedi scritto \">\" significa che devi scrivere qualcosa."
    print "Nella maggior parte dei casi vedrai \">\" quando ti trovi davanti ad una scelta tra 2 o piu' opzioni che ti verranno indicate."
    print "Negli altri casi probabilmente dovrai inserire un dato che non influenza la storia del gioco,"
    print "per esempio la scelta del nome. In questi casi il potrai scrivere qualsiasi cosa tu voglia!"
    print "Ogni volta che il gioco ti fa inserire un testo potrai torn\n"

    separatore(30)
    print "Scegli una di queste opzioni:\n[1]Prossima pagina\n2]Torna al menu'"
    separatore(30)
    opzione = raw_input( prompt)
def intro(): # non finito
    pausa("E' tardo pomeriggio e ti trovi in una piccola citta' chiamata Morio-cho.", 2.5) #cambiare il nome della citta'
    pausa("Nessun abitante sembra conoscerti.", 2.0)
    pausa("Non ricordi nulla sul tuo passato.", 2.0) #ho scritto questo per non dare un background al personaggio
    pausa("L'unico ricordo che hai e' quello di star tornando a casa dopo una lunga giornata.", 2.5)
    pausa("Dato che hai completamente perso la memoria decidi di cercare casa tua nel tentativo di recuperare qualche ricordo.", 3.5) 
    pausa("Aprendo il portafogli trovi una carta d'identita' strappata a meta' e rovinata.", 2.5) 
    pausa("Si riesce malapena a leggere la via ed alcune delle tue caratteristiche fisiche.", 3.0) 
    separatore(30)
    animazione("Via = Le Mani dal Naso\n\nCONNOTATI E CONTRASSEGNI SALIENTI\n\nStatura : 190cm\nCapelli : biondi\nOcchi : azzurri\n", 0.1) # cambiare nome alla via
    separatore(30)
    time.sleep(1.5)
    pausa("Non sai dove si trovi la via.", 1.0)
    invio(30)
def capitolo_1(): # non finito
    global soldi
    cap = 1 
    loop = 0
    big_loop = 0
    indizio = 0

    animazione("\nCapitolo 1 - La casa \n\n", 0.1) # cambiare nome
    separatore(30)

    while big_loop == 0:
        
        while loop == 0: # finito

            if loop == 0:
                pausa("Ti trovi in una piazza.", 1.3)
                pausa("A nord c'e' una chiesa.", 1.3)
                pausa("A sud c'e' una gelateria.", 1.0)
                pausa("A est c'e' un viale.", 1.3)
                pausa("A ovest c'e' un'altro viale.", 1.3)
                invio(30)

            opzione = scelta()

            if opzione == "1": # finito
                pausa("Sei entrato in chiesa.", 1.0)
                pausa("Ci sono delle persone che pregano.",1.0)
                invio(30)
            
            if opzione == "2": # finito
                loop = "gelateria"
                break
                
            if opzione == "3": # finito
                loop = 1
                break
            
            if opzione == "4": # fuinito
                if indizio == 1:
                    pausa("E' quasi sera", 1.0)
                loop = 3
                break
            
            if opzione == "5": # finito
                big_loop = 1
                menu()
                break
        
        while loop == "gelateria": # finito
            if loop == "gelateria":
                pausa("Entri nella gelateria.", 1.5)
                pausa("Hai %g euro." % soldi, 1.5)
                pausa("Un gelato costa 2.50 euro.", 1.5)
                invio(30)

            print "Lo vuoi comprare?\n[1]Si\n[2]No\n[3]Indietro\n[4]Menu'"
            separatore(30)

            opzione_11 = ""
            while opzione_11 != "1" and opzione_11 != "2" and opzione_11 != "3" and opzione_11 != "4":
                opzione_11 = str(raw_input(prompt))

            if opzione_11 == "1":
                if soldi < 2.50:
                    pausa("Non hai abbastanza soldi.", 1.0)
                    loop = 0
                    invio(30)
                    break
                else:
                    pausa("Mangi il gelato ed esci dalla gelateria", 1.0)
                    soldi = soldi - 2.50
                    salva(soldi)
                    pausa("Ora hai %g euro." % soldi, 1.0)
                    invio(30)
                    loop = 0
                    break

            if opzione_11 == "2" or opzione_11 == "3":
                pausa("Esci dalla gelateria.",1.0)
                invio(30)
                loop = 0
                break
            
            if opzione_11 == "4":
                menu()

        while loop == 1: # finito

            if loop == 1:

                pausa("Sei entrato nel viale.", 1.0)
                pausa("a est c'e' un' edicola.", 1.0)
                pausa("a ovest c'e' un viale.",1.0)
                invio(30)

            print"scegli un'opzione\n[1] Vai a est\n[2] Vai a ovest\n[3] Vai al menu'"
            separatore(30)

            opzione_3 = ""

            while opzione_3 != "1" and opzione_3 != "2" and opzione_3 != "3":
                opzione_3 = raw_input(prompt)
                opzione_3 = str(opzione_3)

            separatore(30)

            if opzione_3 == "1":
                loop = 2
                break

            if opzione_3 == "2":
                loop = 0

            if opzione_3 == "3":
                menu()

        while loop == 2: # finito
            
            if loop == 2: 
                pausa("Sei davanti all'edicola.", 1.0)
                invio(30)

            pausa ("scegli un'opzione\n[1] Compra il giornale\n[2] Indietro\n[3] Vai al menu'", 0.0)
            separatore(30)

            opzione_0 = ""

            while opzione_0 != "1" and opzione_0 != "2" and opzione_0 != "3":
                opzione_0 = raw_input(prompt)
                opzione_0 = str(opzione_0)

            separatore(30)
                        
            if opzione_0 == "1":
                loop = "giornalaio"
                break

            if opzione_0 == "2":
                loop = 1
                break

            if opzione_0 == "3":
                menu()

        while loop == "giornalaio":
            pausa("Hai %s euro." % soldi, 1.0)
            pausa("Il giornale costa 0.70 euro.", 1.0)
            pausa("Lo vuoi comprare?", 1.0)

            separatore(30)
            print "Scelgi un' opzione\n[1]Si\n[2]No\n[3]Menu'"
            separatore(30)

            opzione_12 = ""

            while opzione_12 != "1" and opzione_12 != "2" and opzione_12 != "3":
                opzione_12 = str(raw_input(prompt))
            separatore(30)

            if opzione_12 == "1":
                if soldi < 0.70:
                    pausa("Non hai abbastanza soldi.", 1.0)
                    invio(30)
                    loop = 2 
                    break
                else:
                    soldi =  soldi - 0.70
                    salva(soldi)
                    
                    pausa("Hai comprato il giornale.", 1.0)
                    pausa("Ti rimangono %s euro." % soldi , 1.0)
                    
                    separatore(30)
                    pausa("Sul giornale c'e' scritto:",1.0)
                    animazione("Vai 2 volte ad ovest,\n a sud ed infine di nuovo ad ovest\n", 0.1)
                    time.sleep(0.5)
                    invio(30)

                    indizio = 1

                    loop = 2
                    break

            if opzione_12 == "2":
                loop = 2
                break

            if opzione_12 == "3":
                menu()
                break
        
        while loop == 3: # finito
            
            if loop == 3:

                pausa("Sei entrato nel viale.", 1.0)
                pausa("A nord c'e' un cantiere", 1.0)
                pausa("A sud c'e' un viale", 1.0)
                pausa("A est c'e' una piazza", 1.0)
                pausa("A ovest c'e' un'altro vicolo.", 1.0)
                invio(30)

                opzione_2 = scelta()

            if opzione_2 == "1":
                pausa("Non c'e' nessun operaio", 1.0)
                invio(30)
            
            if opzione_2 == "2":
                loop = 4
                break

            if opzione_2 == "3":
                loop = 0
                break

            if opzione_2 == "4":
                loop = 8
                break

            if opzione_2 == "5":
                big_loop = 1
                menu()
                break
                
        while loop == 4: # finito
            
            if loop == 4:
                                                                                            
                pausa("Sei entrato nel viale", 1.0)
                pausa("A nord c'e' un viale.", 1.0)
                pausa("A sud c'e' un viale.", 1.0)
                pausa("A est c'e' un viale.", 1.0)
                pausa("A ovest c'e' un viale.", 1.0)
                invio(30) 

            opzione_4 = scelta()

            if opzione_4 == "1":
                loop = 3
                break

            if opzione_4 == "2":
                loop = 5
                break

            if opzione_4 == "3": #sistemare
                loop = 7
                break

            if opzione_4 == "4":
                loop = 9
                break

            if opzione_4 == "5":
                big_loop = 1
                menu()
                break
        
        while loop == 5: # finito
            
            if loop == 5:

                pausa("Sei entrato nel viale.", 1.0)
                pausa("A nord c'e' un viale.", 1.0)
                pausa("A sud in ristorante", 1.0)
                pausa("A est c'e' un viale.", 1.0)
                pausa("A ovest c'e' un negozio di viestiti.", 1.0)
                invio(30)
                opzione_5 = scelta()

            if opzione_5 == "1":
                loop = 4
                break

            if opzione_5 == "2":
                pausa("Il ristorante e' ancora chiuso.", 1.0)
                invio(30)

            if opzione_5 == "3":
                loop = 6
                break

            if opzione_5 == "4":
                pausa("Sei davanti al negozio di vestiti.", 2.0)
                pausa("I tuoi vestiti sono in perfette condizioni.", 2.0)
                invio(30)

            if opzione_5 == "5":
                big_loop = 1
                menu()
                break
        
        while loop == 6: # finito
            
            if loop == 6:

                pausa("Sei entrato nel viale.", 1.0)
                pausa("A nord c'e' un viale.", 1.0)
                pausa("A sud c'e' una statua.", 1.0)
                pausa("A est c'e' un viale.", 1.0)
                pausa("A ovest c'e' un viale.", 1.0)
                invio(30)

            opzione_6 = scelta()

            if opzione_6 == "1": #finito
                loop = 7
                break

            if opzione_6 == "2":
                pausa("Sei davanti alla statua.", 1.0)
                pausa("La statua e' dedicata ai morti in guerra.", 1.0)
                invio(30)

            if opzione_6 == "3":
                loop = 11
                break

            if opzione_6 == "4":
                loop = 5

            if opzione_6 == "5":
                big_loop = 1
                menu()
                break

        while loop == 7: # finito
            
            if loop == 7:

                pausa("Sei entrato nel viale.", 1.0)
                pausa("A nord c'e' il retro di una gelateria.", 1.0)
                pausa("A sud c'e' una fumetteria.", 1.0)
                pausa("A est c'e' un panificio.", 1.0)
                pausa("A ovest c'e' un viale.", 1.0)
                invio(30)

                opzione_7 = scelta()

                if opzione_7 == "1":
                    pausa("La gelateria non ha un'entrata nel retro.", 1.0)
                    invio(30)

                if opzione_7 == "2":
                    pausa("Il proprietario e' maleducato.", 1.0)
                    invio(30)

                if opzione_7 == "3":
                    pausa("Entri nel panificio.", 1.0)
                    pausa("Compri una focaccia la mangi fuori dalla panetteria.", 1.5)
                    invio(30)

                if opzione_7 == "4":
                    loop = 4
                    break

                if opzione_7 == "5":
                    big_loop = 1
                    menu()
                    break

        while loop == 8: # finito

            if loop == 8:
                pausa("Sei entrato nel viale.", 1.0)
                pausa("A nord c'e' un negozio di scarpe.", 1.0)
                pausa("A sud c'e' un cancello.", 1.0)
                pausa("A est c'e'un viale.", 1.0)
                pausa("A ovest c'e' un libreria.", 1.0)    
                invio(30)

            opzione_8 = scelta()

            if opzione_8 == "1":
                pausa("Le scarpe che hai indosso sono tutte rovinate.", 1.0)
                pausa("Ti compri delle scarpe nuove.", 1.0)
                invio(30)

            if opzione_8 == "2":
                pausa("Sei davanti al cancello.", 1.0)
                pausa("Ti affacci e vedi una casa", 1.0)

            if opzione_8 == "3":
                loop = 3
                break
            
            if opzione_8 == "4":
                pausa("Entri in libreria.", 1.0)
                pausa("Compri un libro e vai via.", 1.0)
                invio(30)

            if opzione_8 == "5":
                big_loop = 1
                menu()
                break

        while loop == 9: # finito
            if loop == 9:
                pausa("Sei entrato nel viale.", 1.0)
                pausa("A nord c'e' un cancello.", 1.0)
                pausa("A sud c'e' una stazione.", 1.0)
                pausa("A est c'e' un viale.", 1.0)
                pausa("A ovest c'e' una casa.", 1.0)
                invio(30)
            opzione_9 = scelta()

            if opzione_9 == "1":
                pausa("Ti affacci e vedi un viale normalissimo.", 1.0)
                invio()

            if opzione_9 == "2":
                pausa("La stazione e' chiusa", 1.0)
                invio(30)

            if opzione_9 == "3":
                loop = 4
                break
            
            if opzione_9 == "4":
                loop = 10
                break

            if opzione_9 == "5":
                big_loop = 1
                menu()
                break
        
        while loop == 10:
            if loop == 10:
                animazione("Sei davanti a casa tua.", 0.1)
                invio(30)
            
            print "scegli un'opzione\n[1] Entra\n[2] Indietro\n[3] Vai al menu'"
            separatore(30)

            opzione_10 = ""

            while opzione_10 != "1" and opzione_10 != "2" and opzione_10 != "3":
                opzione_10= str(raw_input(prompt))

            if opzione_10 == "1":
                pausa("Prima di entrare leggi il nome e cognome scritti sul campanello.", 1.5)

                global nome

                nome = raw_input("A quanto pare ti chiami:\n" + prompt)

                separatore(30)
                animazione("FINE CAPITOLO 1", 1.0)
                invio(30)

                print "scegli un'opzione\n[1] Prossimo capitolo\n[2] Ripeti capitolo 1\n[3] Vai al menu'"

                opzione_11 = ""

                while opzione_11 != "1" and opzione_11 != "2" and opzione_11 != "3":
                    opzione_11 = str(raw_input(prompt)) 

                if opzione_11 == "1":
                    os.system('cls')
                    big_loop = 1
                    break
                        
                if opzione_11 == "2":
                    loop = 0
                    break

                if opzione_11 == "3":
                    menu()

            if opzione_10 == "2":
                loop = 9
                break

            if opzione_10 == "3":
                menu()

        while loop == 11:
            if loop == 11:
                pausa("Sei entrato nel viale.", 1.0)
                pausa("A nord c'e' un viale.", 1.0)
                pausa("A sud c'e' una statua.",1.0)
                pausa("A est c'e' un supermercato.", 1.0)
                pausa("A ovest c'e' un viale", 1.0)
                invio(30)
            
            opzione_12 = scelta()

            if opzione_12 == "1":
                pass

            if opzione_12 == "2":
                pass

            if opzione_12 == "3":
                pass

            if opzione_12 == "4":
                loop = 6
                break

            if opzione_12 == "5":
                menu()
            
def capitolo_2():
    animazione("Capitolo 2 - Primi ed ultimi ricordi", 0.1)
    capitolo = 2
    Loop = 0
    big_loop = 0
    indizio = 0

leggi()
menu()
#invio(30)

capitolo_1()
invio(30)
capitolo_2()
