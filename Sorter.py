import glob
import shutil, os

start_path = 'C:/Users/Juan/Downloads'
IMG_folder = 'C:/Users/Juan/Downloads/IMG'
DOCS_folder = 'C:/Users/Juan/Downloads/DOCS'
BOOKS_Sub = 'C:/Users/Juan/Downloads/DOCS/BOOKS_Sub'
INSTALLER_folder = 'C:/Users/Juan/Downloads/INSTALLER'
ZIP_folder = 'C:/Users/Juan/Downloads/ZIP'

## JPG, GIF, PNG
img = []
for file_name in glob.glob('C:/Users/Juan/Downloads/*.png'):
	img.append(file_name)
for file_name in glob.glob('C:/Users/Juan/Downloads/*.jpg'):
	img.append(file_name)
for file in img:
	shutil.move(os.path.join(start_path,file),IMG_folder)

## PDF, DOC, EXCEL
doc = []
for file_name in glob.glob('C:/Users/Juan/Downloads/*.pdf'):
	doc.append(file_name)
for file in doc:
	shutil.move(os.path.join(start_path,file),DOCS_folder)

### Books 
book = []
for file_name in glob.glob('C:/Users/Juan/Downloads/*.epub'):
	book.append(file_name)
for file_name in book:
	shutil.move(os.path.join(start_path,file_name),BOOKS_Sub)

## exe, msi, jar
installer = []
for file_name in glob.glob('C:/Users/Juan/Downloads/*.exe'):
	installer.append(file_name)
for file_name in glob.glob('C:/Users/Juan/Downloads/*msi'):
	installer.append(file_name)
for file_name in glob.glob('C:/Users/Juan/Downloads/*jar'):
	installer.append(file_name)

for file in installer:
	shutil.move(os.path.join(start_path,file),INSTALLER_folder)

## zip, rar
rar = []
for file_name in glob.glob('C:/Users/Juan/Downloads/*.rar'):
	rar.append(file_name)
for file_name in glob.glob('C:/Users/Juan/Downloads/*.zip'):
	rar.append(file_name)

for file in rar:
	shutil.move(os.path.join(start_path,file),ZIP_folder)