def select_passage(candidates: list[dict]) -> str:
    return sorted(candidates, key=lambda candidate: candidate["score"])[0]["text"]


def cost_receipt(attempts: list[dict]) -> dict:
    total = sum(attempt["cost"] or 0 for attempt in attempts)
    return {"known": True, "amount": total}
