# PassGen 
*A basic password generator*


## Installation
### Using Pip:
```shell script
$ pip3 install -i https://test.pypi.org/simple/ passutil
```

### From sources:

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

The password generation option of this tool supports a default configuration using a file `passutil/data/conf_passgen.ini`, which is used as the default configuration for the tool (ie. without any flag passed).


Here is what it looks like when the package is downloaded: 

```
[PASSWORD_GENERATOR]
use_uppercase = True
use_special_chars = True
use_digits = True
length = 25
show_password = False
copy_to_paperclip = True

```

To modify that configuration, you can either modify the file or use the tool directly, with the conf argument.

## Commands available
```

passutil
    |
    | - info : shows this message
    |
    | - generate   Generate a password. Use the 'conf_passgen.ini' as default.
    |
    | - conf       Manage the default configuration
    |   |
    |   | - show :   show the current state of the file.
    |   |
    |   | - modify : modify the conf
    |   |   |
    |   |   | - copy-to-paper-clip  Change the default value of copy_to_paperclip.
    |   |   | - digits              Change the default value of use_digits.
    |   |   | - length              Change the default value of length.
    |   |   | - show-password       Change the default value of show_password.
    |   |   | - spec-char           Change the default value of use_special_chars.
    |   |   | - uppercase           Change the default value of use_uppercase.
    |
    | - store   Manage encrypted files and passwords in them.
    |   |
    |   |- list-files  List all files encrypted using this tool.
    |   |
    |   |- file        Manage encrypted files
    |   |   |
    |   |   |- delete  Delete a file
    |   |   |- new     Create a new file
    |   |
    |   |- password    Manage password inside an encrypted file
    |   |   |
    |   |   |-add      Get add a new password in an encrypted file.
    |   |   |-delete   Get delete a password in an encrypted file.
    |   |   |-get      Get one or several passwords in an encrypted file.
    |   |   |-get-all  Get all password in an encrypted file.
``` 


