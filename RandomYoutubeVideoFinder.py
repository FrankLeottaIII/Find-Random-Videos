
#Random Youtube Video Finder
#Author: Frank R. Leotta III
# date started: 2/12/2024

#Discription: The program will help you find random youtube videos that may interest you, or ones you can downvote if you want to waste your time doinging that.
    #  This program generates 64 character long youtube ids, puts it into a list, and then goes through each one and checks if:
    #  1. The video is still up, or even exists yet
    #  2. The videos title, description, and first 10 tags if they exist to see if it is something you may be interested in.
    # 3. The videos like to dislike ratio to see if it is worth watching or not.

import scrapetube
import pandas as pd
import random
import csv
import copy
from random import shuffle



def random_youtube_id_generator()->str:
    """Summary:
    Generate a random youtube id.
    
    
    """
    acceptable_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '_']
    random.shuffle(acceptable_characters)
    list2 = copy.deepcopy(acceptable_characters)
    shuffle(list2)
    list3 = add_list_elements_together(acceptable_characters, list2)
    shuffle(acceptable_characters)
    shuffle(list3)
    list4 = add_list_elements_together(acceptable_characters, list3)
    shuffle(acceptable_characters)
    shuffle(list4)
    list5 = add_list_elements_together(acceptable_characters, list4)
    shuffle(acceptable_characters)
    shuffle(list5)
    list6 = add_list_elements_together(acceptable_characters, list5)
    shuffle(acceptable_characters)
    shuffle(list6)
    list7 = add_list_elements_together(acceptable_characters, list6)
    shuffle(acceptable_characters)
    shuffle(list7)
    list8 = add_list_elements_together(acceptable_characters, list7)
    shuffle(acceptable_characters)
    shuffle(list8)
    list9 = add_list_elements_together(acceptable_characters, list8)
    shuffle(acceptable_characters)
    shuffle(list9)
    list10 = add_list_elements_together(acceptable_characters, list9)
    shuffle(acceptable_characters)
    shuffle(list10)
    list11 = add_list_elements_together(acceptable_characters, list10)
    return list11


def find_video_info_e(video_id: str)->dict: #experimental
    """Summary:
    This function will take a youtube video id and return a dictionary with the video's title, description, and first 10 tags if they exist.
    """
    video_info = scrapetube.get_video_info(video_id)
    return video_info

video_ID = "ZpnnXMdvpMA"
video_info = find_video_info_e(video_ID)
print(video_info)

def find_video_like_dislike_ratio_e(video_id: str)->dict: #experimental
    """Summary:
    This function will take a youtube video id and return a dictionary with the video's like to dislike ratio.
    """
    video_like_dislike_ratio = scrapetube.get_video_like_dislike_ratio(video_id)
    return video_like_dislike_ratio



def find video_title(video_id: str)->str:
    video_dict = {}
    for video in videos:
        title = video["title"]["runs"][0]["text"]
        try:
            author = video["shortBylineText"]["runs"][0]["text"]
        except KeyError:
            author = "Error"
        url = "https://www.youtube.com/playlist?list=" + str(video["videoId"])
        duration = video["lengthText"]["simpleText"]
        video_dict[url] = {"title": title,"author": author,"duration": duration, "url": url}  # Add the title and url to the dictionary
    #It goes directory[directory], then the keys in the directory directory, in the order they are listed for the CVS file.

    df = pd.DataFrame.from_dict(video_dict, orient='index')#convert the dictionary to a dataframe with pandas
    filename = input("what do you want to name the csv file? ")
    filename = str(filename)
    df.to_csv(f'{filename}.csv', header=False, encoding='utf-8')



def write_cvs_6_lists(id: list, video_urls: list, video_titles: list , video_author: list, video_publish_date: list , duration: list):
    """Summery:
    This function will write a csv file with the first row being 'ID', the second row being the video urls, the third row being 'Video Title', the fourth row being  video titles, the fifth row being video author, and the last row being video publish date.
    This will only work for lists, not dictionaries.
    """
    writer = csv.writer(open('playlist.csv', 'w', newline='', encoding='utf-8'))# the newline='' is to fix the double spacing
    writer.writerow(['ID','Video URL', 'Video Title', 'Video Author','Video Publish Date', "Duration"])
    for ID, url, title, video_author, video_publish_date, duration in zip(id, video_urls, video_titles, video_author, video_publish_date, duration):
        writer.writerow([ID, url, title, video_author, video_publish_date, duration])



