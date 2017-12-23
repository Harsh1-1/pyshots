import os

file_extns = {"text":('.DOC','.DOCX','.LOG','.MSG','.ODT','.PAGES','.RTF','.TEX','.TXT','.WPD','.WPS'),
"data":('.CSV','.DAT','.GED','.KEY','.KEYCHAIN','.PPS','.PPT','.PPTX','.SDF','.TAR','.TAX2016','.VCF','.XML'),
"audio":('.AIF', '.IFF', '.M3U', '.M4A', '.MID', '.MP3', '.MPA', '.WAV', '.WMA'),
"video":('.3G2','.3GP','.ASF','.AVI','.FLV','.M4V','.MOV','.MP4','.MPG','.RM','.SRT','.SWF','.VOB','.WMV'),
"3d_image_file":('.3DM', '.3DS', '.MAX', '.OBJ'),
"images":('.BMP','.DDS','.GIF','.JPG','.PNG','.PSD','.PSPIMAGE','.TGA','.THM','.TIF','.TIFF','.YUV','.JPEG'),
"vector_images":('.AI', '.EPS', '.PS', '.SVG'),
"pdfs":('.INDD', '.PCT', '.PDF'),
"spreadsheets":('.XLR', '.XLS', '.XLSX'),
"database_files":('.ACCDB', '.DB', '.DBF', '.MDB', '.PDB', '.SQL'),
"executables":('.APK', '.APP', '.BAT', '.CGI', '.COM', '.EXE', '.GADGET', '.JAR', '.WSF'),
"game_files":('.DEM', '.GAM', '.NES', '.ROM', '.SAV'),
"web_files":('.ASP','.ASPX','.CER','.CFM','.CSR','.CSS','.HTM','.HTML','.JS','.JSP','.PHP','.RSS','.XHTML'),
"compressed_files":('.7Z','.CBR','.DEB','.GZ','.PKG','.RAR','.RPM','.SITX','.TAR.GZ','.ZIP','.ZIPX'),
"disk_images":('.BIN', '.CUE', '.DMG', '.ISO', '.MDF', '.TOAST', '.VCD'),
"codes":('.C','.CLASS','.CPP','.CS','.DTD','.FLA','.H','.JAVA','.LUA','.M','.PL','.PY','.SH','.SLN','.SWIFT','.VB','.VCXPROJ','.XCODEPROJ')
}

#default path is current directory as of now
PATH = "./"

# def advance_cleaning():
    #ToDO

def cleaning():
    files_dir_list = os.listdir(PATH)
    for element in files_dir_list:
        if(os.path.isfile(element)):
            flag = False
            ext_list = element.split('.')
            ext = '.' + ext_list[len(ext_list)-1]
            for key,value in file_extns.items():
                if ext.upper() in file_extns[key]:
                    flag = True
                    if(os.path.isdir(key)):
                        os.rename(PATH+element,PATH+key+'/'+element)
                        break
                    else:
                        os.mkdir(key)
                        os.rename(PATH+element,PATH+key+'/'+element)
                        break
            if(not flag):
                if(os.path.isdir('others')):
                    os.rename(PATH+element,PATH+'others/'+element)
                else:
                    os.mkdir('others')
                    os.rename(PATH+element,PATH+'others/'+element)

cleaning()
