class Horse:
    x_distance = 0        # пройденный путь
    # _sound = 'Frrr'  # отсюда наследование не происходит, используется _sound
    def __init__(self, dx):
        self.dx = dx
        sound = 'Frrr' # отсюда наследование не происходит
    def run(self):
        self.x_distance += self.dx
        return self.x_distance

class Eagle:
    y_distance = 0                            # высота полёта
    sound = 'I train, eat, sleep, and repeat!' # звук, который издаёт орёл (отсылка) \ отсюда идёт наследование

    def __init__(self, dy):
        self.dy = dy
    def fly(self):
        self.y_distance += self.dy
        return self.y_distance

class Pegasus(Horse, Eagle):
    def __init__(self):
        super().sound
        super().x_distance
        super().y_distance

    def move(self, dx, dy): # где dx и dy изменения дистанции.
                            # В этом методе должны запускаться наследованные методы run и fly соответственно.
        self.dx = dx
        self.dy = dy
        super().run()
        super().fly()
        return self.x_distance, self.y_distance
    def get_pos(self): # возвращает текущее положение пегаса в виде кортежа - (x_distance, y_distance) в том же порядке.
        result = (self.x_distance, self.y_distance)
        return result
    def voice(self):
        return print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
