import os
import zipfile

os.chdir('/Users/wojtek/PycharmProjects/pragmatic-tutor/Tutorials/data')
print(os.getcwd())

with zipfile.ZipFile('survey_results.zip', 'w', compression=zipfile.ZIP_DEFLATED) as my_zip:
    my_zip.write('survey_results_public.csv')
