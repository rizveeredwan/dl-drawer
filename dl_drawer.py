import math
import os
from PIL import Image, ImageDraw
from math import sin, cos, tan, pi
from PIL import ImageFont


class DLDrawer:
    def __init__(self, width=None, height=None, fontsize=20, stx=10, sty=500):
        # module for deep learning drawing
        if width is None:
            width = 3000
        if height is None:
            height = 1000
        self.width = width
        self.height = height
        self.fontsize = fontsize

        # creating new Image object: Temp
        self.img = Image.new("RGB", (self.width, self.height), 'white')
        self.img1 = ImageDraw.Draw(self.img)

        self.font = ImageFont.truetype(os.path.join("open-sans", "OpenSans-Bold.ttf"), self.fontsize)

        self.startx = stx
        self.starty = sty
        self.currentx = stx
        self.currenty = sty
        self.text_aligny = None

        # storing all the components
        self.components = []

        self.minx, self.miny, self.maxx, self.maxy = stx, sty, stx, sty

    def draw_cube(self, stx, sty, width, height, factor, depth, texts=None, angle=30, color="grey", kernel_size=None,
                  filter_color="yellow", line_gap=10, recursion=0):
        # bottom point in sent
        width_factor = width*factor
        height_factor = height*factor
        theta = angle * math.pi / 180.0
        x = stx
        y = sty - height_factor
        r1 = [(x, y), (x + width_factor, y), (x + width_factor, y + height_factor), (x, y + height_factor)]  # front
        r2 = [(x + depth * sin(theta), y - depth * cos(theta)),  # back
              (x + width_factor + depth * sin(theta), y - depth * cos(theta)),
              (x + width_factor + depth * sin(theta), y + height_factor - depth * cos(theta)),
              (x + depth * sin(theta), y + height_factor - depth * cos(theta))]
        self.img1.polygon(r2, fill=color, outline="black")
        self.img1.polygon(r1, fill=color, outline="black")
        self.img1.polygon([r1[0], r2[0], r2[1], r1[1]], fill=color, outline="black")
        self.img1.polygon([r1[1], r2[1], r2[2], r1[2]], fill=color, outline="black")
        # calculating minx, maxx, miny, maxy
        for i in range(0, len(r1)):
            self.minx = min(self.minx, r1[i][0])
            self.miny = min(self.miny, r1[i][1])
            self.maxx = max(self.maxx, r1[i][0])
            self.maxy = max(self.maxy, r1[i][1])
        for i in range(0, len(r2)):
            self.minx = min(self.minx, r2[i][0])
            self.miny = min(self.miny, r2[i][1])
            self.maxx = max(self.maxx, r2[i][0])
            self.maxy = max(self.maxy, r2[i][1])
        # text align
        if self.text_aligny is None:
            self.text_aligny = math.ceil((r2[0][1] + r2[2][1]) / 2.0)
        # setting up filter/filter text
        _filter = None
        sidex, sidey = r2[2][0], r1[2][1]
        startx, starty = r1[3][0], r1[3][1]
        if kernel_size is not None:
            assert (recursion == 1)
            # work with recursion
            """
            _filter = [(r1[0][0] + (sq / 4.0), r1[0][1] + (sq / 4.0)),
                       (r1[0][0] + (sq / 4.0) + kernel_size, r1[0][1] + (sq / 4.0) + kernel_size)]
            self.img1.rectangle(_filter, fill=filter_color, outline="black")
            """

            self.draw_cube(stx=r1[3][0] + (width_factor / 4.0), sty=r1[3][1] - (height_factor / 4.0),
                           width=kernel_size, height=kernel_size, factor=factor,
                           depth=depth, texts=None, angle=angle, color=filter_color, kernel_size=None,
                           filter_color=filter_color, line_gap=line_gap, recursion=0)

            feature_map = str(height) + "x" + str(width) + "x" + str(depth)
            self.img1.text((startx, starty + line_gap), feature_map, fill="black", font=self.font)
            bbox = self.img1.textbbox((startx, starty + line_gap), feature_map, font=self.font)
            starty = bbox[3]
            sidex = max(bbox[2], sidex)
            sidey = max(bbox[3], sidey)
            self.maxx = max(self.maxx, bbox[2])
            self.minx = min(self.minx, bbox[0])
            self.maxy = max(self.maxy, bbox[3])
            self.miny = min(self.miny, bbox[1])
        # setting up name
        if texts is not None:
            if type(texts) == str:
                self.img1.text((startx, starty + line_gap), texts, fill="black", font=self.font)
                bbox = self.img1.textbbox((startx, starty + line_gap), texts, font=self.font)
                sidex = max(bbox[2], sidex)
                sidey = max(bbox[3], sidey)
                self.maxx = max(self.maxx, bbox[2])
                self.minx = min(self.minx, bbox[0])
                self.maxy = max(self.maxy, bbox[3])
                self.miny = min(self.miny, bbox[1])
            elif type(texts) == list:
                _x = self.write_text(stx=startx, sty=starty + line_gap, texts=texts, line_gap=line_gap)
                # calculating maxy, miny for sidey
                tx, ty = startx, starty + line_gap
                for i in range(0, len(texts)):
                    bbox = self.img1.textbbox((tx, ty), texts[i], font=self.font)
                    sidex = max(bbox[2], sidex)
                    sidey = max(bbox[3], sidey)
                    self.maxx = max(self.maxx, bbox[2])
                    self.minx = min(self.minx, bbox[0])
                    self.maxy = max(self.maxy, bbox[3])
                    self.miny = min(self.miny, bbox[1])
                    ty = bbox[3]+line_gap

        # adding the components to call
        self.components.append(["cube", stx, sty, width, height, factor, depth, texts, angle, color, kernel_size,
                                filter_color, line_gap, recursion])
        # print(self.components[-1])
        return sidex, sidey, _filter

    def draw_arrow(self, stx, sty, length, triangle_size=1, color="black", texts=[], line_gap=10):
        assert (length > 1)
        assert (1 <= triangle_size < length)
        self.img1.line([(stx, sty), (stx + length, sty)], fill="black", width=5)
        t = [(stx + length, sty), (stx + length - triangle_size, sty - triangle_size),
             (stx + length - triangle_size, sty + triangle_size)]
        # draw arrow
        self.components.append(
            ["arrow", stx, sty, length, triangle_size, color, texts, line_gap]
        )
        self.img1.polygon(t, fill=color, outline="black")
        best_width = stx + length
        # update maxx
        self.maxx = max(self.maxx, t[1][0])
        return best_width, sty + triangle_size

    def draw_rectangle(self, stx, sty, width, height, color, grid=False, grid_gap=5, grid_color="black", circle=False,
                       circle_color="white",
                       cycle_gap=5, texts=None, line_gap=5):
        # bottom point is sent
        x = stx
        y = sty - height
        r1 = [(x, y), (x + width, sty)]
        # update minx maxx miny maxy
        self.minx = min(self.minx, x)
        self.maxx = max(self.maxx, x + width)
        self.miny = min(self.miny, y)
        self.maxy = max(self.maxy, sty)
        self.img1.rectangle(r1, fill=color, outline="black")
        if self.text_aligny is None:
            self.text_aligny = math.ceil((sty + y) / 2.0)
        if grid is True:
            i = y
            while i < (y+height):
                self.img1.line([(x, i), (x + width, i)], fill=grid_color)
                i += grid_gap
            i = x
            while i < x+width:
                self.img1.line([(i, y), (i, y + height)], fill=grid_color)
                i += grid_gap
        if circle is True:
            cnt = 0
            i = y
            while i < (y + height):
                cnt += 1
                if cnt <= 3:
                    if (i + width) <= (y + height):
                        self.img1.ellipse([(x, i), (x + width, i + width)], fill=circle_color, outline="black")
                    i = i + width + cycle_gap
                else:
                    self.img1.text((x + width / 2.0, i), ".", fill="black", font=self.font)
                    bbox = self.img1.textbbox((x + width / 2.0, i), texts, font=self.font)
                    i = bbox[3] + line_gap
                    """
                    if (i + width / 2.0) <= (y + height):
                        self.img1.ellipse([(x + 0.25 * width, i), (x + 0.75 * width, i + width / 2.0)],
                                          fill=circle_color,
                                          outline="black")
                    i = i + width / 2.0 + cycle_gap
                    """
            # circle last one
            self.img1.ellipse([(x, y + height - width), (x + width, y + height)], fill=circle_color, outline="black")

        sidex, sidey = x + width, sty
        if texts is not None:
            if type(texts) is str: # single line text or multiple line string
                texts = [texts]
            _x = self.write_text(stx=x, sty=sty+line_gap, texts=texts, line_gap=line_gap)
            sidex = max(sidex, _x)
        self.components.append(['rectangle', stx, sty, width, height, color, grid, grid_gap, grid_color, circle,
                                circle_color, cycle_gap, texts, line_gap, texts, line_gap])
        return sidex

    def write_text(self, stx, sty, texts, line_gap=1):
        # upper point is sent
        # https://stackoverflow.com/questions/43060479/how-to-get-the-font-pixel-height-using-pils-imagefont-class
        # [ABC, DEF, GHI]
        # each in separate line
        maxx = stx
        x, y = stx, sty
        for i in range(0, len(texts)):
            self.img1.text((x, y), texts[i], fill="black", font=self.font)
            bbox = self.img1.textbbox((x, y), texts[i], font=self.font)
            # print(bbox)
            x = bbox[0]
            y = bbox[3] + line_gap
            maxx = max(maxx, bbox[2])
            self.maxx = max(self.maxx, bbox[2])
            self.minx = min(self.minx, bbox[0])

            self.maxy = max(self.maxy, bbox[3])
            self.miny = min(self.miny, bbox[1])
        self.components.append([
            'text', stx, sty, texts, line_gap
        ])
        return maxx

    def negative_shift(self):
        min_y_value = None
        f = False
        if self.miny < 0:
            f = True
            min_y_value = abs(self.miny) + 20
            self.miny = 0
        if f is True:
            for i in range(0, len(self.components)):
                self.components[i][2] += abs(min_y_value)
                self.maxy = max(self.maxy, self.components[i][2])

    def render(self, file_name=None):
        self.negative_shift()
        # creating new Image object: Temp
        self.width = math.ceil(self.maxx) + 100
        self.height = math.ceil(self.maxy) + 100
        print(self.width, self.height)
        del self.img
        self.img = Image.new("RGB", (self.width, self.height), 'white')
        self.img1 = ImageDraw.Draw(self.img)
        for i in range(0, len(self.components)):
            if self.components[i][0] == 'cube':
                self.draw_cube(stx=self.components[i][1], sty=self.components[i][2], width=self.components[i][3], height=self.components[i][4],
                               factor=self.components[i][5], depth=self.components[i][6], texts=self.components[i][7],
                               angle=self.components[i][8], color=self.components[i][9],
                               kernel_size=self.components[i][10], filter_color=self.components[i][11],
                               line_gap=self.components[i][12], recursion=self.components[i][13])
            if self.components[i][0] == "text":
                self.write_text(stx=self.components[i][1], sty=self.components[i][2], texts=self.components[i][3],
                                line_gap=self.components[i][4])
            if self.components[i][0] == "arrow":
                self.draw_arrow(stx=self.components[i][1], sty=self.components[i][2], length=self.components[i][3],
                                triangle_size=self.components[i][4], color=self.components[i][5],
                                texts=self.components[i][6], line_gap=self.components[i][7])
            if self.components[i][0] == "rectangle":
                self.draw_rectangle(stx=self.components[i][1], sty=self.components[i][2], width=self.components[i][3],
                                    height=self.components[i][4], color=self.components[i][5],
                                    grid=self.components[i][6], grid_gap=self.components[i][7],
                                    grid_color=self.components[i][8], circle=self.components[i][9],
                                    circle_color=self.components[i][10], cycle_gap=self.components[i][11],
                                    texts=self.components[i][12], line_gap=self.components[i][13])
        self.img.show()
        if file_name is None:
            file_name = "name.jpg"
        elif file_name.lower().endswith('.jpg') or file_name.lower().endswith('.png') or file_name.lower().endswith('.jpeg'):
            pass
        else:
            print("File name invalid, saving as name.jpg")
            file_name = "name.jpg"
        self.img.save(os.path.join(file_name))

    def add_cube(self, width=40, height=40, factor=2, depth=100, texts="CONV 1", angle=45, color="grey", kernel_size=11,
                 filter_color="yellow", line_gap=10, component_gap=10, forced_x_change=0, forced_y_change=0):
        recursion = 0
        if kernel_size is not None:
            recursion = 1
        _x, _y, _filter = self.draw_cube(stx=self.currentx + component_gap + forced_x_change, sty=self.currenty + forced_y_change,
                                         width=width, height=height,
                                         factor=factor, depth=depth, texts=texts, angle=angle, color=color,
                                         kernel_size=kernel_size, filter_color=filter_color, line_gap=line_gap,
                                         recursion=recursion)
        self.currentx = math.ceil(_x)

    def add_text(self, component_gap=10, texts=[], line_gap=1, forced_x_change=0, forced_y_change=0):
        if self.text_aligny is None:
            self.text_aligny = self.currenty
        _x = self.write_text(stx=self.currentx + component_gap+forced_x_change, sty=self.text_aligny+forced_y_change, texts=texts, line_gap=line_gap)
        self.currentx = math.ceil(_x)

    def add_arrow_with_text(self, component_gap=10, length=30, triangle_size=1, texts=[], line_gap=1, forced_x_change=0, forced_y_change=0):
        if self.text_aligny is None:
            self.text_aligny = self.currenty
        _x1, _y = self.draw_arrow(stx=self.currentx + component_gap+forced_x_change, sty=self.text_aligny+forced_y_change,
                                  length=length, triangle_size=triangle_size, color="black", texts=[],
                                  line_gap=line_gap)
        if len(texts) > 0:
            _x = self.write_text(stx=self.currentx + component_gap+forced_x_change, sty=_y + line_gap+forced_y_change, texts=texts, line_gap=line_gap)
            _x1 = max(_x1, _x)
        self.currentx = math.ceil(_x1)
        return self.currentx

    def add_rectangle(self, component_gap=10, width=100, height=100, color="red", grid=False, grid_gap=5,
                      grid_color="black", circle=False, circle_color="white", cycle_gap=5, texts="FC", line_gap=2, forced_x_change=0, forced_y_change=0):
        _x = self.draw_rectangle(stx=self.currentx + component_gap + forced_x_change, sty=self.currenty+forced_y_change, width=width, height=height,
                                 color=color, grid=grid, grid_gap=grid_gap, grid_color=grid_color, circle=circle,
                                 circle_color=circle_color, cycle_gap=cycle_gap, texts=texts, line_gap=line_gap)
        self.currentx = _x
        return

    def add_multi_plane_image(self, component_gap=10, width=100, height=100, factor=1, plane_number=3, colors=[],
                              grid=False, grid_gap=5,
                              grid_color="black", texts="Image", line_gap=2, plane_shift=5, forced_x_change=0, forced_y_change=0):
        if len(colors) == plane_number:  # each plane's color is defined
            pass
        else:  # 2 color rotation apply
            colors = []
            for i in range(0, plane_number):
                if i % 2 == 0:
                    colors.append('grey')
                else:
                    colors.append('white')
        j = 0
        value = 0
        for i in range(plane_number - 1, -1, -1):
            written_name = None
            if i == 0 and texts is not None:
                written_name = texts
            _x = self.draw_rectangle(stx=self.currentx + component_gap + plane_shift * j + forced_x_change,
                                     sty=self.currenty + plane_shift * j + forced_y_change, width=width * factor, height=height * factor,
                                     color=colors[i], grid=grid, grid_gap=grid_gap, grid_color=grid_color,
                                     texts=written_name, line_gap=line_gap)
            if i == 0:
                self.currentx = _x
            value = value + self.currenty + plane_shift * j
            j += 1
        if self.text_aligny is None:
            self.text_aligny = value
        return


