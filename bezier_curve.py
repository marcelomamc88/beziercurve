#CAÇA AO TESOURO 3 - CURVA DE BEZIER
#TIME PACIENTE TS#01
#MARCELO ALEXANDRE MARTINS DA CONCEIÇÃO
#LUCAS TOSI
#VINÍCIUS ROBERTO

from tkinter import Tk, Canvas, Frame, BOTH
import math
from math import trunc

class Bezier(Frame):

    def __init__(self, lines, iterations, windowWidth, windowHeight):
        super().__init__()

        self.initUI(lines, iterations, windowWidth, windowHeight)


    def initUI(self, lines, iterations, xMax, yMax):
        self.master.title("CE229 - CAÇA AO TESOURO 3 - TS#01 - PACIENTE - Curva de Bezier")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)

        for i in range(0, len(lines)):
            self.create(canvas, lines[i], iterations, yMax)



    def y_adjust(self, lines, yMax):
        r = []
        for line in lines:
            y0 = yMax - line[0][1]
            y1 = yMax - line[1][1]
            r.append([[line[0][0], y0], [line[1][0],y1]])

        return r

    def create(self, canvas, lines, iterations, yMax):

        lines = self.y_adjust(lines, yMax)

        for i in range(1, iterations+1):
            t = (1 / iterations) * i

            for line in lines:
                canvas.create_oval(line[0][0], line[0][1], line[0][0] + 1, line[0][1] + 1, outline="blue", width=3)

            self.run(canvas, t, lines)

        canvas.pack(fill=BOTH, expand=1)


    def run(self, canvas, t, lines):
        dots = []

        for line in lines:
            canvas.create_line(line[0], line[1], stipple="gray25")
            dot = self.calc_dot(t, line[0], line[1])

            dots.append([dot.get('x'), dot.get('y')])

        if len(dots) == 1:
            canvas.create_oval(dot.get("x"), dot.get("y"), dot.get("x") + 1, dot.get("y") + 1, outline="#f11", width=3)
            return dots

        new_lines = []
        index = 0
        c_dots = len(dots)

        for dot in dots:
            if c_dots-1 == index:
                break

            new_lines.append([dots[index], dots[index+1]])
            index += 1

        dots.append(self.run(canvas, t, new_lines))

        return dots



    def calc_dot(self, t, *reta):

        p0 = reta[0]
        p0_x = p0[0]
        p0_y = p0[1]

        p1 = reta[1]
        p1_x = p1[0]
        p1_y = p1[1]

        cateto_a = math.fabs(p1_x - p0_x)
        cateto_b = math.fabs(p1_y - p0_y)

        hipotenusa = math.sqrt(cateto_a**2 + cateto_b**2)

        sin_a = cateto_a / hipotenusa
        sin_b = cateto_b / hipotenusa

        x_resultante = sin_a * hipotenusa * t
        y_resultante = sin_b * hipotenusa * t

        if p0_x < p1_x:
            ret_x = p0_x + x_resultante
        else:
            ret_x = p0_x - x_resultante

        if p0_y < p1_y:
            ret_y = p0_y + y_resultante
        else:
            ret_y = p0_y - y_resultante

        return {"x": ret_x, "y": ret_y}

def main():
    iterations = 75
    window_width = 1400
    window_height = 900
    lines = []

    xy = input("- Entre com os valores dos pontos: \r\n   * Pattern: x1,y1 x2,y2 x3,y3 \r\n   * Valores Mínimos: x: 0 y: 0\r\n   * Valores Máximos: x: {} y: {}\r\n- Para gerar os gráficos default, pressione ENTER\r\n\r\n".format(window_width/100, window_height/100)).split()

    if len(xy) != 0:
        line = []
        dots = []
        for i in range(0, len(xy)):
            str_xy = xy[i].split(',')
            x = trunc(float(str_xy[0])*100)
            y = trunc(float(str_xy[1])*100)

            if x > window_width or y > window_height:
                raise Exception("os eixos X e Y devem ser menores que {},{} respectivamente".format(window_width/100, window_height/100))

            dots.append([x, y])

        for i in range(0, len(dots)-1):
            line.append([dots[i], dots[i+1]])

        lines.append(line)

    else:
        # bezier curve 1
        # [X,Y], [X,Y]
        lines.append([[[100, 0], [0, 340]],
                 [[0, 340], [400, 400]],
                 [[400, 400], [350, 80]],
                 [[350, 80], [300, 200]]])

        # bezier curve 2
        # [X,Y], [X,Y]
        lines.append([[[100, 450], [0, 700]],
                      [[0, 700], [400, 800]],
                      [[400, 800], [370, 430]]])


        # bezier curve 3
        # [X,Y], [X,Y]
        lines.append([[[500, 50], [900, 300]],
                      [[900, 300], [750, 400]],
                      [[750, 400], [600, 300]],
                      [[600, 300], [900, 0]]])

        # bezier curve 4
        # [X,Y], [X,Y]
        lines.append([[[600, 400], [500, 700]],
                      [[500, 700], [850, 450]],
                      [[850, 450], [900, 800]]])

    root = Tk()
    Bezier(lines, iterations, window_width, window_height)
    root.geometry(str(window_width) + "x" + str(window_height) + "+0+0")
    root.mainloop()


if __name__ == '__main__':
    main()