from app import models, db

a = models.Training(name='Jumping Jack',url='https://youtu.be/LecVKn8Q-MM')
b = models.Training(name='Бёрпи',url='https://youtu.b e/1216pZQIUjM')
c = models.Training(name='Выпады назад',url='https://youtu.be/UsJMO-wLf0Y')
d = models.Training(name='Выпады на одну ногу',url='https://youtu.be/pclYaTqMZI4')
e = models.Training(name='Корейские прыжки',url='https://youtu.be/sTSHG_KpAJI')
f = models.Training(name='Подъём ног лёжа на животе',url='https://youtu.be/tXJeR1BNtZg')
g = models.Training(name='Подъём корпуса лёжа на животе',url='https://youtu.be/5eLxwsNCn1Y')
h = models.Training(name='Лодочка',url='https://youtu.be/XpnZE9JzRto')
i = models.Training(name='Ягодичный мостик на одну ногу',url='https://youtu.be/GnwK0H2Aia4')
j = models.Training(name='Отжимания от пола',url='https://youtu.be/LecVKn8Q-MM')
k = models.Training(name='Планка',url='https://youtu.be/DrzPbloObSA')
l = models.Training(name='Планка левая',url='https://youtu.be/tmJZ9K8k1ZA')
m = models.Training(name='Планка правая',url='https://youtu.be/6JZ7hloIpz0')
n = models.Training(name='Приседания с широкой постановкой ног',url='https://youtu.be/cvrAD33LFl0')
o = models.Training(name='Приседания',url='https://youtu.be/OhhXifdyhxs')
p = models.Training(name='Румынская тяга',url='https://youtu.be/361V7dC-hvA')
r = models.Training(name='Ситап',url='https://youtu.be/W-ZBcZnuQqM')
s = models.Training(name='Скалолаз',url='https://youtu.be/uIsw-L9MNw0')
t = models.Training(name='Скручивания',url='https://youtu.be/Sz0naPQqnPY')
u = models.Training(name='Упор присев - упор лёжа',url='https://youtu.be/IjCkC2zEWCI')
x = models.Training(name='Разминка',url='https://youtu.be/c2u6aa64j80')
y = models.Training(name='Пловец',url='https://youtu.be/S6BBqa71zto')
z = models.Training(name='Велосипед',url='https://youtu.be/17AfpEWVGOQ')
q = models.Training(name='Ягодичный мостик',url='https://www.youtube.com/watch?v=oHwmSrbmBLg')

aa  = models.Training(name='TW',url='https://youtu.be/WzyW9iUzxyc')
bb   = models.Training(name='CP',url='https://youtu.be/c45DZdKj5OM')

tt = models.Training(name='1видео',url='https://youtu.be/n3iz5MYpmB8')
xx = models.Training(name='2видео',url='https://youtu.be/l3rCa8AhbuY')
ww = models.Training(name='3видео',url='https://youtu.be/u6FbwWR3lXQ')
yy = models.Training(name='4видео',url='https://youtu.be/ncZI-CxHNuU')


db.session.add(a)
db.session.add(b)
db.session.add(c)
db.session.add(d)
db.session.add(e)
db.session.add(f)
db.session.add(g)
db.session.add(h)
db.session.add(i)
db.session.add(j)
db.session.add(k)
db.session.add(l)
db.session.add(m)
db.session.add(n)
db.session.add(o)
db.session.add(p)
db.session.add(r)
db.session.add(s)
db.session.add(t)
db.session.add(u)
db.session.add(x)
db.session.add(y)
db.session.add(z)
db.session.add(q)

db.session.add(aa)
db.session.add(bb)
db.session.add(tt)
db.session.add(xx)
db.session.add(ww)
db.session.add(yy)
db.session.commit()