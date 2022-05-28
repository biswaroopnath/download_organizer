# organize downlaods folder
import os
import shutil

# edit the following if download folder is in some other places
source = 'C:\\Users\\biswa\\Downloads'

 

class destination:
    documents = source + '\\doc' 
    doc = documents + '\\word'
    psd = documents + '\\psd'
    pdf = documents + '\\pdf'
    zip = documents + '\\zip'
    prproj = documents + '\\premier_pro'
    txt = documents + '\\txt'
    pptx = documents + '\\pptx'
    exe = source + '\\exe'
    others = source + '\\others'
    pic = source + '\\pic'



def make_doc():
    if not os.path.exists(destination.documents):
        os.makedirs(destination.documents)


def make_exe():
    if not os.path.exists(destination.exe):
        os.makedirs(destination.exe)


def make_others():
    if not os.path.exists(destination.others):
        os.makedirs(destination.others)


def make_pic():
    if not os.path.exists(destination.pic):
        os.makedirs(destination.pic)


# sub-directory making func under doc
def make_pdf():
    make_doc()
    if not os.path.exists(destination.pdf):
        os.makedirs(destination.pdf)


def make_pptx():
    make_doc()
    if not os.path.exists(destination.pptx):
        os.makedirs(destination.pptx)


def make_premier_pro():
    make_doc()
    if not os.path.exists(destination.prproj):
        os.makedirs(destination.prproj)


def make_psd():
    make_doc()
    if not os.path.exists(destination.psd):
        os.makedirs(destination.psd)


def make_txt():
    make_doc()
    if not os.path.exists(destination.txt):
        os.makedirs(destination.txt)


def make_word():
    make_doc()
    if not os.path.exists(destination.doc):
        os.makedirs(destination.doc)


def make_zip():
    make_doc()
    if not os.path.exists(destination.zip):
        os.makedirs(destination.zip)


def make_dir():
    for f in allfiles:
        if f.lower().endswith(('.png', '.jpg', '.jpeg')):
            make_pic()
        elif f.lower().endswith(('.pdf')):
            make_pdf()
        elif f.lower().endswith(('.psd')):
            make_psd()
        elif f.lower().endswith(('.doc', '.docx')):
            make_word()
        elif f.lower().endswith(('.exe')):
            make_exe()
        elif f.lower().endswith(('.txt')):
            make_txt()
        elif f.lower().endswith(('.zip')):
            make_zip()
        elif f.lower().endswith(('.ppt', '.pptx')):
            make_pptx()
        elif f.lower().endswith(('.prproj')):
            make_premier_pro()
        else:
            make_others()


def remove_destination_dir():
    if os.path.exists(destination.documents):
        allfiles.remove('doc')
    if os.path.exists(destination.exe):
        allfiles.remove('exe')
    if os.path.exists(destination.others):
        allfiles.remove('others')
    if os.path.exists(destination.pic):
        allfiles.remove('pic')

#for checking if same file is present already
def check(file, dest):
    all = os.listdir(dest)
    for l in all:
        if file == l:
            return True
        else:
            return False


def organize():
    for f in allfiles:
        if f.lower().endswith(('.png', '.jpg', '.jpeg')):
            if check(f, destination.pic):
                continue
            else:
                shutil.move(source + '\\' + f, destination.pic + '\\' + f)
        elif f.lower().endswith(('.pdf')):
            if check(f, destination.pdf):
                continue
            else:
                shutil.move(source + '\\' + f, destination.pdf + '\\' + f)
        elif f.lower().endswith(('.psd')):
            if check(f, destination.psd):
                continue
            else:
                shutil.move(source + '\\' + f, destination.psd + '\\' + f)
        elif f.lower().endswith(('.doc', '.docx')):
            if check(f, destination.doc):
                continue
            else:
                shutil.move(source + '\\' + f, destination.doc + '\\' + f)
        elif f.lower().endswith(('.exe')):
            if check(f, destination.exe):
                continue
            else:
                shutil.move(source + '\\' + f, destination.exe + '\\' + f)
        elif f.lower().endswith(('.txt')):
            if check(f, destination.txt):
                continue
            else:
                shutil.move(source + '\\' + f, destination.txt + '\\' + f)
        elif f.lower().endswith(('.zip')):
            if check(f, destination.zip):
                continue
            else:
                shutil.move(source + '\\' + f, destination.zip + '\\' + f)
        elif f.lower().endswith(('.ppt', '.pptx')):
            if check(f, destination.pptx):
                continue
            else:
                shutil.move(source + '\\' + f, destination.pptx + '\\' + f)
        elif f.lower().endswith(('.prproj')):
            if check(f, destination.prproj):
                continue
            else:
                shutil.move(source + '\\' + f, destination.prproj + '\\' + f)
        else:
            if check(f, destination.others):
                continue
            else:
                shutil.move(source + '\\' + f, destination.others + '\\' + f)


# Driver code

# list all files and dir
allfiles = os.listdir(source)
make_dir()
allfiles = os.listdir(source)
remove_destination_dir()
# uncomment if use telegram desktop
# allfiles.remove('Telegram Desktop')
organize()
exit()
