< [[Python]]

Install needed dependencies in separate Python environment to avoid conflicts

My virtualenv is intalled here: (it's not on PATH so I might have to move it)
`C:\Users\Windows 11\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\Scripts`
*seems to work*

***Create*** new env in current dir, default name "env": **`python -m virtualenv env`** or **`virtualenv env`**

***Activate***: **`source env/bin/activate`**
Unix version
*When activating an env, it should automatically deactivate any other previously activated env*

***Activate***: **`.\env\Scripts\Activate`**
Windows version

Prompt change when env activated:
![[Pasted image 20240905095800.png]]

***Install "dependency"*** on env: pip dependency

***Save list*** all dependencies in "requirements.txt": **`pip freeze > requirements.txt`**

***Re-install*** dependencies: **`pip install -r requirements.txt`**

***De-activate*** env: **`deactivate`**

Create a **`gitignore`** to not push the environment to github