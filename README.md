Esta es una aplicación sencilla creada en Python para transformar el PDF de las notas provisionales de las convocatorias de la AGE, que vienen ordenadas alfabéticamente, a un EXCEL ordenado por nota, para poder saber mejor en que posición se ha quedado.<br>
<br>
El funcionamiento es simple. El desplegable de la fecha de la convocatoria es para que la ponga al final del nombre del archivo Excel que genera. Elige el PDF con las notas y dale al botón "Generar Excel Ordenado". Si todo sale bien, el Excel se creará en la misma carpeta donde se encuentra el PDF y te abrirá el Excel generado.<br>
<br>
He incluido un ejecutable de la aplicación listo para usar en la carpeta &lt;dist&gt;<br>
<br>
Pero si quieres ejecutarlo desde el código puedes seguir estos pasos:<br>
&emsp;1: usa un editor de código como Visual Studio Code<br>
&emsp;2: instala Python desde https://www.python.org/<br>
&emsp;3: instala los paquetes necesarios (pandas, pdfplumber y openpyxl) con los comandos<br>
&emsp;&emsp;- pip install pandas<br>
&emsp;&emsp;- pip install pdfplumber<br>
&emsp;&emsp;- pip install openpyxl<br>
&emsp;4: ejecuta el código<br>
&emsp;5: también puedes hacer un ejecutable instalando pyinstaller con el comando:<br>
&emsp;&emsp;- pip install pyinstaller<br>
&emsp;y después ejecuta siguiente el comando para realizar el ejecutable: <br>
&emsp;&emsp;- pyinstaller --onefile --noconsole --name "PDF_notas_a_EXCEL" --icon="PDF_to_EXCEL.ico" pdf_notas_a_excel-v1.py<br>
<br>
Siéntete libre de modificar el código a tu gusto.<br>
