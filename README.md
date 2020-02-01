# PassGen 
*A basic password generator*


## Installation

1. clone the project 

```shell
$ git clone https://github.com/Nathanmalnoury/passgen
```



2. Python, pip:

This project is written using Python 3.7. Make sure you have this version of Python and the according pip version.

Link to the python downloads options (select 3.7.X) : https://www.python.org/downloads/

Link to an installation guide for pip : https://pip.pypa.io/en/stable/installing



3. Install `requirements.txt`:

```
$ cd ./path/to/PassGen
$ pip install -r requirements.txt
```



4. Install dependencies:

Depending on your OS,  you might need to install a package for the 'copy to paperclip' option to work.

Here is what pyperclip documentation says about it :

> On Windows, no additional modules are needed.
>
> 
>
> On Mac, this module makes use of the pbcopy and pbpaste commands, which should come with the os.
>
> 
>
> On Linux, this module makes use of the xclip or xsel commands, which should come with the os. Otherwise run “sudo apt-get install xclip” or “sudo apt-get install xsel” (Note: xsel does not always seem to work.)





## Configuration:

This program comes with a configuration file `conf.ini`, which is used as the default configuration for the tool (ie. without any flag passed). 



Here is what it looks like : 

```
[DEFAULT]

# integer, default length of the password 
length = 20 

# Boolean, whether to use uppercase characters or not
use_uppercase = True 

# Boolean, whether to use special characters or not
use_special_chars = True 

# Boolean, whether to use digits or not
use_digits = True 

# Boolean, whether to show the password in the CLI or not
show_password = False 

# Boolean, whether to copy the password to the paperclip or not
copy_to_paperclip = True 

```



