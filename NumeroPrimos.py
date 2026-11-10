def es_primo(n):
    """Devuelve True si n es un número primo."""
    if n < 2:
        return False
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return False
    return True


def mostrar_primos(inicio=1, fin=100):
    """
    Muestra y retorna los números primos entre inicio y fin (inclusive).

    Ejemplo
    -------
    >>> mostrar_primos()
    Primos entre 1 y 100 (25): [2, 3, 5, 7, ...]
    """
    primos = [n for n in range(inicio, fin + 1) if es_primo(n)]
    print(f"Primos entre {inicio} y {fin} ({len(primos)}): {primos}")
    return primos