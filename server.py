'''
Sever creato con flask e con socket per la simulazione di attacco dos
Il server gestisce tutto in single-threading così che l'attacco dos avvenga, altrimenti le architetture dei server standard gestirebbero tranquillamente tutte le richieste
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

