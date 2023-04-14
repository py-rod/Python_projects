from pytube import YouTube
import requests
import io
from PIL import Image
import os


# class Linux_mac():
#     def __init__(self):
#         self.obtain_foto_video()
        
        
        
#     def obtain_foto_video(self):
#         # obtain user desktop
#         user = os.getlogin()
#         # obatin system platform
#         system = platform.system()
#         # check if exist that directorie
#         check = os.path.exists(f"/home/{user}/Youtube_Download/images")
        
#         # obtain img video
#         image = video.thumbnail_url
#         response = requests.get(image)
#         image_byte = io.BytesIO(response.content)
#         img = Image.open(image_byte)
        
#         # Linux
#         if system == "Linux" or "Mac" and check:
#             # save img video
#             img.save(f"/home/{user}/Youtube_Download/images/img_video.png")
            
#             #Edit image width
#             src = cv2.imread(f"/home/{user}/Youtube_Download/images/img_video.png", cv2.IMREAD_UNCHANGED)
#             new_width =  180

#             dsize = (new_width, src.shape[0])

#             # resize image
#             output = cv2.resize(src, dsize, interpolation = cv2.INTER_AREA)
            
#             #Save image 
#             cv2.imwrite(f"/home/{user}/Youtube_Download/images/img_video.png",output)

#             #Edit image height
#             src2 = cv2.imread(f"/home/{user}/Youtube_Download/images/img_video.png", cv2.IMREAD_UNCHANGED)
#             new_height =  180

#             dsize = (new_height, src2.shape[1])

#             # resize image
#             output = cv2.resize(src2, dsize, interpolation = cv2.INTER_AREA)
#             #Save image
#             cv2.imwrite(f"/home/{user}/Youtube_Download/images/img_video.png",output)
#         else:
#             # Create folder
#             os.mkdir(f"/home/{user}/Youtube_Download/images")
            
#             # Save img video
#             img.save(f"/home/{user}/Youtube_Download/images/img_video.png")
            
            
#             #Edit image width
#             src = cv2.imread(f"/home/{user}/Youtube_Download/images/img_video.png", cv2.IMREAD_UNCHANGED)
#             new_width =  180

#             dsize = (new_width, src.shape[0])

#             # resize image
#             output = cv2.resize(src, dsize, interpolation = cv2.INTER_AREA)
            
#             #Save image 
#             cv2.imwrite(f"/home/{user}/Youtube_Download/images/img_video.png",output)

#             #Edit image height
#             src2 = cv2.imread(f"/home/{user}/Youtube_Download/images/img_video.png", cv2.IMREAD_UNCHANGED)
#             new_height =  180

#             dsize = (new_height, src2.shape[1])

#             # resize image
#             output = cv2.resize(src2, dsize, interpolation = cv2.INTER_AREA)
#             #Save image
#             cv2.imwrite(f"/home/{user}/Youtube_Download/images/img_video.png",output)



url = "https://www.youtube.com/watch?v=Bg59q4puhmg&list=RDBg59q4puhmg&start_radio=1"
video = YouTube(url)
# obtain img video
image = video.thumbnail_url
response = requests.get(image)
image_byte = io.BytesIO(response.content)
img = Image.open(image_byte)
img.save("mierda/foto.png")
        
        
# size = (180, 180)
# filename = "foto.png"
# outfile = filename
# try:
#     im = Image.open(filename)
#     im.thumbnail(size, Image.Resampling.LANCZOS)
#     im.save(outfile, "PNG")
# except IOError:print("cannot create thumbnail for '%s'" % filename)