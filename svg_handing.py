import svgwrite

from seirpinski import Triangle, get_subtriangle_vertices
from utils import flattener


def svg_sierpinski(dwg, depth, initial_triangle):
    """
    Create the lines in a sierpinski triangle
    :dwg: the svg Drawing object
    :depth: the depth of the Sirepinski triangle being created
    :initial_triangle: the outermost triangle
    """
    subtriangles = get_subtriangle_vertices(initial_triangle, depth)
    flattened = flattener(subtriangles)
    for triangle in flattened:
        dwg.add(dwg.line(triangle.v1, triangle.v2, stroke='black'))
        dwg.add(dwg.line(triangle.v2, triangle.v3, stroke='black'))
        dwg.add(dwg.line(triangle.v3, triangle.v1, stroke='black'))

if __name__ == "__main__":
    right_angled_triangle = Triangle((0, 0), (0, 600), (600, 0))
    dwg = svgwrite.Drawing(filename='test.svg', size=("600px", "600px"), profile='tiny')
    svg_sierpinski(dwg, depth=5, initial_triangle=right_angled_triangle)
    dwg.save()
