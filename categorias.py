def obtener_criterios_por_categoria(oferta_laboral):
    categorias = {}
    for categoria, criterios in oferta_laboral.items():
        categorias[categoria] = list(criterios.keys())
    return categorias
