'''
Sever creato con flask e con socket per la simulazione di attacco dos
Il server gestisce tutto in single-threading così che l'attacco dos avvenga, altrimenti le architetture dei server standard gestirebbero tranquillamente tutte le richieste
'''


'''
from flask import Flask, render_template_string, request
import time
import socket

app = Flask(__name__)

# Otteniamo l'IP locale per mostrarlo a video dopo in cli 
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <title>PORTALE REGISTRO ELETTRONICO - PASCAL</title>
    <style>

        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f6f9; margin: 0; padding: 0; }

        header { background-color: #FFA239; color: white; padding: 20px; text-align: center; }

        .container { max-width: 800px; margin: 40px auto; background: white; padding: 40px; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }

        h1 { margin-top: 0; }
        .status { background-color: #d4edda; color: #155724; padding: 15px; border-radius: 4px; margin-bottom: 20px; border: 1px solid #c3e6cb; }

        input[type="text"], input[type="email"], input[type="password"] { width: 100%; padding: 10px; margin: 10px 0; border: 1px solid #ccc; border-radius: 4px; }

        button { background-color: #FFA239; color: white; padding: 15px 30px; border: none; border-radius: 4px; cursor: pointer; font-size: 18px; width: 100%; }

        button:hover { background-color: #E2852E; }

        .footer { text-align: center; margin-top: 40px; color: #666; font-size: 12px; }

    </style>
</head>
<body>
    <header>
        <h2>ITT BLAISE PASCAL</h2>
        <p>Sistema Informatico Ufficiale</p>
    </header>
    
    <div class="container">
        <div class="status">✅ <strong>Sistema Online:</strong> I server sono operativi e veloci.</div>
        
        <h1>REGISTRO ELETTRONICO A.S. 2025/2026</h1>
        <p>Accedere per inserire voti e presenze</p>
        
        <form action="">
            <label>Nome e Cognome ( PROF/PROF.SSA )</label>
            <input type="text" placeholder="Mario Rossi">
            
            <label>Email professore</label>
            <input type="email" placeholder="prof.mario.rossi@example.com">
            
            <label>Passoword</label>
            <input type="password" placeholder="****">
            
            <button type="button" onclick="alert('Dati inviati con successo!')">Login</button>
        </form>
    </div>

    <div class="footer">
        &copy; 2025 ITT Blaise Pascal - Indirizzo informatico
    </div>
</body>
</html>
"""

@app.route('/') # imposta la route per la pagina web

def home():
    
    client_ip = request.remote_addr # prende l'ip del client 

    print(f"[LOG] Accesso da: {client_ip} - Risposta inviata.")

    time.sleep(0.2) # rallenta per facilitare il crash ( simula un'interrogazione a un database lento )

    return render_template_string(HTML_PAGE) # ritorna la nostra pagina

if __name__=="__main__":

    print("-- SERVER AVVIATO -- ")
    print(f"Host: {hostname} \n INDIRIZZO IP: {local_ip}")
    app.run('0.0.0.0', threaded=False) # lo mettiamo visibile sulla LAN e impostiamo il threaded a FALSE -> che e FONDAMENTALE per rendere il server "stupido" :P
'''

from flask import Flask, render_template_string, request
import time
import socket

app = Flask(__name__)

# --- CONFIGURAZIONE ---
# Variabile globale per attivare/disattivare la modalità "Server Rotto"
SERVER_STRESSATO = False 

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head><title>Scuola Pascal</title></head>
<body style="font-family: sans-serif; text-align: center; padding: 50px;">
    <h1>ITT BLAISE PASCAL</h1>
    <div style="background: #d4edda; padding: 20px; border-radius: 10px; display: inline-block;">
        ✅ STATO SERVER: ONLINE
    </div>
    <p>Benvenuti all'Open Day. Iscriviti qui sotto.</p>
    <button onclick="alert('Iscritto!')" style="padding: 10px 20px; font-size: 1.2em; background: blue; color: white; border: none; cursor: pointer;">ISCRIVITI</button>
    <p style="opacity: 0.1"> ispezionami
    <!-- Hey cosa stai cercando??? vai da uno studente e digli che gli puzzano i piedi per ottenere una ricompensa -->
    </p>
    </body>
</html>
"""

# --- ROTTE SEGRETE PER IL PROF ---
@app.route('/admin/attiva_lag')
def attiva_lag():
    global SERVER_STRESSATO
    SERVER_STRESSATO = True
    print("\n!!! MODALITÀ STRESS ATTIVATA: Il server ora è lentissimo !!!\n")
    return "Lag Attivato! Ora il server simula un carico pesante."

@app.route('/admin/disattiva_lag')
def disattiva_lag():
    global SERVER_STRESSATO
    SERVER_STRESSATO = False
    print("\n--- Modalità Stress Disattivata: Il server respira ---\n")
    return "Lag Disattivato. Tutto torna normale."

# --- ROTTA PUBBLICA ---
@app.route('/')
def home():
    client_ip = request.remote_addr
    
    if SERVER_STRESSATO:
        # Quando attivi il lag, il server dorme per 2 SECONDI a richiesta!
        # Con single-thread, basta pochissimo traffico per ucciderlo.
        print(f"[ATTACCO] {client_ip} sta bloccando la risorsa...")
        time.sleep(2.0) 
    else:
        # Modalità normale: risponde subito, così i ragazzi vedono che funziona
        print(f"[OK] Visita da {client_ip}")
        # Niente sleep, o sleep bassissimo
    
    return render_template_string(HTML_PAGE)

if __name__ == '__main__':
    print(f"IP Server: {local_ip}")
    print("Per far crashare il server, apri in un'altra tab: /admin/attiva_lag")
    
    # Usiamo threaded=False SEMPRE.
    # Ma finché SERVER_STRESSATO è False, è abbastanza veloce da reggere i click.
    # Appena diventa True, muore male.
    app.run(host='0.0.0.0', port=5000, threaded=False)
