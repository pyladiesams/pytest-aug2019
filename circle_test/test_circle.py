from circle import Circle

def test_circle_area():
    '''Verify that circle surface area grater than 7'''
    radius = 1.5
    expected_circle_squre_area = 7
    circle = Circle(radius)
    assert circle.surface_area > expected_circle_squre_area, 'Circle surface area is too small'

def test_circle_length():
    '''Verify that length of circle is less than X'''
    # TODO


