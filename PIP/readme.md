# PIP ( PYTHON PACKAGE MANAGERS )
This is a cli tool which enables you install packages from either pip platfrom or custom packages on github.

# Get version of PIP

```bash
   C:\> pip --version
   // this would list the version of pip
```

# Create a Virtual Environments.

Sometimes there would be a situation where you would like to use a specific installed `packages` within your project without having to clash with other lower version packages. This is where `Virtual Environments` fits in.

Python allows you to create a `venv` using the `venv module`. move to the root of yout pc

Windows: `C:\>`

And use the following commands to create a `venv`

```bash
    C:\> python -m venv (venv name)

    C:\> python -m newenv

    <!-- Executes the activate.bat file within the (newenv) folder and   scripts folder -->

    C:\> newenv\scripts\activate.bat

    <!-- This would automatically activates the newvenv -->

    (newenv) C:\>

```

This way, any packages can be installed within this `virtual env`

```bash
    (newenv) C:\> python -m pip install requests
```


# Using Requirements Files

The pip install command always installs the latest published version of a package, but sometimes your code requires a specific package version to work correctly.

You want to create a specification of the dependencies and versions that you used to develop and test your application so that there are no surprises when you use the application in production.

- # Pinning Requirements
When you share your Python project with other developers, you may want them to use the same versions of external packages that you’re using. Maybe a specific version of a package contains a new feature that you rely on, or the version of a package that you’re using is incompatible with former versions.

These external dependencies are also called requirements. You’ll often find Python projects that pin their requirements in a file called requirements.txt or similar. The requirements file format allows you to specify precisely which packages and versions should be installed.

Running pip help shows that there’s a freeze command that outputs the installed packages in requirements format. You can use this command, redirecting the output to a file to generate a requirements file:

```bash
    (newvenv) C:\> python -m pip freeze > requirements.txt
```

This command creates a requirements.txt file in your working directory with the following content:

```txt
    certifi==x.y.z
    charset-normalizer==x.y.z
    idna==x.y.z
    requests==x.y.z
    urllib3==x.y.z
```

Remember that x.y.z displayed above is a placeholder format for the package versions. Your requirements.txt file will contain real version numbers.

The freeze command dumps the name and version of the currently installed packages to standard output. You can redirect the output to a file that you can later use to install your exact requirements into another system. You can name the requirements file whatever you want. However, a widely adopted convention is to name it requirements.txt.

When you want to replicate the environment in another system, you can run pip install, using the -r switch to specify the requirements file:


```bash
    (newvenv) C:\> python -m pip install -r requirements.txt
```

In the command above, you tell pip to install the packages listed in requirements.txt into your current environment. The package versions will match the version constraints that the requirements.txt file contains. You can run pip list to display the packages you just installed, with their version numbers:

# Fine-Tuning Requirements

The problem with hardcoding your packages’ versions and dependencies is that packages are updated frequently with bug and security fixes. You probably want to leverage those updates as soon as they’re published.

The requirements file format allows you to specify dependency versions using comparison operators that give you some flexibility to ensure packages are updated while still defining the base version of a package.

Open requirements.txt in your favorite editor and turn the equality operators (==) into greater than or equal to operators (>=), like in the example below:


### requirements.txt

```
    certifi>=x.y.z
    charset-normalizer>=x.y.z
    idna>=x.y.z
    requests>=x.y.z
    urllib3>=x.y.z
```

You can change the comparison operator to >= to tell pip to install an exact or greater version that has been published. When you set a new environment by using the requirements.txt file, pip looks for the latest version that satisfies the requirement and installs it.

Next, you can upgrade the packages in your requirements file by running the install command with the --upgrade switch or the -U shorthand:


```bash
    (newvenv) C:\> python -m pip install -U -r requirements.txt
```

If a new version is available for a listed package, then the package will be upgraded.

In an ideal world, new versions of packages would be backward compatible and would never introduce new bugs. Unfortunately, new versions can introduce changes that’ll break your application. To fine-tune your requirements, the requirements file syntax supports additional version specifiers.

