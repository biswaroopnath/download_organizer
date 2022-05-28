# organize downlaods folder
import os
import shutil

source = 'C:\\Users\\user\\Downloads'
allfiles = os.listdir(source)
allfiles.remove('doc')
allfiles.remove('exe')
allfiles.remove('others')
allfiles.remove('pic')
allfiles.remove('Telegram Desktop')


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
    else:
        shutil.move(source + '\\' + f, destination.others + '\\' + f)
