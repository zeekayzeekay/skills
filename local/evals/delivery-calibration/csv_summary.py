from decimal import Decimal


def summarize(rows: list[dict[str, str]]) -> dict[str, object]:
    return {
        "net": sum((Decimal(row["amount"]) for row in rows), Decimal("0")),
        "count": len(rows),
    }
