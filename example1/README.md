This example shows how to use some basic features of `setuptools`.

The first one is `install_requires` which allows you to automatically install
dependencies that you need.

Another one is `entry_points`, where you can declare `console_scripts` which
will then be new commands available in your environment.

This particular example will install the `requests` package as a dependency,
then install a new command `mycommand` in your environment. You can test it
with the help of `virtualenv`:

    $ virtualenv test
    $ source test/bin/activate
    (test)$ pip install ./mymodule/
    (test)$ mycommand

You can also check what would happen if you were missing the dependencies
and distributed the code without a `setup.py`. In this case, `requests` is
not part of the standard library, so unless you install it, it would not be
present. Please note that this time we cannot run `mycommand` since we are not
installing `mymodule`.

    $ virtualenv --clear test
    $ source test/bin/activate
    (test)$ cd mymodule
    (test)$ python -c 'import mymodule.script; mymodule.script.main()'

