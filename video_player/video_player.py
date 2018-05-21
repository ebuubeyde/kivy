#-*-coding:utf-8 -*-
from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout

class video_player(RelativeLayout):

    def __init__(self,**kwargs):
        super(video_player,self).__init__(**kwargs)
        self.video.bind(position = self.slider)
    def slider(self,ins,val):
        self.ilerleme.value = float(val) / float(ins.duration)
    def oynat(self):
        self.video.state = "play"

    def pause(self):
        self.video.state = "pause"

    def dur(self):
        self.video.state = "stop"
    def on_touch_down(self,touch):
        if self.ilerleme.collide_point(*touch.pos):
             self.video.unbind(position = self.slider)
        super(video_player,self).on_touch_down(touch)
    def on_touch_up(self,touch):
        if  self.ilerleme.collide_point(*touch.pos):
            self.video.bind(position = self.slider)
            self.video.seek(self.ilerleme.value)
        
        

class video(App):
    def build(self):
        return video_player()


if __name__ == '__main__':
    video().run()
 
