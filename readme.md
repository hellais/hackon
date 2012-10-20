hackon
======
![Read the source](https://raw.github.com/wiki/hellais/hackon/images/read-the-source.jpg)

Assisting you in going though the dependency hell jungle when you just want to hack on some code.

Setup
-----
To get started with hackon just do the following:

    curl -L i.hackon.io | sh

If you are of the paranoid type you can do the following:

    curl --ssl https://raw.github.com/hellais/hackon/master/i.sh | sh

You may have to restart your terminal session to be up and running.

Currently hackon only supports zsh.

Usage
-----

To list all the projects that are waiting to be hacked on run

   hackon -l

To start hacking on a project run

    hackon projectname

To list the active projects run

    hackon -a

To remove a project from the list of active projects

    hackon -d projectname
