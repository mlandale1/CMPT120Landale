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
    plus = Rectangle(p3,p4)
    plus.draw(win)
    p5 = Point(35,105)
    plus1 = Text(p5,"+")
    plus1.setStyle('italic')
    plus1.setSize(36)
    plus1.draw(win)

    minus = Rectangle(Point(70,130),Point(120,80))
    minus.draw(win)
    minus1 = Text(Point(95,105),"-")
    minus1.setStyle('italic')
    minus1.setSize(36)
    minus1.draw(win)

    times = Rectangle(Point(130,130),Point(180,80))
    times.draw(win)
    times1 = Text(Point(155,105),"×")
    times1.setStyle('italic')
    times1.setSize(36)
    times1.draw(win)

    divide = Rectangle(Point(190,130),Point(240,80))
    divide.draw(win)
    divide1 = Text(Point(215,105),"÷")
    divide1.setStyle('italic')
    divide1.setSize(36)
    divide1.draw(win)

    delete = Rectangle(Point(310,190),Point(360,140))
    delete.draw(win)
    delete1 = Text(Point(335,165),"DEL")
    delete1.setStyle('italic')
    delete1.setSize(20)
    delete1.draw(win)

    num1 = Rectangle(Point(10,270),Point(80,200))
    num1.draw(win)
    num1_ = Text(Point(45,235),"1")
    num1_.setStyle('italic')
    num1_.setSize(36)
    num1_.draw(win)

    num2 = Rectangle(Point(90,270),Point(160,200))
    num2.draw(win)
    num2_ = Text(Point(125,235),"2")
    num2_.setStyle('italic')
    num2_.setSize(36)
    num2_.draw(win)

    num3 = Rectangle(Point(170,270),Point(240,200))
    num3.draw(win)
    num3_ = Text(Point(205,235),"3")
    num3_.setStyle('italic')
    num3_.setSize(36)
    num3_.draw(win)

    num4 = Rectangle(Point(10,350),Point(80,280))
    num4.draw(win)
    num4_ = Text(Point(45,315),"4")
    num4_.setStyle('italic')
    num4_.setSize(36)
    num4_.draw(win)

    num5 = Rectangle(Point(90,350),Point(160,280))
    num5.draw(win)
    num5_ = Text(Point(125,315),"5")
    num5_.setStyle('italic')
    num5_.setSize(36)
    num5_.draw(win)

    num6 = Rectangle(Point(170,350),Point(240,280))
    num6.draw(win)
    num6_ = Text(Point(205,315),"6")
    num6_.setStyle('italic')
    num6_.setSize(36)
    num6_.draw(win)

    num7 = Rectangle(Point(10,430),Point(80,360))
    num7.draw(win)
    num7_ = Text(Point(45,395),"7")
    num7_.setStyle('italic')
    num7_.setSize(36)
    num7_.draw(win)

    num8 = Rectangle(Point(90,430),Point(160,360))
    num8.draw(win)
    num8_ = Text(Point(125,395),"8")
    num8_.setStyle('italic')
    num8_.setSize(36)
    num8_.draw(win)

    num9 = Rectangle(Point(170,430),Point(240,360))
    num9.draw(win)
    num9_ = Text(Point(205,395),"9")
    num9_.setStyle('italic')
    num9_.setSize(36)
    num9_.draw(win)

    num0 = Rectangle(Point(90,510),Point(160,440))
    num0.draw(win)
    num0_ = Text(Point(125,475),"0")
    num0_.setStyle('italic')
    num0_.setSize(36)
    num0_.draw(win)

    eq_sign = Rectangle(Point(170,510),Point(240,440))
    eq_sign.draw(win)
    eq = Text(Point(205,475),"=")
    eq.setStyle('italic')
    eq.setSize(36)
    eq.draw(win)

    Rectangle(Point(10,510),Point(80,440)).draw(win)
    AC = Text(Point(45,475),"AC")
    AC.setStyle('italic')
    AC.setSize(20)
    AC.draw(win)

    Rectangle(Point(10,590),Point(240,520)).draw(win)
    OFF = Text(Point(125,555),"OFF")
    OFF.setStyle('italic')
    OFF.setSize(20)
    OFF.draw(win)

    while True:
        px,py = Point.getX(win.getMouse()),Point.getY(win.getMouse())
        if 10<=px<=60 and 80<=py<=130:
            text.setText(text.getText()+"+")
        if 310<=px<=360 and 140<=py<=190:
            if len(str(text.getText())) <= 1:
                text.setText("")
            else:
                del_text = "".join(list(str(text.getText()))[:-1])
                text.setText(del_text)
        if 70<=px<=120 and 80<=py<=130:
            text.setText(text.getText()+"-")
        if 130<=px<=180 and 80<=py<=130:
            text.setText(text.getText()+"*")
        if 190<=px<=240 and 80<=py<=130:
            text.setText(text.getText()+"/")
        if 250<=px<=300 and 80<=py<=130:
            text.setText(text.getText()+"(")
        if 310<=px<=360 and 80<=py<=130:
            text.setText(text.getText()+")")
        if 90<=px<=160 and 440<=py<=510:
            text.setText(text.getText()+"0")
        if 10<=px<=80 and 200<=py<=270:
            text.setText(text.getText()+"1")
        if 90<=px<=160 and 200<=py<=270:
            text.setText(text.getText()+"2")
        if 170<=px<=240 and 200<=py<=270:
            text.setText(text.getText()+"3")
        if 10<=px<=80 and 280<=py<=350:
            text.setText(text.getText()+"4")
        if 90<=px<=160 and 280<=py<=350:
            text.setText(text.getText()+"5")
        if 170<=px<=240 and 280<=py<=350:
            text.setText(text.getText()+"6")
        if 10<=px<=80 and 360<=py<=430:
            text.setText(text.getText()+"7")
        if 90<=px<=160 and 360<=py<=430:
            text.setText(text.getText()+"8")
        if 170<=px<=240 and 360<=py<=430:
            text.setText(text.getText()+"9")
        if 170<=px<=240 and 440<=py<=510:#=
            try:
                result = eval(text.getText())
            except:
                result = "ERROR"
                text.setText(result)

        
            text.setText("One more click to exit")
            win.getMouse()
            win.close()

main()

