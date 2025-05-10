import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Procesa carpetas de entrada y salida.")
    parser.add_argument("input", type=str, help="Ruta de la carpeta de entrada")
    parser.add_argument("output", type=str, help="Ruta de la carpeta de salida")
    args = parser.parse_args()
    return args.input, args.output