##          VIRTUAL RNVIRONMENTS, PIP
***
Virtual environment provides a self contained directory tree which python installation and additional packages for a project
### Creating a virtual environment
```
    path\virtual\environment\demo > python -m venv .venv
```
###   Activating
```
    ##    Windows
    .venv/scripts/activate

    ##  linux
    source .venv/bin/activate
```
After changing the virtual environment the path will be modified hence we can install adittional packages using `pip` within the environment
```
    ##  powershell
    $Env:PATH

    ##  Windows command prompt
    echo %PATH%

    ##  linux
    echo $Path
```
This displays the path where scripts and bin directory will be scanned first to resolve reference to executable files.
###   Deactivating
```
    (.venv) path..\virtual_environment\demos > deactivate
```

##      PIP (packages with pip)
Python package is collection of related modules in a file.<br/>
Python Package Index (PyPI) is collection of freely available Python packages, which developer can install using `pip`
```
    # Installing playsound package
   pip install playsound

    # Unistalling 
   pip uninstall playsound
```
**Note**<br/>
Always install packages within the virtual environment you are working with to keep Python environment clean.
```
    # List packages
    pip list
```

