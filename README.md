# Tutron

Tutron is a web application that allows students to upload their Python
homework for automatic correction.

## Usage

tbd

## Development

Developers need some technical requirements: `git` is needed to connect to the
GitLab instance, `python >= 3.5` is the programming language used and
`virtualenv ` is needed to install components via `pip` in a separate directory.

### Requirements

* [git][1]
* [python][2] >= 3.5
* [virtualenv][3]

This is an example how to install `virtualenv` and `pip` on a Linux (Ubuntu)
machine. Make sure, that Python3 is already installed and do not get `pip` if
it is already installed to avoid conflicts with the version already installed.
```bash
apt install python3-virtualenv
wget https://bootstrap.pypa.io/get-pip.py && python get-pip.py
pip install -U pip
```

For users of other operating systems, please refer to the official documentation
of the respective tools and programs to be able to install and run them.

### Setting up application in a local environment (Linux/Ubuntu)

An assumption is that you already have access to the [GitLab][4] instance and
have your [SSH key in your profile][5]. Here is an example how to generate a ssh
key ready for GitLab
```bash
# generate ssh-key if not already done, see $HOME/.ssh if you have one
ssh-keygen -t rsa -C "your.email@example.com" -b 4096
```

For convenience, it is assumed that the path to the root directory of the
project is stored in the PROJECT_ROOT variable, which can be saved like this:
```PROJECT_ROOT="your-path-to-the-local-project-folder"``` and the virtual
environment folder is saved in the variable VENV, which can also be saved like
this: ```VENV="${PROJECT_ROOT}/virtual-env"```.

```bash
# clone repository (get project files)
git clone git@gitlab.cl.uni-heidelberg.de:rehl/tutron.git "${PROJECT_ROOT}"
# get virtual environment working and download libraries from `requirements.txt`
virtualenv "${VENV}"
source "${VENV}/bin/activate"
pip install -r "${PROJECT_ROOT}/requirements.txt"
```

### Running application in a local environment (Linux/Ubuntu)

It is planned that this program runs as a web application on a web server and can
be addressed with a public url and the http(s) protocol. Of course, this program
can also be started locally. All you have to do is run the Python file `run.py`.
The intended start parameters can be displayed with `python run.py -h`. Let's assume
that `python` points to Python 3 (you may have to start the application explicitly
with `python3 run.py`) and the virtual environment is set up and activated correctly:

```bash
cd "${PROJECT_ROOT}"/src
python3 run.py
```


[1]: https://git-scm.com/
[2]: https://www.python.org/
[3]: http://docs.python-guide.org/en/latest/dev/virtualenvs/#lower-level-virtualenv
[4]: https://gitlab.cl.uni-heidelberg.de
[5]: https://gitlab.cl.uni-heidelberg.de/profile/keys
