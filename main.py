from dl_drawer import DLDrawer


def create_alex_net():
    obj = DLDrawer(width=None, height=None)

    obj.add_multi_plane_image(component_gap=5, width=227, height=227, factor=1, plane_number=3,
                              colors=["red", "green", "blue"], grid=True, grid_gap=5, grid_color="black", texts="Image",
                              line_gap=2, plane_shift=5)

    obj.add_arrow_with_text(component_gap=5, length=30, triangle_size=5, texts=[], line_gap=1)

    obj.add_cube(square_size=55, factor=2, depth=96, texts=["CONV", "F=11x11", "S=4", "Same"], angle=45,
                 color="#002366", kernel_size=5,
                 filter_color="yellow", line_gap=10, component_gap=5)

    obj.add_arrow_with_text(component_gap=5, length=30, triangle_size=5, texts=["Max", "Pool"], line_gap=1)
    """
    obj.add_cube(square_size=36, factor=2, depth=50, texts=["Pool 1","F=2x2", "S=2", "Same"], angle=45, color="#FFAA1D", kernel_size=11,
                 filter_color="yellow", line_gap=10)
    """

    obj.add_cube(square_size=27, factor=2, depth=256, texts=["CONV", "F=5x5", "S = 1", "Same"], angle=45,
                 color="#002366", kernel_size=3,
                 filter_color="yellow", line_gap=10, component_gap=5)

    obj.add_arrow_with_text(component_gap=5, length=30, triangle_size=5, texts=["Max", "Pool"], line_gap=1,
                            forced_x_change=-50)
    """
    obj.add_cube(square_size=18, factor=2, depth=50, texts=["Pool 2", "F=2x2", "S = 2", "Same"], angle=45, color="#FFAA1D", kernel_size=5,
                 filter_color="yellow", line_gap=10)
    """

    obj.add_cube(square_size=13, factor=2, depth=384, texts=["CONV", "F=3x3", "S = 1", "Same"], angle=45,
                 color="#002366", kernel_size=3,
                 filter_color="yellow", line_gap=10, component_gap=5)

    obj.add_arrow_with_text(component_gap=5, length=30, triangle_size=5, texts=[], line_gap=1, forced_x_change=-150)

    obj.add_cube(square_size=13, factor=2, depth=384, texts=["CONV", "F=3x3", "S = 1", "Same"], angle=45,
                 color="#002366", kernel_size=3,
                 filter_color="yellow", line_gap=10, component_gap=5)

    obj.add_arrow_with_text(component_gap=5, length=30, triangle_size=5, texts=["Max", "Pool"], line_gap=1,
                            forced_x_change=-100)
    """
    obj.add_cube(square_size=9, factor=2, depth=100, texts=["Pool 3", "F=2x2", "S = 2", "Same"], angle=45, color="#FFAA1D", kernel_size=3,
                 filter_color="yellow", line_gap=10)
    """

    obj.add_cube(square_size=13, factor=2, depth=256, texts=["CONV", "F=3x3", "S = 1", "Same"], angle=45,
                 color="#002366", kernel_size=2,
                 filter_color="yellow", line_gap=10, component_gap=5)

    obj.add_arrow_with_text(component_gap=5, length=30, triangle_size=5,
                            texts=["Max", "Pool", "F=2x2", "S = 2", "Same"], line_gap=1, forced_x_change=-50)
    obj.add_cube(square_size=4, factor=2, depth=90, texts=["Pool", "6x6x256"], angle=45, color="#FFAA1D",
                 kernel_size=None,
                 filter_color="yellow", line_gap=10, component_gap=5)

    obj.add_arrow_with_text(component_gap=5, length=30, triangle_size=5, texts=["Flatten"], line_gap=1)
    obj.add_rectangle(component_gap=5, width=30, height=300, color="#800020", grid=False, grid_gap=5,
                      grid_color="black",
                      circle=False, circle_color="white", cycle_gap=5, texts=["FC", "4096"])
    obj.add_arrow_with_text(component_gap=5, length=30, triangle_size=5, texts=[""], line_gap=1)
    obj.add_rectangle(component_gap=5, width=30, height=300, color="#800020", grid=False, grid_gap=5,
                      grid_color="black",
                      circle=False, circle_color="white", cycle_gap=5, texts=["FC", "4096"])
    obj.add_arrow_with_text(component_gap=5, length=30, triangle_size=5, texts=["Softmax"], line_gap=1)
    obj.add_rectangle(component_gap=5, width=30, height=100, color="#FF8A8A", grid=False, grid_gap=5,
                      grid_color="black",
                      circle=False, circle_color="white", cycle_gap=5, texts=["FC", "8"])

    obj.render("alex_net.jpg")