Imagine that a new version, 3.0, of requests is published but introduces an incompatible change that breaks your application. You can modify the requirements file to prevent 3.0 or higher from being installed:

### requirements.txt

```    
    certifi==x.y.z
    charset-normalizer==x.y.z
    idna==x.y.z
    requests>=x.y.z, <3.0
    urllib3==x.y.z
```

# Separating Production and Development Dependencies

Not all packages that you install during the development of your applications will be production dependencies. For example, you’ll probably want to test your application, so you need a test framework. A popular framework for testing is pytest. You want to install it in your development environment, but you don’t want it in your production environment, because it isn’t a production dependency.

You create a second requirements file, requirements_dev.txt, to list additional tools to set up a development environment:

### requirements_dev.txt
```
    pytest>=x.y.z
```

Having two requirements files will demand that you use pip to install both of them, requirements.txt and requirements_dev.txt. Fortunately, pip allows you to specify additional parameters within a requirements file, so you can modify requirements_dev.txt to also install the requirements from the production requirements.txt file:

### requirements_dev.txt

```
    -r requirements.txt
    pytest>=x.y.z
```

Notice that you use the same -r switch to install the production requirements.txt file. Now, in your development environment, you only have to run this single command to install all requirements:

```bash
    (newvenv) C:\> python -m pip install -r requirements_dev.txt
```

# Uninstalling Packages With pip

Once in a while, you’ll have to uninstall a package. Either you found a better library to replace it, or it’s something that you don’t need. Uninstalling packages can be a bit tricky.

Notice that when you installed requests, you got pip to install other dependencies too. The more packages you install, the bigger the chance that multiple packages depend on the same dependency. This is where the show command in pip comes in handy.

Before you uninstall a package, make sure to run the show command for that package:

```
    (newvenv) C:\> python -m pip show requests

    Name: requests
    Version: 2.26.0
    Summary: Python HTTP for Humans.
    Home-page: https://requests.readthedocs.io
    Author: Kenneth Reitz
    Author-email: me@kennethreitz.org
    License: Apache 2.0
    Location: .../python3.9/site-packages
    Requires: certifi, idna, charset-normalizer, urllib3
    Required-by:
```

Notice the last two fields, Requires and Required-by. The show command tells you that requests requires certifi, idna, charset-normalizer, and urllib3. You probably want to uninstall those too. Notice that requests isn’t required by any other package. So it’s safe to uninstall it.

You should run the show command against all of the requests dependencies to ensure that no other libraries also depend on them. Once you understand the dependency order of the packages that you want to uninstall, then you can remove them using the uninstall command:

```bash
    (newvenv) C:\> python -m pip uninstall certifi
```

The uninstall command shows you the files that will be removed and asks for confirmation. If you’re sure that you want to remove the package because you’ve checked its dependencies and know that nothing else is using it, then you can pass a -y switch to suppress the file list and confirmation dialog:

```bash
    (newvenv) C:\> python -m pip uninstall urllib3 -y
```

Here you uninstall urllib3. Using the -y switch, you suppress the confirmation dialog asking you if you want to uninstall this package.

In a single call, you can specify all the packages that you want to uninstall:

```bash
    (newvenv) C:\> python -m pip uninstall -y charset-normalizer idna requests
```

You can pass in multiple packages to the pip uninstall command. If you didn’t add any additional switches, then you’d need to confirm uninstalling each package. By passing the -y switch, you can uninstall them all without any confirmation dialog.

You can also uninstall all the packages listed in a requirements file by providing the -r <requirements file> option. This command will prompt a confirmation request for each package, but you can suppress it with the -y switch:

```bash
    (venv) C:\> python -m pip uninstall -r requirements.txt -y
```

Remember to always check the dependencies of packages that you want to uninstall. You probably want to uninstall all dependencies, but uninstalling a package used by others will break your working environment. In consequence, your project may not work correctly anymore.

If you’re working in a virtual environment, it can be less work to just create a new virtual environment. Then you can install the packages that you need instead of trying to uninstall the packages that you don’t need. However, pip uninstall can be really helpful when you need to uninstall a package from your system Python installation. Using pip uninstall is a good way to declutter your system if you accidentally install a package system-wide.