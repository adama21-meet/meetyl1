from turtle import Turtle
import turtle


class Ball(Turtle):
	def __init__(self,r,color,dx,dy):
		Turtle.__init__(self)
		self.r= r/10
		self.dx = dx
		self.dy = dy
		self.penup()
		self.color(color)
		self.shape('circle')

	def move(self,screen_width,screen_height):
			current_x=self.dx
			self.goto(screen_width,screen_height)
			new_x=current_x+(self.dx-current_x)
			current_y=self.dy
			self.goto(screen_width,screen_height)
			new_y=current_y+(self.dy-current_y)
			right_side=self.xpos+self.r
			left_side=self.xpos-self.r
			up_side=self.ypos+self.r
			down_side=self.ypos-self.r
			self.goto(new_x,new_y)

			ball_size=[right_side,left_side_up_side,down_side]

			if self.pos>ball_size:
				self.xpos=self.xpos-1
				self.ypos=self.ypos-1


me=Ball(5,'black',50,50)

