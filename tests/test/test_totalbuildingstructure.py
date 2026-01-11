import pyvista as pv

def create_detailed_building():
    """Creates a building with windows, doors, and detailed features"""
    
    # Main building structure
    building = pv.Cube(center=(0, 0, 15), x_length=20, y_length=15, z_length=30)
    
    # Create floors (5 floors)
    floors = []
    for i in range(5):
        floor = pv.Plane(center=(0, 0, i * 6), i_size=20, j_size=15)
        floors.append(floor)
    
    # Create windows (4x5 grid)
    windows = []
    for floor in range(5):
        for col in range(4):
            # Front windows
            window = pv.Cube(
                center=(col * 5 - 7.5, -7.6, floor * 6 + 3),
                x_length=2, y_length=0.2, z_length=2
            )
            windows.append(window)
            
            # Back windows
            window_back = pv.Cube(
                center=(col * 5 - 7.5, 7.6, floor * 6 + 3),
                x_length=2, y_length=0.2, z_length=2
            )
            windows.append(window_back)
    
    # Create doors (ground floor)
    door = pv.Cube(center=(0, -7.6, 1.5), x_length=2, y_length=0.2, z_length=3)
    
    # Stairwell (central)
    stairwell = pv.Cylinder(center=(8, 0, 15), direction=(0, 0, 1), 
                           radius=2, height=30)
    
    # Combine all elements
    plotter = pv.Plotter()
    plotter.add_mesh(building, color='tan', opacity=0.8)
    
    for floor in floors:
        plotter.add_mesh(floor, color='gray', opacity=0.3)
    
    for window in windows:
        plotter.add_mesh(window, color='lightblue')
    
    plotter.add_mesh(door, color='brown')
    plotter.add_mesh(stairwell, color='darkgray')
    
    # Save combined building
    combined = building
    for f in floors:
        combined = combined + f
    for w in windows:
        combined = combined + w
    combined = combined + door + stairwell
    
    combined.save('detailed_building.vtk')
    
    plotter.show()
    return combined

# Create building
building = create_detailed_building()