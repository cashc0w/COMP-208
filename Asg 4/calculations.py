def calculate_stress(force, area):
    if area <= 0 or force <= 0:
        raise ValueError("Inputs must be positive to calculate stress.")
    stress = float(force) / float(area)
    return stress

def calculate_safety_factor(yield_strength, applied_stress):
    if applied_stress <= 0 or yield_strength <= 0:
        raise ValueError("Inputs must be positive to calculate safety factor.")
    safety_factor = float(yield_strength) / float(applied_stress)
    return safety_factor

def calculate_weight(material, volume):
    if volume <= 0:
        raise ValueError("Volume must be positive to calculate weight.")
    g = 9.81  # m/s²
    weight = material.get_density() * float(volume) * g
    return weight
