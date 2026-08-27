grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"]],
    "Det": [["the"]],
    "N": [["cat"], ["dog"]],
    "V": [["sees"]]
}


def is_nonterminal(symbol):
    return symbol in grammar


def earley_parse(words):
    chart = [set() for _ in range(len(words) + 1)]

    # Item: (lhs, rhs, dot, origin)
    chart[0].add(("S'", ("S",), 0, 0))

    for i in range(len(words) + 1):
        changed = True

        while changed:
            changed = False

            for item in list(chart[i]):
                lhs, rhs, dot, origin = item

                # Predictor
                if dot < len(rhs):
                    symbol = rhs[dot]

                    if is_nonterminal(symbol):
                        for rule in grammar[symbol]:
                            new_item = (symbol, tuple(rule), 0, i)

                            if new_item not in chart[i]:
                                chart[i].add(new_item)
                                changed = True

                # Scanner
                if dot < len(rhs) and i < len(words):
                    symbol = rhs[dot]

                    if symbol == words[i]:
                        chart[i + 1].add(
                            (lhs, rhs, dot + 1, origin)
                        )

                # Completer
                if dot == len(rhs):
                    for old_item in list(chart[origin]):
                        old_lhs, old_rhs, old_dot, old_origin = old_item

                        if (old_dot < len(old_rhs) and
                            old_rhs[old_dot] == lhs):

                            new_item = (
                                old_lhs,
                                old_rhs,
                                old_dot + 1,
                                old_origin
                            )

                            if new_item not in chart[i]:
                                chart[i].add(new_item)
                                changed = True

    final_item = ("S'", ("S",), 1, 0)

    return final_item in chart[len(words)]


sentence = input("Enter sentence: ")
words = sentence.lower().split()

if earley_parse(words):
    print("Sentence accepted by Earley Parser.")
else:
    print("Sentence rejected.")
