# CLAUDE.md — Calculadora de Fecha de Tratamiento (v2)

## Descripción del proyecto
Aplicación de escritorio en Python con interfaz Tkinter que calcula la fecha de finalización de un tratamiento médico a partir de una fecha de inicio y una duración expresada en días o semanas.

**Archivo principal:** `fecha_tratamiento.py`
**Entorno:** Python 3.14, gestor de paquetes `uv`
**Dependencias:** `tkcalendar==1.6.1`, `babel==2.18.0`

---

## Mejoras pendientes

### UX / Interfaz
- [ ] Validar que la cantidad ingresada sea mayor que 0 antes de calcular.
- [ ] Añadir "Meses" como unidad de duración (requiere `python-dateutil` y `relativedelta`).
- [ ] Restringir el campo de cantidad para aceptar solo dígitos (validación en tiempo real con `validatecommand`).
- [ ] Mostrar el total de días del tratamiento junto a la fecha de fin en el resultado.
- [ ] Deshabilitar el botón "Copiar Resultado" cuando no haya resultado calculado.

### Funcionalidad
- [ ] Historial de cálculos en la sesión: lista desplazable con los últimos N resultados.
- [ ] Exportar el resultado a un archivo `.txt`.
- [ ] Mostrar la fecha de fin en formato largo en español (ej. "19 de febrero de 2026").
- [ ] Modo inverso: calcular la duración entre dos fechas (fecha inicio → fecha fin).

### Código / Arquitectura
- [ ] Encapsular toda la UI y el estado en una clase `App(tk.Tk)` para eliminar variables globales.
- [ ] Separar la lógica de cálculo de fechas en funciones puras independientes de Tkinter.
- [ ] Añadir type hints y docstrings a todas las funciones.

### Modernización de la interfaz
- [ ] Migrar de Tkinter a una biblioteca con aspecto más moderno. Opciones evaluadas:
  - **`CustomTkinter`** *(recomendada)* — wrapper sobre Tkinter con temas oscuro/claro y widgets modernos. Migración casi directa al tener la misma API.
  - **`PyQt6` / `PySide6`** — aspecto nativo del SO, muy profesional. Mayor complejidad para una app pequeña.
  - **`Flet`** — Material Design basado en Flutter, muy visual. Requiere reescritura completa.
  - **`Dear PyGui`** — renderizado GPU, estilo de herramienta/dashboard. Orientado a apps más complejas.

### Distribución
- [ ] Empaquetar como ejecutable con `PyInstaller` para distribución sin necesidad de tener Python instalado.
