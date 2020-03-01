# coding=utf-8
import sympy as sp

class Dem():
    """一个使用DEM模型计算热导率的类"""
    def __init__(self, kr, km, h, particle_size):
        """初始化数据，并求出复合材料增强体的等效热导率"""
        self.kr = kr
        self.km = km
        self.h = h
        self.particle_size = particle_size
        m=kr/h/particle_size
        self.kreff = kr/(1+m)

    def kc(self):
        """返回复合材料的热导率"""
        a = 1
        b = -3*self.kreff
        c = (0.4*(self.kreff-self.km))**3/self.km+3*self.kreff**2
        d = -self.kreff**3
        x = sp.Symbol('x')
        f = a*x**3 + b*x**2 + c*x +d
        x = sp.solve(f)
        return x[0]