**Parte 2 de la práctica II, Optimización 2: reimplementación de secciones de código del paquete construído para uso de niveles de BLAS, compilación a C, cómputo en paralelo, concurrente o distribuido. Preparación para la entrega de su práctica / proyecto final**

Antes de iniciar a trabajar: 

* **Sólo una persona de cada equipo debe darle click a la liga** que está indicada en la publicación de canvas. Una vez que le dé click a la liga tal persona **invite** a sus integrantes de su equipo como **Admin**. Para invitar a su integrante ir dentro del repo a Settings -> Manage Access y enviar la invitación ingresando user de github de su integrante.
    

# Instrucciones

Se encuentran en el archivo [instrucciones.ipynb](instrucciones.ipynb).

Usen `git` para llevar la historia de cambios en la realización de sus notebooks o cualquier otro archivo y subirlos a sus repos. No se revisarán aquellos archivos que tengan un commit con todas las respuestas. El trabajo es incremental.

**Deben usar la funcionalidad de github**: *issues*, *milestones*, *projects*, *reviewers*, *asignees* o lo que ustedes consideren de github que les ayudará a comunicarse/organizarse (no tienen que usar todas las funcionalidades anteriores y cada equipo decide qué usar). Ver por [ejemplo video para crear proyectos en github](https://youtu.be/z4Xpif7HI04).


# Dinámica

Dividir a su equipo para realizar cuatro tareas. **Ustedes deciden qué integrante resuelve qué tarea**:

1. 2 personas que realicen perfilamiento del código.  

2. 2 personas que realicen reimplementación / adición / eliminación de secciones al código de acuerdo al perfilamiento realizado. 

3. 1 persona que sea *project manager* (más detalles de este rol en las notas), cree nuevos *tests* para la reimplementación / adición / eliminación de secciones al código, haga actualización de documentación hecha con *Sphinx* y *software* en las imágenes de *docker*.

Entre todos los y las integrantes tienen que dar *feedback* si es necesario en la resolución de las tareas que haya duda entre ustedes. El *feedback* consiste en resolver/explicar las dudas que existan. **Las personas asignadas a la tarea correspondiente son las que realizan los *commits* una vez resueltas las dudas**.

Los puntos 1, 2 y 3 anteriores los realizan de forma iterativa hasta finalizar las tareas y que estén en acuerdo las y los integrantes de cada equipo con las soluciones.

# Lenguajes de programación

Ustedes eligen el lenguaje de programación a usar. La sugerencia es *Python3*.

# Calificación

La calificación de esta segunda parte es la mitad de la práctica 2. Se asgina una calificación individual por tarea asignada y una calificación por equipo. Se calificará de acuerdo a los *commits* realizados y a los avances que realizan en su trabajo incremental. 

**Tomaré la calificación de esta segunda parte para el % correspondiente del rubro de avances de la** [práctica/proyecto final](https://github.com/ITAM-DS/analisis-numerico-computo-cientifico/tree/optimizacion-2-2022/proyecto_final). Ver [indicaciones-práctica/proyecto final](https://github.com/ITAM-DS/analisis-numerico-computo-cientifico/tree/optimizacion-2-2022/proyecto_final/indicaciones#indicaciones).

# AWS

Adjunten *screenshots* en un directorio de su repo para mostrar su uso de AWS, debe aparecer en el *screenshot* su nombre, clave única u otra forma de identificar su trabajo. El trabajo en la nube consiste en probar las ejecuciones de su paquete.

Todas las personas del equipo conocen cómo levantar, configurar instancias de AWS y desplegar servicios allí. Uds elijan a una persona que sea la encargada de realizar lo anterior.

# Notas

* **Para la entrega crear un archivo con nombre:** `reporte_equipo_<aquí colocar_número>_parte_2_practica_2.ipynb`que contiene ejecución del paquete en el que se muestra el mejoramiento realizado para el recurso elegido (procesador, memoria, tiempo o I/O).

* Renombren este archivo `README.md` por `old_README.md` para que guarden su contenido y creen otro `README.md` donde escriban sus referencias y lo que realizará/realizó cada integrante.

* *Project manager*: es la persona más importante para el éxito del proyecto. Conoce el/los objetivo(s) a resolver, detalla las tareas que realizarán el grupo de programación y el grupo de revisión (creación de *tests* en nuestro caso), organiza y asigna a personas a ambos grupos, crea tarjetas en el [project board de github](https://help.github.com/en/github/managing-your-work-on-github/creating-a-project-board) y [milestones](https://help.github.com/en/github/managing-your-work-on-github/tracking-the-progress-of-your-work-with-milestones) para dar seguimiento a [issues](https://help.github.com/en/github/managing-your-work-on-github/creating-an-issue). Mantiene un contacto directo con el prof para dudas que tengan y para avisar en qué fase se encuentran. Les explica a su equipo de trabajo la correcta creación de *issues*, solución de los mismos y el uso de *milestones* y del *project board*.

* La división de las tareas y roles está está inspirada en el *framework* [scrum](https://www.youtube.com/watch?v=b02ZkndLk1Y&feature=emb_logo) en un ambiente laboral real (y en esta práctica estamos super-simplificando tal *framework*).

* Añadan referencias utilizadas para su trabajo en su `README.md`.

* **Los commits deben tener un mensaje explicatorio, no hacer lo siguiente:**

```
git commit -m "create 1" -i archivo1.txt

git commit -m "update 1" -i archivo1.txt #qué es update 1?

git commit -m "update 2" -i archivo1.txt #qué es update 2?

git commit -m "update 3" -i archivo1.txt #qué es update 3?
```

**así también para los *issues*, *projects*, *milestones*...**

* Esta organización es nuestro *playground* utilicen los repos de aquí para practicar :)

* Recuerden:

    * ir guardando su trabajo si usan binder y usar `git` para llevar la historia de sus cambios en sus repos :)
    * poner las referencias que utilizan (aún si le preguntan a una compañera o compañero de la clase coloquen esto en su entrega) pues no está permitido copiar y escribir que lo hicieron sin citar sus fuentes.


* Para dudas creen un *room* de gitter e ínvitenme :) (si ya lo hicieron omitan este enunciado)

* **Su trabajo individual y su tiempo es muy valioso e importante, también el trabajo en equipo. Si alguna persona del equipo no realizó su tarea asignada, esperaría que lo resolvieran entre ustedes, si no lo resuelven avísenme y no realicen su tarea asignada. Si tienen algún problema (familiar, salud,...) infórmenme con tiempo para ver qué podemos hacer :)**


