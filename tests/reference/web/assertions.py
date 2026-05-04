def contains_any_keyword(text: str, keywords: tuple[str, ...]) -> bool:
    lowered = text.lower()
    return any(keyword.lower() in lowered for keyword in keywords)


def assert_text_matches_keywords(text: str, keywords: tuple[str, ...], label: str) -> None:
    cleaned = text.strip()
    assert cleaned, f"Expected non-empty {label} text"
    assert contains_any_keyword(cleaned, keywords), (
        f"Expected {label} to contain one of {keywords}, got: {cleaned!r}"
    )
