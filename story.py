#-*-coding: utf-8-*-
import time
import random
import sys,time,os

global Loop_1 

foto = 0
n_foto = 0
loop_1 = 0
soldi = 50.0
big_loop_1 = 0
nome_gioco = "24:00"
prompt = "> "
indizio = 0

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
    for char in testo:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(tempo)

    print ""
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
def scambio():
    global foto, n_foto, indizio, soldi
    loop = 0
    big_loop = 0

    pausa("Parli con il signore sulla panchina", 1.5)

    while big_loop == 0:

        if foto == 0:
            loop = 0
        else:
            loop = 2
        
        if foto == 1: # finito
            obbiettivo = "una chiesa"
        if foto == 2: # finito
            obbiettivo = "una statua dedicata ai caduti in guerra"
        if foto == 3: # finito
            obbiettivo = "una fontana"
        if foto == 4: # finito
            obbiettivo = "una statua dedicata ad uno scrittore"
        if foto == 5: # finito
            obbiettivo = "una freccia"
        if foto == 6:
            foto = 1
            obbiettivo = "una chiesa"
        else:
            obbiettivo = "una chiesa"

        while loop == 0:
            if loop == 0:
                pausa("Sembra una persona benestante", 1.0)
                pausa("Dice che ha da qualche anno una grave malattia alle gambe e che ormai non puo' piu' utilizzarle.", 2.5)
                pausa("Gli rimane sono un mese di vita.", 1.0)
                pausa("Vorrebbe visitare la citta' in cui e' nato un'ultima volta prima di morire.", 2.5)
                pausa("Ma dato che tutto cio' non e' possibile si accontenterebbe anche di delle foto.", 2.5)
                pausa("Ti chiede se lo vuoi aiutare e scattare quelle foto per lui.", 2.0)

                separatore(30)

            print "Scelgi un'opzione\n[1] Accetta l'incarico\n[2] Rifiuta\n[3] Indietro\n[4] Menu'"
            separatore(30)

            opzione = ""
            
            while opzione != "1" and opzione != "2" and opzione != "3" and opzione != "4":
                opzione = str(raw_input(prompt))

            separatore(30)

            if opzione == "1":
                pausa("Ti dice che e' disposto a pagarti molto.", 1.0)
                loop = 1
                break

            elif opzione == "2":
                pausa("Hai rifiutato l'incarico.", 1.0)
                invio(30)
                capitolo_1(12)

            elif opzione == "3":
                invio(30)
                capitolo_1(12)

            else:
                menu()

        while loop == 1:
            foto += 1
            
            salva()

            if loop == 1:
                pausa("Vuole che gli porti una foto di %s." % obbiettivo, 1.5)
                pausa("Ti ringrazia.", 1.0)
                invio(30)
                break


        while loop == 2:

            print "Scegli un'opzione:\n[1] Consegna foto\n[2] Nuova consegna\n[3] Indietro\n[4] Menu'"
            separatore(30)
            opzione_1 = ""

            while opzione_1 != "1" and opzione != "2" and opzione != "3" and opzione != "4":
                opzione_1 = raw_input(prompt)

            separatore(30)

            if opzione_1 == "1":
                s_foto = float(n_foto * 5.00)
                soldi += s_foto
                if n_foto != 0:
                    pausa("Consegni %s foto." % n_foto , 1.0)
                    pausa("Il vecchio ti da %g euro per ogni foto." % s_foto, 1.2)
                    pausa("Ora hai %s euro." % soldi, 1.0)
                else:
                    pausa("Non hai foto da consegnare", 1.0)
                    invio(30)

                separatore(30)

                n_foto = 0
                salva()

            elif opzione_1 == "2":
                pausa("Chiedi al vecchio altre foto da scattare.")
                loop = 1
                break

            elif opzione == "3":
                capitolo_1(12)
            
            else:
                menu()
    
def scatta():
    loop = 0
    scatto = 1
    while loop == 0:

        print "Scegli un'opzione\n[1] Scatta foto\n[2] Indietro\n[3] Menu'"

        opzione = ""

        while opzione != "1" and opzione != "2" and opzione != "3":
            opzione = raw_input(prompt) 

        if opzione == "1":
            if scatto != "1":
                print "Hai già scattato una foto in questo luogo."
            else:
                pausa("Hai scattato la foto.", 1.0)
                n_foto += 1
            invio(30)
            continue

        if opzione == "3":
            menu()
        
        salva()

    return opzione
