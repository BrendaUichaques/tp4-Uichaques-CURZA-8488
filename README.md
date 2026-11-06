# TP4 - Automatización y Scripting

**Alumna:** Brenda Alejandra Uichaques  
**Legajo:** 8488  
**Universidad Nacional del Comahue - CURZA**

Este trabajo práctico consiste en implementar un servicio de análisis de tráfico web utilizando Docker, automatizar su configuración con Ansible y comprobar su funcionamiento mediante pruebas de Python y GitHub Actions.

## Tarea 1: Docker y Docker Compose

Se crearon los siguientes archivos:

- **`docker/Dockerfile`:** utiliza Alpine Linux, instala GoAccess y configura un usuario sin privilegios.
- **`docker/docker-compose.yml`:** define los servicios `web_server` (Nginx) y `log_analyzer` (GoAccess), junto con los volúmenes compartidos.
- **`docker/nginx.conf`:** configura el servidor web y el acceso al reporte HTML.
- **`docker/goaccess.conf`:** configura la lectura de los registros `access.log` y la generación de `report.html`.
- **`docker/.env`:** establece los puertos personalizados 8088 y 9088.

Para ejecutar los contenedores:

```bash
cd docker
docker compose up -d --build
docker compose ps
```

El servidor web utiliza el puerto **8088** y el reporte de GoAccess se consulta en el puerto **9088**.

## Tarea 2: Ansible

Se crearon dos archivos:

- **`ansible/hosts.ini`:** define el grupo `[lab_systems]` y utiliza `localhost` para las pruebas locales.
- **`ansible/playbook.yml`:** automatiza la instalación de Docker, la copia de archivos de configuración y el despliegue de los contenedores. Incluye un handler que reinicia Nginx cuando cambia su configuración.

Para ejecutar el playbook desde la raíz del proyecto:

```bash
ansible-playbook -i ansible/hosts.ini ansible/playbook.yml --ask-become-pass
```

Se comprobó la idempotencia obteniendo `changed=0` y el funcionamiento del handler al modificar `nginx.conf`.

## Tarea 3: Python y GitHub Actions

Se crearon los siguientes archivos:

- **`tests/test_config.py`:** contiene dos pruebas que verifican que `docker-compose.yml` tenga una sintaxis YAML correcta y que estén definidos los servicios requeridos.
- **`.github/workflows/ci-pipeline.yml`:** configura GitHub Actions para ejecutar las pruebas automáticamente ante eventos `push` y `pull_request` sobre la rama `main`.

Para ejecutar las pruebas localmente:

```bash
python3 -m unittest tests/test_config.py -v
```

Las dos pruebas finalizaron correctamente con el resultado `OK`. También se comprobó su ejecución exitosa mediante GitHub Actions.
