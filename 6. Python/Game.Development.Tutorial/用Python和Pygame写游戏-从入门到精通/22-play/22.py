# -*- coding: utf-8 -*-
# 注意文件编码也必须是utf-8
SCREEN_SIZE = (800, 600)
# 存放音乐文件的位置
MUSIC_PATH = "./MUSIC"
 
import pygame
from pygame.locals import *
from math import sqrt
import os
import os.path
 
def get_music(path):
 
    # 从文件夹来读取所有的音乐文件
    raw_filenames = os.listdir(path)
 
    music_files = []
    for filename in raw_filenames:
        # 不是Windows的话，还是去掉mp3吧
        if filename.lower().endswith('.ogg') or filename.lower().endswith('.mp3'):
            music_files.append(os.path.join(MUSIC_PATH, filename))
 
    return sorted(music_files)
 
class Button(object):
    """这个类是一个按钮，具有自我渲染和判断是否被按上的功能"""
    def __init__(self, image_filename, position):
 
        self.position = position
        self.image = pygame.image.load(image_filename)
 
    def render(self, surface):
        # 家常便饭的代码了
        x, y = self.position
        w, h = self.image.get_size()
        x -= w / 2
        y -= h / 2
        surface.blit(self.image, (x, y))
 
    def is_over(self, point):
        # 如果point在自身范围内，返回True
        point_x, point_y = point
        x, y = self.position
        w, h = self.image.get_size()
        x -= w /2
        y -= h / 2
 
        in_x = point_x >= x and point_x < x + w
        in_y = point_y >= y and point_y < y + h
        return in_x and in_y
 
def run():
 
    pygame.mixer.pre_init(44100, 16, 2, 1024*4)
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE, 0)     
 
    #font = pygame.font.SysFont("default_font", 50, False)
    # 为了显示中文，我这里使用了这个字体，具体自己机器上的中文字体请自己查询
    # 详见本系列第四部分：http://eyehere.net/2011/python-pygame-novice-professional-4/
    font = pygame.font.SysFont("simsunnsimsun", 50, False)    
 
    x = 100
    y = 240
    button_width = 150
    buttons = {}
    buttons["prev"] = Button("prev.png", (x, y))
    buttons["pause"] = Button("pause.png", (x+button_width*1, y))
    buttons["stop"] = Button("stop.png", (x+button_width*2, y))
    buttons["play"] = Button("play.png", (x+button_width*3, y))
    buttons["next"] = Button("next.png", (x+button_width*4, y))
 
    music_filenames = get_music(MUSIC_PATH)
    if len(music_filenames) == 0:
        print "No music files found in ", MUSIC_PATH
        return
 
    white = (255, 255, 255)
    label_surfaces = []
    # 一系列的文件名render
    for filename in music_filenames:
        txt = os.path.split(filename)[-1]
        print "Track:", txt
        # 这是简体中文Windows下的文件编码，根据自己系统情况请酌情更改
        txt = txt.split('.')[0].decode('gb2312')
        surface = font.render(txt, True, (100, 0, 100))
        label_surfaces.append(surface)
 
    current_track = 0
    max_tracks = len(music_filenames)
    pygame.mixer.music.load( music_filenames[current_track] )  
 
    clock = pygame.time.Clock()
    playing = False
    paused = False
 
    # USEREVENT是什么？请参考本系列第二部分：
    # http://eyehere.net/2011/python-pygame-novice-professional-2/
    TRACK_END = USEREVENT + 1
    pygame.mixer.music.set_endevent(TRACK_END)
 
    while True:
 
        button_pressed = None
 
        for event in pygame.event.get():
 
            if event.type == QUIT:
                return
 
            if event.type == MOUSEBUTTONDOWN:
 
                # 判断哪个按钮被按下
                for button_name, button in buttons.iteritems():
                    if button.is_over(event.pos):
                        print button_name, "pressed"
                        button_pressed = button_name
                        break
 
            if event.type == TRACK_END:
                # 如果一曲播放结束，就“模拟”按下"next"
                button_pressed = "next"
 
        if button_pressed is not None:
 
            if button_pressed == "next":
                current_track = (current_track + 1) % max_tracks
                pygame.mixer.music.load( music_filenames[current_track] )
                if playing:
                    pygame.mixer.music.play()
 
            elif button_pressed == "prev":
 
                # prev的处理方法：
                # 已经播放超过3秒，从头开始，否则就播放上一曲
                if pygame.mixer.music.get_pos() > 3000:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.play()
                else:
                    current_track = (current_track - 1) % max_tracks
                    pygame.mixer.music.load( music_filenames[current_track] )
                    if playing:
                        pygame.mixer.music.play()
 
            elif button_pressed == "pause":
                if paused:
                    pygame.mixer.music.unpause()
                    paused = False
                else:
                    pygame.mixer.music.pause()
                    paused = True
 
            elif button_pressed == "stop":
                pygame.mixer.music.stop()
                playing = False
 
            elif button_pressed == "play":
                if paused:
                    pygame.mixer.music.unpause()
                    paused = False
                else:
                    if not playing:
                        pygame.mixer.music.play()
                        playing = True
 
        screen.fill(white)
 
        # 写一下当前歌名
        label = label_surfaces[current_track]
        w, h = label.get_size()
        screen_w = SCREEN_SIZE[0]
        screen.blit(label, ((screen_w - w)/2, 450))
 
        # 画所有按钮
        for button in buttons.values():
            button.render(screen)
 
        # 因为基本是不动的，这里帧率设的很低
        clock.tick(5)
        pygame.display.update()
 
if __name__ == "__main__":
 
    run()
