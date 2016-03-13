===============================
DV Processing
===============================

Volunteer app for finding DV court processor.


Quickstart
----------

Assumptions:

* Assumes node.js and bower are installed. If it is not, `install node.js and therefore npm<http://shapeshed.com/setting-up-nodejs-and-npm-on-mac-osx/>`_ and then `run these commands to install bower<http://stackoverflow.com/questions/12369390/bower-command-not-found/20628131#20628131>`_.

First, set your app's secret key as an environment variable. For example, example add the following to ``.bashrc`` or ``.bash_profile``.

.. code-block:: bash

    export DVPROCESSING_SECRET='something-really-secret'


Then run the following commands to bootstrap your environment.


::

    git clone https://github.com/lorenanicole/DVProcessing
    cd DVProcessing
    pip install -r requirements/dev.txt
    pip install -r requirements.txt
    bower install
    python manage.py server

You will see a pretty welcome screen in your browser at the IP address it lists for you.

Now hit Control+C in the command line to stop the server from running so you can proceed.

Once you have installed your DBMS, created a database and database user, updated the connection string in line 37 of the `DVProcessing/settings.py` file, then run the following to create your app's database tables and perform the initial migration:

::

    python manage.py db upgrade
 
Now you can run the app again.
  
::

    python manage.py server



Deployment
----------

In your production environment, make sure the ``DVPROCESSING_ENV`` environment variable is set to ``"prod"``.


Shell
-----

To open the interactive shell, run ::

    python manage.py shell

By default, you will have access to ``app``, ``db``, and the ``User`` model.


Running Tests
-------------

To run all tests, run ::

    python manage.py test


Migrations
----------

Whenever a database migration needs to be made. Run the following commands:
::

    python manage.py db migrate

This will generate a new migration script. Then run:
::

    python manage.py db upgrade

To apply the migration.

For a full migration command reference, run ``python manage.py db --help``.
