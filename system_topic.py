#import sys
# Methods for interacting with python interpreter

# execute 'date +%H:%M:%S' and get output:

import subprocess
code = subprocess.call(["date", "+%H:%M:%S is ok"])
print(code)

output = subprocess.check_output(["date", "+%H:%M:%S"])



# decode the bytestring to ascii
output_ascii = output.decode('ascii')
print(output_ascii)


# strip leading and trailing spaces:
print(output_ascii.strip())


def open_terminal(profile, directory):
  """open a terminal with a custom profile in the given directory"""
  cmd = "gnome-terminal"
  args = (
    "--window-with-profile",profile,
    "--working-directory",directory
  )

#  subprocess.call([cmd, *args])

# open_terminal("day", "/data/python_demos/music")

def open_vscode(directory):
  """open VS Code editor and load given directory"""
  cmd = "code"

 # subprocess.call([cmd, directory])

#open_vscode("/data/python_demos/music")

def load_browser(profile, url):
  """open Chrome browser in new window,
     with the given user profile and loads the specified URLs
  """
  cmd = "google-chrome"
  args = "--new-window --profile-directory=" + "'{:s}' {:s}".format(profile, url)

  subprocess.call(cmd + " " + args, shell=True)


urls_to_load = [
  "https://mail.google.com",
  "http://wwwcourses.github.io/ProgressBG-VMware-Python"
]


load_browser("Profile 7",  " ".join(urls_to_load))



print("*"*40)

code = subprocess.call(["pwd"])
print(code)
print("*"*40)

import os
myPWD=os.getcwd()
print("*"*40)
# print(os.listdir(os.getcwd()))
os.chdir('/')
print(os.listdir(path='.'))
#os.mkdir(path)
#os.makedirs(path)
#os.rename(src, dst)
#os.rmdir(path)
print(os.path.join(myPWD,'data'))
os.chdir(myPWD)
for j in os.listdir(myPWD):
  if j[0] == 'I':
    print (j)
print("*"*40)

print( list(filter(lambda entry: entry.startswith(('I','O','d')), os.listdir(myPWD) )) )

os.mkdir(os.path.join(myPWD,'data'))
print( list(filter(lambda entry: entry.startswith(('I','O','d')), os.listdir(myPWD) )) )
os.rename(os.path.join(myPWD,'data'),os.path.join(myPWD,'sata'))
print( list(filter(lambda entry: entry.startswith(('I','O','s')), os.listdir(myPWD) )) )
os.rmdir(os.path.join(myPWD,'sata'))
print( list(filter(lambda entry: entry.startswith(('I','O','d')), os.listdir(myPWD) )) )



#path =  os.getcwd()
#filenames = os.listdir(path)
#for filename in filenames:
#  os.rename(os.path.join(path,filename), os.path.join(path,filename.replace(" ", "-").lower()) )
  
      

#fh = open(file_path, mode="mode") 
#fh.readlines()
#fh.read()
#fh.write(str)
#fh.writelines(sequence)
#os.remove(file_path)

#contents =f.read()

#with open("test.txt") as fh:
#    data = fh.read()
#    # do something with data

print(os.stat('.',follow_symlinks=True))

# Create a simple backup function to archive the content in one folder (src) int oother folder (dest), 
# while setting a timestamp into filenames, as explained in the function docstring below
def backup(src, dest):
  """Backup files in src folder into dest folder.
    Do not remove the files in source folder.
    To each file attach suffix with curent timestamp in the form
    '2018-04-12_18-30-45'

  Args:
      src (string): Source folder
      dest (string): Destination folder

  Example:
    /src/track5.mp3 => /dest/track5.mp3_2018-04-12_18-30-45
  """

#  To get the current timestamp, you can use next function:
def get_timestamp():
  #get the current local date-time
  cldt = datetime.datetime.today()

  # get the timestamp as a string with given format
  timestamp = datetime.datetime.strftime(cldt, '%Y-%m-%d_%H_%M_%S')

  return timestamp

# See: https://pastebin.com/MAPV3P0M







# Distribute files in one folder (src) into a corresponding sub-folders, 
# according to their file-type, as explained in the function docstring bellow
def cataloger(src):
        """Distribute files in the src folder into a corresponding sub-folders,
        according to their file-type.

        Each catalogue, is a subfolder made by a filename extension

        Examples:
         /data/notes1.txt => /data/txt/notes1.txt
         /data/notes2.txt => /data/txt/notes2.txt
         /data/picture1.png => /data/png/picture1.png
         /data/track1.mp3 => /data/mp3/track1.mp3

        Args:
            src (string): source folder
        """

#To extract the file extension, you can use the os.path.splitext() method from the os.path module
import os.path

filename = "/data/new/test.txt"
extension = os.path.splitext(filename)[1][1:]

print(extension)

#Please, prefix your filenames/archive with your name initials, before sending.
#For instance: iep_task1.py or iep_tasks.rar










