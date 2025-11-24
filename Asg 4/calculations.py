def calculate_stress(force, area):
    stress = float(force) / float(area)
    return stress

def calculate_safety_factor(yield_strength, applied_stress):
    safety_factor = float(yield_strength) / float(applied_stress)
    return safety_factor

def calculate_weight(material, volume):
    g = 9.81  # m/s²
    weight = material.get_density() * float(volume) * g
    return weight
