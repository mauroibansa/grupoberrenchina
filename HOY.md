# Menú y plato del día

La web lee `hoy.json` y muestra la entrada con la fecha de hoy (hora de España). Si no hay entrada para hoy, no enseña platos: Fuerte Santiago muestra "Pregunta por el menú de hoy" y Mar y Monte el texto genérico del plato del día. Se pueden dejar cargados días futuros.

Formato (fecha AAAA-MM-DD). Cada grupo es una lista de platos, y cada plato va solo en español o como ["español", "inglés"]:

```json
{
  "fuerte-santiago": {
    "2026-10-06": {
      "primeros": [["Salmorejo", "Salmorejo (cold tomato soup)"], ["Ensalada mixta", "Mixed salad"]],
      "segundos": [["Merluza a la plancha", "Grilled hake"]],
      "postre": [["Flan casero", "Homemade flan"]],
      "precio": 12
    }
  },
  "mar-y-monte": {
    "2026-10-06": { "plato": [["Lentejas con chorizo", "Lentils with chorizo"]] },
    "2026-10-11": { "cerrado": true }
  }
}
```

- `precio` es opcional (por defecto 12 € y 6 €).
- `incluye` es opcional, por ejemplo `["Pan y bebida", "Bread and a drink"]`.
- `"cerrado": true` muestra que ese día no hay menú o plato del día.

Para editarlo a mano: abrir `hoy.json` en GitHub, pulsar el lápiz, cambiar y "Commit changes". La web se actualiza en un par de minutos.
