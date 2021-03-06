<p align = "center">
    <img src="images/logo_itam.png" width="300" height="110" />

---

## Tabla de contenido:
    
1. [Integrantes y roles asignados](https://github.com/optimizacion-2-2022-gh-classroom/practica-2-segunda-parte-EddOselotl#integrantes-y-roles-asignados)
    
2. [Acerca de este proyecto](https://github.com/optimizacion-2-2022-gh-classroom/practica-2-segunda-parte-EddOselotl#acerca-de-este-proyecto)
    
3. [Estructura básica del repositorio](https://github.com/optimizacion-2-2022-gh-classroom/practica-2-segunda-parte-EddOselotl#estructura-b%C3%A1sica-del-repositorio)
    
4. [¿Qué lenguajes y paqueterías utlizamos?](https://github.com/optimizacion-2-2022-gh-classroom/practica-2-segunda-parte-EddOselotl#qu%C3%A9-lenguajes-y-paqueter%C3%ADas-utlizamos)

5. [Ambientes en Contenedor](https://github.com/optimizacion-2-2022-gh-classroom/practica-2-segunda-parte-EddOselotl#ambientes-en-contenedor)

6. [Instancia de AWS](https://github.com/optimizacion-2-2022-gh-classroom/practica-2-segunda-parte-EddOselotld#instancia-de-aws)

7. [Resultados obtenidos](https://github.com/optimizacion-2-2022-gh-classroom/practica-2-segunda-parte-EddOselotld#resultados-obtenidos)
    
8. [Referencias](https://github.com/optimizacion-2-2022-gh-classroom/practica-2-primera-parte-urieluard#referencias)
    
---

## Integrantes y roles asignados

|     ***Integrante***      |             ***Usuario de GitHub***             |  ***Rol asignado***        |                       
|:-------------------------:|:-----------------------------------------------:|:--------------------------:|
|  Ita                      |    [sancas96](https://github.com/sancas96)      | Equipo de Programación     | 
|  Luz                      |    [LuzVerde23](https://github.com/LuzVerde23)  | Equipo de Programación     | 
|  Edgar                    |    [EddOselotl](https://github.com/EddOselotl)  | Administrador del proyecto | 
|  Uriel                    |    [urieluard](https://github.com/urieluard)    | Equipo de Programación     | 

---    

## Acerca de este proyecto
    
La segunda parte de la práctica 2 tiene como objetivo reimplementar su método numérico trabajado en las prácticas anteriores (MaxFlowAeiu) con alguna mejora en su desempeño, por ejemplo: 

  > Utilizando niveles de BLAS 
  
  > Cómputo en paralelo (CPU/GPU) 
  
  > Con compilación a C (por ejemplo vía cython, rcpp) o julia 
  
Para identificar las áreas de oportunidad en las que podría ser conveniente utilizar alguna de las estrategias amencionadas, se toma de referencia el perfilamiento de memoria, uso de procesador o tiempo de ejecución del paquete.
 
## Estructura básica del repositorio

```
practica-2-segunda-parte-EddOselotl:
 |
 ├── README.md                                   <- Contiene información relevante del proyecto.
 │
 ├── reporte_equipo_2_parte_2_practica_2.ipynb   <- Note Book con el reporte donde se muestran los resultados de las pruebas realizadas al algoritmo.
 |
 ├── BD                                          <- Bases de datos utilizadas para comprobar el método
 │
 ├── dockerfiles                                 <- Carpeta con archivo de Docker que crea la imágen del entorno para la ejecución del método
 │
 ├── notebooks_apoyo                             <- Notebooks de apoyo al proyecto (Aquí se encuentra el NB taggeado para uso con Minikube, Kubeflow y Kale)
 |
 ├── src                                         <- Códigos y archivos necesarios para instalar la nueva versión del paquete MaxFlowAeiu           
 │
 └── images                                      <- Contiene las imágenes utilizadas en el repositorio.
``` 

## ¿Qué lenguajes y paqueterías utlizamos?

<img src="images/minikube.jpeg" width="270" height="100" />

[Minikube](https://minikube.sigs.k8s.io/docs/start/)


<img src="images/kubeflow.png" width="270" height="100" />

[kubeflow](https://www.kubeflow.org/)


<img src="images/kale_logo.png" width="270" height="100" />

[kubeflow-kale](https://github.com/kubeflow-kale/kale)

<img src="images/cython.png" width="270" height="100" />

[Cython](https://cython.org/)    

---

## Ambientes en Contenedor

### Binder

En el siguiente botón se realiza el lanzamiento de un ambiente ejeutable donde se podrá interactuar con el paquete realizado (**MaxFlowAeiu**) y se ejecuta el notebook del reporte.
    
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/optimizacion-2-2022-gh-classroom/practica-2-segunda-parte-EddOselotl/main?labpath=reporte_equipo_2_parte_2_practica_2.ipynb)

### Docker

De igual forma, en este repositorio se cuenta con un archivo de Docker (Docker File) para crear una imagen del contenedor con las librerías y el paquete MaxFlowAeiu para que pueda ser utilizado desde [Docker](https://www.docker.com/).

<p align = "center">
    <img src="images/Docker-Logo.png" width="300" height="110" />

Las imágenes de Docker que se utilizaron de referencia para esta práctica se tomaron de [-1-](https://github.com/optimizacion-2-2022-gh-classroom/practica-2-primera-parte-urieluard#referencias)

---

## Instancia de AWS

Se creó una instancia de AWS con las siguientes características:
  
  > Máquina m5.2xlarge
  
  > AMI ubuntu 20.04
  
  > Almacenamiento de 30 GB
  
  > En la sección de configuración de _User data_ se utilizo este [script](https://github.com/ITAM-DS/analisis-numerico-computo-cientifico/wiki/6.Minikube-y-AWS)

<p align = "center">
    <img src="images/aws.png" width="300" height="110" />


> **Note** Para poder correr el Notebook del reporte en la instancia de _AWS_ se requiere instalar el paquete `MaxFlowAeiu` en su versión reimplementada (0.1.3), así como el paquete de `cython`, utilizando los siguientes comandos, desde la terminal de la instancia:

```
pip install "git+https://github.com/optimizacion-2-2022-gh-classroom/practica-2-segunda-parte-EddOselotl.git#egg=MaxFlowAeiu&subdirectory=src"
```
```
pip install cython
```   
---

## Resultados obtenidos

Tras la reimplementación realizada con compilación a **C**, se obtuvo una mejora significativa en el tiempo de ejecución del método _MaxFlowAeiu_. En la siguiente tabla se mustran una comparación de los tiempos de ejecución requeridos antes y después de la nueva implementación:

|     ***Red probada***     |   ***Ejecución (MaxFlowAeiu==0.1.2)***          |  ***Ejecución (MaxFlowAeiu==0.1.3)***   |                       
|:-------------------------:|:-----------------------------------------------:|:---------------------------------------:|
|  Pequeña (13 nodos)       |   CPU: 0.006 ms ; Wall Time: 0.011 ms             |  CPU: 0.002 ms ; Wall Time: 0.004 ms  | 
|  Mediana (44 nodos)       |   CPU: 0.007 ms ; Wall Time: 0.014 ms             |  CPU: 0.002 ms ; Wall Time: 0.004 ms  | 
|  Grande (1000 nodos)      |   CPU: 0.006 ms ; Wall Time: 0.012 ms             |  CPU: 0.003 ms ; Wall Time: 0.004 ms  | 
---

## Documentación del paquete

La documentación del paquete realizado se hizo con [Sphinx](https://www.sphinx-doc.org/en/master/) y se puede consultar en este [link](https://optimizacion-2-2022-gh-classroom.github.io/practica-2-segunda-parte-EddOselotl/index.html).

<p align = "center">
    <img src="images/sphinxheader.png" width="300" height="110" />

Para poder consultar el paquete en [Pypi](https://pypi.org/project/MaxFlowAeiu/)     

La creación del paquete se realizó con PyPi y se tomó de referencia el artículo publicado en la esta [liga](https://towardsdatascience.com/create-your-own-python-package-and-publish-it-into-pypi-9306a29bc116)

---

## Referencias

[1] Dockerfiles, Erick Palacios Moreno -ITAM [(liga al repositorio)](https://github.com/palmoreck/dockerfiles/tree/master/jupyterlab/kale/general/certs/0.6.1)
    
[2] Wiki del repositorio de la materia de Análisis Numérico y Computo Científico, Erick Palacios Moreno -ITAM [(liga al repositorio)](https://github.com/ITAM-DS/analisis-numerico-computo-cientifico/wiki/6.Minikube-y-AWS)
