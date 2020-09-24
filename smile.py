import arcade

def main():
    arcade.open_window(700,700,"Smile Demo")
    arcade.set_background_color(arcade.color.AFRICAN_VIOLET)
    face= arcade.create_ellipse(350,350,300,300, arcade.color.ANTIQUE_BRASS)
    points= [(250,350),(450,350),(350,425)]
    nose= arcade.create_polygon(points, arcade.color.GRANNY_SMITH_APPLE)
    eye1= arcade.create_ellipse(300,450,100,100,arcade.color.BANANA_YELLOW)
    eye2= arcade.create_ellipse(500,450,100,100,arcade.color.BANANA_YELLOW)

    arcade.start_render()
    face.draw()
    nose.draw()
    eye1.draw()
    eye2.draw()
    arcade.draw_arc_outline(350,200,200,200,arcade.color.RED_DEVIL,180,360,3)
    arcade.finish_render()

    arcade.run()
main()