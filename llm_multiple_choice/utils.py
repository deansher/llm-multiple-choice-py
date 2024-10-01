def format_choice_codes(code_set: ChoiceCodeSet) -> str:
    codes_sorted = sorted(code.code for code in code_set.codes)
    return ", ".join(str(code) for code in codes_sorted)
