import urllib.request
import requests 
from bs4 import BeautifulSoup # Read html 
import os


def download_file(url, dst_path):
    with urllib.request.urlopen(url) as web_file:
        with open(dst_path, 'wb') as local_file:
            local_file.write(web_file.read())

def download_file_HTML(output_folder, photoURL, dates, webURL):

    images = []

    if os.path.exists(output_folder) == False:
      os.mkdir(output_folder)

    #Access photos taken on a specific date
  
    for i in dates:
      soup = BeautifulSoup(requests.get(baseURL + str(i)).content,'lxml') # Analyze URL with bs

      #Get jpg and png info
    
      for link in soup.find_all("img"): # imgタグを取得しlinkに格納
          if link.get("src").endswith(".jpg"): # imgタグ内の.jpgであるsrcタグを取得
              images.append(link.get("src")) # imagesリストに格納
          elif link.get("src").endswith(".png"): # imgタグ内の.pngであるsrcタグを取得
    	      images.append(link.get("src")) # imagesリストに格納

      for target in images: # imagesからtargetに入れる
          re = requests.get(webURL + target[1:])
          with open(os.path.join(output_folder, target.split('/')[-1]), 'wb') as f: # imgフォルダに格納
              f.write(re.content) # .contentにて画像データとして書き込む

    print("OK")
