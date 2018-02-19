
import os
import sys
import subprocess
import imageio


#x= "ffprobe -v error -count_frames -select_streams v:0 \
#  -show_entries stream=nb_read_frames -of default=nokey=1:noprint_wrappers=1 \
#  /home/sakshi/Documents/work/mp4videos/new.mp4"

#image_count = int(os.system(x))
#i_c = x
"""r = subprocess.check_output(x, shell = True)
print('\n \n \n \n \n')
os.system(x)'''
#print r"""
var = "ffmpeg -i '/home/sakshi/Documents/work/mp4videos/SampleVideo.mp4' -t 5 -r 30 -f image2 '/home/sakshi/Documents/work/imgFolder/allFrames/'image%d.jpg " 
 

os.system(var)
