from laptop_business import Laptop_Business
laptop_empresarial = Laptop_Business(
    marca="Dell",
    procesador="Intel i7",
    memoria=16,
    almacenamiento=512,
    duracion_bateria=8,
    costo=1200,
    impuesto=15
)

diagnostico = laptop_empresarial.realizar_diagnostico_sistema()

print("Diagnóstico del sistema:")
for clave, valor in diagnostico.items():
    print(f"{clave}: {valor}")