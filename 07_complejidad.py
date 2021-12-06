import time

def factorial(n):
    repuesta = 1
    while n>1:
        repuesta *=n
        n -= 1
    return repuesta
#End of factorial

def factorial_r(n):
    if n == 1:
        return 1
    
    return n*factorial(n-1)
#End of factorial_r

if __name__ == "__main__":
    n = 100000
    #Con esto se puede medir el tiempo en que se ejecuta
    #se llama al modulo time y se invoca la función time del mismo.
    comienzo = time.time()
    factorial(n)
    print("metodo normal")
    final = time.time()
    print(final-comienzo)
    print()

    comienzo = time.time()
    factorial_r(n)
    print("metodo recursivo")
    final = time.time()
    print(final-comienzo)

    """
    from bokeh.plotting import figure, output_file, show

if __name__ == '__main__':
    output_file('graficado_simple.html')
    fig = figure()
    
    total_vals = int(input('Cuantos valores quieres graficar?'))
    x_vals = list(range(total_vals))
    y_vals = []

    for x in x_vals:
        val = int(input(f'Valor y para {x}'))
        y_vals.append(val)

    fig.line(x_vals, y_vals, line_width=2)
    show(fig)
    """