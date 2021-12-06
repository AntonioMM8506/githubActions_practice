from bokeh.plotting import figure, output_file, show

if __name__ == '__main__':
    output_file('graficado_simple.html')
    fig = figure()

    total_vals = int(input('Cuantos valores quieres graficar?'))
    x_vals = list(range(total_vals))
    y_vals = []

    for x in x_vals:
        val = int(input(f'Valor y para {x}: '))
        y_vals.append(val)

    output_file('ejemplo_bokeh.html')
    fig.line(x_vals, y_vals, line_width=2)
    #fig.vbar(x_vals, y_vals, width=2)
    
    show(fig)

    #On terminal:
    #source env/Scripts/activate
    #py graficado_simple.py