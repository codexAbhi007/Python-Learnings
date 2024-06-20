import os 

if(not os.path.exists ("05_os_module/new_folder")):
    os.mkdir("05_os_module/new_folder")


for i in range(50):
    if (not os.path.exists(f"05_os_module/new_folder/Day{i+1}")):
        os.mkdir()

print(os.getcwd())
