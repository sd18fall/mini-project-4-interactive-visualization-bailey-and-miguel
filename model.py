"""
BrickBreaker model code
"""
class Key(object):
    """ Encodes the state of a brick in the game """
    def __init__(self,height,width,x,y,name,color=(255,255,255)):
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        self.name=name
        self.color=color

    def __str__(self):
        return "Key height=%f, width=%f, x=%f, y=%f, name=%s" % (self.height,
                                                          self.width,
                                                          self.x,
                                                          self.y, self.name)
                                                           
class PianoModel(object):
    """ Encodes a model of the game state """
    def __init__(self, size):
        self.key = []
        self.width = size[0]
        self.height = size[1]
        self.key_width = 20
        self.key_height = 100
        self.key_space = 2
        y=0
        for x in range(self.key_space,
                       self.width - self.key_space - self.key_width,
                       self.key_width + self.key_space):
            #change to easier to read and manipulate, based on counter
            y=y+1
            name = "key #" + str(y)
            self.key.append(Key(self.key_height,
                                    self.key_width,
                                    x,
                                    10, name))
       

    
            
                
    def __str__(self):
        output_lines = []
        for key in self.key:
            output_lines.append(str(key))
        return "\n".join(output_lines)
    
def update(num):
    keyx=PianoModel.key[num]
    PyGameWindowView.draw((255, 0, 255), keyx)