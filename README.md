# convertPDF_to_img (PNG)
```console
user@user:~$ main.py -h

usage: main.py [-h] -f FILE [-b BEGIN] [-e END] command

positional arguments:
  command</br>

options:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  The filename
  -b BEGIN, --begin BEGIN Initial page
  -e END, --end END     Final page

```
#Exemple to use
```console
user@user:~$ main.py convert -f "name_file.pdf" -b 2 -e 20
```
