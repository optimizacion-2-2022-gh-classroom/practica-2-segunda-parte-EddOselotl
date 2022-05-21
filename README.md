<p align = "center">
    <img src="images/logo_itam.png" width="300" height="110" />

---

## Tabla de contenido:
    
1. [Integrantes y roles asignados](https://github.com/optimizacion-2-2022-gh-classroom/practica-2-primera-parte-urieluard#integrantes-y-roles-asignados)
    
2. [Acerca de este proyecto](https://github.com/optimizacion-2-2022-gh-classroom/practica-2-primera-parte-urieluard#acerca-de-este-proyecto)
    
3. [Estructura básica del repositorio](https://github.com/optimizacion-2-2022-gh-classroom/practica-2-primera-parte-urieluard#estructura-b%C3%A1sica-del-repositorio)
    
4. [¿Qué lenguajes y paqueterías utlizamos?](https://github.com/optimizacion-2-2022-gh-classroom/practica-2-primera-parte-urieluard#qu%C3%A9-lenguajes-y-paqueter%C3%ADas-utlizamos)

5. [Ambientes en Contenedor](https://github.com/optimizacion-2-2022-gh-classroom/practica-2-primera-parte-urieluard#ambientes-en-contenedor)

6. [Instancia de AWS](https://github.com/optimizacion-2-2022-gh-classroom/practica-2-primera-parte-urieluard#instancia-de-aws)

7. [Resultados obtenidos](https://github.com/optimizacion-2-2022-gh-classroom/practica-2-primera-parte-urieluard#resultados-obtenidos)
    
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
 │
 └── images                                      <- Contiene las imágenes utilizadas en el repositorio.
``` 

## ¿Qué lenguajes y paqueterías utlizamos?



---

## Ambientes en Contenedor

### Binder

En el siguiente botón se realiza el lanzamiento de un ambiente ejeutable donde se podrá interactuar con el paquete realizado (**MaxFlowAeiu**) y se ejecuta el notebook del reporte.
    
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/optimizacion-2-2022-gh-classroom/practica-2-segunda-parte-EddOselotl/main?labpath=%2Fnotebooks_apoyo%2Freimplementacion.ipynb)

### Docker

De igual forma, en este repositorio se cuenta con un archivo de Docker (Docker File) para crear una imagen del contenedor con las librerías y el paquete MaxFlowAeiu para que pueda ser utilizado desde [Docker](https://www.docker.com/).

<p align = "center">
    <img src="images/Docker-Logo.png" width="300" height="110" />

Las imágenes de Docker que se utilizaron de referencia para esta práctica se tomaron de [-1-](https://github.com/optimizacion-2-2022-gh-classroom/practica-2-primera-parte-urieluard#referencias)

---

## Instancia de AWS

Se creó una instancia de AWS con las siguientes características:
  
  > Máquina m4.16xlarge
  
  > AMI ubuntu 20.04 - ami-042e8287309f5df03
  
  > Almacenamiento de 100 GB
  
  > En la sección de configuración de _User data_ se utilizo este [script](https://github.com/palmoreck/scripts_for_useful_tools_installations/blob/main/AWS/ubuntu_20.04/optimizacion_2/script_profiling_and_BLAS.sh)

<p align = "center">
    <img src="images/aws.png" width="300" height="110" />

---

## Resultados obtenidos

Tras la reimpelenetación realizada (con .... ) se obtuvo una mejora significativa en el tiempo de ejecución del método _MaxFlowAeiu_. En la siguientes figuras se mustran los tiempos de ejecución requeridos antes y después de la implementación:





---

## Documentación del paquete

La documentación del paquete realizado se hizo con [Sphinx](https://www.sphinx-doc.org/en/master/) y se puede consultar en este [link](https://optimizacion-2-2022-gh-classroom.github.io/practica-2-primera-parte-urieluard/index.html).

<p align = "center">
    <img src="images/sphinxheader.png" width="300" height="110" />

Para poder consultar el paquete en [Pypi](https://pypi.org/project/MaxFlowAeiu/)     

La creación del paquete se realizó con PyPi y se tomó de referencia el artículo publicado en la esta [liga](https://towardsdatascience.com/create-your-own-python-package-and-publish-it-into-pypi-9306a29bc116)

---

## Referencias

[1] Dockerfiles, Erick Palacios Moreno -ITAM [(liga al repositorio)](https://github.com/palmoreck/dockerfiles/tree/master/jupyterlab/kale/general/certs/0.6.1)
    
[2] Wiki del repositorio de la materia de Análisis Numérico y Computo Científico, Erick Palacios Moreno -ITAM [(liga al repositorio)](https://github.com/ITAM-DS/analisis-numerico-computo-cientifico/wiki/6.Minikube-y-AWS)
