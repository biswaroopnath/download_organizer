# organize downlaods folder
import os
import shutil

# edit the following if download folder is in some other places
source = 'C:\\Users\\user\\Downloads'


class destination:
    pic = 'C:\\Users\\user\\Downloads\\pic'
    doc = 'C:\\Users\\user\\Downloads\\doc\\word'
    psd = 'C:\\Users\\user\\Downloads\\doc\\psd'
    pdf = 'C:\\Users\\user\\Downloads\\doc\\pdf'
    exe = 'C:\\Users\\user\\Downloads\\exe'
    zip = 'C:\\Users\\user\\Downloads\\doc\\zip'
    prproj = 'C:\\Users\\user\\Downloads\\doc\\premier_pro'
    txt = 'C:\\Users\\user\\Downloads\\doc\\txt'
    pptx = 'C:\\Users\\user\\Downloads\\doc\\pptx'
    others = 'C:\\Users\\user\\Downloads\\others'

    documents = 'C:\\Users\\user\\Downloads\\doc'


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
    if os.path.exists('C:\\Users\\user\\Downloads\\doc'):
        allfiles.remove('doc')
    if os.path.exists('C:\\Users\\user\\Downloads\\exe'):
        allfiles.remove('exe')
    if os.path.exists('C:\\Users\\user\\Downloads\\others'):
        allfiles.remove('others')
    if os.path.exists('C:\\Users\\user\\Downloads\\pic'):
        allfiles.remove('pic')


def organize():
    for f in allfiles:
        if f.lower().endswith(('.png', '.jpg', '.jpeg')):
            shutil.move(source + '\\' + f, destination.pic + '\\' + f)
        elif f.lower().endswith(('.pdf')):
            shutil.move(source + '\\' + f, destination.pdf + '\\' + f)
        elif f.lower().endswith(('.psd')):
            shutil.move(source + '\\' + f, destination.psd + '\\' + f)
        elif f.lower().endswith(('.doc', '.docx')):
            shutil.move(source + '\\' + f, destination.doc + '\\' + f)
        elif f.lower().endswith(('.exe')):
            shutil.move(source + '\\' + f, destination.exe + '\\' + f)
        elif f.lower().endswith(('.txt')):
            shutil.move(source + '\\' + f, destination.txt + '\\' + f)
        elif f.lower().endswith(('.zip')):
            shutil.move(source + '\\' + f, destination.zip + '\\' + f)
        elif f.lower().endswith(('.ppt', '.pptx')):
            shutil.move(source + '\\' + f, destination.pptx + '\\' + f)
        elif f.lower().endswith(('.prproj')):
            shutil.move(source + '\\' + f, destination.prproj + '\\' + f)
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
