# Version 1
import pdfplumber
import pandas as pd
import re
import os
from datetime import datetime
from tkinter import Tk, ttk, Button, Label, filedialog, messagebox  

class AplicacionOposicion:
    def __init__(self, root: Tk): # Incicializar la ventana
        self.root = root
        self.root.title("Extractor de Notas de Oposición")
        self.root.geometry("450x350")
        self.root.attributes('-topmost', True)

        # Cambia el icono de la ventana de la aplicación ---
        try:
            self.root.iconbitmap("PDF_to_EXCEL.ico")
        except Exception:
            # Si el archivo no se encuentra, el programa continuará sin romperse
            pass

        self.ruta_pdf_seleccionado = ""

        # Selector de año
        Label(root, text="1. Selecciona el Año de la Convocatoria:", font=("Arial", 10, "bold")).pack(pady=(15, 5))
        ano_actual = datetime.now().year
        anyos_disponibles = [str(año) for año in range(ano_actual, ano_actual - 15, -1)]

        self.combo_anos = ttk.Combobox(root, values=anyos_disponibles, state="readonly", font=("Arial", 10), width=15)
        self.combo_anos.set(str(ano_actual))
        self.combo_anos.pack(pady=5)

        # Selector de PDF
        Label(root, text="2. Selecciona el archivo PDF de la lista:", font=("Arial", 10, "bold")).pack(pady=(15, 5))
        self.btn_buscar = Button(root, text="Buscar PDF...", command=self.buscar_pdf, font=("Arial", 10), bg="#2196F3", fg="white")
        self.btn_buscar.pack(pady=5)

        # Etiqueta dinámica que mostrará el nombre del archivo seleccionado
        self.lbl_archivo = Label(root, text="Ningún archivo seleccionado", font=("Arial", 9, "italic"), fg="gray", wraplength=400)
        self.lbl_archivo.pack(pady=5)

        # Divider visual
        ttk.Separator(root, orient='horizontal').pack(fill='x', padx=30, pady=10)

        # Botón de procesar (desactivado al principio)
        self.btn_procesar = Button(root, text="Generar Excel Ordenado", command=self.ejecutar_proceso, font=("Arial", 11, "bold"), bg="#4CAF50", fg="white", state="disabled")
        self.btn_procesar.pack(pady=10)

        # Etiqueta de estado de procesamiento (empieza vacía)
        self.lbl_estado = Label(root, text="", font=("Arial", 10, "italic"), fg="#002244")
        self.lbl_estado.pack(pady=5)

        # Créditos / Disclaimer al pie de la ventana
        self.lbl_creditos = Label(root, text="Aplicación desarrollada por Juan Perete Pinar con ayuda de la IA", font=("Arial", 8, "italic"), fg="gray")
        self.lbl_creditos.pack(pady=(10, 0))
        self.lbl_contacto = Label(root, text="Contacto: juan.peretepinar@gmail.com", font=("Arial", 8, "italic"), fg="gray")
        self.lbl_contacto.pack(side="bottom", pady=(2, 10))

        
    def buscar_pdf(self): # Abre el explorador de archivos y actualiza el texto de la interfaz.
        ruta = filedialog.askopenfilename(title="Selecciona el PDF de la oposición",filetypes=[("Archivos PDF", "*.pdf")])

        
        if ruta: self.ruta_pdf_seleccionado = ruta # Usamos el operador ternario para acortar el texto si el nombre es muy largo
        nombre_corto = os.path.basename(ruta)
        self.lbl_archivo.config(text=f"Archivo: {nombre_corto}", fg="black")
        self.btn_procesar.config(state="normal") # Activamos el botón de procesar 


    def ejecutar_proceso(self): # Lanza el proceso y muestra un mensaje de éxito o error al terminar.
        # Mostramos el mensaje de carga y desactivamos los controles
        self.lbl_estado.config(text="Procesando PDF, por favor espera...", fg="#2196F3")
        self.btn_procesar.config(state="disabled")
        self.btn_buscar.config(state="disabled")
        
        # Forzamos a la ventana a dibujarse con el nuevo texto antes de congelarse con el PDF
        self.root.update()
        ano = self.combo_anos.get()
        exito, ruta_excel = AplicacionOposicion.procesar_oposicion(self.ruta_pdf_seleccionado, ano)

        if exito:  # Cierra la aplicación por completo al terminar con éxito
            self.lbl_estado.config(text="¡Completado con éxito!", fg="#4CAF50")
            os.startfile(ruta_excel) # Abre el Excel con el programa predeterminado de Windows
            messagebox.showinfo("¡Éxito!", f"El archivo Excel se ha creado correctamente en:\n\n{ruta_excel}")
            self.root.destroy()  # Cierra la aplicación   
        else:
            self.lbl_estado.config(text="Error en el procesamiento", fg="red")
            messagebox.showerror("Error", "No se han podido extraer datos válidos del PDF.\nComprueba el formato de las notas.")
            # Si falla, volvemos a activar los botones para dejarle reintentar
            self.btn_procesar.config(state="normal")
            self.btn_buscar.config(state="normal")


    @staticmethod
    def extraer_datos_columna(texto_columna): # Procesa el texto línea por línea para extraer DNI, Nombre y Nota.
        filas = []
        lineas = texto_columna.split('\n')

        for linea in lineas:
            linea = linea.strip()
            if not linea:
                continue

            # FILTRO: Si la línea contiene la palabra "Registros" (o similares), saltamos a la siguiente (para que no procese los piés de página)
            if "Registros" in linea or "Nº" in linea:
                continue

            # Esta expresión regular busca:
            # 1. El DNI al principio (incluye números entre asteriscos)
            # 2. El nombre y apellidos en el medio
            # 3. La nota al final (número con coma decimal)
            match_linea = re.search(r'^(\*+\d+\*+)\s+(.+?)\s(\d+,\d+)+$', linea)
            

            if match_linea:
                dni = match_linea.group(1)
                nombre = match_linea.group(2)
                nota_texto = match_linea.group(3)
                # Convertimos la nota a número flotante sustituyendo la coma por punto
                nota_numero = float(nota_texto.replace(',', '.'))
                
                filas.append({
                    "DNI": dni, 
                    "Apellidos y nombre": nombre, 
                    "Nota": nota_numero})
        return filas
    

    @staticmethod
    def procesar_oposicion(ruta_pdf, ano_convocatoria): #Realiza la lectura del PDF y genera el archivo Excel ordenado. 
        carpeta_origen = os.path.dirname(ruta_pdf)
        nombre_excel = f"resultado_notas_convocatoria_{ano_convocatoria}.xlsx"
        excel_path = os.path.join(carpeta_origen, nombre_excel)    

        datos_finales = []

        with pdfplumber.open(ruta_pdf) as pdf:
            for i, pagina in enumerate(pdf.pages):
                ancho = pagina.width
                alto = pagina.height

                # Dividimos la página verticalmente por la mitad para simular dos columnas
                mitad = ancho / 2

                # Definimos las cajas de las columnas (izquierda y derecha)

                # Bounding box: (x0, top, x1, bottom)
                caja_izquierda = (0, 0, mitad, alto)
                caja_derecha = (mitad, 0, ancho, alto)

                # Extraemos el texto de cada mitad

                texto_izq = pagina.within_bbox(caja_izquierda).extract_text()
                texto_der = pagina.within_bbox(caja_derecha).extract_text()

                # Procesamos columna izquierda

                if texto_izq:
                    datos_finales.extend(AplicacionOposicion.extraer_datos_columna(texto_izq))

                # Procesamos columna derecha (si existe contenido real de dos columnas)

                if texto_der and len(texto_der.strip()) > 2: # Evita espacios vacíos o ruido
                    datos_finales.extend(AplicacionOposicion.extraer_datos_columna(texto_der))

        # Convertimos los datos estructurados en una tabla de Pandas

        df = pd.DataFrame(datos_finales)

        if not df.empty:
            df = df.sort_values(by="Nota", ascending=False)
            df.insert(0, "Posición", range(1, len(df) + 1)) # Insertamos la columna "Posición"
            df.to_excel(excel_path, index=False)
            return True, excel_path
        return False, None

# --- FLUJO PRINCIPAL DEL PROGRAMA ---
if __name__ == "__main__":
    ventana_principal = Tk()
    app = AplicacionOposicion(ventana_principal)
    ventana_principal.mainloop()
    