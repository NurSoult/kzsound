from math import pi


def circle_area(radius):

    if radius < 0:
        raise ValueError("Радиус теріс сан бола алмайды")

    if type(radius) not in [int, float]:
        raise TypeError("Радиус нақты сан болу керек")

    return pi * radius ** 2


# r_list = [2, 0, -3, 2 + 3j, True, [2], 'seven']
# message = 'Шеңбердің ауданы {radius} -->  {area}'
#
# for r in r_list:
#     s = circle_area(r)
#     print(message.format(radius=r, area=s))
