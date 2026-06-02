# FreeRadio — NVDA Add-on

FreeRadio es un complemento de radio por Internet para el lector de pantalla NVDA. Su principal objetivo es proporcionar a los usuarios un fácil acceso a miles de estaciones de radio por Internet. Toda la interfaz y todas las funciones se han diseñado teniendo en cuenta la accesibilidad total para NVDA.

## El Directorio de Radio Browser

FreeRadio utiliza la base de datos abierta de [Radio Browser](https://www.radio-browser.info/) por su catálogo de estaciones. Radio Browser es un directorio gratuito impulsado por la comunidad que alberga más de 50.000 estaciones de radio por Internet de todo el mundo. No se requiere registro ni cuenta y su API está abierta a todos. Cada estación incluye información sobre dirección, país, género, idioma y bitrate; las estaciones se clasifican según los votos de los usuarios. FreeRadio se conecta a esta API a través de servidores espejo ubicados en Alemania, Países Bajos y Austria; Si un servidor es inaccesible, pasa automáticamente al siguiente.

## Añadir una estación a Radio Browser

Si una estación que está buscando no aparece en el directorio de Radio Browser, puedes enviarlo tú mismo a [https://www.radio-browser.info/add](https://www.radio-browser.info/add). No es necesario tener cuenta ni registrarse.

Llene el formulario en esta página:

- **Stream URL** *(requerido)* — la URL directa del flujo de audio, terminando en `.mp3`, `.aac`, `.ogg` o similar. Esta no es la dirección del sitio web de la estación; esta es la dirección del flujo  bruto de transmisión que pegarías en un reproductor multimedia. La mayoría de las estaciones publican la URL de su flujo de transmisión en su sitio web o en su sección "Escuchar en directo".
- **Station name** *(requerido)* — el nombre de la estación como debería aparecer en el directorio.
- **Homepage** — la dirección del sitio web de la estación.
- **Country and language** — seleccione el país y el idioma de transmisión en las listas desplegables.
- **Tags** — palabras clave separadas por comas, por genre o topic, por ejemplo `news`, `jazz`, `classical`. Estos se utilizan para buscar y filtrar.
- **Logo URL** — un enlace directo a la imagen del logotipo de la estación, si está disponible.

Después del envío, la estación se revisa y se añade al directorio público. Una vez aceptado, aparecerá automáticamente en los listados de países y de búsqueda de FreeRadio, ya que el directorio se actualiza desde la API en directo.

## Requisitos

- NVDA 2024.1 o posterior
- Windows 10 o posterior
- Conexión a Internet

## Instalación

Descarga el archivo `.nvda-addon`, pulsa Intro y reinicia NVDA cuando se te solicite.

## Atajos de teclado

Todos los atajos se pueden reasignar desde el Menú NVDA → Preferencias → Gestos de Entrada → FreeRadio. Estos atajos funcionan desde cualquier lugar, independientemente de qué ventana tenga el foco.

| Atajo | Función | Descripción |
|---|---|---|
| `Ctrl+Win+R` | Abrir el navegador de estaciones | Abre la ventana del navegador si está cerrada o la trae al segundo plano si ya está abierta. |
| `Ctrl+Win+P` | Pausar / reanudar | Pausa la estación actual si se está reproduciendo; se reanuda cuando está en pausa. Si no se reproduce nada, inicia la última estación o abre la lista de favoritos según su configuración. Al pulsar dos veces en sucesión rápida, irás directamente a la pestaña que elijas. Pulsar tres veces puede activar una acción separada dependiendo de su configuración. |
| `Ctrl+Win+S` | Detener | Detiene completamente la estación actual y reinicia el reproductor. |
| `Ctrl+Win+→` | Siguiente favorito | Salta  a la siguiente estación en la lista de favoritos. Vuelve al principio y al final de la lista. |
| `Ctrl+Win+←` | Favorito anterior | Salta a la estación anterior en la lista de favoritos. Salta al final cuando está al principio. |
| `Ctrl+Win+↑` | Aumentar el volumen | Aumenta el volumen de 10 ; máximo 100. |
| `Ctrl+Win+↓` | Disminuir el volumen | Disminuye el volumen de 10 ; mínimo 0. |
| `Ctrl+Win+V` | Añadir a favoritos | Añade la estación que se está reproduciendo actualmente a la lista de favoritos. Anuncia si la emisora ya está en la lista. |
| `Ctrl+Win+I` | Información de la Estación | Anuncia el nombre de la estación que se está reproduciendo actualmente. Pulsa dos veces para mostrar los detalles como el país, el género y el bitrate en un diálogo. Pulsa tres veces para copiar la información de la pista actual (metadatos ICY) al portapapeles si está disponible; Si no hay metadatos presentes, inicia el reconocimiento de música de Shazam en su lugar. Pulsa cuatro veces para forzar el reconocimiento de música en caso de metadatos ICY incorrectos. |
| `Ctrl+Win+M` | Espejo de audio | Poner en espejo el flujo actual hacia un dispositivo de salida de audio adicional simultáneamente. Pulsa nuevamente para detener la puesta en espejo. |
| `Ctrl+Win+E` | Grabación instantánea | Pulsa una vez para comenzar a grabar la estación actual; pulsa nuevamente para detener. Pulsa **dos veces** para comenzar una **grabación de la canción**: El archivo lleva el nombre de la pista actual y la grabación se detiene automáticamente cuando cambia la pista. Pulsa nuevamente dos veces mientras la grabación de una canción está activa para detenerla antes de tiempo. La reproducción continúa sin interrupción en todos los modos de grabación. Solo disponible para estaciones que transmiten metadatos ICY. |
| `Ctrl+Win+W` | Abrir la carpeta de grabaciones | Abre la carpeta que contiene los archivos guardados en el Explorador de archivos. |
| *((no asignado)* | Alternar notificaciones silenciosas | Alternar la configuración de Silenciar notificaciones sobre la marcha. Asignar una combinación de teclas a través del Menú NVDA → Preferencias → Gestos de Entrada → FreeRadio. |

Los atajos siguientes/anteriores sólo recorren la lista de favoritos; No funcionan con la lista de todas las estaciones. Cuando una lista tiene el foco en la ventana del navegador, las teclas de flecha izquierda y derecha tienen el mismo propósito — ver la sección de Atajos en el cuadro de diálogo.

## Navegador de Estaciones

FreeRadio también añade un subMenú **FreeRadio** en el Menú Herramientas de NVDA. Desde allí puede abrir directamente el Navegador de Estaciones y los Ajustes de FreeRadio.

La ventana abierta con `Ctrl+Win+R` contiene cinco pestañas: Todas las estaciones, Favoritos, Grabación, Temporizador y Canciones favoritas. Puedes navegar entre las pestañas con `Ctrl+Tab`.

Cuando se abre la pestaña Todas las estaciones, las 1000 estaciones más votadas se cargan automáticamente desde Radio Browser. Al seleccionar un país de la lista desplegable, se actualiza la lista para mostrar estaciones de ese país. Al escribir en el cuadro de búsqueda se realiza instantáneamente una búsqueda completa en toda la base de datos de Radio Browser simultáneamente por nombre, país y género.

La lista desplegable **Dispositivo de salida** en la parte inferior de la ventana del navegador (fuera de las pestañas) enumera todos los dispositivos de salida de audio reconocidos por BASS. Al seleccionar un dispositivo, se redirige inmediatamente la salida de audio a él y se guarda la elección de forma permanente; el mismo dispositivo se utiliza automáticamente en la siguiente sesión. Si el dispositivo seleccionado no está conectado, el complemento vuelve automáticamente al valor predeterminado del sistema. Este control solo funciona cuando el BASS backend está activo.

Los controles de **Volumen** (0–200) y **Efectos** en la misma área se puede ajustar en cualquier momento cuando la ventana está abierta. Desde la lista de Efectos, Coro, Compresión, Distorsión, Eco, Flanger, Gargle, Reverberación, EQ: Bass Boost, EQ: Treble Boost y EQ: Vocal Boost se puede activar simultáneamente; Los cambios se aplican instantáneamente al flujo activo. Estos controles solo son completamente funcionales cuando el BASS backend está activo.

El botón **Reproducir/Pausar** También se encuentra en la parte inferior de la ventana. Si no se reproduce ninguna estación, se inicia la estación seleccionada; si ya se está reproduciendo una emisora, la reproducción se interrumpe.

Cuando se selecciona una estación en la lista, el botón **Detalles de la estación** muestra información como el país, el idioma, el género, el formato, el bitrate, el sitio web y el flujo URL en un cuadro de diálogo separado. Cada campo aparece en su propio cuadro de texto de solo lectura; puedes moverte entre los campos con Tab y copia toda la información al portapapeles de una vez con el botón **Copiar todo al portapapeles**. Este botón está disponible en las pestañas Todas las estaciones y Favoritos.

### Atajos en el cuadro de diálogo

Las siguientes teclas solo funcionan cuando la ventana del Navegador de Estaciones está activa.

### Teclas F

| Atajo | Función | Descripción |
|---|---|---|
| `F1` | Guía de ayuda | Abre el archivo de ayuda del complemento en el navegador predeterminado. Primero se busca la guía del idiomas NVDA activo; si no se encuentra, se abre la guía predeterminada. |
| `F2` | que esta reproduciendo  | Anuncia la estación que se está reproduciendo actualmente y el nombre de la pista. Pulsa dos veces para mostrar los detalles como el país, el género y el bitrate en un diálogo. Pulsa tres veces para copiar la información de la pista actual (metadatos ICY) al portapapeles si está disponible; si no hay metadatos presentes, inicia el reconocimiento de música de Shazam en su lugar. Pulsa cuatro veces para forzar el reconocimiento de música en caso de metadatos ICY incorrectos. |
| `F3` | Estación anterior | Salta a la estación anterior en la pestaña Todas las estaciones o Favoritos y comienza a reproducir inmediatamente. Salta al final cuando está al principio de la lista. |
| `F4` | Station suivante | Salta a la siguiente estación en la pestaña Todas las estaciones o Favoritos y comienza a reproducir inmediatamente. Vuelve al principio al final de la lista. |
| `F5` | Disminuir el volumen | Disminuye el volumen de 10 (mínimo 0). |
| `F6` | Aumentar el volumen | Aumenta el volumen de 10 (máximo 200). |
| `F7` | Pausar/reanudar | Pausa la estación actual si se está reproduciendo; se reanuda cuando está en pausa y el medio está cargado. |
| `F8` | Detener | Detiene completamente la estación actual y reinicia el reproductor. |
| `F9` | Renombrar | Abre el cuadro de diálogo para renombrar la estación enfocada en la pestaña Favoritos. |

### Lista y Atajos de Navegación

| Atajo | Función | Descripción |
|---|---|---|
| `→` | Siguiente estación | Cuando la lista Todas las estaciones o Favoritos esté enfocada, salta a la siguiente estación y la reproduce inmediatamente. Vuelve al principio al final de la lista. |
| `←` | Estación anterior | Cuando la lista Todas las estaciones o Favoritos está enfocada, salta a la estación anterior y la reproduce inmediatamente. Salta al final cuando está al principio. |
| `Intro` | Reproducir | Cuando la lista Todas las estaciones o Favoritos está enfocada, inmediatamente comienza a reproducir la estación seleccionada. Cambia a la estación seleccionada incluso si ya se está reproduciendo otra estación. |
| `Espacio` | Reproducir/Pausar | Se detiene si se está reproduciendo una estación; de lo contrario, comienza a reproducir la estación seleccionada. |
| `Ctrl+Tab` | Pestaña siguiente | Pasa a la siguiente pestaña (Todas las estaciones → Favoritos → Grabación → Temporizador → Canciones favoritas). |
| `Ctrl+Shift+Tab` | Pestaña anterior | Pasa a la pestaña anterior. |
| `Escape` | Ocultar | Oculta la ventana; el complemento continúa reproduciéndose en segundo plano. |

### Atajos de Volumen

| Atajo | Función | Descripción |
|---|---|---|
| `Ctrl+↑` | Aumentar el volumen | Aumenta el volumen de 10. Funciona sólo cuando la ventana del navegador está abierta. |
| `Ctrl+↓` | Disminuir el volumen | Disminuye el volumen de 10. Funciona sólo cuando la ventana del navegador está abierta. |

### Atajos de la Tecla Alt

| Atajo | Función | Descripción |
|---|---|---|
| `Alt+R` | Ir al cuadro de búsqueda | Mueve el foco al cuadro de texto de búsqueda. Busca en Radio Browser con el texto en el campo de búsqueda; el nombre, el país y el género se buscan simultáneamente. |
| `Alt+V` | Añadir/Eliminar un favorito | Añade la estación seleccionada a los favoritos; lo elimina si ya está en la lista. |
| `Alt+1` | Todas las estaciones | Cambia a la pestaña Todas las estaciones. |
| `Alt+2` | Favoritos | Cambia a la pestaña Favoritos. |
| `Alt+3` | Grabación | Cambia a la pestaña Grabación. |
| `Alt+4` | Temporizador | Cambia a la pestaña Temporizador. |
| `Alt+5` | Canciones favoritas | Cambia a la pestaña Canciones favoritas. |
| `Alt+K` | Cerrar | Cierra la ventana; el complemento continúa reproduciéndose en segundo plano. |

## Favoritos

La lista de favoritos es una colección de emisoras personales almacenada permanentemente. Para añadir una estación, selecciónela de la lista y pulse el botón Añadir a favoritos o usa el atajo `Alt+V`. El mismo atajo elimina una estación que ya está en la lista cuando se selecciona.

Los favoritos se pueden jugar con `Ctrl+Win+→` y `Ctrl+Win+←`; estos atajos funcionan incluso cuando la ventana del navegador no está abierta.

Para eliminar una emisora ​​de la lista de favoritos, selecciónela y pulse el botón **Eliminar estación** o la tecla `Suprimir`. Después de la eliminación, el foco y la selección pasan automáticamente a la siguiente estación de la lista. Si la estación eliminada fue la última, el foco se mueve a la estación anterior. Si la lista queda vacía, el foco se mueve al botón Reproducir.

### Reordenar Favoritos

Con una estación seleccionada en la pestaña Favoritos, pulse la `coma` para entrar en modo de desplazamiento; escuchará un pitido. Navegue hasta la posición de destino con las teclas de flecha, luego pulse la `coma` nuevamente. La estación se coloca en la posición elegida y la nueva organización queda inmediatamente registrada. Al pulsar la `coma` nuevamente en la misma posición se cancela el desplazamiento.

### Añadir una Estación Personalizada

Para añadir una estación que no está en Radio Browser, use el botón Añadir una estación personalizada. En el cuadro de diálogo que aparece, ingresa el nombre de la estación y la URL del flujo  de transmisión para añadirla directamente a tus favoritos. Las estaciones personalizadas se pueden escuchar y reorganizar como cualquier otro favorito.

### Perfil de Audio de la Estación

La pestaña Favoritos incluye dos botones para administrar los ajustes de audio por estación:

**Guardar perfil de audio para esta estación** — guarda el nivel de volumen actual y los efectos activos (coro, EQ, etc.) como perfil vinculado a esta emisora específica. Cada vez que esa estación comienza a reproducirse, el volumen y los efectos guardados se aplican automáticamente, anulando los valores predeterminados globales.

**Borrar perfil de audio** — elimina el perfil de audio guardado de la estación seleccionada. Después de borrar, la estación vuelve a los ajustes globales de volumen y efectos. Este botón solo está activo cuando la estación seleccionada ya tiene un perfil guardado.

Los dos botones están ubicados debajo de la lista de favoritos y solo se activan cuando se selecciona una estación de la lista.

## Reconocimiento de Música

Pulse tres veces `Ctrl+Win+I` activa el reconocimiento de música basado en Shazam para el flujo que se está reproduciendo actualmente. El reconocimiento sólo comienza cuando no hay metadatos ICY (información de la pista transmitida por la estación) disponibles; si hay metadatos presentes, se copian al portapapeles en su lugar.

El reconocimiento funciona de la siguiente manera: se captura una breve muestra de audio a partir del flujo usando ffmpeg, se aplica el algoritmo de huellas digital de Shazam y el resultado se envía a los servidores de Shazam. Si el reconocimiento tiene éxito, el título de la canción, el artista, el álbum y el año de lanzamiento serán anunciados por NVDA y copiado automáticamente al portapapeles. Si la opción **Guardar las canciones favoritas en un archivo de texto** esta activado, el resultado del reconocimiento también se añade a `likedSongs.txt`.

**Retorno de audio:** Suenan dos pitidos ascendentes cuando comienza el reconocimiento y dos pitidos descendentes cuando finaliza. Suena un pitido corto cada 2 segundos mientras el proceso está en progreso.

**Requisito:** ffmpeg.exe requerido. Un ffmpeg.exe colocado en la carpeta del complementos se utiliza automáticamente; si está en una ubicación diferente, la ruta se puede establecer en las Opciones. Descargar ffmpeg desde [ffmpeg.org](https://ffmpeg.org/download.html).

## Espejo de Audio

El atajo `Ctrl+Win+M` pone los espejos del flujo que se está reproduciendo actualmente en un segundo dispositivo de salida de audio simultáneamente. Esto es útil para escuchar en dos dispositivos diferentes al mismo tiempo, como altavoces y auriculares.

Al pulsar por primera vez, aparece un cuadro de diálogo de selección que enumera los dispositivos de salida disponibles. Una vez elegido el dispositivo, comienza la puesta en espejo y la reproducción principal continúa sin interrupción. Al pulsar el atajo nuevamente se detiene la la puesta en espejo.

**Casos de uso:**
- **Altavoces + auriculares** — Dejar que un invitado siga el mismo programa con los auriculares mientras tu escuchas a través de los altavoces de la computadora.
- **Configuración de grabación** — Dirija la salida principal a los altavoces  y la segunda salida a una grabadora externa o interfaz de audio para captura externa.
- **Multihabitación** — Reproduzca simultáneamente a través de un altavoz Bluetooth y el altavoz incorporado; no se necesita software adicional para transportar el audio a otra habitación.
- **Monitoreo remoto** — En una sesión de pantalla compartida o de escritorio remoto, tanto el lado local como el remoto pueden escuchar el mismo flujo simultáneamente.

> **Nota:** La puesta en espejo de audio solo está disponible cuando el BASS backend está activo. Si se cambia el volumen mientras la puesta en espejo está activo, ambas salidas se actualizan simultáneamente.

## Grabación

Las grabaciones se guardan de forma predeterminada en `Documentos\FreeRadio Recordings\`. El nombre del archivo incluye el nombre de la estación (o el título de la canción, en modo de grabación de canciones) y la hora de inicio de la grabación. La carpeta de grabaciones se puede cambiar en cualquier momento desde el Menú NVDA → Preferencias → Opciones → FreeRadio → **Carpeta de grabaciones**. Debido a que el motor de grabación se conecta directamente al flujo de transmisión, el audio se escribe en el disco tal como se recibe; no se aplica ningún procesamiento ni recodificación; La calidad de grabación es la misma que la calidad de transmisión.

**Grabación instantánea:** Mientras se reproduce una estación, pulse una vez `Ctrl+Win+E`. Pulse nuevamente para detener. La reproducción continúa sin interrupción.

**Grabación de la canción:** Pulse `Ctrl+Win+E` **dos veces** en sucesión rápida mientras se reproduce una estación que transmite metadatos ICY. La grabación comienza inmediatamente y lleva el nombre del título de la pista actual. Cuando cambia la pista, la grabación se detiene automáticamente y NVDA anuncia el nombre del archivo grabado. Si desea terminar la grabación antes del final de la pista, ppulse `Ctrl+Win+E` dos veces nuevamente. Si la estación actual no transmite metadatos ICY, la grabación de la canción no está disponible y NVDA te lo notificará.

**Grabación programada:** Abra la pestaña Grabación en el navegador. Seleccione una estación de sus favoritos, ingrese la hora de inicio en formato HH:MM y la duración en minutos, luego elige un modo de grabación:

- **Grabar mientras escuchas** — reproduce y graba simultáneamente. Se inicia un backend de reproducción usando el orden de prioridad BASS → VLC → PotPlayer → Windows Media Player.
- **Solo grabación** — Graba silenciosamente en segundo plano sin ninguna salida de audio; El motor de grabación se conecta directamente al flujo de  transmisión.

Si la hora ingresada ya pasó, la grabación se programa para el día siguiente. NVDA anuncia cuándo comienza y cuándo termina una grabación.

## Temporizador

Abra la pestaña Temporizador en el navegador de estaciones (`Alt+4`). Se pueden añadir dos tipos de temporizador:

**Alarma — iniciar la radio:** Comienza a reproducir automáticamente una estación seleccionada de sus favoritos a la hora especificada. Elija una estación e ingrese la hora en formato HH:MM.

**Apagado — detener la radio:** Detiene la reproducción a la hora especificada. Cuando suena el temporizador, el volumen se reduce gradualmente durante 60 segundos antes de que se detenga la reproducción. No es necesaria ninguna selección de estación; simplemente ingrese la hora.

Para ambos tipos, si la hora ingresada ya pasó, la acción se programa para el día siguiente. Los temporizadores pendientes se enumeran en la pestaña; seleccione uno y pulse el botón Eliminar el temporizador seleccionado para cancelarlo.

## Opciones

Las siguientes opciones se pueden configurar desde el Menú NVDA → Preferencias → Opciones → FreeRadio:

| Opción | Descripción |
|---|---|
| Dispositivo de salida de audio (BASS backend) | Establece el dispositivo de salida de audio para la reproducción de la radio. La lista incluye todos los dispositivos del sistema BASS-compatible más una opción "valor predeterminado del sistema". Los cambios se aplican inmediatamente después de guardarlos; Si el dispositivo seleccionado se desconecta, el complemento vuelve automáticamente al valor predeterminado del sistema y anuncia el cambio. Activo solo cuando se utiliza el BASS backend. |
| Volumen | Establece el volumen cuando se inicia el complemento (0–200). Los cambios realizados durante la reproducción con `Ctrl+Win+↑` / `Ctrl+Win+↓` también se reflejan aquí. |
| Efecto de audio predeterminado | Establece el efecto de audio aplicado cuando se inicia NVDA o una estación comienza a reproducirse. El efecto seleccionado corresponde a la lista de efectos en el navegador de estaciones. Activo solo cuando se utiliza el BASS backend. |
| Transición de cambio de estación(BASS backend) | Controla el comportamiento de transición al conmutar entre las estaciones. **Corte instantáneo** (por defecto) detiene la estación anterior justo antes de que comience la nueva. **Fundido encadenado corto (1 segundo)** y **Fundido encadenado normal (2 segundos)** inicia inmediatamente la nueva estación sin interrupción, luego desaparece gradualmente la estación anterior en segundo plano una vez confirmado el nuevo flujo activo. No tiene ningún efecto ni impacto en el rendimiento cuando se establece en Corte instantáneo. Solo disponible cuando el BASS backend está en uso. |
| Reanudar la última estación al iniciar NVDA | Cuando está habilitado, la última estación escuchada se reinicia automáticamente cada vez que se inicia NVDA. |
| Anunciar automáticamente los cambios de pista (metadatos ICY) | Cuando está habilitado, NVDA lee automáticamente el nombre de la nueva pista cada vez que cambia en una estación que transmite metadatos ICY. La primera canción también se anuncia inmediatamente al cambiar a una nueva estación. Deshabilitado por defecto. |
| Silenciar notificaciones | Cuando está habilitado, NVDA no anuncia cambios de estación, cambios de estado de reproducción (reproducir, pausar, detener) o eventos de grabación (iniciado, detenido, terminado). Mensajes de error, comentarios sobre favoritos, resultados de reconocimiento de música y notificaciones de las actualizaciones no se ven afectadas. También se puede activar sobre la marcha mediante un gesto de entrada no asignado. Deshabilitado por defecto. |
| Guardar las canciones favoritas en un archivo de texto | Cuando está habilitado, la información de la pista se copia al portapapeles pulsando `Ctrl+Win+I` tres veces y también se añade a `Documentos\FreeRadio Recordings\likedSongs.txt`. Si no hay metadatos ICY disponibles, el resultado del reconocimiento de Shazam se guarda en el mismo archivo. Deshabilitado por defecto. |
| Cuando Ctrl+Win+P se pulsa sin reproducción activa | Determina qué sucede cuando se pulsa este atajo y no hay nada  en reproducción: iniciar la última estación o abrir la lista de favoritos. |
| Cuando Ctrl+Win+P se pulsa dos veces | Selecciona lo que sucede cuando se pulsa el atajo dos veces en sucesión rápida: no hacer nada, abrir la lista de favoritos, abrir la pestaña de grabación o abrir la pestaña del temporizador. Cuando "No hacer nada" es seleccionado, la primera pulsación responde instantáneamente sin demora. |
| Cuando Ctrl+Win+P se pulsa tres veces | Selecciona lo que sucede cuando se pulsa el atajo tres veces en sucesión rápida: no hacer nada, abrir la lista de favoritos, abrir búsqueda de emisoras, abrir la pestaña de grabación o abrir la pestaña del temporizador. |
| Buscar actualizaciones automáticamente al iniciar | Cuando está habilitado, una verificación de actualización en segundo plano se ejecuta cada vez que se inicia NVDA; se le notificará si se encuentra una nueva versión. Cuando está deshabilitado, los controles automáticos se detienen pero los controles manuales permanecen disponibles. |
| Ruta ffmpeg.exe | Ruta de acceso al ffmpeg.exe usado para el reconocimiento de música. Si se deja vacío, un ffmpeg.exe en la carpeta del complementos se usa automáticamente. |
| Ruta VLC | Si VLC no está instalado o se encuentra en una ubicación no estándar, aquí se puede ingresar la ruta completa al ejecutable. |
| Ruta wmplayer.exe | Ingrese la ruta a Windows Media Player aquí si es necesario. |
| Ruta PotPlayer | Si PotPlayer se encuentra en una ubicación no estándar, su ruta se puede ingresar aquí. |
| Carpeta de grabaciones | Establece la carpeta donde se guardan los archivos grabados. Si se deja en blanco, la ubicación predeterminada `Documentos\FreeRadio Recordings\` se utiliza. Un botón Explorar carpeta le permite seleccionar la carpeta de forma interactiva. Los cambios entran en vigor inmediatamente después de guardarlos. |
| Desactivar la verificación de conectividad a Internet antes de reproducir | Recomendado para usuarios que experimentan un retraso antes de que una estación comience a reproducirse. También es útil cuando el DNS está bloqueado. |

## Silenciar Notificaciones

Cuando **Silenciar notificaciones** está habilitado en las Opciones, NVDA silencia los siguientes anuncios automáticos:

- Nombre de la estación cuando comienza a reproducirse una nueva estación
- Cambios de estado de reproducción: reproducir, pausar, detener
- Eventos de grabación: iniciado, detenido, terminado (grabaciones instantáneas, de canciones y programadas)
- Anuncios de cambio de pista ICY, incluso cuando **Anunciar automáticamente los cambios de pista**   también está habilitado

Los siguientes anuncios **no** se ven afectados intencionalmente: mensajes de error, comentarios sobre favoritos (añadido / ya en la lista), resultados de reconocimiento de música y notificaciones de actualización.

La configuración se puede alternar desde el Menú NVDA → Preferencias → Opciones → FreeRadio, o instantáneamente en cualquier momento mediante un gesto de entrada no asignado (asignar uno desde el Menú NVDA → Preferencias → Gestos de Entrada → FreeRadio). Cuando está habilitado, NVDA anuncia una vez "Notificaciones silenciadas" o "Notificaciones reactivadas" para confirmar el cambio.

## Anunciar automáticamente los cambios de pista

Cuando la opción **Anunciar automáticamente los cambios de pista** se activa en las Opciones, FreeRadio comprueba el flujo de metadatos ICY de la estación activa en segundo plano aproximadamente cada 5 segundos. Cuando cambia la pista, NVDA lee automáticamente el nuevo título; no es necesario pulsar ninguna tecla.

Al cambiar a una nueva emisora, la información de la primera pista se anuncia tan pronto como se establece la conexión. Si cambia a una estación que no transmite metadatos ICY, el sistema permanece en silencio y la información de la pista de la estación anterior no se repite.

Esta función está desactivada de forma predeterminada y se puede alternar desde el Menú NVDA → Preferencias → Opciones → FreeRadio.

## Canciones favoritas

Cuando la opción **Guardar las canciones favoritas en un archivo de texto** está activado, la información de la pista se copia al portapapeles pulsando tres veces `Ctrl+Win+I` también se añade línea por línea a `Documentos\FreeRadio Recordings\likedSongs.txt`.

En las estaciones que transmiten metadatos ICY, el título de la pista y el artista se guardan directamente. En las estaciones sin metadatos ICY, el resultado del reconocimiento de Shazam se guarda en el mismo archivo; ambas fuentes comparten la misma lista. El archivo se crea automáticamente si no existe; cada entrada se añade al final del archivo y las entradas anteriores nunca se eliminan.

## Pestaña de Canciones favoritas

La pestaña **Canciones favoritas** en el navegador de estaciones se muestran todas las pistas guardadas en `likedSongs.txt`. La lista se recarga automáticamente desde el archivo cada vez que se abre la pestaña.

Seleccionar una pista de la lista permite las siguientes acciones:

- **Reproducir en Spotify:** Intenta abrir la aplicación de escritorio de Spotify directamente. Si la aplicación no está instalada, vuelve al sitio web de Spotify y automáticamente comienza a reproducir el primer resultado.
- **Reproducir en YouTube (`Alt+O`):** Busca en YouTube la pista seleccionada y abre los resultados en el navegador predeterminado.
- **Eliminar (`Alt+M`):** Elimina la pista seleccionada de `likedSongs.txt` y  actualiza la lista. La tecla `Suprimir` también activa este botón cuando la lista está enfocada.
- **Refrescar (`Alt+E`):** Vuelve a cargar la lista desde el archivo.

Los botones Spotify, YouTube y Eliminar sólo se activan cuando se selecciona una pista real en la lista.

## Reproducción

El complemento selecciona un backend de reproducción usando el siguiente orden de prioridad:

1. **BASS** — el backend predeterminado y principal. No se requiere instalación por separado; viene incluido con el complemento. BASS envía el audio directamente a la pila de audio de Windows y aparece en el mezclador de volumen de Windows como una fuente de audio independiente llamada "pythonw.exe", separada de NVDA. Esto significa que el audio de FreeRadio circula en un canal completamente separado del habla de NVDA: la radio no se corta, no se mezcla ni se ve afectada por la propia configuración de audio de NVDA mientras NVDA está hablando. El usuario puede ajustar el volumen de la radio independientemente de NVDA en el Mezclador de volumen de Windows. Admite HTTP, HTTPS y la mayoría de los formatos de flujo integrados. La puesta en espejo  de audio solo está disponible con este backend.
2. **VLC** — se hace cargo si el BASS falla. Se busca automáticamente en ubicaciones de instalación comunes, carpetas de perfil de usuario y la RUTA del sistema.
3. **PotPlayer** — probado si no se encuentra VLC. Se busca automáticamente en ubicaciones de instalación comunes.
4. **Windows Media Player** — utilizado como último recurso; requiere que el componente WMP esté instalado en el sistema.

## Comprobación de Actualización

FreeRadio busca automáticamente nuevas versiones a través de GitHub.

**Comprobación automática:** Se ejecuta silenciosamente en segundo plano 15 segundos después de que se inicia NVDA. Si se encuentra una nueva versión, se le notificará; si no se encuentra ninguno, no se muestra ningún mensaje.

**Comprobación manual:** Se puede activar a solicitud desde Herramientas NVDA → FreeRadio → **Buscar actualizaciones…**. Cuando se inicia de esta manera, el resultado se anuncia incluso si la versión está actualizada.

**Cuando se encuentra una actualización:** Se abre un cuadro de diálogo que muestra el número de versión y la versión instalada.

- Si hay un archivo `.nvda-addon` directamente descargable disponible en la release de GitHub, se muestra un botón **Descargar y Instalar**. Una vez confirmado, el archivo se descarga en segundo plano, NVDA anuncia cuándo comienza la descarga y La propia pantalla de instalación se abre automáticamente.
- Si no hay ningún enlace de descarga directa disponible,, un botón **Abrir la página** se muestra y la página de la release en GitHub se abre en el navegador predeterminado.

**Para desactivar las comprobaciones automáticas:** Deshabilitar la opción **Buscar actualizaciones automáticamente al iniciar** desde el Menú NVDA → Preferencias → Opciones → FreeRadio.

## Licencia

GPL v2