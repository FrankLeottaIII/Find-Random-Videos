
#Random Youtube Video Finder
#Author: Frank R. Leotta III
# date started: 2/12/2024

#Discription: The program will help you find random youtube videos that may interest you, or ones you can downvote if you want to waste your time doinging that.
    #  This program generates 64 character long youtube ids, puts it into a list, and then goes through each one and checks if:
    #  1. The video is still up, or even exists yet
    #  2. The videos title, description, and first 10 tags if they exist to see if it is something you may be interested in.
    # 3. The videos like to dislike ratio to see if it is worth watching or not.

#need to do:
    # 1. make a ist of 64 random youtube ids, Test to see if they are valid, for error handling

#run it throug a loop, and add to each of the lists the video info.


import scrapetube
import pandas as pd
import random
import csv
import copy
from random import shuffle
import time
import pytube
from pytube import YouTube
from pytube import Playlist
from pytube import Channel
from pytube import extract
from pytube import request
import requests
from  requests import get
from bs4 import BeautifulSoup
import datetime

def add_two_lists_elements(list1, list2):  
    """Summary:
    Add two lists elements together.
    """
    return [x + y for x, y in zip(list1, list2)]

def random_youtube_id_generator()->str:
    """Summary:
    Generate a random youtube id.
    
    
    """
    acceptable_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '_']
    random.shuffle(acceptable_characters)
    list2 = copy.deepcopy(acceptable_characters)
    shuffle(list2)
    list3 = add_two_lists_elements(acceptable_characters, list2)
    shuffle(acceptable_characters)
    shuffle(list3)
    list4 = add_two_lists_elements(acceptable_characters, list3)
    shuffle(acceptable_characters)
    shuffle(list4)
    list5 = add_two_lists_elements(acceptable_characters, list4)
    shuffle(acceptable_characters)
    shuffle(list5)
    list6 = add_two_lists_elements(acceptable_characters, list5)
    shuffle(acceptable_characters)
    shuffle(list6)
    list7 = add_two_lists_elements(acceptable_characters, list6)
    shuffle(acceptable_characters)
    shuffle(list7)
    list8 = add_two_lists_elements(acceptable_characters, list7)
    shuffle(acceptable_characters)
    shuffle(list8)
    list9 = add_two_lists_elements(acceptable_characters, list8)
    shuffle(acceptable_characters)
    shuffle(list9)
    list10 = add_two_lists_elements(acceptable_characters, list9)
    shuffle(acceptable_characters)
    shuffle(list10)
    list11 = add_two_lists_elements(acceptable_characters, list10)
    return list11

def add_to_dict(List1 : list)->dict:
    """Summary:
    This function will add the 64 generated youtube ids to a dictionary, with the key being the id, and the value the list filled with ids.
    """
    dictionary = {}
    for id in List1:
        dictionary[id] = List1
    return dictionary

def find_video_info(video_id: str)->dict:
    """Summary: 
        Creates a youtube object using the pytube module and gets the title, description, and tags of the video.
        
        """
    video = YouTube(f"https://www.youtube.com/watch?v={video_id}")
    video_info = {"title": video.title, "description": video.description, "tags": video.keywords}
    return video_info

# print(find_video_info("ZpnnXMdvpMA"))


def find_video_info_d(video_id: str)->dict:
    """Summary:
    This function will take a youtube video id and return a dictionary with the 'ID','Video URL', 'Video Title', 'Video Author','Video Publish Date', and "Duration"
    """
    video = YouTube(f"https://www.youtube.com/watch?v={video_id}")
    video_info = {"ID": video_id, "Video URL": f"https://www.youtube.com/watch?v={video_id}", "Video Title": video.title, "Video Author": video.author, "Video Publish Date": video.publish_date, "Duration": video.length}
    return video_info



def convert_datetime_to_month_day_year(date: datetime.datetime)->str:
    """Summary:
    This function will take a datetime object and return a string with the month, day, and year.
    """
    return date.strftime("%B %d, %Y")


# ID = "aolI_Rz0ZqY"

# varible = find_video_info_d(ID)
# varible["Video Publish Date"] = convert_datetime_to_month_day_year(varible["Video Publish Date"])
# varible["Duration"] = str(datetime.timedelta(seconds=varible["Duration"]))




