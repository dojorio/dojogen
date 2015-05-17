DojoGen
==========

This project generates folders for coding dojo sessions following the pattern YYYYMMDD[_extra]_language_problem.

I (João Felipe Pimentel) started this project in a fork of [DojoTools](https://github.com/JoaoFelipe/dojotools) and now I'm extracting it to a separate project.

Installing and using DojoGen is simple and easy. Please check our installation and basic usage guidelines below.


Quick Installation
------------------

To install DojoGen, you should follow these basic instructions:

If you have pip, just run:
```bash
$ pip install dojogen
```


If you do not have pip, but already have Git (to clone our repository) and Python:
```bash
$ git clone git@github.com:dojorio/dojogen.git
$ cd dojogen
$ ./setup.py install
```
This installs DojoGen on your system.

Usage
-----------

There are 3 basic commands: generate (g), language (l), help (h)

1- Generate: generates a folder for the coding dojo session

Just call it with the desired language and problem
```
$ dojogen generate python fizz_buzz
```
Generates 20150517_python_fizz_buzz


You can also pass extra arguments to describe custom dojo sessions
```
$ dojogen g python fizz_buzz freshmen
```
Generates 20150517_freshmen_python_fizz_buzz with fizz_buzz.py and test_fizz_buzz.py


There are also extra options:

Use non-specified generator or ignore language files: (-i/--ignore)
```
$ dojogen g -i python fizz_buzz
```
Generates an empty 20150517_python_fizz_buzz


Specify the path (-p/--path)
```
$ dojogen g -p ~/dojo_niteroi python fizz_buzz
```
Generates 20150517_python_fizz_buzz inside ~/dojo_niteroi directory


2- Language: shows existing generators

```
$ dojogen language
moonscript
javascript
pascal
python
java
coffeescript
c
haskell
lua
ruby
```

3- Help: describes how to prepare the environment for a language

```
$ dojogen help ruby
Dependencies:
  ruby
  rspec

TestUnit:
  It uses rspec that can be downloaded by
  gem install rspec

Interactive Shell:
  irb
```

Contributing
----

If you want to create a new generator, you just need to create a folder inside the generators directory and a text file inside generators/help.
The name of the folder and text file will be the name of the generator.

Please, make sure you create a file run.dojo inside the generator with the command line used to compile and run tests (if applyable) and a .dojoignore with rules to ignore compiled files.

Some strings will be replaced by the problem name according to the expected case.
Using the problem name fizz_buzz as example:
```
'___dojogen___'       : 'fizz_buzz'
'___class_dojogen___' : 'FizzBuzz',
'___down_dojogen___'  : 'fizzbuzz',
'___camel_dojogen___' : 'fizzBuzz',
```

Contact
----

Do not hesitate to contact me:

* João Felipe Pimentel <joaofelipenp@gmail.com>

License Terms
-------------

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
