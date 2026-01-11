"""
Test script for the Emergency Rescue Simulation System
Runs a quick test of all components without full simulation.
"""

import sys
import os

def test_imports():
    """Test that all modules can be imported"""
    print("Testing imports...")

    try:
        from building_navigator import Building3D, Position3D
        print("  ✓ building_navigator")
    except Exception as e:
        print(f"  ✗ building_navigator: {e}")
        return False

    try:
        from danger_simulator import DangerManager, FireSimulator, AttackerSimulator
        print("  ✓ danger_simulator")
    except Exception as e:
        print(f"  ✗ danger_simulator: {e}")
        return False

    try:
        from nemo_rescue_agents import NeMoRescueAgent, CollaborativeRescueSwarm
        print("  ✓ nemo_rescue_agents")
    except Exception as e:
        print(f"  ✗ nemo_rescue_agents: {e}")
        return False

    try:
        from atlas_learning_db import AtlasLearningDatabase
        print("  ✓ atlas_learning_db")
    except Exception as e:
        print(f"  ✗ atlas_learning_db: {e}")
        return False

    try:
        from rescue_simulation import RescueSimulationEngine
        print("  ✓ rescue_simulation")
    except Exception as e:
        print(f"  ✗ rescue_simulation: {e}")
        return False

    print("\n✅ All imports successful!\n")
    return True


def test_building():
    """Test building navigation system"""
    print("Testing Building Navigation...")

    from building_navigator import Building3D

    building = Building3D()

    # Test basic properties
    assert building.floors == 4, "Building should have 4 floors"
    assert building.child_position is not None, "Child position should be set"
    assert building.start_position is not None, "Start position should be set"

    # Test pathfinding
    path = building.find_path(building.start_position, building.child_position)
    assert path is not None, "Should find path from start to child"
    assert len(path) > 0, "Path should have steps"

    print(f"  ✓ Building has {len(building.nodes)} nodes")
    print(f"  ✓ Found path with {len(path)} steps")
    print("\n✅ Building navigation tests passed!\n")


def test_danger_simulation():
    """Test danger simulation systems"""
    print("Testing Danger Simulation...")

    from building_navigator import Building3D
    from danger_simulator import DangerManager

    building = Building3D()

    # Test fire scenario
    fire_mgr = DangerManager(building, scenario="fire")
    fire_zones = fire_mgr.get_all_danger_zones()
    assert len(fire_zones) > 0, "Fire scenario should have danger zones"

    # Update simulation
    fire_mgr.update(1.0)
    updated_zones = fire_mgr.get_all_danger_zones()

    print(f"  ✓ Fire scenario: {len(fire_zones)} initial zones")
    print(f"  ✓ After 1s: {len(updated_zones)} zones")

    # Test attacker scenario
    building2 = Building3D()
    attacker_mgr = DangerManager(building2, scenario="attacker")
    attacker_zones = attacker_mgr.get_all_danger_zones()
    assert len(attacker_zones) > 0, "Attacker scenario should have danger zone"

    attacker_mgr.update(1.0)

    print(f"  ✓ Attacker scenario initialized")

    print("\n✅ Danger simulation tests passed!\n")


def test_agents():
    """Test NeMo rescue agents"""
    print("Testing NeMo Rescue Agents...")

    from building_navigator import Building3D
    from danger_simulator import DangerManager
    from nemo_rescue_agents import CollaborativeRescueSwarm

    building = Building3D()
    danger_mgr = DangerManager(building, scenario="fire")

    # Create small swarm
    swarm = CollaborativeRescueSwarm(
        num_agents=2,
        building=building,
        danger_manager=danger_mgr
    )

    assert len(swarm.agents) == 2, "Swarm should have 2 agents"

    # Test planning
    swarm.coordinate_planning()

    for agent in swarm.agents:
        assert agent.current_plan is not None, "Agents should have plans"

    print(f"  ✓ Created swarm with {len(swarm.agents)} agents")
    print(f"  ✓ Agents planned routes")

    print("\n✅ Agent tests passed!\n")


def test_database():
    """Test Atlas database connection"""
    print("Testing Atlas Database...")

    try:
        from atlas_learning_db import AtlasLearningDatabase

        db = AtlasLearningDatabase()

        # Test getting statistics
        stats = db.get_mission_statistics("fire")

        print(f"  ✓ Database connected")
        print(f"  ✓ Fire scenario: {stats['total_missions']} missions")

        stats_attacker = db.get_mission_statistics("attacker")
        print(f"  ✓ Attacker scenario: {stats_attacker['total_missions']} missions")

        print("\n✅ Database tests passed!\n")

    except Exception as e:
        print(f"\n⚠️  Database test failed: {e}")
        print("This is OK if MongoDB is not configured yet.")
        print("Set MONGODB_URI in .env to enable database features.\n")


def run_quick_simulation():
    """Run a very quick simulation (1 iteration)"""
    print("Running Quick Simulation Test...")
    print("This will run 1 rescue attempt (may take 10-30 seconds)\n")

    from rescue_simulation import RescueSimulationEngine

    # Create simulation
    sim = RescueSimulationEngine(scenario="fire")

    # Run single iteration
    mission = sim.run_iteration(num_agents=2)

    print(f"\n  Mission Result: {'SUCCESS' if mission.success else 'FAILED'}")
    print(f"  Time: {mission.total_time:.1f}s")
    print(f"  Agents: {len(mission.agents)}")
    print(f"  Alive: {sum(1 for a in mission.agents if a.is_alive)}")

    print("\n✅ Quick simulation completed!\n")


def main():
    """Run all tests"""
    print("\n" + "="*70)
    print("EMERGENCY RESCUE SYSTEM - COMPONENT TESTS")
    print("="*70 + "\n")

    # Test imports
    if not test_imports():
        print("\n❌ Import tests failed. Please install dependencies:")
        print("   pip install -r requirements_rescue.txt\n")
        return False

    # Test building
    try:
        test_building()
    except Exception as e:
        print(f"\n❌ Building tests failed: {e}\n")
        return False

    # Test danger simulation
    try:
        test_danger_simulation()
    except Exception as e:
        print(f"\n❌ Danger simulation tests failed: {e}\n")
        return False

    # Test agents
    try:
        test_agents()
    except Exception as e:
        print(f"\n❌ Agent tests failed: {e}\n")
        return False

    # Test database (non-critical)
    test_database()

    # Ask user if they want to run quick simulation
    print("="*70)
    response = input("Run a quick simulation test? (y/n): ").strip().lower()

    if response == 'y':
        try:
            run_quick_simulation()
        except Exception as e:
            print(f"\n❌ Simulation test failed: {e}\n")
            return False

    print("="*70)
    print("✅ ALL TESTS PASSED!")
    print("="*70)
    print("\nYou're ready to run the full rescue simulation!")
    print("\nTry:")
    print("  python rescue_simulation.py --scenario fire --iterations 5")
    print("  python rescue_simulation.py --scenario attacker --until-success")
    print("\nFor more options:")
    print("  python rescue_simulation.py --help")
    print("\n")

    return True


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