def create_leaf_net():

    obj = DLDrawer(width=None, height=None)

    obj.add_multi_plane_image(component_gap=5, width=227, height=227, factor=1, plane_number=3,
                              colors=["red", "green", "blue"], grid=True, grid_gap=5, grid_color="black",
                              texts="Image",
                              line_gap=2, plane_shift=5)

    obj.add_arrow_with_text(component_gap=5, length=30, triangle_size=5, texts=[], line_gap=1)

    obj.add_cube(square_size=73, factor=2, depth=50, texts=["CONV", "F=11x11", "S=3", "Same"], angle=45,
                 color="#002366", kernel_size=5,
                 filter_color="yellow", line_gap=10, component_gap=5)

    obj.add_arrow_with_text(component_gap=5, length=30, triangle_size=5, texts=["Max", "Pool"], line_gap=1)
    """
    obj.add_cube(square_size=36, factor=2, depth=50, texts=["Pool 1","F=2x2", "S=2", "Same"], angle=45, color="#FFAA1D", kernel_size=11,
                 filter_color="yellow", line_gap=10)
    """

    obj.add_cube(square_size=36, factor=2, depth=100, texts=["CONV", "F=11x11", "S = 1", "Same"], angle=45,
                 color="#002366", kernel_size=3,
                 filter_color="yellow", line_gap=10, component_gap=5)

    obj.add_arrow_with_text(component_gap=5, length=30, triangle_size=5, texts=["Max", "Pool"], line_gap=1,
                            forced_x_change=0)
    """
    obj.add_cube(square_size=18, factor=2, depth=50, texts=["Pool 2", "F=2x2", "S = 2", "Same"], angle=45, color="#FFAA1D", kernel_size=5,
                 filter_color="yellow", line_gap=10)
    """

    obj.add_cube(square_size=18, factor=2, depth=150, texts=["CONV", "F=5x5", "S = 1", "Same"], angle=45,
                 color="#002366", kernel_size=3,
                 filter_color="yellow", line_gap=10, component_gap=5)

    obj.add_arrow_with_text(component_gap=5, length=30, triangle_size=5, texts=[], line_gap=1, forced_x_change=0)

    obj.add_cube(square_size=18, factor=2, depth=100, texts=["CONV", "F=5x5", "S = 1", "Same"], angle=45,
                 color="#002366", kernel_size=3,
                 filter_color="yellow", line_gap=10, component_gap=5)

    obj.add_arrow_with_text(component_gap=5, length=30, triangle_size=5, texts=["Max", "Pool"], line_gap=1,
                            forced_x_change=0)
    """
    obj.add_cube(square_size=9, factor=2, depth=100, texts=["Pool 3", "F=2x2", "S = 2", "Same"], angle=45, color="#FFAA1D", kernel_size=3,
                 filter_color="yellow", line_gap=10)
    """

    obj.add_cube(square_size=9, factor=2, depth=90, texts=["CONV", "F=3x3", "S = 1", "Same"], angle=45,
                 color="#002366", kernel_size=2,
                 filter_color="yellow", line_gap=10, component_gap=5)

    obj.add_arrow_with_text(component_gap=5, length=30, triangle_size=5,
                            texts=["Max", "Pool", "F=2x2", "S = 2", "Same"], line_gap=1, forced_x_change=0)
    obj.add_cube(square_size=4, factor=2, depth=90, texts=["Pool", "4x4x90"], angle=45, color="#FFAA1D",
                 kernel_size=None,
                 filter_color="yellow", line_gap=10, component_gap=5)

    obj.add_arrow_with_text(component_gap=5, length=30, triangle_size=5, texts=["Flatten"], line_gap=1)
    obj.add_rectangle(component_gap=5, width=30, height=250, color="#800020", grid=False, grid_gap=5,
                      grid_color="black",
                      circle=False, circle_color="white", cycle_gap=5, texts=["FC", "800"])
    obj.add_arrow_with_text(component_gap=5, length=30, triangle_size=5, texts=[""], line_gap=1)
    obj.add_rectangle(component_gap=5, width=30, height=250, color="#800020", grid=False, grid_gap=5,
                      grid_color="black",
                      circle=False, circle_color="white", cycle_gap=5, texts=["FC", "800"])
    obj.add_arrow_with_text(component_gap=5, length=30, triangle_size=5, texts=["Soft","max"], line_gap=1)
    obj.add_rectangle(component_gap=5, width=30, height=80, color="#FF8A8A", grid=False, grid_gap=5,
                      grid_color="black",
                      circle=False, circle_color="white", cycle_gap=5, texts=["FC", "8"])

    obj.render("leaf_net.jpg")
    print("done")



