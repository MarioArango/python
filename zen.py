import this

print(this)

#1. Bello es mejor que feo 
#Python es un lenguaje muy limpio y superior semanticamente

#2. Explicito es mejor que implicito
#Si podemos hacer algo más código con el fin de que sea más 
#entendible, es mejor que hacer poco código inentendible.

#3. Simple es mejor que complejo
#Si podemos hacerlo de una forma sencilla, es mejor usar esa forma

#4. Complejo es mejor que complicado
# Si debemos que extendernos contal de solucionar el problema
# es mejor que hacerlo simple y mal

#5. Plano es mejor que anidado
#Bloque debajo de otro

#6. Espaciado es mejor que denso
#Identacion obligatoria, siempre se cumple

#7. La legibilidad es importante
#Código entendible y legible

#8. Los casos especiales no son lo suficientemente especiales
#para romper las reglas
#Si se puede respetar las reglas, se debe hacerlo

#9. La practicidad le gana a la pureza
#Pero si las reglas de python rompe la practicidad del codigo,
#entonces sí, romple las reglas.

#10. Los errores nunca deberian pasar silenciosamente
#Siempre se deben manejar de forma explicita, sin asumir

#11. A menos que se silencien explicitamente
#Siempre se maneja los errores de forma explicita

#12. Frente a la ambiguedad evitar la tentacion de adivinar
#El codigo debe representar siempre lo mismo

#13. Debiería haber una, y preferiblemente solo una, manera obvia de hacerlo

#14. A pesar de que esa manera no sea obvia a menos que seas holandes

#15. Ahora es mejor que nunca
#Si tenemos la solucion, apliquemosla

#16. A pesar de que nunca  es muchas veces mejor  que ahora mismo
#Si por apresurarnos desarrollamos mal codigo, entonces dejemoslo para despues

#17. Si la implementacion es dificil de explicar, es una mala idea

#18. Si la implementacion es facil de explicar, puede que sea una buena idea

#19. Los espacios de nombre, son una gran idea, tengamos más de esos
#


#PEP
#Nos dice los estandares de python
#PEP8: guia de estilos de python

#Crear entorno virtual
#python -m venv venv

#Activar el modulo
#.\venv\Scripts\activate

#Desactivar
#deactivate

#Alias para activar rapido
#doskey avenv=.\venv\Scripts\activate
#ahora se digita avenv y se activa el entrono virtual

#PIP
#Es el gestor de modulos de python <> npm
#Packege installer for python

#pip freeze -> Muestra todos los modulos instalados en el proyecto o entorno virtual

#pip install pandas -> Se instala el modulo pandas

#pip freeze > requirements.txt -> compartir el archivo de dependencias y tener las mismas versiones
#crea el archivo requiremetns.txt <> package.json

#Para compartir el proyecto via github
#pip install -r requeriments.txt -> descarga las dependencias <> npm install

#En el .gitignore incluir venv <> node_modeules
