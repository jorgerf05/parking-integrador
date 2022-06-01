# parking-integrador

## Proyecto para Taller de Bases de datos, graficación y Fundamentos de Telecomunicaciones

parking-integrador es un proyecto que busca ayudar a controlar la administración de lugares dentro del estacionamiento del ITE. Utiliza Qt como framework para el aspecto
gráfico, MySQL como servidor de base de datos y Python como lenguaje base. Se necesita tener instalado MySQL, Python y PyQT5 para usar esta app.

### Instrucciones de instalación en Linux

Para distribuciones basadas en Debian:
```bash
sudo apt install mariadb-server
```
Para distribuciones basadas en Arch:

```bash
sudo pacman -S mariadb
```
Una vez instalado, podemos iniciar el servicio con la ayuda de systemd:

```bash
sudo systemctl start mariadb
```