def continua(numero, n):
    global loop_1
    loop_1 = n

    separatore(numero)
    print "Vuoi continuare?\n[1] Si\n[2] No"
    separatore(numero)
    risposta = ""
    while risposta != "1" and risposta != "2":    
        risposta = raw_input(prompt)

    if risposta == "1":
        loop_1 += 1
    if risposta == "2":
        menu()       

def salva():
    global indizio
    
    try:
        with open("salvataggi.txt"):
            with open("salvataggi.txt ", "w") as score:
                score.write(str(soldi))
                score.write(str(foto))
                score.write(str(n_foto))
                score.write(str(indizio))

    except IOError:
        with open("salvataggi.txt", "w") as score:
            score.write(soldi,"\n", foto, "\n", n_foto, "\n", indizio)
def leggi():

    try:
        f = open("salvataggi.txt", "r")
        soldi_1 = f.readline(1)
        foto_1 = f.readline(2)
        n_foto_1 = f.readline(3)
        indizio_1 = f.readline(4)

        if foto_1 == "":
            foto = 0

        elif soldi_1 == "":
            soldi = 50.0

        elif n_foto_1 == "":
            n_foto = 0

        elif indizio_1 == "":
            indizio = 0
        else:
            soldi = float(soldi_1)
            foto = float(foto_1)
            n_foto = float(n_foto_1)
            indizio = float(indizio_1)


    except IOError:
        soldi = 50.0
        foto = 0
        indizio = 0
        n_foto = 0
    finally:
        f.close()

def menu():
    global loop_1
    loop = 0 
    big_loop = 0

    while big_loop == 0:    
        if big_loop != 0:
            break

        while loop == 0:
            if loop != 0:
                break

            separatore(30)
            animazione("\n\tMenu'\n", 0.1)
            separatore(30) 

            print "Scegli un'opzione\n[1] Gioca\n[2] Guida\n[3] Carica un capitolo\n[4] Statistiche"
            separatore(30)

            opzione = ""

            while opzione != "1" and opzione != "2" and opzione != "3" and opzione != "4": #input validation  
                opzione = str(raw_input(prompt))

            separatore(30)

            if opzione == "1":
                
                loop_1 = 1
                intro()
                break
                
            if opzione == "2":
                guida()
            
            if opzione == "3":
                loop = 1
                break

            if opzione == "4":
                print "Statistiche\nSoldi: %s euro" % soldi
                
                if foto != 0:
                    print "Foto: %s" % foto

                invio(30)
                time.sleep(2.0)     

        while loop == 1:
            if loop != 1:
                break

            pausa("scegli il capitolo da caricare\n[1] Introduzione\n[2] Capitolo 1\n[3] Capitolo 2\n[4] Indietro",0.0)
            separatore(30)

            opzione_1 = ""
            while opzione_1 != "1" and opzione_1 != "2" and opzione_1 != "3" and opzione_1 != "4":
                opzione_1 = str(raw_input(prompt))
            
            if opzione_1 == "2":
                loop_1 = 2
                big_loop = 1
                break

            if opzione_1 == "1":
                loop_1 = 1
                big_loop = 1
                break
                
            if opzione_1 == "3":
                loop_1 = 3
                big_loop = 1
                break
        
            if opzione_1 ==  "4":
                loop = 0
                break
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

    animazione("\n\tIntroduzione\n", 0.1)
    separatore(30)

    pausa("E' tardo pomeriggio e ti trovi in una piccola citta' chiamata Morio-cho.", 2.7) #cambiare il nome della citta'
    pausa("Nessun abitante sembra conoscerti.", 2.0)
    pausa("Non ricordi nulla sul tuo passato.", 2.0) #ho scritto questo per non dare un background al personaggio
    pausa("L'unico ricordo che hai e' quello di star tornando a casa dopo una lunga giornata.", 3.0)
    pausa("Dato che hai completamente perso la memoria decidi di cercare casa tua nel tentativo di recuperare qualche ricordo.", 4.0) 
    pausa("Aprendo il portafogli trovi una carta d'identita' strappata a meta' e rovinata.", 3.5) 
    pausa("Si riesce malapena a leggere la via ed alcune delle tue caratteristiche fisiche.", 3.5) 
    invio(30)
    animazione("Via = Le Mani dal Naso\n\nCONNOTATI E CONTRASSEGNI SALIENTI\n\nStatura : 190cm\nCapelli : biondi\nOcchi : azzurri", 0.1) # cambiare nome alla via
    separatore(30)
    time.sleep(1.5)
    pausa("Non sai dove si trovi la via.", 1.0)
    continua(30, 1)
