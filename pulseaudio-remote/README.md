# Pulseaudio Remote

Pulseaudio tiene una característica, desconocida por mí hasta hace poco, que es la posibilidad de transmitir el audio a través de TCP hacia otras tarjetas de sonido.
A diferencia de hacer streaming de audio, con esta funcionalidad se puede especificar cuál va a ser el destino/s de nuestro audio.

Yo le he encontrado una gran utilidad en los siguientes casos:
- Acceder por VNC a una máquina GNU/Linux desde otra con menor potencia, y aprovechar todas las funcionalidades multimedia que la de mayor potencia ofrece.
- En el caso de usar __mpd__ en una máquina virtual o pc remoto, poder tener el audio de esta en nustro cliente.
- También es posible tener hilo musical en casa sin necesidad de cablear. Se puede aprovechar la WiFi, o el cableado LAN existente.


