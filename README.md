# Cartas Grupo Berrenchina

Carta digital de Restaurante Fuerte Santiago y A.A.V.V. San García - Mar y Monte (Algeciras).

- `index.html`: la web completa (portada, carta de cada local, alérgenos, español e inglés).
- `logos/`: logos vectoriales.

Se publica con GitHub Pages desde la rama `main`.

## Dominio grupoberrenchina.com

Cuando el dominio esté comprado:

1. En el panel DNS del registrador:
   - Registros A de `@` a 185.199.108.153, 185.199.109.153, 185.199.110.153 y 185.199.111.153
   - Registro CNAME de `www` a `mauroibansa.github.io`
2. En GitHub: Settings → Pages → Custom domain → `grupoberrenchina.com` → Save. Cuando el certificado esté listo, marcar "Enforce HTTPS".

## Dos cartas

- `index.html`: carta pública, sin bebidas. No se edita a mano.
- `mesa-*/index.html`: carta completa con bebidas, solo para el QR de mesa (noindex, sin enlaces desde la pública). Es la que se edita.
- Tras editarla: `python3 build.py` regenera `index.html` quitando lo marcado entre `/*BEBIDAS*/` y `/*FIN-BEBIDAS*/`.
