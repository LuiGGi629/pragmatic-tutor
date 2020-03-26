import os
import zipfile

os.chdir('/Users/wojtek/PycharmProjects/s-o-f/data/')
print(os.getcwd())

with zipfile.ZipFile('survey_results.zip', 'r') as my_zip:
    print(my_zip.namelist())
    my_zip.extractall()
