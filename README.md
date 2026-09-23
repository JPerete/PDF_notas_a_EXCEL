Esta es una aplicación sencilla creada en Python para transformar el PDF de las notas provisionales de las convocatorias de la AGE, que vienen ordenadas alfabéticamente, a un EXCEL ordenado por nota, pasa poder saber mejor en que posición se ha quedado.

Para ejecutarlo lo más sencillo es seguir estos pasos:
  1: usar un editor de código como Visual Studio Code
  2: instalar Python desde https://www.python.org/
  3: instalar los paquetes necesarios (pandas, pdfplumber y openpyxl) con los comandos
    - pip install pandas
    - pip install pdfplumber
    - pip install openpyxl
  4: ejecutar el código
  5: también puedes hacer un ejecutable instalando pyinstaller con el comando:
    - pip install pyinstaller
    y después ejecutando el comando: 
    - pyinstaller --onefile --noconsole --name "PDF_notas_a_EXCEL" --icon="PDF_to_EXCEL.ico" pdf_notas_a_excel-v1.py

  Siéntete libre de modificar el código a tu gusto.
