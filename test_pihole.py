import socket
import sys

def check_port(host, port, timeout=3):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            return s.connect_ex((host, port)) == 0
    except Exception:
        return False

def run_tests(host="127.0.0.1"):
    print(f"🧪 Probando conectividad con Pi-hole en: {host}")
    
    web_ok = check_port(host, 8080)
    dns_ok = check_port(host, 8053)

    print(f"  🌐 Interfaz Web (Puerto 8080): {'✅ OK' if web_ok else '❌ FALLO'}")
    print(f"  🛡️ Servicio DNS (Puerto 8053):  {'✅ OK' if dns_ok else '❌ FALLO'}")

    if web_ok and dns_ok:
        print("\n✨ ¡Todas las pruebas pasaron exitosamente!")
        sys.exit(0)
    else:
        print("\n❌ Error: Al menos un servicio no está respondiendo.")
        sys.exit(1)

if __name__ == "__main__":
    # Permite pasar la IP o Host como argumento, o usa 127.0.0.1 por defecto
    target_host = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
    run_tests(target_host)