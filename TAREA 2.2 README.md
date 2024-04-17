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
   Unicamente aqui estamos dando como entrada un saludo normal, en mi caso `Hola`
   ~~~
   expresion_regular = re.compile(r"hola", re.IGNORECASE)
   ~~~

   ![WhatsApp Image 2024-04-16 at 21 35 18_11509e7c](https://github.com/JAEP-22/Yesenia/assets/160981030/7a45aec8-192d-4902-b4b4-bf13fddee8a7)




