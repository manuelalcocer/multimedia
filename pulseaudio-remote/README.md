# Pulseaudio Remote.

Pulseaudio tiene una característica, desconocida por mí hasta hace poco, que es la posibilidad de transmitir el audio a través de TCP hacia otras tarjetas de sonido remotas.

A diferencia de hacer streaming de audio, con esta funcionalidad se puede especificar cuál va a ser el destino/s de nuestro audio.

Yo le he encontrado una gran utilidad en los siguientes casos:
- Acceder por VNC a una máquina GNU/Linux desde otra con menor potencia, y aprovechar todas las funcionalidades multimedia que la de mayor potencia ofrece.
- En el caso de usar __mpd__ en una máquina virtual o pc remoto, poder tener el audio de esta en nuestro cliente.
- También es posible tener hilo musical en casa sin necesidad de cablear. Se puede aprovechar la WiFi, o el cableado LAN existente.

## Dependencias y consideraciones previas.

- pulseaudio
- pulseaudio-zeroconf
- avahi-daemon (no es imprescindible)

### Opcional (recomendada).

- pasystray

## Funcionamiento.

Pulseaudio se puede configurar para que __publique__ o __descubra__ las tarjetas de sonido disponibles en la red, o ambas funciones. Para esto es necesario __avahi-daemon__.

Con los comandos __pacmd list-sinks__ y __pactl__ se pueden configurar manualmente las salidas (sinks) a utilizar, en este caso no es necesario __avahi-daemon__.

# Instalación y configuración de pulseaudio.

## Instalación.
- Debian:

~~~
# apt-get update && apt-get install pulseaudio pulseaudio-module-zeroconf 
~~~

- Archlinux:

~~~
# pacman -Syy && pacman -S pulseaudio pulseaudio-zeroconf 
~~~

## Configuración.

Editar __/etc/pulse/default.pa__:

~~~
# Permite la transmisión de audio a través de la lan
load-module module-native-protocol-tcp [opciones]¹
# En caso de usar avahi-daemon 'publica' la tarjeta en la red
load-module module-zeroconf-publish
# En caso de usar avahi-daemon 'detecta' automáticamente
# las tarjetas de red  exsitentes.
load-module module-zeroconf-discover
~~~

Hay que tener en cuenta una cosa.

Al habilitar el __módulo de protocolo tcp__, tanto el cliente (equipo que emite), como el servidor (equipo que publica su tarjeta en la red), deben compartir la misma __cookie__. Esto hay que hacerlo de forma manual, copiando el fichero: __~/.config/pulse/cookie__ , en todos los equipos que vayan a compartir recursos. Da igual cuál coger, cliente o servidor, lo único necesario es que sea la misma en todas las máquinas.

Si no se quiere tener que andar copiando la __cookie__ de máquina en máquina, se puede poner la línea de la siguiente forma:

~~~
load-module module-native-protocol-tcp auth-ip-acl=127.0.0.1;192.168.0.0/24 auth-anonymous=1
~~~

Eso permite ir definiendo segmentos de red sobre los cuales va a estar disponible el recurso.

