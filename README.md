##  FlaskClassic - Criptomonedas - VZ VII

Es un proyecto basado en consultas de precios reales de criptomonedas en una API externa llamada **Coinmarketcap** , las consultas y compras se realizaran con **dinero ficticio**.

## Instalación
1. Crear entorno virtual y activarlo.


      **Crearlo** :  python -m venv venv **ó** python3 -m venv venv 


	**Activarlo** :  Si tu sistema operativo es **Windows** :  venv\Scripts\activate  si es **MAC OS**: source venv/bin/activate

1. Instalar las dependencias del fichero requirements.txt

  	 pip install -r requirements.txt

1. Duplicar el fichero .env_template y renombrar a .env
       
	   Los valores deben ser:
            FLASK_APP=run.py
            FLASK_ENV= el que querais

1. **IMPORTANTE** Comprobar que has intruducido correctamente la API KEY, que ira  en el fichero **apiKEY.py**. En el caso de **no disponer** de API KEY lea el mensaje que aparece en el fichero .

1. Ejecutar comando : **flask run**
1. Abrir el navegador , introducir la dirección que se le asignará . Ej : localhost:5000 y a disfrutar.
## Soporte
Si tiene alguna duda puede consultar algunas de las páginas que le dejo a continuación:


[Página oficial de precios ](https://coinmarketcap.com/es/ "Página oficial de precios ")


[HTML](https://www.w3schools.com/html/ "HTML")


[CSS/WEB](https://developer.mozilla.org/es/docs/Web/CSS "CSS/WEB")
