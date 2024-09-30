from project import function_argv, function_csv, function_randomizer
import pytest

def main():
    test_function_argv()
    test_function_csv()
    test_function_randomizer()

def test_function_argv():
    with pytest.raises(SystemExit):
        function_argv()


def test_function_csv():
    # Definir las listas esperadas
    index_0_en = [
        "Definitely", "No doubt", "Clearly", "Probably", "Surely",
        "The best is", "Always", "Never", "You should", "You could",
        "The solution is", "Try", "Consider", "Make sure to", "Don't forget to",
        "The secret is", "The ideal is", "The worst would be",
        "It is essential to", "It is crucial to"
    ]

    # Índice 1 en inglés
    index_1_en = [
        "ignore", "forget", "blame", "hide", "lie about",
        "confuse", "avoid", "sabotage", "reject", "abandon",
        "ruin", "procrastinate on", "underestimate", "insult", "interrupt",
        "destroy", "deceive", "pretend", "run away from", "lose"
    ]

    # Índice 2 en inglés
    index_2_en = [
        "everything", "that", "the situation", "the problems", "the opportunities",
        "the details", "the truth", "the facts", "the possibilities", "reality",
        "the options", "the answers", "the decisions", "the advice", "the doubts",
        "the solutions", "the results", "the promises", "the hopes", "the expectations"
    ]

    # Índice 3 en inglés
    index_3_en = [
        "without thinking twice", "as soon as possible", "immediately", "every day", "whenever you can",
        "just because", "for fun", "without any reason", "without regrets", "with conviction",
        "with a smile", "anywhere", "without doubt", "in public", "with pride",
        "without looking back", "at all costs", "with energy", "forever", "without limits"
    ]

    # Índice 0 en español
    index_0_es = [
        "Definitivamente deberías", "Sin duda tienes que", "Claramente es mejor", "Probablemente deberías considerar", "Seguramente es buena idea",
        "Lo mejor sería", "Siempre es útil", "Nunca dudes en", "Deberías", "Podrías intentar",
        "La solución es", "Intenta", "Considera", "Asegúrate de", "No olvides",
        "El secreto es", "Lo ideal es", "Lo peor sería",
        "Es fundamental", "Es crucial"
    ]

    # Índice 1 en español
    index_1_es = [
        "ignorar", "olvidar", "culpar a", "esconder", "mentir sobre",
        "confundir", "evitar", "sabotear", "rechazar", "abandonar",
        "arruinar", "procrastinar en", "subestimar", "insultar a", "interrumpir",
        "destruir", "engañar a", "fingir",
        "huir de", "perder"
    ]

    # Índice 2 en español
    index_2_es = [
        "todo", "eso", "la situación", "los problemas", "las oportunidades",
        "los detalles", "la verdad", "los hechos", "las posibilidades", "la realidad",
        "las opciones", "las respuestas", "las decisiones", "los consejos", "las dudas",
        "las soluciones", "los resultados", "las promesas", "las esperanzas", "las expectativas"
    ]

    # Índice 3 en español
    index_3_es = [
        "sin pensarlo dos veces", "lo antes posible", "inmediatamente", "todos los días", "cada vez que puedas",
        "porque sí", "por diversión", "sin motivo alguno", "sin arrepentimientos", "con convicción",
        "con una sonrisa", "en cualquier lugar", "sin dudar", "en público", "con orgullo",
        "sin mirar atrás", "a toda costa", "con energía", "para siempre", "sin límites"
    ]

    # Aserciones
    assert function_csv("EN") == (index_0_en, index_1_en, index_2_en, index_3_en)
    assert function_csv("ES") == (index_0_es, index_1_es, index_2_es, index_3_es)

def test_function_randomizer():

    i0= [1]
    i1= [2]
    i2= [3]
    i3= [4]

    assert function_randomizer(i0,i1,i2,i3) ==  "1 2 3 4 :)"
