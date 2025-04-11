# Listas

planetas = ["Mercurio", "Venus", "Tierra", "Marte", "Júpiter", "Saturno", "Urano", "Neptuno"]


gravedad_en_planetas = [3.7, 8.87, 9.81, 3.71, 24.79, 10.44, 8.69, 11.15]
peso_bus=124054 
print(f"en la tierra un autobus de 2 pisos pesa: {peso_bus}N")
print(f"En Mercurio un autobus de 2 pisos pesa {peso_bus*gravedad_en_planetas[0]}N")
print(f"Lo mas liviano que seria un autobus en el sistema solar sería: {peso_bus*min(gravedad_en_planetas)}")
print(f"Lo mas pesado que seria un autobus en el sistema solar sería: {peso_bus*max(gravedad_en_planetas)}")