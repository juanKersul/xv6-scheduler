import matplotlib.pyplot as plt
import numpy as np

# Imports de RR, CPU/IO
from medida_RR_10ms import cpuμ_10msRR, ioμ_10msRR
from medida_RR_1ms import cpuμ_1msRR, ioμ_1msRR
from medida_RR_01ms import cpuμ_01msRR, ioμ_01msRR

# Imports de MLFQ, CPU/IO
from medida_MLFQ_10ms import cpuμ_10msMLFQ, ioμ_10msMLFQ
from medida_MLFQ_1ms import cpuμ_1msMLFQ, ioμ_1msMLFQ
from medida_MLFQ_01ms import cpuμ_01msMLFQ, ioμ_01msMLFQ


# Gráficos CPU, 10ms
def cpubench_10ms():
    # Faltaría agregar los mismos datos pero con planificador MLFQ
    xlabels = ["1-0", "1-1", "1-2", "2-0", "2-1", "2-2"]
    x = np.arange(len(xlabels))
    ancho = 0.4
    barras_RR_cpu = plt.bar(
        x - ancho / 2, cpuμ_10msRR, ancho, edgecolor="black", label="Round Robin"
    )
    barras_MLFQ_cpu = plt.bar(
        x + ancho / 2, cpuμ_10msMLFQ, ancho, edgecolor='black', label="MLFQ"
    )

    grafico(
        x,
        xlabels,
        "KFLOPS",
        "Nº cpubench - Nº iobench",
        "RRvsMLFQ, Medición CPU, Q=10",
        [barras_RR_cpu,barras_MLFQ_cpu],
        "Planificador",
    )


# Gráficos IO, 10ms
def iobench_10ms():
    # Faltaría agregar los mismos datos pero con planificador MLFQ
    xlabels = ["0-1", "1-1", "1-2", "0-2", "2-1", "2-2"]
    x = np.arange(len(xlabels))
    ancho = 0.4
    barras_RR_io = plt.bar(
        x - ancho / 2, ioμ_10msRR, ancho, edgecolor="black", label="Round Robin"
    )
    barras_MLFQ_io = plt.bar(
        x + ancho / 2, ioμ_10msMLFQ, ancho, edgecolor='black', label="MLFQ"
    )

    grafico(
        x,
        xlabels,
        "IOP250T",
        "Nº cpubench - Nº iobench",
        "RRvsMLFQ, Medición IO, Q=10",
        [barras_RR_io,barras_MLFQ_io],
        "Planificador",
    )


# Gráficos Comparativos de CPU RR, entre 10ms 1ms 0.1ms
def cpubench_RR():
    # Faltaría agregar los mismos datos pero con planificador MLFQ
    xlabels = ["1-0", "1-1", "1-2", "2-0", "2-1", "2-2"]
    x = np.arange(len(xlabels))
    ancho = 0.32
    barras_RR_10ms_cpu = plt.bar(
        x - ancho, cpuμ_10msRR, ancho, edgecolor="black", label="10ms"
    )
    barras_RR_1ms_cpu = plt.bar(x, cpuμ_1msRR, ancho, edgecolor="black", label="1ms")
    barras_RR_01ms_cpu = plt.bar(
        x + ancho, cpuμ_01msRR, ancho, edgecolor="black", label="0.1ms"
    )
    grafico(
        x,
        xlabels,
        "KFLOPS",
        "Nº cpubench - Nº iobench",
        "Comparación de escenarios RR CPU",
        [barras_RR_10ms_cpu, barras_RR_1ms_cpu, barras_RR_01ms_cpu],
        "quantum",
    )


# Gráficos Comparativos de IO RR, entre 10ms 1ms 0.1ms
def iobench_RR():
    # Faltaría agregar los mismos datos pero con planificador MLFQ
    xlabels = ["0-1", "1-1", "1-2", "0-2", "2-1", "2-2"]
    x = np.arange(len(xlabels))
    ancho = 0.32
    barras_RR_10ms_io = plt.bar(
        x - ancho, ioμ_10msRR, ancho, edgecolor="black", label="10ms"
    )
    barras_RR_1ms_io = plt.bar(x, ioμ_1msRR, ancho, edgecolor="black", label="1ms")
    barras_RR_01ms_io = plt.bar(
        x + ancho, ioμ_01msRR, ancho, edgecolor="black", label="0.1ms"
    )
    grafico(
        x,
        xlabels,
        "IOP250T",
        "Nº cpubench - Nº iobench",
        "Comparación de escenarios RR IO",
        [barras_RR_10ms_io, barras_RR_1ms_io, barras_RR_01ms_io],
        "quantum",
    )

