class Component:
    def __init__(self, x, y, layer, rotation, designator):
        self.x = x
        self.y = y
        self.layer = layer
        self.rotation = rotation
        self.designator = designator
            
class Board:
    def __init__(self, pandas_data_frame):
        self.component_list = []
        for _, row in pandas_data_frame.iterrows():
            designator = row['Designator']
            x = row['Center-X(mm)']
            y = row['Center-Y(mm)']
            layer = row['Layer']
            rotation = row['Rotation']
            
            layer = True
            if layer != "TopLayer":
                layer = False

            c = Component(x,y,layer,rotation,designator)
            self.component_list.append(c)
        self.__fill_transform_metadata__()
        

    def __fill_transform_metadata__(self):
        self.x1_mm = 136.3308 #self.component_list[0].x
        self.x2_mm = 17.8618 #self.component_list[1].x
        self.x3_mm = 31.1 #self.component_list[2].x
        
        self.y1_mm = 121.272  #self.component_list[0].y
        self.y2_mm = 24.2183 #self.component_list[1].y
        self.y3_mm = 114.575 #self.component_list[2].y

        print(f"Requested components: {self.component_list[0].designator}, {self.component_list[1].designator}, {self.component_list[2].designator}")

        #TODO: ask for self.x1,y1,x2,y2,x3,y3 here via prompt
        self.x1 = 5950
        self.y1 = 1356
        self.x2 = 2889
        self.y2 = 3876
        self.x3 = 3229
        self.y3 = 1530
