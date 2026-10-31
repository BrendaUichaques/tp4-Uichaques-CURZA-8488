# Imagen base ligera: Alpine Linux
FROM alpine:3.20

# Instalamos GoAccess (analizador de logs)
RUN apk add --no-cache goaccess tzdata

# Usuario no-root por seguridad
RUN addgroup -S -g 1000 goaccess \
    && adduser -S -u 1000 -G goaccess -h /home/goaccess goaccess

# /srv/logs: volumen con access.log | /srv/report: donde se escribe report.html
RUN mkdir -p /srv/logs /srv/report /etc/goaccess \
    && chown -R goaccess:goaccess /srv/report

COPY goaccess.conf /etc/goaccess/goaccess.conf

# Ruta de logs que debe leer el contenedor
ENV LOG_FILE=/srv/logs/access.log

# Puerto WebSocket para tiempo real
EXPOSE 7890

# El proceso corre sin privilegios
USER goaccess

# Espera a que Nginx cree el log y lanza GoAccess en tiempo real
CMD ["sh", "-c", "until [ -f \"$LOG_FILE\" ]; do echo 'Esperando access.log...'; sleep 1; done; exec goaccess \"$LOG_FILE\" --config-file=/etc/goaccess/goaccess.conf --output=/srv/report/report.html --real-time-html"]
