# Repositorio de instancia de Odoo14 en github codespaces con modulos personalizados

Este repositorio contiene mi proyecto y se ha configurado para que puedas trabajar en él de forma eficiente utilizando GitHub Codespaces.

## Acceso a GitHub Codespaces

Para acceder a este proyecto en GitHub Codespaces, sigue estos pasos:

1. **Fork este repositorio:** Haz clic en el botón "Fork" en la esquina superior derecha de esta página para crear una copia de este repositorio en tu propia cuenta de GitHub.

2. **Abre GitHub Codespaces:** Ve a tu repositorio recién bifurcado y haz clic en el botón "Code" (Código) y selecciona "Open with Codespaces" (Abrir con Codespaces) en el menú desplegable.

3. **Espera a que se cargue:** GitHub Codespaces configurará un entorno de desarrollo en la nube para ti. Esto puede llevar un tiempo dependiendo del tamaño de tu proyecto.

Ejemplo de vista dentro de base de datos

![Alt text](/assets/img/img.png)
![Alt text](/assets/img/img_1.png)

Scripts necesarios para levantar la instancia
```
docker compose up -d
docker compose up -d --build
docker compose up --build


curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

```





