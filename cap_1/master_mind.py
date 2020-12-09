import random
import time, os, sys

prompt = '> '
comb = ""
gioca = True

def animazione(testo,tempo):
    
    for char in testo:
        sys.stdout.write(char)
        sys.stdout.flush()
        if time_sleep == True:
            time.sleep(tempo)

def separatore(numero):
    print  "_" * numero + "\n"

def combinazione():
    global c1, c2, c3, c4
    l = ["1", "2", "3", "4", "5", "6"]
    
    random.shuffle(l)

    c1 = l[0]
    c2 = l[1]
    c3 = l[2]
    c4 = l[3]

    #c1 = random.randint(1,6)
    #while c2 != c1 and c3 and c4 and c5 and c6:
        #c2 = random.randint(1,6)
    #while c3 != c1 and c2 and c4 and c5 and c6:
        #c3 = random.randint(1,6)
    #while c4 != c1 and c3 and c2 and c5 and c6:
    #    c4 = random.randint(1,6)
    c = [c1, c2, c3, c4]
    return c

def colori():
    separatore(73)
    
    print """
\t1 = rosso     4 = verde     B = giusto al posto sbagliato
\t2 = giallo    5 = bianco    N = giusto al posto giusto
\t3 = blu       6 = viola     \ = sbagliato
    """
    separatore(73)

def verify(code, attempt):
  response = []
  for n in range(4):
    if attempt[n] == code[n]:
      response.append('N')
    elif attempt[n] in code:
      response.append
      ('B')
    else:
      response.append('\\')
  random.shuffle(response)
  return ' - '.join(response)

def ver_win(p):

    vittoria = True
     
    if p == "NNNN":
        vittoria = True
    else:
        vittoria = False

    return vittoria



def master_mind():

    vittoria = False
    c = combinazione()
    comb = ""

    while vittoria == False:

        colori()
        print "scegli 4 colori da mettere:"

        scelta = ""+

        #validation imput 
        while n != 4:
            scelta = list(raw_input( prompt ))

            for n in scelta:
                pass
            
            if scelta[0] or scelta[1] or scelta[2] or scelta[3] != "1" or "2" or "3" or "4" or "5" or "6":
                print "errore: caratteri non validi"
                if scelta[1] != "1" and "2" and "3" and "4" and "5" and "6":
                    print scelta[1]
                print scelta


            if len(scelta) > 4:
                print "errore: hai scritto troppi numeri"
            if len(scelta) < 4:
                print "errore: hai scritto troppi pochi numeri"

        list(scelta)

        s1 = int(scelta[0])
        s2 = int(scelta[1])
        s3 = int(scelta[2])
        s4 = int(scelta[3])

        s = str(s1) + str(s2) + str(s3) + str(s4)

        p = ""
        p1 = ""
        p2 = ""
        p3 = ""
        p4 = ""
        
        p = verify(c, scelta)

        comb += "\n" + str(s) + "\t" + str(p) + "\n"

        vittoria = ver_win(p)

        if vittoria == False:
            separatore(28)
            print comb

        
        else:
            print "Hai vinto!"
            break



while gioca == True:

    master_mind()

    print "Vuoi giocare ancora?\n[1] Si\n[2] No"

    opzione = ""

    while opzione != "1" and opzione != "2":
        opzione = raw_input(prompt)
    
    if opzione == "1":
        gioca = True

    if opzione == "2":
        gioca = False

    