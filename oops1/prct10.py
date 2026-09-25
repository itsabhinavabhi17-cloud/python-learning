class xiomi:
    def __init__(self,camera,processor):
        self.camera=camera
        self.processor=processor
       

class vivo(xiomi):
    def __init__(self,camera,processor,zoom):
        super().__init__(camera,processor)
        self.zoom=zoom
        print(self.camera)
        
class oppo(xiomi):
    
    def __init__(self,camera,processor,coloros):
        super().__init__(camera,processor)

        self.coloros=coloros
    
        print(self.processor)

class iq(vivo,oppo):
    def __init__(self,camera,processor,zoom,coloros):
        vivo.__init__(self,zoom)
        oppo.__init__(self,coloros)
        camera=camera
        processor=processor
        print(self.zoom)
        print(self.coloros)
        

obj=iq("sony","snapdragon",200,"enhanced")
