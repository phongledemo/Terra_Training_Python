



# # clip = VideoFileClip("movie_2.mp4")

# from typing import Concatenate
# from moviepy.editor import *

# lrc_file = open('Billie Eilish - Happier Than Ever.lrc')
# lrc_string = ''.join(lrc_file.readlines())


# u=''
# s=[]
# for i in lrc_string:
#     if i =="[":
#         u+=i
#     if u!='':
#         u+=i
#     if i == "]":
#         s.append(u)
#         u=''

# p=[]
# for i in s:
#     i = i.replace("[","")
#     i = i.replace("]","")
#     p.append(i)


# #Change minute to second
# total_lyric_second = []
# for i in p:
#     minutes = i.split(":")[0]
#     second = i.split(":")[1]
#     total_second = 60*int(minutes) + float(second)
#     total_second = float("{:.2f}".format(total_second))
#     total_lyric_second.append(total_second)
# print(total_lyric_second)
# with open('Billie Eilish - Happier Than Ever.txt') as f:
#     lines = f.readlines()
# print(lines)


# clip = VideoFileClip("Billie Eilish - Happier Than Ever (Official Music Video)-5GJWxDKyk3A.mp4") 
# # clip = clip.subclip(0, 20)    
# # clip = clip.volumex(0.8) 
# # txt_clip = TextClip(lines[0], fontsize = 40, color = 'black').set_pos('bottom').set_duration(10)
# # txt_clip_1 = TextClip(lines[1], fontsize = 40, color = 'black').set_pos('bottom').set_duration(10)
# # video = CompositeVideoClip([clip, txt_clip]) 
# # video.write_videofile("media.mp4")
    
# # # showing video 
# # video.ipython_display(width = 280)
# main_clip = clip.subclip(0, total_lyric_second[0])
# combined = concatenate_videoclips([main_clip])
# print(len(total_lyric_second))
# print(len(lines))
# for i in range(0, len(lines)):
#     duration = total_lyric_second[i+1] - total_lyric_second[i]
#     next_clip = clip.subclip(total_lyric_second[i], total_lyric_second[i+1])
#     txt_clip = TextClip(lines[i], fontsize = 40, color = 'black').set_pos('bottom').set_duration(duration)
#     video = CompositeVideoClip([next_clip, txt_clip]) 
#     combined = concatenate_videoclips([combined, video])

# combined.write_videofile("media.mp4")


from moviepy.editor import *

#Open file lrc
lrc_file = open('Billie Eilish - Happier Than Ever.lrc')
lrc_string = ''.join(lrc_file.readlines())

#Take lines
with open('Billie Eilish - Happier Than Ever.lrc') as f:
    lines = f.readlines()

#variables
time = []
lyric = []

#Take time
for i in lines:
    time.append(i[1:9])

#Change minute to second
total_lyric_second = []
for i in time:
    minutes = i.split(":")[0]
    second = i.split(":")[1]
    total_second = 60*int(minutes) + float(second)
    total_second = float("{:.2f}".format(total_second))
    total_lyric_second.append(total_second)
#Take lyric
for i in range(0,len(lines)):
    i = lines[i].split("]")[1]
    i = i.split("[")[0]
    lyric.append(i)
#Load video
clip = VideoFileClip("Billie Eilish - Happier Than Ever (Official Music Video)-5GJWxDKyk3A.mp4") 


# #Add lyric to video
# main_clip = clip.subclip(0, total_lyric_second[0])
# combined = concatenate_videoclips([main_clip])

# for i in range(0, len(lyric)-1):
#     duration = total_lyric_second[i+1] - total_lyric_second[i]
#     next_clip = clip.subclip(total_lyric_second[i], total_lyric_second[i+1])
#     txt_clip = TextClip(lyric[i], fontsize = 50, color = 'white', font = 'Courier').set_pos('bottom').set_duration(duration)
#     video = CompositeVideoClip([next_clip, txt_clip]) 
#     combined = concatenate_videoclips([combined, video])

# #Save video
# combined.write_videofile("media.mp4")


#Choice time song

# clip_trim = VideoFileClip("media.mp4").subclip(20,40)
# combined = concatenate_videoclips([clip_trim])
# combined.write_videofile("heelo.mp4")





