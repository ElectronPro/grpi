#This is a python Wrapper used for uploading photos and video to instagram using the official graph api
#Made by @ElectronPro




import requests
import json
import os
import time
from urllib.parse import quote


class upload:
        def photo(link,captio,graphapitokenenvname):
            accesstoken = os.getenv(f"{graphapitokenenvname}")

            imglink = {}

            encodecap = quote(captio)

            data = {}

            # accesstoken = f"{appid}|{crysecret}"
            try:

                fetcher = requests.get(f"https://graph.facebook.com/v17.0/me/accounts?fields=about,name,id,username,access_token&access_token={accesstoken}")

                gotdat = json.loads(fetcher.content)

                # print(gotdat)

                data["pageaccesstok"] = gotdat["data"][0]["access_token"]
                data["pageid"] = gotdat["data"][0]["id"]
                time.sleep(2)
                os.system("clear")

                idofrpage = str(data["pageid"])

                pageaccessid = str(data["pageaccesstok"])


                gogetter  = requests.get(f"https://graph.facebook.com/v17.0/{idofrpage}?fields=connected_instagram_account&access_token={pageaccessid}")

                os.system("clear")

                instaid = json.loads(gogetter.content)

                data["ig-user-id"] = instaid["connected_instagram_account"]["id"]

                os.system("clear")

                # print(data)

                time.sleep(2)

                igtok = str(data["ig-user-id"])

                finalinsta = requests.get(f"https://graph.facebook.com/v17.0/{igtok}?fields=name,username,id&access_token={accesstoken}")

                os.system("clear")

                os.system("clear")

                shsd = requests.post(f"https://graph.facebook.com/v17.0/{igtok}/media?image_url={link}&caption={encodecap}&access_token={pageaccessid}")
                time.sleep(10)
                # print(shsd.status_code)

                fcdoom = json.loads(shsd.content)
                # print(fcdoom)
                imagecontain = fcdoom["id"]
                # print(link)

                imglink["containid"] = imagecontain
                # print(imglink)
                mediaid = str(imglink["containid"])


                finalpost = requests.post(f"https://graph.facebook.com/v17.0/{igtok}/media_publish?creation_id={mediaid}&access_token={pageaccessid}")
            
            except Exception as error:
                 return print("The error ===> {}".format(error))

        def video(link,captio,graphapitokenenvname):
            accesstoken = os.getenv(f"{graphapitokenenvname}")
             
            imglink = {}

            encodecap = quote(captio)

            data = {}

            # accesstoken = f"{appid}|{crysecret}"

            try:


                fetcher = requests.get(f"https://graph.facebook.com/v17.0/me/accounts?fields=about,name,id,username,access_token&access_token={accesstoken}")

                gotdat = json.loads(fetcher.content)

                # print(gotdat)

                data["pageaccesstok"] = gotdat["data"][0]["access_token"]
                data["pageid"] = gotdat["data"][0]["id"]
                time.sleep(2)
                os.system("clear")

                idofrpage = str(data["pageid"])

                pageaccessid = str(data["pageaccesstok"])


                gogetter  = requests.get(f"https://graph.facebook.com/v17.0/{idofrpage}?fields=connected_instagram_account&access_token={pageaccessid}")

                os.system("clear")

                instaid = json.loads(gogetter.content)

                data["ig-user-id"] = instaid["connected_instagram_account"]["id"]

                os.system("clear")

                # print(data)

                time.sleep(2)

                igtok = str(data["ig-user-id"])

                finalinsta = requests.get(f"https://graph.facebook.com/v17.0/{igtok}?fields=name,username,id&access_token={accesstoken}")

                os.system("clear")

                os.system("clear")

                shsd = requests.post(f"https://graph.facebook.com/v17.0/{igtok}/media?video_url={link}&caption={encodecap}&access_token={pageaccessid}")
                time.sleep(10)
                # print(shsd.status_code)

                fcdoom = json.loads(shsd.content)
                # print(fcdoom)
                imagecontain = fcdoom["id"]
                # print(link)

                imglink["containid"] = imagecontain
                # print(imglink)
                mediaid = str(imglink["containid"])


                finalpost = requests.post(f"https://graph.facebook.com/v17.0/{igtok}/media_publish?creation_id={mediaid}&access_token={pageaccessid}")
            except Exception as error:
                 return print("The error ===> {}".format(error))

        def ready(graphapitokenenvname):
            try:
            
                checkstat = requests.get(f"https://graph.facebook.com/v17.0/me/accounts?fields=id&access_token={graphapitokenenvname}")
                status = checkstat.status_code  
                if status ==200:
                    return True
                else:
                    return False
                
            except Exception as error:
                 return print("The error ===> {}".format(error))




