Esta es una aplicación sencilla creada en Python para transformar el PDF de las notas provisionales de las convocatorias de la AGE, que vienen ordenadas alfabéticamente, a un EXCEL ordenado por nota, pasr poder saber mejor en que posición se ha quedado.<br>
<br>
Para ejecutarlo lo más sencillo es seguir estos pasos:<br>
&emsp;1: usar un editor de código como Visual Studio Code<br>
&emsp;2: instalar Python desde https://www.python.org/<br>
&emsp;3: instalar los paquetes necesarios (pandas, pdfplumber y openpyxl) con los comandos<br>
&emsp;&emsp;- pip install pandas<br>
&emsp;&emsp;- pip install pdfplumber<br>
&emsp;&emsp;- pip install openpyxl<br>
&emsp;4: ejecutar el código<br>
&emsp;5: también puedes hacer un ejecutable instalando pyinstaller con el comando:<br>
&emsp;&emsp;- pip install pyinstaller<br>
&emsp;y después ejecutando el comando: <br>
&emsp;&emsp;- pyinstaller --onefile --noconsole --name "PDF_notas_a_EXCEL" --icon="PDF_to_EXCEL.ico" pdf_notas_a_excel-v1.py<br>
<br>
También he incluido un ejecutable de la aplicación listo para usar en la carpeta "dist"<br>
<br>
Siéntete libre de modificar el código a tu gusto.<br>
