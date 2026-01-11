# 4-Story Building Navigation System

**Quick Reference Guide**

---

## Quick Start (30 seconds)

```bash
# 1. Install dependencies
pip install ai2thor pyvista numpy trimesh

# 2. Run main simulation
python building_navigation_sim.py

# 3. Choose option [2] for normal speed
```

---

## Project Structure

```
building/
├── building_navigation_sim.py          ← Main simulation file
├── BUILDING_DOCUMENTATION.md           ← Complete documentation
├── README.md                           ← This file
│
└── test/                               ← All testing scripts
    ├── create_4story_advanced.py       ← Building generator (recommended)
    ├── create_4story_building.py       ← Building generator (basic)
    ├── run_building_generator.py       ← Interactive launcher
    │
    ├── test_floor_connectivity.py      ← Animated navigation
    ├── test_simple_path.py             ← Static path visualization
    ├── test_wall_floor_separation.py   ← Structural analysis
    ├── run_all_tests.py                ← Test runner
    │
    └── view_building.py                ← 3D viewer
```

---

## Main Simulation

**File:** `building_navigation_sim.py`

This is the **primary simulation** showing realistic agent navigation through a 4-story building.

### Features

✓ Free floor exploration (agent can move anywhere on each floor)
✓ Boundary enforcement (1m wall margin - no escaping!)
✓ Blue line navigation to stairs
✓ Smooth stair climbing between floors
✓ Real-time visualization
✓ Comprehensive verification reports

### Usage

```bash
python building_navigation_sim.py
```

### What You'll See

- **Red agent**: Moving freely on floors
- **Blue agent**: Following path to stairs
- **Orange agent**: Climbing stairs
- Building shown semi-transparent to see inside
- Progress counter and position display
- Green box showing safe navigation area

---

## Generate Buildings

**Before running simulations, generate a building:**

```bash
cd test

# Recommended: Advanced version with realistic geometry
python create_4story_advanced.py

# OR: Basic version (faster, simpler)
python create_4story_building.py

# OR: Use interactive menu
python run_building_generator.py
```

**Output Files:**
- `ai2thor_4story_building.vtk` - For visualization
- `ai2thor_4story_building.stl` - For 3D printing/CAD
- `ai2thor_4story_building.ply` - For point clouds

---

## Testing Suite

### Quick Path Check

```bash
cd test
python test_simple_path.py
```

Shows static path through all floors. Fast verification.

### Animated Navigation

```bash
cd test
python test_floor_connectivity.py
```

Watch agent navigate through building in real-time.

### Structural Analysis

```bash
cd test
python test_wall_floor_separation.py
```

Interactive menu with:
- Floor separation slices
- Wall cross-sections
- Stairwell connectivity analysis

### Run All Tests

```bash
cd test
python run_all_tests.py
```

Master test runner with interactive menu.

---

## Complete Documentation

For detailed information, see:

📖 **[BUILDING_DOCUMENTATION.md](BUILDING_DOCUMENTATION.md)**

This comprehensive guide includes:
- Installation details
- System architecture
- Customization options
- Troubleshooting
- Bug fixes & improvements
- Advanced topics
- Technical reference

---

## Key Features

### Building Generation
- 4 stacked floors from AI2Thor scenes
- Connected stairwell (2.5m × 4.0m)
- Windows and doors
- Multiple export formats

### Navigation System
- **Free floor movement** - Agent explores entire floor
- **Boundary enforcement** - 1m wall margin
- **Blue line paths** - Floor to stairs
- **Stair climbing** - 12 steps per flight
- **No wall penetration** - All waypoints verified

### Improvements (v2.0)
✓ Fixed: Agent staying within building bounds
✓ Fixed: Free floor exploration (not just 4 points)
✓ Fixed: PyVista has_actor() error
✓ Fixed: Camera orientation (floor 0 at bottom)

---

## Customization

### Change Floors

Edit in any file:
```python
num_floors = 6  # Change from 4
```

### Change Floor Height

```python
floor_height = 3.5  # Change from 3.0m
```

### Change Scene

In `test/create_4story_advanced.py`:
```python
scene_name = 'FloorPlan302'  # Try 301-330
```

---

## Troubleshooting

### No building file found
```bash
cd test
python create_4story_advanced.py
```

### AI2Thor won't start
- Reduce quality from 'Ultra' to 'High'
- Check display settings

### Window won't open
- Try different terminal
- Check OpenGL support

For more solutions, see [BUILDING_DOCUMENTATION.md](BUILDING_DOCUMENTATION.md#troubleshooting)

---

## Requirements

- Python 3.7+
- AI2Thor
- PyVista
- NumPy
- Trimesh (optional)

```bash
pip install ai2thor pyvista numpy trimesh
```

---

## Files Overview

| File | Purpose |
|------|---------|
| `building_navigation_sim.py` | Main simulation (improved version) |
| `BUILDING_DOCUMENTATION.md` | Complete comprehensive documentation |
| `test/create_4story_advanced.py` | Building generator (realistic) |
| `test/test_floor_connectivity.py` | Animated navigation test |
| `test/test_simple_path.py` | Static path visualization |
| `test/test_wall_floor_separation.py` | Structural analysis |
| `test/run_all_tests.py` | Test runner |
| `test/view_building.py` | 3D viewer |

---

## Quick Commands

```bash
# Main simulation
python building_navigation_sim.py

# Generate building
cd test && python create_4story_advanced.py

# Quick test
cd test && python test_simple_path.py

# All tests
cd test && python run_all_tests.py

# View building
cd test && python view_building.py
```

---

## What Gets Verified

✓ All 4 floors accessible
✓ Stairwell connects all floors
✓ Agent stays within building bounds
✓ Free movement on each floor
✓ Proper floor separation
✓ Wall boundaries respected
✓ Continuous path ground-to-top

---

## Next Steps

1. **Run main simulation** - See it in action
2. **Read full documentation** - Understand the system
3. **Generate custom buildings** - Try different scenes
4. **Modify parameters** - Adjust floors, heights, etc.
5. **Export for games** - Use STL files in Unity/Unreal

---

**Version:** 2.0
**Status:** Production Ready ✓
**License:** MIT

For complete documentation: [BUILDING_DOCUMENTATION.md](BUILDING_DOCUMENTATION.md)
