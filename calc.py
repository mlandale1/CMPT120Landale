from graphics import *
from math import *

def main():
	win = GraphWin('Simple Calculator',400,600)
	win.setBackground('slategray')
	p1 = Point(10,70)
	p2 = Point(390,10)
	display_box = Rectangle(p1,p2)
	display_box.draw(win)
	text = Text(Point(190,30),"")
	text.setStyle('italic')
	text.setSize(15)
	text.draw(win)

	p3 = Point(10,130)
	p4 = Point(60,80)
	p5 = Point(35,105)

	plus1 = Text(p5,"+")
	plus1.setStyle('italic')
	plus1.setSize(36)
	plus = Button(plus1, Rectangle(p3,p4))
	plus.drawButton(win)

	minus1 = Text(Point(95,100),"-")
	minus1.setStyle('italic')
	minus1.setSize(36)
	minus = Button(minus1, Rectangle(Point(70,130),Point(120,80)))
	minus.drawButton(win)

	times1 = Text(Point(155,115),"*")
	times1.setSize(36)
	times = Button(times1, Rectangle(Point(130,130),Point(180,80)))
	times.drawButton(win)

	divide1 = Text(Point(215,105),"/")
	divide1.setSize(36)
	divide = Button(divide1, Rectangle(Point(190,130),Point(240,80)))
	divide.drawButton(win)

	delete1 = Text(Point(335,165),"DEL")
	delete1.setStyle('italic')
	delete1.setSize(20)
	delete = Button(delete1, Rectangle(Point(310,190),Point(360,140)))
	delete.drawButton(win)

	num1_ = Text(Point(45,235),"1")
	num1_.setStyle('italic')
	num1_.setSize(36)
	num1 = Button(num1_, Rectangle(Point(10,270),Point(80,200)))
	num1.drawButton(win)

	num2_ = Text(Point(125,235),"2")
	num2_.setStyle('italic')
	num2_.setSize(36)
	num2 = Button(num2_, Rectangle(Point(90,270),Point(160,200)))
	num2.drawButton(win)

	num3_ = Text(Point(205,235),"3")
	num3_.setStyle('italic')
	num3_.setSize(36)
	num3 = Button(num3_, Rectangle(Point(170,270),Point(240,200)))
	num3.drawButton(win)

	num4_ = Text(Point(45,315),"4")
	num4_.setStyle('italic')
	num4_.setSize(36)
	num4 = Button(num4_, Rectangle(Point(10,350),Point(80,280)))
	num4.drawButton(win)

	num5_ = Text(Point(125,315),"5")
	num5_.setStyle('italic')
	num5_.setSize(36)
	num5 = Button(num5_,Rectangle(Point(90,350),Point(160,280)))
	num5.drawButton(win)

	num6_ = Text(Point(205,315),"6")
	num6_.setStyle('italic')
	num6_.setSize(36)
	num6 = Button(num6_, Rectangle(Point(170,350),Point(240,280)))
	num6.drawButton(win)

	num7_ = Text(Point(45,395),"7")
	num7_.setStyle('italic')
	num7_.setSize(36)
	num7 = Button(num7_, Rectangle(Point(10,430),Point(80,360)))
	num7.drawButton(win)

	num8_ = Text(Point(125,395),"8")
	num8_.setStyle('italic')
	num8_.setSize(36)
	num8 = Button(num8_, Rectangle(Point(90,430),Point(160,360)))
	num8.drawButton(win)

	num9_ = Text(Point(205,395),"9")
	num9_.setStyle('italic')
	num9_.setSize(36)
	num9 = Button(num9_, Rectangle(Point(170,430),Point(240,360)))
	num9.drawButton(win)

	num0_ = Text(Point(125,475),"0")
	num0_.setStyle('italic')
	num0_.setSize(36)
	num0 = Button(num0_, Rectangle(Point(90,510),Point(160,440)))
	num0.drawButton(win)

	eq = Text(Point(205,475),"=")
	eq.setStyle('italic')
	eq.setSize(36)
	eq_sign = Button(eq, Rectangle(Point(170,510),Point(240,440)))
	eq_sign.drawButton(win)

	AC = Text(Point(45,475),"AC")
	AC.setStyle('italic')
	AC.setSize(20)
	ACButton = Button(AC, Rectangle(Point(10,510),Point(80,440)))
	ACButton.drawButton(win)

	OFF = Text(Point(125,555),"OFF")
	OFF.setStyle('italic')
	OFF.setSize(20)
	OFFButton = Button(OFF, Rectangle(Point(10,590),Point(240,520)))
	OFFButton.drawButton(win)

	while True:
		click = win.getMouse()
		if num1.inside(click):
			num1.printIn(text)
		elif num2.inside(click):
			num2.printIn(text)
		elif num3.inside(click):
			num3.printIn(text)
		elif num4.inside(click):
			num4.printIn(text)
		elif num5.inside(click):
			num5.printIn(text)
		elif num6.inside(click):
			num6.printIn(text)
		elif num7.inside(click):
			num7.printIn(text)
		elif num8.inside(click):
			num8.printIn(text)
		elif num9.inside(click):
			num9.printIn(text)
		elif num0.inside(click):
			num0.printIn(text)
		elif ACButton.inside(click):
			text.setText("")
		elif divide.inside(click):
			divide.printIn(text)
		elif plus.inside(click):
			plus.printIn(text)
		elif times.inside(click):
			times.printIn(text)
		elif minus.inside(click):
			minus.printIn(text)
		elif delete.inside(click):
			text.setText(text.getText()[0:-1])
		elif eq_sign.inside(click):
			try:
				# You have to use your equation solving function
				result = eval(text.getText())
				text.setText(result)
			except:
				result = "ERROR"
				text.setText(result)
		elif OFFButton.inside(click):
			text.setText("One more click to exit")
			win.getMouse()
			win.close()


class Button(object):
	"""a collection of methods for number buttons"""

	def __init__(self, text, rect):
		"""sets the number for the button"""
		self.myText = text
		self.myRectangle = rect
		self.myString = text.getText()

	def getText(self):
		"""returns which number"""
		return self.myText

	def setText(self, newText):
		"""updates the number"""
		self.myText = newText

	def getString(self):
		"""returns the string of the button"""
		return self.myString

	def setString(self, newString):
		"""sets new string for the button"""
		self.myString = newString

	def getRectangle(self):
		"""returns which button"""
		return self.myRectangle

	def setRectangle(self, newRect):
		"""updates the button"""
		self.myRectangle = newRect

	def inside(self, point):
		"""Is the point in the rectangle"""
		# gets the lower left and upper right of the button
		ll = self.myRectangle.getP1()
		ur = self.myRectangle.getP2()
		return ll.getX() < point.getX() < ur.getX() and ur.getY() < point.getY() < ll.getY()
	
	def printIn(self, text):
		"""prints the number in the calculator"""
		text.setText(str(text.getText())+self.myString)

	def drawButton(self, window):
		self.myRectangle.draw(window)
		self.myText.draw(window)


main()