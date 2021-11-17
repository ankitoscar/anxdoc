# ANXDoc

![anxdoc.png](https://www.incimages.com/uploaded_files/image/1920x1080/shutterstock_619960997_370864.jpg)

This project is a web-app which helps to track user's mental state using computer vision and neural networks. 

    The objectives of this project:
  - To monitor user's face while sitting in front of a camera.
  - To study long term impacts of screen exposure of user.

# Features

  - The project utilizes computer vision and deep learning to track user's face and analyse it to predict their state.
  - It also generates a report which will help in analysing the user's state over a period of time.


# Data

  The data consists of images of students on laptop and phone webcams, where they are attending some sort of online class or meeting. The images are of various resolutions, but since our task is to single out the face, we can do it on any resolution and get the face for getting the output.

  Link to the dataset is [here](https://drive.google.com/file/d/1cwj0yEXWF5EysbMoZM1CpMw6OsvqZRd5/view?usp=sharing).

# How to run?

1. Clone the repository in your own system using

    `git clone https://github.com/ankitoscar/anxdoc.git`

2. To install all the required dependencies, run the following command.

    `pip install -r requirements.txt`

3. Run this command to run the web app.

    `python app\manage.py runserver`
### Tech

The libraries and frameworks used in this project till now are:

* [Opencv](https://opencv.org/) - Used for computer vision.
* [NumPy](https://numpy.org/) - Awesome mathematical library for python
* [Tensorflow](https://www.tensorflow.org/) - For deep learning application.
* [Django](https://www.djangoproject.com/) - For making web application.

### Todos

 - Improve the model.
 - Create an interactive UI and build a real-time prediction mechanism.
 - Implement integrations with various apps like Microsoft Teams, Zoom, Webex, etc.

![abnb.png](https://www.voicesofyouth.org/sites/voy/files/images/2021-08/1b7f385e-fe6b-4aab-88b3-1966b43dadc3.jpeg)
### Versions:

- 1.0 - Only some basic files, will add more files and attach UI images soon in future.


License
----

Apache 2.0 License.

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>

