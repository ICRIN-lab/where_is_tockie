# Where Is Tockie Task 

##CONTENTS OF THIS FILE

* Introduction
* Where is Tockie Task
* Task design example
* Requirements
* Contributions
* More informations
* Contact


##INTRODUCTION

Our research team is studying different aspects of psychiatric disorders. Our present project is all about exploring obssessive compulsive disorders' secret garden. For that matter, we designed original home-made cognitive tasks, fresh out of the oven!

##Where is Tockie Task

*Where is Tockie* is a cognitive task inspired by the famous game *Where is Charlie*. The novelty is that we aren't looking for Charlie this time. 
In fact, we are looking for anything else but Charlie.
We display 35 different images, and in each trial the subject is questioned about details related to the image.
Then, we ask the participant after each question whether or not he/she wants to see the image again.

All the questions are stored in a [dictionary](images_dict.py).

The images are stored in the file "img". 
A training session is lauched including 3 images. 
Afterward, the task begins and contains 32 trials. 


The task starts with instructions written in french, and are designed for "Trackpad" response.

##Task Design example

Here is an example of the task. 

![whereistockie](img/img_readme/img_wit_readme.png)

![wheristockie](img/img_readme/qst_wit1_readme.png) 

![wheristockie](img/img_readme/qst_wit2_readme.png) 


##REQUIREMENTS

###Imports :

We use the package PsychoPy under Python 3.6 to run the tasks. Furthermore, Where Is Tockie Task requires the import of time, as the time spent by the participants is a valuable data.
```python
import time
from psychopy import visual, gui, data, core
from images_dict import dic
from Template_Task_Psychopy.task_template import TaskTemplate
```

In order to import TaskTemplate, here are our recommendations. :

* **Step 1** : Clone Template_Task_Psychopy repository from GitHub 


Here's the link :  <a href="https://github.com/ICRIN-lab/Template_Task_Psychopy.git"> here </a>


* **Step 2**: Create a symbolic link locally with Template_Task_Psychopy :

```python
  yourtask_directory % ln -s ../Template_Task_Psychopy Template_Task_Psychopy
```  



###Specificities :

If you want to try this cognitive task using your keyboard, don't forget to the response_pad to False

```python
class Where_Is_Tockie(TaskTemplate):
    nb_ans = 4
    response_pad = False  # has to be set on "True" if a trackpad is used.
```

##Contributions

To contribute, please fork the repository, hack in a feature branch, and send a pull request.

##More informations

Homepage: [iCRIN Lab](http://icrin.fr/)

##Contact us

Mail : contact@icrin.fr
Twitter : https://twitter.com/RedwanMaatoug