import shutil


shutil.copy(r'29_shutil_module\main.py',r'29_shutil_module\copy.py')
print("File copied!")

shutil.copytree(r'07_MFR',r'29_shutil_module/new_folder_copied')
print("Folder copied!")

shutil.rmtree('05_os_module/new_folder')
print("Deleted!")