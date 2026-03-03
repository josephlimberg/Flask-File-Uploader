# Flask-File-Uploader
Un sistema cliente-servidor ligero construido con Python y Flask para la transferencia y gestión de archivos remotos. Permite a los usuarios subir archivos, organizarlos en estructuras de directorios dinámicas y verificar su existencia en el servidor a través de una API HTTP, utilizando una interfaz de línea de comandos (CLI) interactiva.

 ** Creación dinámica de rutas:** Genera automáticamente las carpetas necesarias en el servidor basándose en la ruta especificada por el cliente.
 ** Subida de archivos HTTP:** Utiliza peticiones POST (`requests`) para la transferencia segura de archivos.
 ** Prevención de colisiones:** Verifica la existencia de archivos en el servidor antes de subirlos, ofreciendo opciones para sobrescribir, renombrar o cancelar la operación.
 ** Interfaz CLI amigable:** Menú interactivo en la terminal para facilitar la experiencia del usuario.
