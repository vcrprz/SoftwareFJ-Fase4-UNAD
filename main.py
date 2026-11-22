# main.py
from utilidades.logger import GestorLogs
from utilidades.excepciones import ErrorSistemaFJ
from modelos.cliente import Cliente
from modelos.servicio import ReservaSala


def ejecutar_simulacion():
    """
    Ejecuta 10 operaciones completas sobre los módulos disponibles (Clientes y Servicios),
    demostrando manejo robusto de excepciones y registro en logs sin interrumpir la ejecución.
    """
    logger = GestorLogs()
    logger.registrar_evento("INFO", "=== INICIO DE SIMULACIÓN SOFTWARE FJ ===")

    clientes = []
    servicios = []

    print("\n========================================================")
    print("   SISTEMA DE GESTIÓN SOFTWARE FJ - SIMULACIÓN FASE 4")
    print("========================================================\n")

    # 1. Registro válido de Cliente 1
    try:
        c1 = Cliente("CLI-001", "Laura Gómez", "laura.gomez@empresa.com", "3104567890")
        clientes.append(c1)
        print(f"[OP 01 - ÉXITO] Cliente registrado: {c1.obtener_resumen()}")
    except ErrorSistemaFJ as e:
        logger.registrar_evento("ERROR", f"OP 01 Fallida: {e}")
        print(f"[OP 01 - ERROR CONTROLADO] {e}")

    # 2. Registro válido de Cliente 2
    try:
        c2 = Cliente("CLI-002", "Carlos Mendoza", "cmendoza@tech.co", "3209876543")
        clientes.append(c2)
        print(f"[OP 02 - ÉXITO] Cliente registrado: {c2.obtener_resumen()}")
    except ErrorSistemaFJ as e:
        logger.registrar_evento("ERROR", f"OP 02 Fallida: {e}")
        print(f"[OP 02 - ERROR CONTROLADO] {e}")

    # 3. Registro inválido de Cliente (Correo sin @)
    try:
        c_inv1 = Cliente("CLI-003", "Pedro Pérez", "correo_invalido.com", "3001112233")
        clientes.append(c_inv1)
    except ErrorSistemaFJ as e:
        logger.registrar_evento("ERROR", f"OP 03 Fallida (Correo inválido): {e}")
        print(f"[OP 03 - ERROR CONTROLADO] Registro rechazado: {e}")

    # 4. Registro inválido de Cliente (Teléfono muy corto)
    try:
        c_inv2 = Cliente("CLI-004", "Ana Ruiz", "ana@dominio.com", "123")
        clientes.append(c_inv2)
    except ErrorSistemaFJ as e:
        logger.registrar_evento("ERROR", f"OP 04 Fallida (Teléfono inválido): {e}")
        print(f"[OP 04 - ERROR CONTROLADO] Registro rechazado: {e}")

    # 5. Creación válida de Sala Ejecutiva
    try:
        s1 = ReservaSala("SRV-001", "Sala Juntas Ejecutiva", 80000.0, capacidad=20, tiene_proyector=True)
        servicios.append(s1)
        print(f"[OP 05 - ÉXITO] Servicio creado: {s1.obtener_resumen()}")
    except ErrorSistemaFJ as e:
        logger.registrar_evento("ERROR", f"OP 05 Fallida: {e}")
        print(f"[OP 05 - ERROR CONTROLADO] {e}")

    # 6. Creación válida de Sala de Capacitación
    try:
        s2 = ReservaSala("SRV-002", "Sala Capacitación Norte", 60000.0, capacidad=35, tiene_proyector=False)
        servicios.append(s2)
        print(f"[OP 06 - ÉXITO] Servicio creado: {s2.obtener_resumen()}")
    except ErrorSistemaFJ as e:
        logger.registrar_evento("ERROR", f"OP 06 Fallida: {e}")
        print(f"[OP 06 - ERROR CONTROLADO] {e}")

    # 7. Creación inválida de Servicio (Tarifa negativa)
    try:
        s_inv1 = ReservaSala("SRV-003", "Sala Error Tarifa", -45000.0, capacidad=10)
        servicios.append(s_inv1)
    except ErrorSistemaFJ as e:
        logger.registrar_evento("ERROR", f"OP 07 Fallida (Tarifa negativa): {e}")
        print(f"[OP 07 - ERROR CONTROLADO] Servicio rechazado: {e}")

    # 8. Creación inválida de Servicio (Capacidad fuera de rango)
    try:
        s_inv2 = ReservaSala("SRV-004", "Auditorio Gigante", 150000.0, capacidad=500)
        servicios.append(s_inv2)
    except ErrorSistemaFJ as e:
        logger.registrar_evento("ERROR", f"OP 08 Fallida (Capacidad inválida): {e}")
        print(f"[OP 08 - ERROR CONTROLADO] Servicio rechazado: {e}")

    # 9. Cálculo de costo polimórfico válido con descuento (10%) e IVA (19%)
    try:
        total = servicios[0].calcular_costo(duracion=3, descuento=0.10)
        logger.registrar_evento("INFO", f"Cálculo exitoso para {servicios[0].nombre}: ${total:,.2f}")
        print(f"[OP 09 - ÉXITO] Costo calculado (3 horas con 10% dto + IVA): ${total:,.2f}")
    except ErrorSistemaFJ as e:
        logger.registrar_evento("ERROR", f"OP 09 Fallida: {e}")
        print(f"[OP 09 - ERROR CONTROLADO] {e}")

    # 10. Cálculo de costo fallido por servicio no disponible
    try:
        servicios[1].disponible = False
        servicios[1].calcular_costo(duracion=2)
    except ErrorSistemaFJ as e:
        logger.registrar_evento("ERROR", f"OP 10 Fallida (Servicio no disponible): {e}")
        print(f"[OP 10 - ERROR CONTROLADO] Operación bloqueada: {e}")

    print("\n========================================================")
    print(f"RESUMEN FINAL: {len(clientes)} Clientes válidos | {len(servicios)} Servicios válidos")
    print("Todos los errores fueron capturados y registrados en 'logs/sistema.log'.")
    print("========================================================\n")
    logger.registrar_evento("INFO", "=== FIN DE SIMULACIÓN SOFTWARE FJ ===")


if __name__ == "__main__":
    ejecutar_simulacion()
