"""Тесты для модуля script."""

import pytest

from script import extract_phone_number, find_duplicate_phones, parse_profiles


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("+7 927 345 67 89", "+79273456789"),
        ("8 (999) 456-78-90", "+79994567890"),
        ("8 915 678 90 12", "+79156789012"),
        ("+7 (914) 082-34-96", "+79140823496"),
        ("sid111@gmail.com", None),
        ("igorrr@gmail.com", None),
    ],
)
def test_extract_phone_number(text: str, expected: str | None) -> None:
    """Проверка извлечения и нормализации номера телефона."""
    assert extract_phone_number(text) == expected


def test_parse_profiles() -> None:
    """Проверка парсинга анкет из текста."""
    text = (
        "1)\n"
        "Фамилия: Иванов\n"
        "Имя: Алексей\n"
        "Номер телефона или email: +7 927 345 67 89\n"
        "\n"
        "2)\n"
        "Фамилия: Петрова\n"
        "Имя: Мария\n"
        "Номер телефона или email: 8 (999) 456-78-90\n"
    )
    profiles = parse_profiles(text)

    assert len(profiles) == 2

    assert profiles[0]["surname"] == "Иванов"
    assert profiles[0]["name"] == "Алексей"
    assert profiles[0]["phone"] == "+79273456789"

    assert profiles[1]["surname"] == "Петрова"
    assert profiles[1]["name"] == "Мария"
    assert profiles[1]["phone"] == "+79994567890"


def test_find_duplicate_phones() -> None:
    """Проверка поиска дубликатов номеров."""
    profiles = [
        {"surname": "Архипова", "phone": "+79996181012"},
        {"surname": "Трофимов", "phone": "+79996181012"},
        {"surname": "Иванов", "phone": "+79273456789"},
    ]

    duplicates = find_duplicate_phones(profiles)

    assert len(duplicates) == 1
    assert "+79996181012" in duplicates
    assert len(duplicates["+79996181012"]) == 2


def test_find_duplicate_phones_empty() -> None:
    """Проверка, что при отсутствии дубликатов возвращается пустой словарь."""
    profiles = [
        {"surname": "Иванов", "phone": "+79273456789"},
        {"surname": "Петрова", "phone": "+79994567890"},
    ]

    duplicates = find_duplicate_phones(profiles)

    assert duplicates == {}
