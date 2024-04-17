# Expresiones Regulares con bot de Telegram

## Creacion del bot en Telegram 

1. Para poder iniciar nuestra practica con el bot primero tenemos que instalar `Telegram` en nuestro dispositivo movil
2. Buscar el bot llamado `BotFaher`
3. Mande el mensaje `/start` para que me diera el manual de instrucciones
4. Coloque el comando `/newbot` para crear nuestro nuevo bot personal
5. Nos pide el nombre que le queremos colocar en mi caso le puse el nombre de `Joshi` con el nombre de usuario `Ifeelfantasticbot`
6. Al realizar todo esto nos deberia proporcionar un token que nos servira mas adelante

## Instalacion de python y la biblioteca del bot
1. Instalar `Python` en nuestro ordenador para poder ejecutar nuestro `Script` en Visual

   ![image](https://github.com/JAEP-22/Yesenia/assets/160981030/1b7ab18b-41d1-496e-adab-c3a09ba95278)

2. Instalar la biblioteca `python-telegram-bot` ***EL CODIGO MOSTRADO ACONTINUACION SE EJECUTA UNICAMENTE EN EL CMD*** 
   ~~~
   pip install python-telegram-bot
   ~~~

## Token 
1. Con el codigo que nos proporciono el profesor buscar el apartado de `"Token"` para asi colocar el nuestro
   
![image](https://github.com/JAEP-22/Yesenia/assets/160981030/61542403-219b-40b2-9334-d59119e97c3e)

2. Ejecutamos nuestro codigo y ahora si ***que empiece la magia***

## Platicando con el bot 

1. Para poder hacer que nuestro bot no responda unicamente con la palabra `Hola` procedi a colocar mas expreciones regulares para asi hacerlo un poco mas complejo

## Expresiones regulares 

1. Saludo
   - Unicamente aqui estamos dando como entrada un saludo normal, en mi caso `Hola`
   ~~~
   expresion_regular = re.compile(r"hola", re.IGNORECASE)
   ~~~
![WhatsApp Image 2024-04-16 at 21 37 00_65aa1985](https://github.com/JAEP-22/Yesenia/assets/160981030/ebe629d1-bb8d-4028-b7ff-49712963bc30)

2. Menu
   - Al momento de poner en nuestra frase la palabra `Menu` nos despliega un menu muy interesante del dia
   ~~~
   expresion_menu = re.compile(r"Menu", re.IGNORECASE)
   ~~~

![WhatsApp Image 2024-04-16 at 22 28 56_1df72f28](https://github.com/JAEP-22/Yesenia/assets/160981030/48ef82ca-c70c-4b90-9908-79cfd8766e3a)

3. Si
   - Aqui al momento de poner que `si` nos gustaria probar el menu nos pide nuestra direccion
   ~~~
   expresion_si = re.compile(r"si", re.IGNORECASE)
   ~~~
![WhatsApp Image 2024-04-16 at 22 35 28_7f0c686b](https://github.com/JAEP-22/Yesenia/assets/160981030/6914ef57-a714-41b9-aa45-4e8b497824f8)

4. No
   - Cuando decimos que `no` estamos interesados en el menu nos sale el siguiente mensaje    
   ~~~
   expresion_no = re.compile(r"no", re.IGNORECASE)
   ~~~
![WhatsApp Image 2024-04-16 at 22 35 29_f28f9143](https://github.com/JAEP-22/Yesenia/assets/160981030/d163af35-8957-4231-91c9-1ef1ddabce6a)

5. Direccion
   - Aqui unicamente vamos a dar la direccion en la cual queremos que llegue nuestro producto y nos informara de que si queremos mas o no
   ~~~
   expresion_direccion = re.compile(r"(calle)*[a-zA-Z0-9_.+-]" , re.IGNORECASE)
   ~~~ 
![WhatsApp Image 2024-04-16 at 22 41 13_8fc10330](https://github.com/JAEP-22/Yesenia/assets/160981030/14a7f2b7-4f66-41c6-a321-544b99af2b16)

6. Reju
   - Al momento de seleccionar esta opcion nos saldra el siguiente mensaje
   ~~~
   expresion_reju = re.compile(r"reju")
   ~~~
   ![WhatsApp Image 2024-04-16 at 22 43 49_7be9bb58](https://github.com/JAEP-22/Yesenia/assets/160981030/ad010ee2-f074-40bd-aa29-7c05ca2b67d3)

7. Dijo que no
   - Cuando dices la frase `Soy tacano` utilice la misma expresion que en el paso 4

   ![WhatsApp Image 2024-04-16 at 22 41 15_9c07e8ab](https://github.com/JAEP-22/Yesenia/assets/160981030/c139f3d8-f381-4269-bca6-0b68ef2c3cc7)

## Concluciones 

