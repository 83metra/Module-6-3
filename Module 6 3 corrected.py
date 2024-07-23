class Horse:
    x_distance = 0        # пройденный путь
    __sound = 'Frrr'  
    
    def run(self):
        self.x_distance += self.dx
        return self.x_distance

class Eagle:
    y_distance = 0                             # высота полёта
    sound = 'I train, eat, sleep, and repeat!' # звук, который издаёт орёл (отсылка)

    def fly(self):
        self.y_distance += self.dy
        return self.y_distance

class Pegasus(Horse, Eagle):

    def move(self, dx, dy): # где dx и dy изменения дистанции.
                            # В этом методе должны запускаться наследованные методы run и fly соответственно.
        self.dx = dx
        self.dy = dy
        self.run()
        self.fly()
        return
    def get_pos(self): # возвращает текущее положение пегаса в виде кортежа - (x_distance, y_distance) в том же порядке.
        return (self.x_distance, self.y_distance)
    def voice(self):
        return print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
