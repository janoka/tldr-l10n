# Automated translation for TLDR pages

## What is this?

This is a project to automatically translate TLDR pages into other languages. The goal is to make it easy for people to contribute translations, and to make it easy for people to find translations.

## How does it work?

The TLDR pages are stored in a git repository. Each page is stored in a separate file, and each file is named after the command it describes. For example, the page for the `git` command is stored in the file `git.md`.

Please see more on the [TLDR project](https://github.com/tldr-pages/tldr).

## Prerequisites

- Python 3.9 or higher
- Python virtual environment module
- Deepl API key, see [here](https://www.deepl.com/pro#developer)
- Git and GitHub account

## How can I install it?

```shell
git clone https://github.com/janoka/tldr-t9n.git
cd tldr-t9n

# Initialize the python virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install dependencies
python3 -m pip install -r requirements.txt
```

Make a fork of [TLDR Pages](https://github.com/tldr-pages/tldr) at GitHub to your account there and clone it to your computer.

E.g.:

```shell
# Following you forked the TLDR pages repository to your account:
git clone https://github.com/janoka/tldr.git
```

Go back to the project folder and make a copy of the [`env.example`](env.example) file and name it `.env`. Then edit the `.env` file and set the `TLDR_REPO` variable to the path of the TLDR repository on your computer.

```shell
python3 main.py
```

## Credits

- [TLDR Pages](https://github.com/janoka/tldr)
- [Deepl API for automated translation](https://www.deepl.com/pro#developer)
  - [Deepl Pro Licenc](https://www.deepl.com/en/pro-license)
- [Python](https://www.python.org/)
  - [Python PIP](https://pypi.org/project/pip/)
  - [Python Virtual Environment](https://docs.python.org/3/library/venv.html)
- [Git](https://git-scm.com/)
- [GitHub](https://github.com)
