Setting up a server and deploying Pelican
##########################################
:date: 2022-03-01 17:20
:category: webdev, self-sovereignty
:tags: webdev, self-sovereignty, Linux, Pelican, Python, VPS
:summary: Notes about setting up a server with Pelican and deploying a static website to it


.. THIS IS JUST A CONVENTION, ANY (from a list of) SYMBOL CAN BE USED AS LONG AS YOU ARE CONSISTENT !!!
.. # with overline, for parts
.. = with overline, for chapters
.. -, for sections
.. ~, for subsections
.. ", for subsubsections
.. ^, for paragraphs


.. chapter 1
.. ===========
.. section 1.1
.. ------------
.. subsection 1.1.1
.. ~~~~~~~~~~~~~~~~~
.. subsubsection 1.1.1.a
.. """"""""""""""""""""""
.. paragraph
.. ^^^^^^^^^^^^^^^^^^^^^^
.. section 1.2
.. ------------
.. chapter 2
.. ==========

.. try this is the same as above
.. chapter 1
.. ===========
.. section 1.1
.. ++++++++++++
.. subsection 1.1.1
.. -----------------
.. subsubsection 1.1.1.a
.. ~~~~~~~~~~~~~~~~~~~~~~
.. paragraph
.. ^^^^^^^^^^^^^^^^^^^^^^
.. section 1.2
.. +++++++++++++
.. chapter 2
.. ==========

.. Try this ... and it should be same as above !
.. chapter 1
.. ************
.. section 1.1
.. ===========
.. subsection 1.1.1
.. -----------------
.. subsubsection 1.1.1.a
.. ^^^^^^^^^^^^^^^^^^^^^^
.. paragraph
.. """"""""""
.. section 1.2
.. ===========
.. chapter 2
.. ************



.. THIS DOES NOT WORK!
.. chapter 1
.. ###########
.. section 1.1
.. ------------
.. subsection 1.1.1
.. ~~~~~~~~~~~~~~~~~
.. subsubsection 1.1.1.a
.. """"""""""""""""""""""
.. paragraph
.. ^^^^^^^^^^^^^^^^^^^^^^
.. section 1.2
.. ------------
.. chapter 2
.. ###########


Intro
======

This article provides some background info and tries to serve as a quick guide on the steps required to set up a server and *deploy* it (fancy word for upload the webpage to the server). I hope can help someone (or even my future me)

First thing to consider is what kind of website you want to create, what the state of *dev-ops* skills (as they call it now) are, and what is the willingness/time you want to dedicate to learn and mantain the infrastructure that comes along with the actual content of your website. This article is focused on someone who just wants to create a static blog (ie. no marketplace or social site that needs of *dynamic* content), and has some linux and programming experience.

As a **self-sovereignty** enthusiast myself, I've chosen to go this (harder than strictly required) way. However, if you just want to get your message across as quickly as possible, you can for sure look into something easier like `medium <https://www.medium.com/>`_, or setting up a wordpress site. If instead you want to walk in the path of the self-sovereign individual, own your data and train your webdev linux skills, then you may want to read this article. With no more introduction, let's dive right into it.


Setup
=============

My choice for the static site generator has been `Pelican <https://github.com/getpelican/pelican/>`_ , which is based on python. I also did some research on the possibility of using a CMS like Wagtail (built on Django) but drop the idea after few hours wasted on trying to set up a database, *nginx*, *gunicorn* (and some other fancy infrastructure I have no idea about) at the server side. 

So, for the whole setup you will need the following things and steps listed below, along with what I ended up choosing (I am not super-knowledgeable in this area, but after a bit of *market research* in Reddit I think these are reasonably good options) 

1. Domain name
2. Hosting
3. Install OS and required infrastructure on the server side
4. Work on your content
5. Deploy content to server

I will now develop a bit further some of these points

Domain name
------------
I used Namecheap for this. You might as well go with a free hosting solution, that you can redirect

Hosting
--------
I decided on a VPS (Virtual private server) and not on a dedicated server, as I do not have the speed/load/bandwidth requirements (unless this blog really picks up!) that would justify the need for it. And so far I have no complaints: installing stuff, logging in, displaying the page, etc. seems good enough for the price I paid (4.99 euros/month with German hosting Contabo)

Conneting domain and hosting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
you need to do this ....


Install OS and required infrastructure on the server side
----------------------------------------------------------

After purchasing the VPS, you can choose what OS you want to install (you can change this later as well). I chose Fedora Linux as that's the OS I am familiar with. You are then sent via email a ``ssh`` login and pass, and also the login details for a ``vnc`` session. So now you need to ssh into the server and install the following stuff (remember to first create a user so you do not do all this things as ``root``)

.. code-block:: shell

   sudo dnf install blabla

then do this

.. code-block:: shell

  sudo dnf install blabla


and thats it


