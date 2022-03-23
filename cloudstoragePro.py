import os
from dropbox.files import WriteMode
import dropbox
class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root,directorys,files in os.walk(file_from):
            relative_path= os.path.relpath(local_path,file_from)
            dropbox_path = os.path.join(file_to,relative_path)
          
        
        f=open(local_path,'rb')
        dbx.files_upload(f.read(),dropbox_path,mode=WriteMode('overwrite'))

def main():
    access_token='sl.BEXdWn-bNyr-pZiH6MOs75gGB9YnxT6qAQHZpsCMfwvXIsDR4bnG__kGTrPD4-KSk29naQ3O0T9FgdCS3xaRAKPof9iBQryocUxayJ0erEuy0ZnF2Ow8COl2c6Zp50Hm-pgw4xU'
    transferData = TransferData(access_token)

    file_from=input("enter the file paths to transfer")
    file_to=input("enter the file paths to upload")
    transferData.upload_file(file_from,file_to) 
    print("file has been moved")         

main()     