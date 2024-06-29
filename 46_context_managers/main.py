class Open_File():

    def __init__(self,filename,mode) -> None:
        self.filename = filename
        self.mode = mode
        print('init method called!')

    def __enter__(self):
        print('Enter method called!')
        self.file = open(self.filename,self.mode)
        return self.file
    
    def __exit__(self,exc_type,exc_val,traceback):
        print('Exit method called!')
        self.file.close()


with Open_File(r'46_context_managers\files\sample.txt','w') as f:
    # print(f)
    f.write('Testing...')

print(f.closed)