from materials import Material, MaterialLibrary
from calculations import calculate_stress, calculate_safety_factor, calculate_weight
def main():
    # Create library and add materials
    library = MaterialLibrary()
    steel = Material("Steel AISI 304", "Metal", 7850, 200e9, 205e6)
    aluminum = Material("Aluminum 6061", "Metal", 2700, 68.9e9, 276e6)
    carbon_fiber = Material("Carbon Fiber", "Composite", 1600, 230e9,600e6)
    library.add_material(steel)
    library.add_material(aluminum)
    library.add_material(carbon_fiber)
    
    # Find materials
    metal_materials = library.find_by_type("Metal")
    print(f"Found {len(metal_materials)} metal materials")
    # Update material properties using setter methods
    print("Steel before update:\n"+str(steel))
    steel.set_yield_strength(210e6) # Updated yield strength from new test results
    print("Steel after update:\n"+str(steel))
    # Update material properties using update_material method
    print("Aluminum in library before update:\n"+str(library.find_by_name("Aluminum 6061")))
    library.update_material("Aluminum 6061", {"density": 2710,"yield_strength": 280e6}) # Corrected data using dictionary
    print("Aluminum in library after update:\n"+str(library.find_by_name("Aluminum 6061")))
    
    # Perform calculations
    applied_force = 10000 # 10 kN
    cross_section = -0.01 # 100 cm²
    stress = calculate_stress(applied_force, cross_section)
    safety_factor = calculate_safety_factor(steel.get_yield_strength(),stress)
    print(f"Calculated stress: {stress} Pa")
    print(f"Safety factor for Steel: {safety_factor}")
    volume = 0.005 # m³
    weight = calculate_weight(carbon_fiber, volume) 
    print(f"Weight of {volume} m³ of Carbon Fiber: {weight} N")
    # Find best material
    best_material = library.get_best_specific_strength()
    print(f"Best specific strength: {best_material.get_name()}")
    
if __name__ == "__main__":
    main()