from __future__ import annotations

import tkinter as tk
from datetime import date, datetime, timedelta

import customtkinter as ctk
from babel.dates import format_date
from dateutil.relativedelta import relativedelta
from tkcalendar import DateEntry

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


# ── Funciones puras ───────────────────────────────────────────────────────────

def calcular_fecha_fin(fecha_inicio: date, cantidad: int, unidad: str) -> tuple[date, int]:
    """Retorna (fecha_fin, total_dias). Soporta Días, Semanas y Meses."""
    if unidad == "Días":
        fecha_fin = fecha_inicio + timedelta(days=cantidad)
        total_dias = cantidad
    elif unidad == "Semanas":
        fecha_fin = fecha_inicio + timedelta(weeks=cantidad)
        total_dias = cantidad * 7
    else:  # Meses
        fecha_fin = fecha_inicio + relativedelta(months=cantidad)
        total_dias = (fecha_fin - fecha_inicio).days
    return fecha_fin, total_dias


def calcular_duracion(fecha_inicio: date, fecha_fin: date) -> dict:
    """Retorna dict con total_dias, semanas y dias_restantes."""
    total_dias = (fecha_fin - fecha_inicio).days
    return {
        "total_dias": total_dias,
        "semanas": total_dias // 7,
        "dias_restantes": total_dias % 7,
    }


def formatear_fecha_larga(fecha: date) -> str:
    """Formatea una fecha en español largo: '19 de febrero de 2026'."""
    return format_date(fecha, format="long", locale="es_ES")


# ── App ───────────────────────────────────────────────────────────────────────

