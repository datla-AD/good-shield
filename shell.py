import numpy as np

def calculate_attenuation(initial_intensity, linear_attenuation_coefficient, thickness):
    """
    Calculates the attenuated intensity of radiation using the Beer-Lambert Law.

    Args:
        initial_intensity (float): The initial intensity of the radiation.
        linear_attenuation_coefficient (float): The linear attenuation coefficient of the material (cm^-1).
        thickness (float): The thickness of the shielding material (cm).

    Returns:
        float: The attenuated intensity of the radiation.
    """
    attenuated_intensity = initial_intensity * np.exp(-linear_attenuation_coefficient * thickness)
    return attenuated_intensity

# Example usage
initial_gamma_intensity = 1000  # Arbitrary units
lead_lac = 0.5  # Example linear attenuation coefficient for lead at a specific energy (cm^-1)
shield_thickness = 10  # cm

final_intensity = calculate_attenuation(initial_gamma_intensity, lead_lac, shield_thickness)
print(f"Initial intensity: {initial_gamma_intensity}")
print(f"Attenuated intensity after {shield_thickness} cm of lead: {final_intensity}")
