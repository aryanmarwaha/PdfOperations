# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# ::For any queries please feel free to Contact the Devoleper :::::::
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ::Aryan Marwaha::
# ::GitHub   > "https://github.com/aryanmarwaha" 
# ::LinkedIn > "https://www.linkedin.com/in/aryan-marwaha-0029b5219/"
# ::Twitter  > "https://twitter.com/AryanMarwaha3"
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#####################################################################
# 1. Requirements:
# 		> You'll need to make sure that you've already installed Python3 on to your system.
# 		> You'll need to install pdfx module on to your system.
#
# 2. Procedure:
# 		step1 : Paste the target PDF(pdf-file, you want to extract the links from) in the PdfToTxt directory.
# 		step2 : Copy the target-File 's name and paste it into the Specify_FileName.txt and save it.
# 		Step3 : Execute(RUN) the program by clicking on the "Convert_RUN" shortcut.
#
# 3. Result:
# 		You'll see that a new file has been created (named "Target-File_Name"+"extracted_linkAry.txt").
#####################################################################

import pdfx

#Enter the File-Path or Name below :

f=open('../Specify_FileName.txt')

file_name= str(f.read())
f.close()
file_path=("../"+file_name)

# You can also specify the file path below and comment out the above statement
# file_path='Specify File PATH...'

pdf =pdfx.PDFx(file_path)

# all the final extracted links -will be stored in the list(refrences_list) at the end of the program.

references_list = list(pdf.get_references())
i=0
for each_link in references_list:
	filter1= str(each_link).split()
	filter1.remove(filter1[0])
	filter1=''.join(filter1)
	for char in filter1:
		filter1=filter1.replace('>','')
	references_list[i]=filter1
	i+=1
resFile_name= "../"+file_name+"extracted_linkAry.txt"
f=open(resFile_name,'w')
for i in references_list:
	f.write('\n')
	f.write(i)
	f.write('\n')

	print(i)
	print()
f.close()

