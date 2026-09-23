Esta es una aplicación sencilla creada en Python para transformar el PDF de las notas provisionales de las convocatorias de la AGE, que vienen ordenadas alfabéticamente, a un EXCEL ordenado por nota, pasa poder saber mejor en que posición se ha quedado.<br>
<br>
Para ejecutarlo lo más sencillo es seguir estos pasos:<br>
  1: usar un editor de código como Visual Studio Code<br>
  2: instalar Python desde https://www.python.org/<br>
  3: instalar los paquetes necesarios (pandas, pdfplumber y openpyxl) con los comandos<br>
    - pip install pandas<br>
    - pip install pdfplumber<br>
    - pip install openpyxl<br>
  4: ejecutar el código<br>
  5: también puedes hacer un ejecutable instalando pyinstaller con el comando:<br>
    - pip install pyinstaller<br>
    y después ejecutando el comando: <br>
    - pyinstaller --onefile --noconsole --name "PDF_notas_a_EXCEL" --icon="PDF_to_EXCEL.ico" pdf_notas_a_excel-v1.py<br>
<br>
  Siéntete libre de modificar el código a tu gusto.<br>
