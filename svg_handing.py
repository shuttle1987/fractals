import svgwrite

from seirpinski import Triangle, get_subtriangle_vertices
from utils import flattener


def svg_sierpinski(dwg, depth):
    """
    :dwg: the svg Drawing object
    :depth: the depth of the Sirepinski triangle being created
    """
    right_angled_triangle = Triangle((0, 0), (0, 100), (100, 0))
    subtriangles_test = get_subtriangle_vertices(right_angled_triangle, depth)
    flattened = flattener(subtriangles_test)
    for triangle in flattened:
        print(triangle)
        dwg.add(dwg.line(triangle.v1, triangle.v2, stroke='black'))
        dwg.add(dwg.line(triangle.v2, triangle.v3, stroke='black'))
        dwg.add(dwg.line(triangle.v3, triangle.v1, stroke='black'))

if __name__ == "__main__":
    dwg = svgwrite.Drawing(filename='test.svg', size=("800px", "600px"), profile='tiny')
    svg_sierpinski(dwg, 3)
    dwg.save()
