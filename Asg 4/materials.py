class Material:
    def __init__(self, name:str, material_type:str, density:float, youngs_modulus:float, yield_strength:float):
        self.name = str(name)
        self.material_type = str(material_type)
        if density <= 0:
            raise ValueError("density must be positive")
        self.density = float(density)  # in kg/m^3
        if youngs_modulus <= 0:
            raise ValueError("youngs_modulus must be positive")
        self.youngs_modulus = float(youngs_modulus)  # in Pa
        if yield_strength <= 0:
            raise ValueError("yield_strength must be positive")
        self.yield_strength = float(yield_strength)  # in Pa

    def get_specific_strength(self):
        return self.yield_strength / self.density  
    
    def __str__(self):
        s="Material: " + self.name
        s += f"\nType: {self.material_type}"
        s += f"\nDensity: {self.density} kg/m^3"
        s += f"\nYoung's Modulus: {self.youngs_modulus:.2e} Pa"
        s += f"\nYield Strength: {self.yield_strength:.2e} Pa"
        s += f"\nSpecific Strength: {self.get_specific_strength():.2e} Pa·m^3/kg"
        return s
    
    #getters and setters
    # name
    def get_name(self) -> str:
        return self.name

    def set_name(self, new_name: str):
        self.name = str(new_name)

    # material_type
    def get_material_type(self):
        return self.material_type

    def set_material_type(self, new_type: str):
        self.material_type = str(new_type)

    # density (kg/m^3)
    def get_density(self):
        return self.density

    def set_density(self, new_density: float):
        if new_density <= 0:
            raise ValueError("density must be positive")
        self.density = float(new_density)

    # youngs_modulus (Pa)
    def get_youngs_modulus(self):
        return self.youngs_modulus

    def set_youngs_modulus(self, new_modulus: float):
        if new_modulus < 0:
            raise ValueError("youngs_modulus must be non-negative")
        self.youngs_modulus = float(new_modulus)

    # yield_strength (Pa)
    def get_yield_strength(self):
        return self.yield_strength

    def set_yield_strength(self, new_strength: float):
        if new_strength < 0:
            raise ValueError("yield_strength must be non-negative")
        self.yield_strength = float(new_strength)

class MaterialLibrary:
    def __init__(self, list_of_materials=None):
        self.library = []
        if not list_of_materials is None:
            for mat in list_of_materials:
                if not isinstance(mat, Material):
                    raise ValueError("All items in list_of_materials must be Material instances")
            self.library = list_of_materials
        

    def add_material(self, material: Material):
        for mat in self.library:
            if mat.get_name() == material.get_name():
                raise ValueError("Material with this name already exists in library")
        self.library.append(material)

    def find_by_name(self, name: str):
        for mat in self.library:
            if mat.get_name() == name:
                return mat
        return None

    def find_by_type(self, material_type: str):
        lst=[]
        for mat in self.library:
            if mat.get_material_type() == material_type:
                lst.append(mat)
        return lst

    def get_all_materials(self):
        return self.library
    
    def get_best_specific_strength(self):
        best_mat = self.library[0]
        for mat in self.library:
            if mat.get_specific_strength() > best_mat.get_specific_strength():
                best_mat = mat
        return best_mat
    
    def update_material(self,name,property_dict):
        mat = self.find_by_name(name)
        if mat is None:
            raise ValueError("Material not found in library")
        
        for key, value in property_dict.items():
            if key == "name":
                mat.set_name(value)
            elif key == "material_type":
                mat.set_material_type(value)
            elif key == "density":
                mat.set_density(value)
            elif key == "youngs_modulus":
                mat.set_youngs_modulus(value)
            elif key == "yield_strength":
                mat.set_yield_strength(value)
            else:
                return False #an error happened in one of the keys
        return True
    