def create_vgg16_net():
    obj = DLDrawer(width=None, height=None)

    obj.add_multi_plane_image(component_gap=5, width=227, height=227, factor=0.5, plane_number=3,
                              colors=["red", "green", "blue"], grid=True, grid_gap=5, grid_color="black", texts="Image",
                              line_gap=2, plane_shift=5)

    obj.add_arrow_with_text(component_gap=5, length=30, triangle_size=5, texts=[], line_gap=1)

    obj.add_cube(square_size=227, factor=0.5, depth=64, texts=[], angle=45,
                 color="#002366", kernel_size=None,
                 filter_color="yellow", line_gap=10, component_gap=5)
    obj.add_cube(square_size=227, factor=0.5, depth=64, texts=[], angle=45,
                 color="#002366", kernel_size=None,
                 filter_color="yellow", line_gap=10, component_gap=-30)
    obj.add_cube(square_size=227, factor=0.5, depth=64, texts=[], angle=45,
                 color="#002366", kernel_size=None,
                 filter_color="yellow", line_gap=10, component_gap=-30)

    obj.add_arrow_with_text(component_gap=5, length=30, triangle_size=5, texts=[], line_gap=1)
    """
    obj.add_cube(square_size=36, factor=2, depth=50, texts=["Pool 1","F=2x2", "S=2", "Same"], angle=45, color="#FFAA1D", kernel_size=11,
                 filter_color="yellow", line_gap=10)
    """

    obj.add_cube(square_size=113, factor=0.5, depth=128, texts=[], angle=45,
                 color="#002366", kernel_size=None,
                 filter_color="yellow", line_gap=10, component_gap=5)
    obj.add_cube(square_size=113, factor=0.5, depth=128, texts=[], angle=45,
                 color="#002366", kernel_size=None,
                 filter_color="yellow", line_gap=10, component_gap=-80)

    obj.add_arrow_with_text(component_gap=5, length=30, triangle_size=5, texts=[], line_gap=1,
                            forced_x_change=-30)
    """
    obj.add_cube(square_size=18, factor=2, depth=50, texts=["Pool 2", "F=2x2", "S = 2", "Same"], angle=45, color="#FFAA1D", kernel_size=5,
                 filter_color="yellow", line_gap=10)
    """

    obj.add_cube(square_size=56, factor=0.5, depth=256, texts=[], angle=45,
                 color="#002366", kernel_size=None,
                 filter_color="yellow", line_gap=10, component_gap=5)
    obj.add_cube(square_size=56, factor=0.5, depth=256, texts=[], angle=45,
                 color="#002366", kernel_size=None,
                 filter_color="yellow", line_gap=10, component_gap=-170)
    obj.add_cube(square_size=56, factor=0.5, depth=256, texts=[], angle=45,
                 color="#002366", kernel_size=None,
                 filter_color="yellow", line_gap=10, component_gap=-170)

    obj.add_arrow_with_text(component_gap=5, length=30, triangle_size=5, texts=[], line_gap=1, forced_x_change=-120)

    obj.add_cube(square_size=28, factor=0.5, depth=512, texts=[], angle=45,
                 color="#002366", kernel_size=None,
                 filter_color="yellow", line_gap=10, component_gap=5)
    obj.add_cube(square_size=28, factor=0.5, depth=512, texts=[], angle=45,
                 color="#002366", kernel_size=None,
                 filter_color="yellow", line_gap=10, component_gap=-350)
    obj.add_cube(square_size=28, factor=0.5, depth=512, texts=[], angle=45,
                 color="#002366", kernel_size=None,
                 filter_color="yellow", line_gap=10, component_gap=-350)

    obj.add_arrow_with_text(component_gap=5, length=30, triangle_size=5, texts=[], line_gap=1,
                            forced_x_change=-300)
    """
    obj.add_cube(square_size=9, factor=2, depth=100, texts=["Pool 3", "F=2x2", "S = 2", "Same"], angle=45, color="#FFAA1D", kernel_size=3,
                 filter_color="yellow", line_gap=10)
    """

    obj.add_cube(square_size=14, factor=0.5, depth=512, texts=[], angle=45,
                 color="#002366", kernel_size=None,
                 filter_color="yellow", line_gap=10, component_gap=5)
    obj.add_cube(square_size=14, factor=0.5, depth=512, texts=[], angle=45,
                 color="#002366", kernel_size=None,
                 filter_color="yellow", line_gap=10, component_gap=-350)
    obj.add_cube(square_size=14, factor=0.5, depth=512, texts=[], angle=45,
                 color="#002366", kernel_size=None,
                 filter_color="yellow", line_gap=10, component_gap=-350)

    obj.add_arrow_with_text(component_gap=5, length=30, triangle_size=5, texts=["Flatten"], line_gap=1, forced_x_change=-130)
    obj.add_rectangle(component_gap=5, width=30, height=300, color="#800020", grid=False, grid_gap=5,
                      grid_color="black",
                      circle=False, circle_color="white", cycle_gap=5, texts=["FC", "4096"])
    obj.add_arrow_with_text(component_gap=5, length=30, triangle_size=5, texts=[""], line_gap=1)
    obj.add_rectangle(component_gap=5, width=30, height=300, color="#800020", grid=False, grid_gap=5,
                      grid_color="black",
                      circle=False, circle_color="white", cycle_gap=5, texts=["FC", "4096"])
    obj.add_arrow_with_text(component_gap=5, length=30, triangle_size=5, texts=["Softmax"], line_gap=1)
    obj.add_rectangle(component_gap=5, width=30, height=100, color="#FF8A8A", grid=False, grid_gap=5,
                      grid_color="black",
                      circle=False, circle_color="white", cycle_gap=5, texts=["FC", "8"])

    obj.render("vgg16_net.jpg")


#create_alex_net()
#create_leaf_net()
create_vgg16_net()