# coding=utf-8

from dem import Dem
import sympy as sp 

def dem_model():
    """DEM模型计算热导率"""
    while True:
        # 输入数据
        print("结束请输入q退出\n")
        kr = input("请输入增强体的热导率(W/mK):\n")
        if kr == 'q':
            break
        kr = float(kr)
        km = input("\n请输入基体的热导率(W/mK):\n")
        if km == 'q':
            break
        km = float(km)
        h = input("\n请输入界面热导:\n")
        if h == 'q':
            break
        h = float(h)
        p_size = input("\n请输入增强体的直径(m):\n")
        if p_size == 'q':
            break
        p_size = float(p_size)
        dem = Dem(kr, km, h, p_size)
        kc = round(dem.kc(), 2)

        # 输出结果
        print("\n该复合材料热导率为:\t" + str(kc) + "(W/mK).\n")
        active = input("是否继续进行计算:yes or no?\n")
        if active == 'no':
            break

# 选择模型
choice = input("请选择功能，enter确认\nDEM\nAMM\nH_J\n")

if choice == 'dem' or 'DEM' or 'Dem':
    # 使用DEM模型计算热导率
    dem_model()