start_time = 10
end_time = 25
lyric_startTime = 15
lyric_endTime = 25

clip_vip = clip.subclip(10,25)
lyric_stamp = []

for i in range(0,len(total_lyric_second)-1):
    if lyric_startTime <= total_lyric_second[i] <= lyric_endTime:
        lyric_stamp.append(i)

print(lyric_stamp)
print(len(lyric_stamp))
main_clip = clip_vip.subclip(0, total_lyric_second[lyric_stamp[0]]-start_time)
combined = concatenate_videoclips([main_clip])

if len(lyric_stamp) == 1:
    print('a')
    next_clip = clip_vip.subclip(lyric_startTime - start_time, end_time - start_time)
    duration = lyric_endTime - lyric_startTime
    txt_clip = TextClip(lyric[lyric_stamp[0]], fontsize = 50, color = 'white', font = 'Courier').set_pos('bottom').set_duration(duration)
    video = CompositeVideoClip([next_clip, txt_clip])
    combined = concatenate_videoclips([combined, video])

else:
    for i in range(0,len(lyric_stamp)):
        if i == (len(lyric_stamp) - 1):
            next_clip = clip_vip.subclip(total_lyric_second[lyric_stamp[i]] - start_time, end_time - start_time)
            duration = end_time - total_lyric_second[lyric_stamp[i]]
            txt_clip = TextClip(lyric[lyric_stamp[i]], fontsize = 50, color = 'white', font = 'Courier').set_pos('bottom').set_duration(duration)
            video = CompositeVideoClip([next_clip, txt_clip])
            combined = concatenate_videoclips([combined, video])
            combined.write_videofile("feels.mp4")
        else:
            next_clip = clip_vip.subclip(total_lyric_second[lyric_stamp[i]] - start_time, total_lyric_second[lyric_stamp[i+1]] - start_time)
            duration = total_lyric_second[lyric_stamp[i+1]] - total_lyric_second[lyric_stamp[i]]
            txt_clip = TextClip(lyric[lyric_stamp[i]], fontsize = 50, color = 'white', font = 'Courier').set_pos('bottom').set_duration(duration)
            video = CompositeVideoClip([next_clip, txt_clip])
            combined = concatenate_videoclips([combined, video])






    # if (lyric_startTime <= total_lyric_second[i]) and(total_lyric_second[i+1] <=lyric_endTime):
    #     duration = total_lyric_second[i+1] - total_lyric_second[i]
    #     txt_clip = TextClip(lyric[i], fontsize = 50, color = 'white', font = 'Courier').set_pos('bottom').set_duration(duration)
    #     next_clip = clip_vip.subclip(total_lyric_second[i], total_lyric_second[i+1])
    #     video = CompositeVideoClip([next_clip, txt_clip]) 
    #     combined = concatenate_videoclips([combined, video])

    # if (lyric_startTime <= total_lyric_second[i]) and (lyric_endTime <= total_lyric_second[i+1]):
    #     duration = lyric_endTime - total_lyric_second[i]
    #     txt_clip = TextClip(lyric[i], fontsize = 50, color = 'white', font = 'Courier').set_pos('bottom').set_duration(duration)
    #     next_clip = clip_vip.subclip(total_lyric_second[i], lyric_endTime)
    #     video = CompositeVideoClip([next_clip, txt_clip])
    #     combined = concatenate_videoclips([combined, video])


# combined.write_videofile("feels.mp4")






    # starttime = 10
    # if lyric_startTime <= total_lyric_second[i]:
    #     starttime = [total_lyric_second[i-1]-10, total_lyric_second[i]-10]
    #     txt_clip = TextClip(lyric[i], fontsize = 50, color = 'white', font = 'Courier').set_pos('bottom').set_duration(total_lyric_second[i+1] - total_lyric_second[i])
    #     main_clip =clip.subclip(10, total_lyric_second[i-1])
    #     next_clip = clip.subclip(total_lyric_second[i-1], total_lyric_second[i])

    #     clip_smail = CompositeVideoClip([clip, txt_clip]) 
    # if lyric_endTime <= total_lyric_second[i]:
    #     endtime = [total_lyric_second[i-1], total_lyric_second[i]]


