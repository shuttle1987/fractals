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
        midpoint13 = (self.v1[0]+self.v2[0])/2, (self.v1[1]+self.v2[1])/2
        midpoint23 = (self.v2[0]+self.v3[0])/2, (self.v2[1]+self.v3[1])/2

        tri1 = Triangle(self.v1, midpoint12, midpoint13)
        tri2 = Triangle(self.v1, midpoint12, midpoint23)
        tri3 = Triangle(self.v1, midpoint13, midpoint23)
        return [tri1, tri2, tri3]
        

def get_subtriangle_vertices(sierpinski_triangle, vertices=None, depth=0):
    """Find the triangles contained within the given triangle"""
    
    if depth == 0:
        return vertices
    else:
        pass
