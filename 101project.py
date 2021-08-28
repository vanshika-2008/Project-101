import dropbox 
import os
from dropbox import files
from dropbox.files import WriteMode

class TransferData :
    def __init__(self, access_token) :
        self.access_token = access_token
    
    def uploadFiles(self, source,destination) :
        dbx = dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(source) :
            for filename in files :
                localPath = os.path.join(root,filename)
                relativePath = os.path.relpath(localPath, source)
                dropBoxPath = os.path.join(destination, relativePath)
                file = open(localPath, "rb")
                dbx.files_upload(file.read(),dropBoxPath, mode=WriteMode("overwrite"))

def main()  :
    access_token = '2PE6-dJs8HwAAAAAAAAAAeQMH0DgbWCIl9KpnzTLTrrkBrsroS6H3dr91Y7Hqps8'
    upload = TransferData(access_token)
    source = str(input("Enter the folder path to transfer : "))
    destination = input("Enter the path to upload to dropbox : ")

    upload.uploadFiles(source,destination)
    print('File is now moved to the given path!')

main()