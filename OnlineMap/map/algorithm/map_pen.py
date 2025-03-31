from xml.etree.ElementTree import Element

class Color:
    #RGB-цвета
    red = 0
    green = 0
    blue = 0
    def __init__(self, r,g,b):
        self.red = r
        self.green = g
        self.blue = b


class Vertice:
    #Вершина. Необходимо для построения линии и графа смежности
    x, y = None, None
    def __init__(self, x, y):
        self.x = x; self.y = y
    def get_coords(self):
        return self.x, self.y

class Line:
    # Линия отображаемая на карте
    stroke_color = None # Цвет линии (по умолчанию красный)
    stroke_linecap = None # Стиль линии (по умолчанию закруглённый)
    line_length = None; distance_betwen_lines = None # Длина и растояние между линиями
    x1, x2, y1, y2 = None, None, None, None

    def __init__(self, vertice_1: Vertice, vertice_2: Vertice, color = Color(255, 0, 0), 
                 linecap = 'round', length = 10, distance = 5):
        self.x1, self.y1 = vertice_1.get_coords()
        self.x2, self.y2 = vertice_2.get_coords()
        self.stroke_color = color
        self.stroke_linecap = linecap
        self.line_length = length; self.distance_betwen_lines = distance

    def get_line_code(self, root: Element):
        line = Element('line')
        line.set('x1', self.x1)
        line.set('y1', self.y1)
        line.set('x2', self.x2)
        line.set('y2', self.y2)

        # Устанавливаем цвет линии
        r, g, b = self.stroke_color.red, self.stroke_color.green, self.stroke_color.blue
        line.set('style', f'stroke-linecap: {self.stroke_linecap}; stroke: rgb({r}, {g}, {b})')

        # Устанавливаем толщину линии (4px)
        line.set('stroke-width', '4')

        # Устанавливаем прерывистый стиль (8px длина штриха, 8px пробел)
        line.set('stroke-dasharray', '8,8')

        # line.set('stroke-dashoffset', '8');

        # Добавляем линию в корневой элемент
        root.append(line)