def capitolo_1(n_loop): # non finito
    global soldi, indizio
    loop = n_loop
    big_loop = 0



    while big_loop == 0:
        
        while loop == 0: # finito

            if loop == 0:
                separatore(30)
                animazione("\n\tCapitolo 1 - La casa\n", 0.1) # cambiare nome
                separatore(30)
                
                pausa("Ti trovi in una piazza.", 1.3)
                pausa("A nord c'e' una chiesa.", 1.3)
                pausa("A sud c'e' un'edicola.", 1.0)
                pausa("A est c'e' un viale.", 1.3)
                pausa("A ovest c'e' un'altro viale.", 1.3)
                invio(30)

            opzione = scelta()

            if opzione == "1": # finito
                if foto == 1:
                    loop = "chiesa"
                    break
                else:
                    pausa("Sei entrato in chiesa.", 1.0)
                    pausa("Ci sono delle persone che pregano.",1.0)
                    invio(30)
            
            if opzione == "2": # finito
                loop = 2
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
        
        while loop == "chiesa": # finito
            if loop == "chiesa":
                pausa("Sei davanti alla chiesa.", 1.0)

            separatore(30)
            print "scegli un'opzione\n[1] Entra\n[2] Scatta una foto\n[3] Indietro\n[4] Menu'"
            
            opzione_14 = ""

            while opzione_14 != "1" and opzione_14 != "2" and opzione_14 != "3" and opzione_14 != "4":
                opzione_14 = raw_input(prompt)

            separatore(30)

            if opzione == "1":
                pausa("Sei entrato in chiesa.", 1.0)
                pausa("Ci sono delle persone che pregano.", 1.0)
                invio(30)
            
            if opzione == "2":
                pausa("Hai scattato la foto.", 1.0)
                n_foto += 1
                salva()
                invio(30)

            if opzione == "3":
                loop = 0
                break

            if opzione == "4":
                menu()
                break

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

        while loop == "giornalaio": #finito
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
                    salva()
                    
                    pausa("Hai comprato il giornale.", 1.0)
                    pausa("Ti rimangono %s euro." % soldi , 1.0)
                    
                    separatore(30)
                    pausa("Sul giornale c'e' scritto:",1.0)
                    animazione("Vai 2 volte ad ovest,\na sud ed infine di nuovo ad ovest", 0.1)
                    time.sleep(0.5)
                    invio(30)

                    indizio = 1
                    salva()

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
                pausa("A nord c'e' un cantiere.", 1.0)
                pausa("A sud c'e' un viale.", 1.0)
                pausa("A est c'e' una piazza.", 1.0)
                pausa("A ovest c'e' un viale.", 1.0)
                invio(30)

                opzione_2 = scelta()

            if opzione_2 == "1":
                pausa("Non c'e' nessun operaio.", 1.0)
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
                loop = "vestiti"
                invio(30)

            if opzione_5 == "5":
                big_loop = 1
                menu()
                break

        while loop == "vestiti": # finito
            if loop == "vestiti":
                pausa("Sei entrato nel negozio di vestiti.", 1.0)
                pausa("Hai %s euro." % soldi, 0.5)
                pausa("Una maglietta costa 8.00 euro.", 1.0)
                invio(30)

            print "La vuoi comprare?\n[1] Si\n[2] No\n[3] Indietro\n[4] Menu'"

            opzione_13 = ""
        
            while opzione_13 != "1" and opzione_13 != "2" and opzione_13 != "3" and opzione_13 != "4":
                opzione_13 = str(raw_input(prompt))
            
            if opzione_13 == "1":
                
                if soldi < 8.00:
                    pausa("Non hai abbastanza soldi.")
                    loop = 5
                    invio(30)
                    break
                else:
                    soldi = soldi - 8.00
                    pausa("Hai comprato una maglietta.", 1.0)
                    pausa("Ora hai %s euro" % soldi , 1.0)
                    loop = 5
                    invio(30)
                    salva()
                    break

            if opzione_13 == "2" or opzione_13 == "3":
                loop = 5
                invio(30)
                break

            if opzione_13 == "4":
                menu()

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
                if foto == "2":
                    scatta()
                    if scatta == "2":
                        continue
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
                    pausa("Sei entrato nel panificio.", 1.0)
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
                pausa("A ovest c'e' una fontana.", 1.0)    
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
                pausa("Sei davanti alla fontana.", 1.0)
                pausa("Ci sono tante monete nel fondo.", 1.0)
                if foto == 3:
                    scatta()

                    if scatta == "2":
                        continue
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
                animazione("FINE CAPITOLO 1", 0.1)
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
                pausa("A est c'e' un museo.", 1.0)
                pausa("A ovest c'e' un viale", 1.0)
                invio(30)
            
            opzione_12 = scelta()

            if opzione_12 == "1":
                loop = 12
                break

            if opzione_12 == "2":
                pausa("Sei davanti alla statua.", 1.0)
                pausa("E' dedicata ad uno scrittore morto da tempo.", 1.5)
                if foto == 4:
                    scatta()

                    if scatta == "2":
                        continue
                invio(30)

            if opzione_12 == "3":
                loop = "museo"

            if opzione_12 == "4":
                loop = 6
                break

            if opzione_12 == "5":
                menu()

        while loop == "museo":
            if loop == "museo":
                pausa("Sei entrato nel museo.", 1.0)
                pausa("A nord c'e' una freccia.", 1.5)
                pausa("A sud c'e' l'uscita.", 1.0)
                pausa("A est c'e' un'elmo.")
                pausa("A ovest c'e' uno scudo.")

            opzione_15 = scelta()
            
            if opzione_15 == "1":
                pausa("Sei davantia alla freccia.", 1.0)
                pausa("Questa freccia sembra essere vecchia qualche centinaio di anni.", 2.0)
                if foto == 5:
                    scatta()
                    
                    if scatta == "2":
                        continue

                invio(30)

            elif opzione_15 == "2":
                loop = 11
                break

            elif opzione_15 == "3":
                pausa("Sei davanti all'elmo", 1.0)
                pausa("Questo elmo sembra essere vecchia qualche centinaio di anni.", 2.0)
                invio(30)

            elif opzione_15 == "4":
                pausa("Sei davanti allo scudo.", 1.0)
                pausa("Questo scudo sembra essere vecchia qualche centinaio di anni.", 2.0)
                invio(30)

            else:
                menu()

        while loop == 12:
            if loop == 12:
                pausa("Sei entrato nel viale.", 1.0)
                pausa("A nord c'e' un vecchio seduto su una panchina.", 2.0)
                pausa("A sud c'e' un viale", 1.0)
                pausa("A est c'e' una gelateria.", 1.0)
                pausa("A ovest c'e' una macelleria", 1.0)
                invio(30)

            opzione_16 = scelta()

            if opzione_16 == "1":
                scambio()

            elif opzione_16 == "2":
                loop == 11
                break

            elif opzione_16 == "3":
                loop == "gelateria"

            elif opzione_16 == "4":
                pausa("La coda e' troppo lunga.", 1.0)
                invio(30)

            else:
                menu()

        while loop == "gelateria":
            if loop == "gelateria":
                pausa("Sei entrato in gelateria.",1.0)
                pausa("Un gelato costa 2.50 euro",1.0)
                pausa("Hai %s euro"% soldi, 1.0)

            print "Lo vuoi comprare?\n[1] Si\n[2] No\n[3] Menu'"

            opzione_17 = ""

            while opzione_17 != "1" and "2" and "3":
                opzione_17 = raw_input(prompt)

            if opzione_17 == "1":
                if soldi > 2.50:
                    soldi = soldi -  2.50

                    salva()

                    pausa("Compri il gelato.", 1.0)
                    pausa("Ora hai %s euro." % soldi)
                else:
                    pausa("Non hai abbastanza soldi.")

                invio(30)
                loop = 12
                break

            if opzione_17 == "2":
                pausa("Non compri il gelato")

                invio(30)
                loop = 12
                break

            else:
                menu()         
def capitolo_2(numero): # non finito
    animazione("Capitolo 2 - Primi ed ultimi ricordi", 0.1)
    Loop = numero
    big_loop = 0

leggi()
scambio()

while loop_1 == 0:
    if loop_1 != 0:
        break        
    menu()    
while loop_1 == 1:
    if loop_1 != 1:
        break
    intro()
while loop_1 == 2:
    if loop_1 != 2:
        break
    capitolo_1(12)
while loop_1 == 3:
    if loop_1 != 3:
        break
    capitolo_2()
