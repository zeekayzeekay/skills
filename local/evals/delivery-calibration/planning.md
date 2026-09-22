# Request

Use delivery-mode-engineering to propose the smallest sensible implementation plan for this tool. Planning only: no files, source changes, installs, live calls or delegation. The requirements below are settled; record any assumptions in the answer.

I want a personal read-only command-line recipe finder on my Windows laptop. It reads public recipe Markdown files from one configured folder, matches a query using deterministic text matching, and prints the most relevant passages with their source paths. I need useful matching against a small set of meal questions, not just a command that exits successfully. The recipe files are reconstructible from the public originals. The tool creates no durable records, corrections, annotations or paid effects and makes no network calls. One small matching module and ordinary file/configuration handling are fine.

If it works I may distribute it to a few colleagues as independent installs, each pointing at their own folder. There is no shared database, common corpus, merging of histories, server, login or synchronization planned. I do want configuration and module boundaries that avoid an expensive redesign for those separate installs. I will be the only human maintainer; two AI sessions may assist me. Use the current personal scope and say what evidence would establish it.
