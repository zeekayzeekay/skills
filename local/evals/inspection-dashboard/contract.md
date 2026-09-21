# Inspection dashboard change

This is a local prototype used by one operator. An inspection may contain several results. If any sensor reports a fault, the public summary must say `fault` and name the affected sensor. If no fault exists but a required sensor was not read, the summary is `unknown`. Only all-clear required sensors may be reported as `clear`. Results can arrive in any order.

The public `summarize` function is the stable boundary. The GUI consumes its returned `status` and `message`. No cloud, hardware or operator-data access is authorized for this review. Run only synthetic checks. Review only, no fixes.
