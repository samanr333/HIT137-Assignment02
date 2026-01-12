# https://docs.python.org/3/library/turtle.html
import turtle
# Main Function
def main():
    # Ask the user how they want their shape to look
    no_of_sides = int(input("Enter the number of sides: "))
    side_length = int(input("Enter the side length: "))      
    recursuion_depth = int(input("Enter the recursion depth: "))
 
    # Making the drawing speed faster
    turtle.speed(0)
 
    # Lift the pen and move the turtle to a good starting spot
    turtle.penup()
    turtle.goto(-side_length/2, side_length/2)
    turtle.pendown()
 
    # Drawing each side of the shape
    for i in range(no_of_sides):
        draw_side(side_length, recursuion_depth)
        # Turning  the turtle to get ready for the next side
        turtle.right(360 / no_of_sides)
 
    # Keeping the window open for display
    turtle.done()
    
if __name__ == "__main__":
    main()