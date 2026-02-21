# 🩺 Calculadora de Fecha de Tratamiento

Aplicación de escritorio para calcular la fecha de finalización de un tratamiento médico, o la duración entre dos fechas. Diseñada para uso rápido en entornos clínicos o administrativos.

---

## ¿Qué hace?

### Modo normal — *Calcular fecha de fin*
Dado una fecha de inicio y una duración (en días, semanas o meses), calcula la fecha exacta en que termina el tratamiento.

**Ejemplo:**
> Inicio: 20-01-2026 · Duración: 1 mes
> → ✅ Finaliza el 20 de febrero de 2026 (20-02-2026 · 31 días en total)

### Modo inverso — *Calcular duración*
Dadas dos fechas (inicio y fin), calcula cuántos días dura el período y lo desglosa en semanas y días.

**Ejemplo:**
> Inicio: 01-01-2026 · Fin: 19-02-2026
> → 📏 Duración: 49 días (7 semanas exactas)

---

## Funcionalidades

| Funcionalidad | Detalle |
|---|---|
| Unidades de duración | Días, Semanas, Meses |
| Formato de fecha largo | "19 de febrero de 2026" en español |
| Validación de entrada | El campo cantidad solo acepta dígitos (en tiempo real) |
| Validación de lógica | Cantidad > 0; fecha fin > fecha inicio en modo inverso |
| Copiar al portapapeles | Botón deshabilitado hasta que haya un resultado calculado |
| Limpiar campos | Resetea todos los campos al estado inicial |
| Interfaz moderna | Tema oscuro con CustomTkinter |

---

## Capturas

```
┌─────────────────────────────────────────────────┐
│  Modo:  [ Calcular fecha de fin │ Calcular dur.] │
│                                                 │
│  📅 Fecha de inicio:  [19-02-2026 ▼]            │
│                                                 │
│  ⏱️ Unidad de duración:  [Días ▼]               │
│  💊 Cantidad:  [30         ]                    │
│                                                 │
│          [ Calcular Fecha de Fin ]              │
│                                                 │
│   ✅ Finaliza el 21 de marzo de 2026            │
│      (21-03-2026 · 30 días en total)            │
│                                                 │
│    [ 📋 Copiar ]       [ 🧹 Limpiar ]           │
└─────────────────────────────────────────────────┘
```

---

## Instalación y uso

### Requisitos
- Python 3.14+
- [`uv`](https://docs.astral.sh/uv/) (gestor de paquetes y entornos)

### Pasos

```bash
# 1. Clonar o descargar el proyecto
cd fecha_tratamiento/v2

# 2. Instalar dependencias
uv sync

# 3. Ejecutar la aplicación
uv run fecha_tratamiento.py
```

---

## Dependencias

| Librería | Versión | Uso |
|---|---|---|
| [`customtkinter`](https://github.com/TomSchimansky/CustomTkinter) | ≥ 5.2.2 | Interfaz gráfica moderna (tema oscuro/claro) |
| [`tkcalendar`](https://github.com/j4321/tkcalendar) | ≥ 1.6.1 | Widget `DateEntry` para seleccionar fechas con calendario |
| [`python-dateutil`](https://dateutil.readthedocs.io/) | ≥ 2.9 | `relativedelta` para cálculos correctos en meses |
| [`babel`](https://babel.pocoo.org/) | ≥ 2.18 | Formato de fecha largo en español ("19 de febrero de 2026") |

---

## Arquitectura del código

```
fecha_tratamiento.py
│
├── calcular_fecha_fin(fecha_inicio, cantidad, unidad)
│       Función pura. Retorna (fecha_fin, total_dias).
│
├── calcular_duracion(fecha_inicio, fecha_fin)
│       Función pura. Retorna dict con total_dias, semanas y dias_restantes.
│
├── formatear_fecha_larga(fecha)
│       Función pura. Retorna string en español largo vía Babel.
│
└── class App(ctk.CTk)
        Toda la interfaz y el estado de la aplicación.
        ├── _build_ui()           — construcción de widgets
        ├── _cambiar_modo()       — alterna entre modo normal e inverso
        ├── _calcular_fecha_fin() — lógica modo normal
        ├── _calcular_duracion()  — lógica modo inverso
        ├── _validar_digitos()    — filtro en tiempo real del campo cantidad
        ├── _on_resultado_change()— habilita/deshabilita botón Copiar
        ├── _copiar_resultado()   — copia al portapapeles
        └── _limpiar()            — resetea todos los campos
```

---

## Herramientas utilizadas en el desarrollo

| Herramienta | Rol |
|---|---|
| **Python 3.14** | Lenguaje de programación |
| **uv** | Gestión del entorno virtual y dependencias |
| **CustomTkinter** | Framework de UI con tema oscuro y widgets modernos |
| **tkcalendar** | Selector de fecha visual integrado con Tkinter |
| **python-dateutil** | Aritmética de fechas con meses exactos (`relativedelta`) |
| **Babel** | Internacionalización: formato de fechas en español |
| **Claude Code** | Asistente de desarrollo (refactoring, diseño de arquitectura, implementación) |
| **Git** | Control de versiones |
