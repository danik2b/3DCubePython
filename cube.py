# import turtle module and math module
from turtle import *
import math as Math

# create a cube class
class Cube:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

        # verticies for the cube.
        self.verticies = [[-self.x, -self.y, -self.z],
                          [-self.x, -self.x, self.y],
                          [-self.x, self.y, -self.z],
                          [-self.x, self.y, self.z],
                          [self.x, -self.y, -self.z],
                          [self.x, -self.y, self.z],
                          [self.x, self.y, -self.z],
                          [self.x, self.y, self.z]]
        # edges for the cube.
        self.edges = [[0, 1],[1, 3],
                      [3, 2],[2, 0],
                      [4, 5],[5, 7],
                      [7, 6],[6, 4],
                      [0, 4],[1, 5],
                      [2, 6],[3, 7]]

    # draw all connected points.
    def drawPoints(self):
        for i in range(len(self.verticies)):
            penup()
            goto(self.verticies[i][0], self.verticies[i][1]);
            pendown()
            dot(5)

    # draw all lines connected to each of the points.
    def drawLines(self):
        for i in range(len(self.edges)):
            penup()
            goto(self.verticies[self.edges[i][0]][0], self.verticies[self.edges[i][0]][1])
            pendown()
            goto(self.verticies[self.edges[i][1]][0], self.verticies[self.edges[i][1]][1])
    #rotate the cube on the X axis.
    def rotateX(self, theta):
        for i in range(len(self.verticies)):
            self.verticies[i][1] = self.verticies[i][1] * Math.cos(theta) - self.verticies[i][2] * Math.sin(theta)
            self.verticies[i][2] = self.verticies[i][2] * Math.cos(theta) + self.verticies[i][1] * Math.sin(theta)
    #rotate the cube on the Y axis
    def rotateY(self, theta):
        for i in range(len(self.verticies)):
            self.verticies[i][0] = self.verticies[i][0] * Math.cos(theta) - self.verticies[i][2] * Math.sin(theta)
            self.verticies[i][2] = self.verticies[i][2] * Math.cos(theta) + self.verticies[i][0] * Math.sin(theta)
    #rotate the cube on the Z axis    
    def rotateZ(self, theta):
        for i in range(len(self.verticies)):
            self.verticies[i][0] = self.verticies[i][0] * Math.cos(theta) - self.verticies[i][1] * Math.sin(theta)
            self.verticies[i][1] = self.verticies[i][1] * Math.cos(theta) + self.verticies[i][0] * Math.sin(theta)
            
    def run(self):
        while True:
            #rotate on all axis
            self.rotateX(10 * 0.0001)
            self.rotateY(10 * 0.0001)
            self.rotateZ(10 * 0.0001)
            self.drawPoints() #This just draws the dots in the corners. 
            self.drawLines()
            tracer(0,0) #instantly draw, don't stutter.
            update() #update board each iteration.
            clear() #finally clear the board for next iteration.

hideturtle()
speed(0)
c1 = Cube(100, 100, 100)
c1.run()
