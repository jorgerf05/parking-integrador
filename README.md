# parking-integrador

## Proyecto para Taller de Bases de datos, Graficación y Fundamentos de Telecomunicaciones

parking-integrador es un proyecto que busca ayudar a controlar la administración de lugares dentro del estacionamiento del ITE. Utiliza Qt como framework para el aspecto
gráfico, MySQL como servidor de base de datos y Python como lenguaje base. Se necesita tener instalado MySQL, Python y PyQT5 para usar esta app.

### Requisitos pre-instalación (Linux)

Para distribuciones basadas en Debian:
```bash
sudo apt install mariadb-server
sudo apt install python3-pip
pip3 install PyQt5
```
Para distribuciones basadas en Arch:

```bash
sudo pacman -S mariadb
sudo pacman -S python-pip
pip3 install PyQt5
```
Una vez instalado, podemos iniciar el servicio con la ayuda de systemd:

```bash
sudo systemctl start mariadb
```
### Instalación de parking-integrador

```bash
cd ~
git clone https://github.com/jorgerf05/parking-integrador
cd parking-integrador
python3 Main.py
```
