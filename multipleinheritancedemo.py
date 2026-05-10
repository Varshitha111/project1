class Camera:
    camera_mp=0
    def __init__(self,camera_mp):
        self.camera_mp=camera_mp
    def take_photo(self):
        pass
class MusicPlayer(Camera):
    brand=""
    def __init__(self,brand):
        self.brand=brand
    def play_music(self):
        pass
class SmartPhone(MusicPlayer):
    model_name=""
    def __init__(self,model_name):
        self.model_name=model_name
        super().__init__(self,camera_mp)
        super().__init__(self,brand)
    def show_details(self):
ob1=SmartPhone()
ob2=SmartPhone()