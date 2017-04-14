# hacktx-api-directory
Searchable directory of APIs from companies sponsoring Freetail Events.
# Setup
Virtualenv is highly recommended to manage dependencies. This code uses Frozen-Flask to automatically generate the static pages for hosting on Github Pages. To change the APIs available, you can edit the ```app/data.json``` file..
## To install on a Unix system:
In the root level of your cloned directory:
```bash
virtualenv -p /usr/bin/python3<.x> venv
source venv/bin/activate
pip install -r requirements.txt
```
Then, edit ```app/data.json``` as you please. When you are done, run
```bash
python app/freezer.py
```

The result page is generated into the ```/docs``` directory