# Gráficos Comparativos de CPU MLFQ, entre 10ms 1ms 0.1ms
def cpubench_MLFQ():
    xlabels = ["1-0", "1-1", "1-2", "2-0", "2-1", "2-2"]
    x = np.arange(len(xlabels))
    ancho = 0.32
    barras_MLFQ_10ms_cpu = plt.bar(
        x - ancho, cpuμ_10msMLFQ, ancho, edgecolor="black", label="10ms"
    )
    barras_MLFQ_1ms_cpu = plt.bar(
        x, cpuμ_1msMLFQ, ancho, edgecolor="black", label="1ms"
    )
    barras_MLFQ_01ms_cpu = plt.bar(
        x + ancho, cpuμ_01msMLFQ, ancho, edgecolor="black", label="0.1ms"
    )
    grafico(
        x,
        xlabels,
        "KFLOPS",
        "Nº cpubench - Nº iobench",
        "Comparación de escenarios MLFQ CPU",
        [barras_MLFQ_10ms_cpu, barras_MLFQ_1ms_cpu, barras_MLFQ_01ms_cpu],
        "quantum",
    )
    


# Gráficos Comparativos de IO MLFQ, entre 10ms 1ms 0.1ms
def iobench_MLFQ():
    xlabels = ["0-1", "1-1", "1-2", "0-2", "2-1", "2-2"]
    x = np.arange(len(xlabels))
    ancho = 0.32
    barras_MLFQ_10ms_io = plt.bar(
        x - ancho, ioμ_10msMLFQ, ancho, edgecolor="black", label="10ms"
    )
    barras_MLFQ_1ms_io = plt.bar(
        x, ioμ_1msMLFQ, ancho, edgecolor="black", label="1ms"
    )
    barras_MLFQ_01ms_io = plt.bar(
        x + ancho, ioμ_01msMLFQ, ancho, edgecolor="black", label="0.1ms"
    )
    grafico(
        x,
        xlabels,
        "IOP250T",
        "Nº cpubench - Nº iobench",
        "Comparación de escenarios MLFQ IO",
        [barras_MLFQ_10ms_io, barras_MLFQ_1ms_io, barras_MLFQ_01ms_io],
        "quantum",
    )


def grafico(x, x_labels, y_title_label, x_title_label, title, barras, aclaracion):
    """Realiza un gráfico, tomando cómo parámetros: (las divisiónes del eje x, nombres de esas divs, nombre del eje y, nombre del eje x, título del gráfico, y aclaración de lo que se grafica)"""
    plt.xticks(x, x_labels)
    plt.ylabel(f"{y_title_label}", fontsize=14)
    plt.xlabel(f"{x_title_label}", fontsize=12)
    plt.title(f"{title}", fontsize=20)
    if isinstance(barras, list):
        for i in range(len(barras)):
            label_bars(barras[i])
    else:
        label_bars(barras)
    plt.legend(title=f"{aclaracion}")
    plt.show()


def label_bars(bars):
    """Datos sobre las barras."""
    for rect in bars:
        height = int(rect.get_height())
        plt.annotate(
            "{}".format(height),
            xy=(rect.get_x() + rect.get_width() / 2, height),
            xytext=(0, 3),
            textcoords="offset points",
            ha="center",
        )


# Gráficos Comparativos de CPU/IO 10ms, entre RR y MLFQ
cpubench_10ms()
iobench_10ms()

## Gráficos Comparativos RR de CPU/IO, entre 10ms 1ms 0.1ms
cpubench_RR()
iobench_RR()

## Gráficos Comparativos RR de CPU/IO, entre 10ms 1ms 0.1ms
cpubench_MLFQ()
iobench_MLFQ()