def find_video_tags(video_id: str)->list:
    """Summary:
    This function will take a youtube video id and return a list with the first 10 tags if they exist.
    #this will shorten the tags to 200 characters, and replace the commas with spaces.
    """
    html = requests.get(f"https://www.youtube.com/watch?v={video_id}")
    soup = BeautifulSoup(html.text, 'html.parser')
    get_tags = soup.find('meta', {'name': 'keywords'})
    get_tags = str(get_tags)
    get_tags = get_tags.replace('<meta content="', "")
    get_tags = get_tags.replace('" name="keywords"/>', "")  
    get_tags = list(get_tags)
    # get_tags = get_tags[250:]
    if len(get_tags) > 200:
        get_tags = get_tags[:200]#this is to limit the tags to 250 characters starting from the beginning of the list
    else:
        get_tags = get_tags
    get_tags = "".join(get_tags)
    get_tags = get_tags.replace(",", "  ")
    # get_tags = str(get_tags)
    return get_tags
# id = []
# video_URL = []
# Video_Title  = []
# Video_Author = []
# Video_Publish_Date = []
# Video_Duration = []
# Video_Tags = []

# varible["Tags"] = find_video_tags(ID)

# id.append(varible["ID"])
# video_URL.append(varible["Video URL"])
# Video_Title.append(varible["Video Title"])
# Video_Author.append(varible["Video Author"])
# Video_Publish_Date.append(varible["Video Publish Date"])
# Video_Duration.append(varible["Duration"])
# Video_Tags.append(varible["Tags"])






# print(find_video_tags("ZpnnXMdvpMA"))

def write_cvs_7_from_list(id, video_urls, video_titles, video_author, video_publish_date, duration, tags):
    """Summary:
    This function will write a csv file with the first row being 'ID', the second row being the video urls, the third row being 'Video Title', the fourth row being  video titles, the fifth row being video author, the 6th row being video publish date.
    This will only work for dictionaries, not lists.
    """
    writer = csv.writer(open('playlistq.csv', 'w', newline='', encoding='utf-8'))# the newline='' is to fix the double spacing
    writer.writerow(['ID','Video URL', 'Video Title', 'Video Author','Video Publish Date', "Duration", "Tags"])
    for id, video_url, video_title, video_author, video_publish_date, video_duration, video_tags in zip(id, video_urls, video_titles, video_author, video_publish_date, duration, tags):
        writer.writerow([id, video_url, video_title, video_author, video_publish_date, video_duration, video_tags])

def ammened_cvs_7_from_list(id, video_urls, video_titles, video_author, video_publish_date, duration, tags):
    """Summary:
    This function will ammend a csv file with the first row being 'ID', the second row being the video urls, the third row being 'Video Title', the fourth row being  video titles, the fifth row being video author, the 6th row being video publish date.
    This will only work for dictionaries, not lists.
    """
    writer = csv.writer(open('playlistq.csv', 'a', newline='', encoding='utf-8'))# the newline='' is to fix the double spacing
    writer.writerow(['ID','Video URL', 'Video Title', 'Video Author','Video Publish Date', "Duration", "Tags"])
    for id, video_url, video_title, video_author, video_publish_date, video_duration, video_tags in zip(id, video_urls, video_titles, video_author, video_publish_date, duration, tags):
        writer.writerow([id, video_url, video_title, video_author, video_publish_date, video_duration, video_tags])

# write_cvs_7_from_list(id, video_URL, Video_Title, Video_Author, Video_Publish_Date, Video_Duration, Video_Tags)



#find out if the video is still up, or even exists yet
def is_video_valid(video_id: str)->bool:
    """Summary:
    This function will take a youtube video id and return a boolean value of True if the video is valid, and False if it is not.
    """
    try:
        video = YouTube(f"https://www.youtube.com/watch?v={video_id}")
        return True
    except:
        return False

print("\n\nn\n\n\n")