class App(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()
        self.title("🩺 Calculadora de Tratamiento")
        self.geometry("450x510")
        self.resizable(False, False)

        self.resultado = tk.StringVar()
        self.resultado.trace_add("write", self._on_resultado_change)
        self.modo_inverso = tk.BooleanVar(value=False)
        self.cantidad_var = tk.StringVar()
        self.cantidad_var.trace_add("write", self._validar_digitos)

        self._build_ui()

    # ── Validaciones ──────────────────────────────────────────────────────────

    def _validar_digitos(self, *_args) -> None:
        valor = self.cantidad_var.get()
        if valor and not valor.isdigit():
            self.cantidad_var.set("".join(c for c in valor if c.isdigit()))

    def _on_resultado_change(self, *_args) -> None:
        estado = "normal" if self.resultado.get() else "disabled"
        self.btn_copiar.configure(state=estado)

    # ── Construcción de la UI ─────────────────────────────────────────────────

    def _build_ui(self) -> None:
        # Selector de modo
        ctk.CTkLabel(self, text="Modo:", anchor="w").pack(
            fill="x", padx=24, pady=(20, 0)
        )
        self.seg_modo = ctk.CTkSegmentedButton(
            self,
            values=["Calcular fecha de fin", "Calcular duración"],
            command=self._cambiar_modo,
        )
        self.seg_modo.set("Calcular fecha de fin")
        self.seg_modo.pack(fill="x", padx=20, pady=(4, 14))

        # Fecha de inicio
        ctk.CTkLabel(self, text="📅 Fecha de inicio:", anchor="w").pack(
            fill="x", padx=24
        )
        frame_fi = ctk.CTkFrame(self, fg_color="transparent")
        frame_fi.pack(fill="x", padx=24, pady=(4, 10))
        self.entry_fecha_inicio = DateEntry(
            frame_fi,
            date_pattern="dd-mm-yyyy",
            locale="es_ES",
            background="darkblue",
            foreground="white",
            borderwidth=2,
        )
        self.entry_fecha_inicio.pack(anchor="w")

        # Contenedor dinámico (alterna entre modo normal e inverso)
        self.frame_contenido = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_contenido.pack(fill="x", padx=20)

        # ── Modo normal ────────────────────────────────────────────
        self.frame_normal = ctk.CTkFrame(self.frame_contenido, fg_color="transparent")

        ctk.CTkLabel(self.frame_normal, text="⏱️ Unidad de duración:", anchor="w").pack(
            fill="x"
        )
        self.combo_unidad = ctk.CTkOptionMenu(
            self.frame_normal, values=["Días", "Semanas", "Meses"]
        )
        self.combo_unidad.set("Días")
        self.combo_unidad.pack(anchor="w", pady=(4, 10))

        ctk.CTkLabel(self.frame_normal, text="💊 Cantidad:", anchor="w").pack(fill="x")
        self.entry_cantidad = ctk.CTkEntry(
            self.frame_normal,
            textvariable=self.cantidad_var,
            placeholder_text="Ej: 30",
            width=140,
        )
        self.entry_cantidad.pack(anchor="w", pady=(4, 8))

        # ── Modo inverso ───────────────────────────────────────────
        self.frame_inverso = ctk.CTkFrame(self.frame_contenido, fg_color="transparent")

        ctk.CTkLabel(self.frame_inverso, text="📅 Fecha de fin:", anchor="w").pack(
            fill="x"
        )
        frame_ff = ctk.CTkFrame(self.frame_inverso, fg_color="transparent")
        frame_ff.pack(fill="x", pady=(4, 8))
        self.entry_fecha_fin = DateEntry(
            frame_ff,
            date_pattern="dd-mm-yyyy",
            locale="es_ES",
            background="darkblue",
            foreground="white",
            borderwidth=2,
        )
        self.entry_fecha_fin.pack(anchor="w")

        # Modo normal visible por defecto
        self.frame_normal.pack(fill="x")

        # Botón calcular
        self.btn_calcular = ctk.CTkButton(
            self, text="Calcular Fecha de Fin", command=self._calcular
        )
        self.btn_calcular.pack(pady=(16, 4))

        # Label de resultado
        self.lbl_resultado = ctk.CTkLabel(
            self,
            textvariable=self.resultado,
            font=ctk.CTkFont(size=13, weight="bold"),
            wraplength=400,
            justify="center",
        )
        self.lbl_resultado.pack(pady=10)

        # Botones copiar / limpiar
        frame_btns = ctk.CTkFrame(self, fg_color="transparent")
        frame_btns.pack(pady=4)

        self.btn_copiar = ctk.CTkButton(
            frame_btns,
            text="📋 Copiar",
            command=self._copiar_resultado,
            state="disabled",
            width=130,
        )
        self.btn_copiar.pack(side="left", padx=6)

        self.btn_limpiar = ctk.CTkButton(
            frame_btns,
            text="🧹 Limpiar",
            command=self._limpiar,
            fg_color="gray40",
            hover_color="gray30",
            width=130,
        )
        self.btn_limpiar.pack(side="left", padx=6)

    # ── Cambio de modo ────────────────────────────────────────────────────────

    def _cambiar_modo(self, valor: str) -> None:
        if valor == "Calcular duración":
            self.frame_normal.pack_forget()
            self.frame_inverso.pack(fill="x")
            self.btn_calcular.configure(text="Calcular Duración")
            self.modo_inverso.set(True)
        else:
            self.frame_inverso.pack_forget()
            self.frame_normal.pack(fill="x")
            self.btn_calcular.configure(text="Calcular Fecha de Fin")
            self.modo_inverso.set(False)
        self.resultado.set("")

    # ── Acciones ──────────────────────────────────────────────────────────────

    def _calcular(self) -> None:
        if self.modo_inverso.get():
            self._calcular_duracion()
        else:
            self._calcular_fecha_fin()

    def _calcular_fecha_fin(self) -> None:
        fecha_inicio = self.entry_fecha_inicio.get_date()
        unidad = self.combo_unidad.get()
        cantidad_str = self.cantidad_var.get()

        if not cantidad_str:
            self.resultado.set("⚠️ Introduce una cantidad.")
            return

        cantidad = int(cantidad_str)
        if cantidad <= 0:
            self.resultado.set("⚠️ La cantidad debe ser mayor que 0.")
            return

        fecha_fin, total_dias = calcular_fecha_fin(fecha_inicio, cantidad, unidad)
        fecha_larga = formatear_fecha_larga(fecha_fin)
        fecha_corta = fecha_fin.strftime("%d-%m-%Y")
        self.resultado.set(
            f"✅ Finaliza el {fecha_larga}\n({fecha_corta} · {total_dias} días en total)"
        )

    def _calcular_duracion(self) -> None:
        fecha_inicio = self.entry_fecha_inicio.get_date()
        fecha_fin = self.entry_fecha_fin.get_date()

        if fecha_fin <= fecha_inicio:
            self.resultado.set("⚠️ La fecha de fin debe ser posterior a la de inicio.")
            return

        datos = calcular_duracion(fecha_inicio, fecha_fin)
        total = datos["total_dias"]
        semanas = datos["semanas"]
        dias_r = datos["dias_restantes"]

        if semanas > 0 and dias_r > 0:
            sp = "s" if semanas != 1 else ""
            dp = "s" if dias_r != 1 else ""
            detalle = f"{semanas} semana{sp} y {dias_r} día{dp}"
        elif semanas > 0:
            sp = "s" if semanas != 1 else ""
            detalle = f"{semanas} semana{sp} exacta{'s' if semanas != 1 else ''}"
        else:
            dp = "s" if total != 1 else ""
            detalle = f"{total} día{dp}"

        self.resultado.set(f"📏 Duración: {total} días\n({detalle})")

    def _copiar_resultado(self) -> None:
        self.clipboard_clear()
        self.clipboard_append(self.resultado.get())
        self.update()

    def _limpiar(self) -> None:
        self.entry_fecha_inicio.set_date(datetime.today())
        self.entry_fecha_fin.set_date(datetime.today())
        self.cantidad_var.set("")
        self.combo_unidad.set("Días")
        self.resultado.set("")


if __name__ == "__main__":
    app = App()
    app.mainloop()
