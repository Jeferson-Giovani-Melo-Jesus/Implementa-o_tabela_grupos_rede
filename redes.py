def calcular_subrede(quantidade_maquinas):
    if quantidade_maquinas == 0:
        return "0.0.0.0/32", 1
    bits_necessarios = 1
    while (2 ** bits_necessarios) - 2 < quantidade_maquinas:
        bits_necessarios += 1
    prefixo = 32 - bits_necessarios
    total_enderecos = 2 ** bits_necessarios
    return prefixo, total_enderecos

def calcular_enderecos(base_ip, prefixo, total_enderecos):
    ip_base = int.from_bytes(map(int, base_ip.split('.')), 'big')
    return ['.'.join(map(str, (ip_base + i).to_bytes(4, 'big'))) for i in range(total_enderecos)]

def incrementar_ip(ip, incremento):
    ip_parts = list(map(int, ip.split('.')))
    ip_int = sum(ip_parts[i] << (8 * (3 - i)) for i in range(4)) + incremento
    return '.'.join(map(str, [(ip_int >> (8 * i)) & 0xFF for i in range(3, -1, -1)]))

def main():
    print("Bem-vindo ao sistema de cálculo de sub-redes!")
    setores_info = []
    base_ip = input("Informe o endereço IP base (ex: 192.168.0.0): ").strip()
    ip_atual = base_ip

    while True:
        setor = input("Informe o nome do setor (ou 'sair' para terminar): ").strip().lower()
        if setor == 'sair':
            break
        maquinas = int(input(f"Quantidade de maquinas ha no setor {setor}? ").strip())
        prefixo, total_enderecos = calcular_subrede(maquinas)
        enderecos = calcular_enderecos(ip_atual, prefixo, total_enderecos)
        setores_info.append((setor, maquinas, f"{ip_atual}/{prefixo}", enderecos[1], enderecos[2:2+maquinas]))
        ip_atual = incrementar_ip(enderecos[-1], 1)

    print("\nTabela de Sub-redes:")
    print(f"{'Setor':<15}{'Máquinas':<10}{'Sub-rede':<18}{'Gateway':<15}{'Endereços'}")
    for setor, maquinas, subrede, gateway, enderecos in setores_info:
        enderecos_str = ', '.join(enderecos)
        print(f"{setor:<15}{maquinas:<10}{subrede:<18}{gateway:<15}{enderecos_str}")

if __name__ == "__main__":
    main()