def main():
    """Summary:
    This function will run the program and call all relevent functions.
    """
    random_youtube_ids = []
    while True:
        youtube_id = random_youtube_id_generator()
        print(youtube_id)
        print("\n")
        time.sleep(2)
        if is_video_valid(youtube_id):
            random_youtube_ids.append(youtube_id)
            if len(random_youtube_ids) == 1: #this is to test if the youtube ids are valid
                print(random_youtube_ids)
                break


    # print(random_youtube_ids)
    print("n\n\n\n\n\n\n\"")
    if len(random_youtube_ids) == 0:
        print("There are no valid youtube ids.")
    else:
        print("There are valid youtube ids.")
        print(random_youtube_ids)
        failed_youtube_ids = []
        id = []
        video_URL = []
        Video_Title  = []
        Video_Author = []
        Video_Publish_Date = []
        Video_Duration = []
        Video_Tags = []
        
        iD = "aolI_Rz0ZqY"
        varible = find_video_info_d(iD)
        varible["Video Publish Date"] = convert_datetime_to_month_day_year(varible["Video Publish Date"])
        varible["Duration"] = str(datetime.timedelta(seconds=varible["Duration"]))
        varible["Tags"] = find_video_tags(id)
        id.append(varible["ID"])
        video_URL.append(varible["Video URL"])
        Video_Title.append(varible["Video Title"])
        Video_Author.append(varible["Video Author"])
        Video_Publish_Date.append(varible["Video Publish Date"])
        Video_Duration.append(varible["Duration"])
        Video_Tags.append(varible["Tags"])
        print ("this is a test\n\n")
        # print(varible)

        write_cvs_7_from_list(id, video_URL, Video_Title, Video_Author, Video_Publish_Date, Video_Duration, Video_Tags)
        for id in random_youtube_ids:
            varible = find_video_info_d(id)

            varible["Video Publish Date"] = convert_datetime_to_month_day_year(varible["Video Publish Date"])
            varible["Duration"] = str(datetime.timedelta(seconds=varible["Duration"]))
            varible["Tags"] = find_video_tags(id)
            id.append(varible["ID"]) #string object has no attribute append... this is the error
            video_URL.append(varible["Video URL"])
            Video_Title.append(varible["Video Title"])
            Video_Author.append(varible["Video Author"])
            Video_Publish_Date.append(varible["Video Publish Date"])
            Video_Duration.append(varible["Duration"])
            Video_Tags.append(varible["Tags"])
            print(varible)
            ammened_cvs_7_from_list(id, video_URL, Video_Title, Video_Author, Video_Publish_Date, Video_Duration, Video_Tags)
        # for i in random_youtube_ids: #this is to test if the youtube ids are valid
    #     try:
    #         varible = find_video_info_d(i)
    #         varible["Video Publish Date"] = convert_datetime_to_month_day_year(varible["Video Publish Date"])
    #         varible["Duration"] = str(datetime.timedelta(seconds=varible["Duration"]))
    #         varible["Tags"] = find_video_tags(i)
    #         id.append(varible["ID"])
    #         video_URL.append(varible["Video URL"])
    #         Video_Title.append(varible["Video Title"])
    #         Video_Author.append(varible["Video Author"])
    #         Video_Publish_Date.append(varible["Video Publish Date"])
    #         Video_Duration.append(varible["Duration"])
    #         Video_Tags.append(varible["Tags"])
    #         print(varible)
    #     except:
    #         failed_youtube_ids.append(random_youtube_ids)

    # print(id)
    # print(video_URL)
    # print(Video_Title)
    # print(Video_Author)
    # print(Video_Publish_Date)

    # write_cvs_7_from_list(id, video_URL, Video_Title, Video_Author, Video_Publish_Date, Video_Duration, Video_Tags)





    #     for i in range(len(random_youtube_ids)):
    #         if len(random_youtube_ids) == 0:
    #             break
    #         try:
    #             varible = find_video_info_d(i)
    #             varible["Video Publish Date"] = convert_datetime_to_month_day_year(varible["Video Publish Date"])
    #             varible["Duration"] = str(datetime.timedelta(seconds=varible["Duration"]))
    #             varible["Tags"] = find_video_tags(i)
    #             id.append(varible["ID"])
    #             video_URL.append(varible["Video URL"])
    #             Video_Title.append(varible["Video Title"])
    #             Video_Author.append(varible["Video Author"])
    #             Video_Publish_Date.append(varible["Video Publish Date"])
    #             Video_Duration.append(varible["Duration"])
    #             Video_Tags.append(varible["Tags"])
    #         except:
    #             failed_youtube_ids.append(random_youtube_id)
    # # write_cvs_7_from_list(id, video_URL, Video_Title, Video_Author, Video_Publish_Date, Video_Duration, Video_Tags)
    # print(failed_youtube_ids)
        print("The program has finished running.")
    # print(add_to_dict(random_youtube_ids))
    # print(find_video_info("ZpnnXMdvpMA"))
    # print(find_video_info_d("ZpnnXMdvpMA"))
    # print(find_video_tags("ZpnnXMdvpMA"))
    # print(write_cvs_7_from_list("ZpnnXMdvpMA"))

if __name__ == "__main__":
    main()