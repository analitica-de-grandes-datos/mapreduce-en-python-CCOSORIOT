#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    for linea in sys.stdin:
        columnas = linea.strip().split('   ')
        columnas2 = columnas[0]
        sys.stdout.write("{}\t1\n".format(columnas2))