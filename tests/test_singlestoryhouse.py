import ai2thor.controller as tc
import time
import math

# Create the AI2-THOR controller with a high-resolution render target
controller = tc.Controller(
    width=1920,
    height=1080,
    quality='Ultra'
)

# Initialize the complex urban multi-story apartment (FloorPlan301)
event = controller.step(dict(
    action='Initialize',
    gridSize=0.25,
    agentCount=1,
    scene='FloorPlan301'
))
# Removed 'SetScreenSize' -- not a valid AI2-THOR action per error message in file_context_0

# Location/feature hints for FloorPlan301:
# - Front doors with glass panels
# - Internal stairs at approx x=2-3, z=0
# - Windows on both front and back
# - Multiple floors accessible by stairs

def orbit_building(center_x=0, center_z=0, radius=8, height=2.5, orbits=1, steps=72, sleep_time=0.07):
    print("Starting orbital fly-around to showcase the whole building...")
    for orbit in range(orbits):
        for i in range(steps):
            angle_rad = 2 * math.pi * i / steps
            x = center_x + radius * math.sin(angle_rad)
            z = center_z + radius * math.cos(angle_rad)
            rotation = (360 * i / steps + 180) % 360
            controller.step({
                'action': 'TeleportFull',
                'agentId': 0,
                'x': x,
                'y': height,
                'z': z,
                'rotation': rotation,
                'horizon': -10,
                'standing': True,
                'forceAction': True
            })
            time.sleep(sleep_time)
    print("Orbital view complete.")

# Exterior fly-around for urban building intro
controller.step({
    'action': 'TeleportFull',
    'agentId': 0,
    'x': 0.0,
    'y': 2.5,
    'z': -9.0,   # Just outside the main entrance of FloorPlan301
    'rotation': 0.0,
    'horizon': -13.0,
    'standing': True,
    'forceAction': True
})
print("Initial exterior wide shot")
time.sleep(2)
orbit_building(center_x=0.0, center_z=0.0, radius=9, height=3.5, orbits=1, steps=90, sleep_time=0.055)

print("Orbital urban building view demonstration complete.")

# Interior showcase: Enter through front door.
entrance_position = {
    'x': 0.0,
    'y': 1.0,
    'z': -5.0,
    'rotation': 0.0,
    'horizon': 0.0,
    'standing': True,
    'forceAction': True
}
controller.step({'action': 'TeleportFull', 'agentId': 0, **entrance_position})
print("Approaching urban building entrance...")
time.sleep(1.5)

# Move inside, look around (door, windows, stairs ahead)
controller.step({'action': 'TeleportFull', 'agentId': 0, 'x': 0.0, 'y': 1.0, 'z': -2.0, 'rotation': 0.0, 'horizon': 0.0, 'standing': True, 'forceAction': True})
time.sleep(1)
controller.step({'action': 'RotateRight', 'agentId': 0})
time.sleep(0.65)
controller.step({'action': 'RotateRight', 'agentId': 0})
time.sleep(0.65)
controller.step({'action': 'RotateLeft', 'agentId': 0})
time.sleep(0.65)

# Walk to the stairwell, look up the stairs
controller.step({'action': 'TeleportFull', 'agentId': 0, 'x': 2.1, 'y': 1.0, 'z': 0.0, 'rotation': 90.0, 'horizon': -30.0, 'standing': True, 'forceAction': True})
print("Focusing on the main stairwell for multi-story navigation.")
time.sleep(1.5)

# Ascend one floor to highlight multi-story
controller.step({'action': 'TeleportFull', 'agentId': 0, 'x': 2.3, 'y': 3.0, 'z': 0.0, 'rotation': 0, 'horizon': 0.0, 'standing': True, 'forceAction': True})
print("At upper story. Show a window or opening view to outside.")
time.sleep(1.4)
controller.step({'action': 'RotateRight', 'agentId': 0})
time.sleep(0.5)
controller.step({'action': 'RotateRight', 'agentId': 0})
time.sleep(0.7)
controller.step({'action': 'LookDown', 'agentId': 0})
time.sleep(0.4)

# Look at the window (many upper stories have windows to the exterior)
controller.step({'action': 'TeleportFull', 'agentId': 0, 'x': 0.0, 'y': 3.0, 'z': 3.9, 'rotation': 180, 'horizon': -13, 'standing': True, 'forceAction': True})
print("Looking out upper story window/opening.")
time.sleep(1.5)

print("Urban multi-story building introduction complete.")
