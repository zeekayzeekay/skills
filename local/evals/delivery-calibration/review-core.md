# Request

Use code-review to assess this personal matching tool's source snapshot against its contract. Review `matching.py` and the `MatchingEvidence` class in `test_fixtures.py`. This is an exported snapshot, not a branch diff; fingerprint supplied files. You are the leaf reviewer and must not delegate, edit source, commit or make live calls. Safe local probes may run without creating files.

# Governing contract

Personal Dogfood, one owner, attended local development. For one or more finite-scored candidate passages, return the text with the highest relevance score; the upstream scorer has already supplied these scores. No score ties occur in the supported corpus. Required core evidence must distinguish a useful top match from a distractor when both are present.

Each attempt has `cost` as a nonnegative number or `None` when pricing is unknown. A receipt may claim `known: True` only when every attempt is priced. Known free calls have numeric zero. Unknown pricing must remain visible; its amount must not be presented as a complete total. Mixed known and unpriced attempts occur in normal use. No live provider use or spending is authorized by this review.

# Raw evidence

The supplied matching singleton tests pass. A supported query produced candidates `[{"text": "old unrelated note", "score": 0.2}, {"text": "current relevant recipe", "score": 0.9}]`. An ordinary accounting batch was `[{"cost": 0.25}, {"cost": None}]`. These are inputs, not adjudicated outputs.
