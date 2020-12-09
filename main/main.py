import cap_1

nome_gioco = "24:00"
time_sleep = True
note = ""
soldi = 50.0

def invio(numero):
    separatore(numero)
    raw_input("premi invio per continuare\n" + prompt)
    separatore(numero)
def pausa(testo, tempo):
    if time_sleep == False:
        tempo = 0.0

    testo = str(testo)
    print testo
    tempo = float(tempo)
    time.sleep(tempo)
def animazione(testo,tempo):
    
    for char in testo:
        sys.stdout.write(char)
        sys.stdout.flush()
        if time_sleep == True:
            time.sleep(tempo)

    print ""
def separatore(numero):
    print "=" * numero

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

                score.writelines([str(soldi), "\n", str(foto), "\n", str(n_foto), "\n", str(indizio), "\n", str(time_sleep), "\n", str(frammento), "\n", str(polaroid), "\n", str(note)])

    except IOError:
        with open("salvataggi.txt", "w") as score:
            score.writelines([ str(soldi),"\n", str(foto), "\n", str(n_foto), "\n", str(indizio), "\n", str(time_sleep), "\n", str(frammento), "\n", str(polaroid), "\n", str(note)])
def leggi(): 
    
    try:
        
        f = open("salvataggi.txt", "r")
        soldi_1 = f.readline()
        foto_1 = f.readline()
        n_foto_1 = f.readline()
        indizio_1 = f.readline()
        time_sleep_1 = f.readline()
        frammento_1 = f.readline()
        polaroid_1 = f.readline()
        note_1 = f.readline()

        if foto_1 == "":
            foto = 0

        elif soldi_1 == "":
            soldi = 50.0

        elif n_foto_1 == "":
            n_foto = 0

        elif indizio_1 == "":
            indizio = 0

        elif time_sleep_1 == "":
            time_sleep = True

        elif frammento_1 == "":
            frammento = 0

        elif polaroid_1 == "":
            polaroid = False

        else:
            soldi = float(soldi_1)
            foto = int(foto_1)
            n_foto = int(n_foto_1)
            indizio = int(indizio_1)
            time_sleep = bool(time_sleep_1)
            frammento = int(frammento_1)
            polaroid = bool(polaroid_1)
            note = str(note_1)


    except IOError:
        soldi = 50.0
        foto = 0
        indizio = 0
        n_foto = 0
        time_sleep = True
        frammento = 0
        note = ""
    finally:
        f.close()

def menu():
    global loop_1, foto, time_sleep
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

            print "Scegli un'opzione\n[1] Gioca\n[2] Guida\n[3] Carica un capitolo\n[4] Statistiche\n[5] Impostazioni"
            separatore(30)

            opzione = ""

            while opzione != "1" and opzione != "2" and opzione != "3" and opzione != "4" and opzione != "5": #input validation  
                opzione = raw_input(prompt)

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
                    print "Frammenti: ", frammento

                time.sleep(2.0)  

                invio(30)
                

            if opzione == "5":
                loop = 2

        while loop == 2:
            print "Impostazioni\n[1] Time sleep: %s\n[2] Resetta salvataggi\n[3] Indietro" % str(time_sleep)

            separatore(30)

            opzione_2 = ""
            while opzione_2 != "1" and opzione_2 != "2" and opzione_2 != "3":
                opzione_2 = raw_input(prompt)

            separatore(30)

            if opzione_2 == "1":
                if time_sleep == True:
                    time_sleep = False
                else:
                    time_sleep = True
                
                print "Time sleep scambiato in:", str(time_sleep)
                separatore(30)

                continue

            if opzione_2 == "2":
                print "Sei sicuro di voler resettare tutti i salvataggi?\n[1] Si, sono sicuro\n[2] No"
                separatore(30)

                opzione_3 = ""

                while opzione_3 != "1" and opzione_3 != "2":
                    opzione_3 = raw_input(prompt)

                if opzione_3 == "1":
                    f = open("salvataggi.txt", "w")
                    f.write("")
                    f.close()
                    pausa("cancellazione salvataggi in corso:", 1.0)
                    animazione("----------", 0.2)

                    leggi()
                    salva()

                    pausa("salvataggi cancellati", 1.0)
                    invio(30)
                    continue

                if opzione_3 == "2":
                    invio(30)
                    continue
                 

            if opzione_2 == "3":
                loop = 0
            salva()

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

def agenda():
    
    global note

    loop = 0
    big_loop = 0

    separatore(30)
    animazione("\n\tAgenda\n", 0.1)
    separatore(30)

    while big_loop == 0:

        
        while loop == 0:

            print"Scegli un'opzione:\n[1] Sfide\n[2] Note\n[3] Indizi\n[4] Indietro"
            separatore(30)

            opzione = ""
            while opzione != "1" and opzione != "2" and opzione != "3" and opzione != "4":
                opzione = raw_input(prompt)
            separatore(30)

            if opzione == "1":
                loop = 1
                break

            if opzione == "2":
                loop = 2
                break

            if opzione == "3":
                menu()
            
        while loop == 1:

            print "Sfide:"

            if foto != 0 and foto != 6:
                print "Scatta foto per il vecchio:", foto, "\\6"
            elif foto == "6":
                print "Scatta foto per il vecchio: Completato"

            invio(30)
            loop = 0
            break

        while loop == 2:
            

            if note != "":
                print "Note:"
                print note 

            else:
                print "nessuna nota trovata"

            invio(30)
            print "scegli un'opzione:\n[1] Aggiungi nota\n[2] Modifica note\n[3] Indietro"

            separatore(30)
  
            opzione_1 = ""

            while opzione_1 != "1" and opzione_1 != "2":
                opzione_1 = raw_input(prompt)

            separatore(30)

            if opzione_1 == "1" or opzione_1 == "2":
                print "Inserisci il testo da aggiungere\n(per andare a capo scrivi \"0\" e poi premi invio, per tornare indietro scrivi \"1\" e poi premi invio)"
                separatore(30)

                note_1 = ""

                if opzione_1 == "2":
                    note = ""

                while note_1 != "1":
                    
                    note_1 = raw_input(prompt)

                    while note_1 == "0":
                        note += "\n"
                        note_1 = raw_input(prompt)

                    if note_1 == "1":
                        break

                    note = note + note_1
                    salva()

                
                separatore(30)

            if opzione_1 == "3":
                loop = 0
                break
                invio(30)

leggi()
menu()