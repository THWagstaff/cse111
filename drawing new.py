import tkinter as tk


def main():
    # The width and height of the scene window.
    width = 800
    height = 500

    # Create the Tk root object.
    root = tk.Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()


def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    """Draw a scene in the canvas. scene_left, scene_top,
    scene_right, and scene_bottom contain the extent in
    pixels of the region where the scene should be drawn.
    Parameters
        scene_left: left side of the region; less than scene_right
        scene_top: top of the region; less than scene_bottom
        scene_right: right side of the region
        scene_bottom: bottom of the region
    Return: nothing

    If needed, the width and height of the
    region can be calculated like this:
    scene_width = scene_right - scene_left + 1
    scene_height = scene_bottom - scene_top + 1
    """
    # Call your functions here, such as draw_sky, draw_ground,
    # draw_snowman, draw_tree, draw_shrub, etc.
    
    draw_sky(canvas)
    draw_ground(canvas)
    draw_cloud(canvas)
    draw_sun(canvas)
    tree_center = scene_left + 500
    tree_top = scene_top + 100
    tree_height = 150
    draw_grass(canvas)
    draw_pine_tree(canvas, tree_center, tree_top, tree_height)
    draw_teton(canvas)
    create_text(canvas)
    


# Define more functions here, like draw_sky, draw_ground,
# draw_cloud, draw_tree, draw_kite, draw_snowflake, etc.


def draw_sky(canvas):
    sky_x1 = 0
    sky_y1 = 0
    sky_x2 = 800
    sky_y2 = 300
    canvas.create_rectangle(sky_x1,sky_y1,sky_x2,sky_y2, fill="skyBlue2")
    
def draw_ground(canvas):
    g_x1 = 0
    g_y1 = 300
    g_x2 = 800
    g_y2 = 500
    canvas.create_rectangle(g_x1,g_y1,g_x2,g_y2, fill="darkGreen")

def draw_cloud(canvas):
    c_x1 = 50
    c_y1 = 80
    c_x2 = 290
    c_y2 = 140
    canvas.create_oval(c_x1,c_y1,c_x2,c_y2, fill="mintCream", outline="mintCream")
    canvas.create_oval(c_x1 * 2,c_y1/1.3,c_x2,c_y2 * 1.1, fill="mintCream", outline="mintCream")
    canvas.create_oval(c_x1*1.1,c_y1*1.1,c_x2*1.1,c_y2, fill="mintCream", outline="mintCream")

def draw_sun(canvas):
    s_x1 = 700
    s_y1 = 40
    s_x2 = 760
    s_y2 = 100
    canvas.create_oval(s_x1,s_y1,s_x2,s_y2, fill="gold", outline="gold")

def draw_pine_tree(canvas, peak_x, peak_y, height):
    """Draw a single pine tree.
    Parameters
        canvas: The tkinter canvas where this
            function will draw a pine tree.
        peak_x, peak_y: The x and y location in pixels where
            this function will draw the top peak of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    """
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = peak_x - trunk_width / 2
    trunk_right = peak_x + trunk_width / 2
    trunk_bottom = peak_y + height + 50

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = peak_x - skirt_width / 2
    skirt_right = peak_x + skirt_width / 2
    skirt_bottom = peak_y + skirt_height


    # Draw the trunk of the pine tree.
    canvas.create_rectangle(trunk_left-30, skirt_bottom+30,
            trunk_right+30, trunk_bottom+30,
            outline="gray20", width=1, fill="BurlyWood3")

    # Draw the crown (also called skirt) of the pine tree.
    canvas.create_polygon(peak_x, (peak_y*1.85)+30,
            skirt_right, skirt_bottom+30,
            skirt_left, skirt_bottom+30,
            outline="gray20", width=1, fill="SaddleBrown")
    
def draw_grass(canvas):
    for i in range(300,500,50):
        scene_left = 0
        scene_right = 800
        canvas.create_line(scene_left,i,scene_right,i,width=10, fill="ForestGreen")
    for i in range(0,800,50):
        scene_top = 300
        scene_bottom = 800
        canvas.create_line(i,scene_top,i,scene_bottom,width=10, fill="SpringGreen4")
    #50 = grid range
def draw_teton(canvas):
    mount_x = 200
    mount_y = 100
    mount_right = 290
    mount_left = 110
    mount_bottom = 300

    
    canvas.create_polygon(mount_x-90, mount_y+50,
            mount_right-90, mount_bottom,
            mount_left-90, mount_bottom,
            outline="gray20", width=2, fill="grey77")
    canvas.create_polygon(mount_x+110, mount_y+60,
            mount_right+110, mount_bottom,
            mount_left+110, mount_bottom,
            outline="gray20", width=2, fill="grey77")
    canvas.create_polygon(mount_x, mount_y,
            mount_right, mount_bottom,
            mount_left, mount_bottom,
            outline="gray20", width=2, fill="grey77")
def create_text(canvas):
    canvas.create_text(600,20,text="Welcome To the Tetons!", font=76,fill="white")

# Call the main function so that
# this program will start executing.
main()