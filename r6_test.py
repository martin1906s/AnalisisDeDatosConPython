import r6

# miAuto= r6.Auto("Toyota", "Corolla", 2020, 15000)

# miAuto.mostrar_info()
# miAuto.actualizar_kilometraje(20000)
# miAuto.realizar_viaje(5000)
# miAuto.estado_auto()

auto1 = r6.Auto.crear_auto("Honda", "Civic")
auto2 = r6.Auto.crear_auto("Ford", "Focus")
auto1.mostrar_info()
auto2.mostrar_info()
print(r6.Auto.comparar_kilometraje(auto1, auto2))
 