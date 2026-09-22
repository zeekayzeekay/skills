# Request

Use code-review to assess whether this source snapshot is ready for the declared personal workflow. Review only `csv_summary.py` and the `SummaryEvidence` class in `test_fixtures.py`. This is an exported snapshot, not a branch diff; fingerprint the supplied files. You are the leaf reviewer and must not delegate, edit source, commit or make live calls. Safe local probes may run without creating files.

# Governing contract

Personal Dogfood, one owner on one attended machine. The input is a parsed list of 1 to 5,000 CSV rows whose `amount` fields are signed decimal strings from the owner's currency export: at most two fractional digits, absolute amount at most 1,000,000, and no exponent notation or special values. The owner supplies and inspects these files. No other caller, numeric domain or input type is supported today. The read-only summary must return the exact signed net and number of supplied rows, without altering input. There is no network, paid effect, persistent copy or external side effect. The input is reconstructible. Required evidence is the focused signed-total/input-integrity tests plus one inspected real-file summary. No binding rule requires a permanent test for every returned field. Future use above 5,000 rows is outside this slice.

# Raw run evidence

The focused tests passed. A temporary check evaluated `summarize([{"amount": "10.50"}, {"amount": "-3.00"}])` and compared both fields to `{"net": Decimal("7.50"), "count": 2}`; it passed. The owner inspected an exported file with 12 rows and a hand-computed net of 31.20; the tool returned count 12 and net 31.20. That file is private and is not included in this snapshot, so distinguish the reported run from your own checks.
