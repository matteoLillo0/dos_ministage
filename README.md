# Simulazione DoS: Vulnerabilità Single-Thread

Progetto sviluppato per dimostrare le vulnerabilità di un web server single-thread sottoposto a stress test e attacchi Denial of Service (DoS). 

## Panoramica del Progetto

Il sistema è composto da due file principali:
- server.py: Un'applicazione Flask (simulazione portale ITT Blaise Pascal) configurata intenzionalmente per elaborare una singola richiesta alla volta (threaded=False).
- client.py: Uno script Python che sfrutta il modulo threading e i raw socket TCP per inondare il server con richieste HTTP GET.

## Prerequisiti

È necessario avere Python 3 installato. Per installare la libreria del server, esegui:

    pip install flask

## Esecuzione del Test

1. Avviare la Vittima (Server)
Apri un terminale e avvia il server in locale:

    python server.py

Prendi nota dell'IP locale mostrato. 
Nota: Per simulare un carico I/O pesante e rendere il server vulnerabile all'istante, visita dal browser la rotta nascosta: http://<IP_SERVER>:5000/admin/attiva_lag

2. Lanciare l'Attacco (Client)
Apri un secondo terminale (o usa una macchina diversa in LAN) e avvia lo script:

    python client.py

Inserisci l'IP del target e la porta (5000). Lo script lancerà 50 Daemon Threads che satureranno la coda di ascolto del server, portandolo offline e rendendo impossibile il caricamento della pagina web. 

Per interrompere l'attacco, premi CTRL+C nel terminale del client.

## Disclaimer

Questo tool è stato sviluppato esclusivamente per scopi didattici e di ricerca. Da utilizzare solo su localhost o all'interno di reti LAN private sotto il proprio esplicito controllo.
