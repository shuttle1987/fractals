"""
Sierpinski triangle creation
"""

class Triangle:
    """
    The Sierpinski triangle contains self similar triangles.
    This is a representation of a 2dimensional triangle in Euclidean plane.
    """
    def __init__(self, v1, v2, v3):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3

    def subtriangles(self):
        """Returns the Triangles contained within this one"""
        midpoint12 = (self.v1[0]+self.v2[0])/2, (self.v1[1]+self.v2[1])/2
        midpoint13 = (self.v1[0]+self.v3[0])/2, (self.v1[1]+self.v3[1])/2
        midpoint23 = (self.v2[0]+self.v3[0])/2, (self.v2[1]+self.v3[1])/2

        tri1 = Triangle(self.v1, midpoint12, midpoint13)
        tri2 = Triangle(self.v2, midpoint12, midpoint23)
        tri3 = Triangle(self.v3, midpoint13, midpoint23)
        return [tri1, tri2, tri3]

    def __repr__(self):
        return "Triangle({},{},{})".format(self.v1, self.v2, self.v3)
        

def get_subtriangle_vertices(sierpinski_triangle, depth=0):
    """Find the triangles contained within the given triangle"""
    
    if depth == 0:
        return sierpinski_triangle
    else:
        new_triangles = sierpinski_triangle.subtriangles()
        return [get_subtriangle_vertices(triangle, depth-1) for triangle in new_triangles]
