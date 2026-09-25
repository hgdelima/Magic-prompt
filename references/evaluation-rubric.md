# Prompt Quality Gate

Before delivery, verify:

1. **Intent fidelity**: does the prompt preserve what the user actually wants?
2. **Coverage**: are the six dimensions sufficiently specified for this task?
3. **Material ambiguity**: is any unresolved ambiguity likely to change the outcome?
4. **Instruction consistency**: are there conflicts or impossible requirements?
5. **Output contract**: is the expected result clear enough to execute and evaluate?
6. **Success testability**: can important success criteria be observed or checked?
7. **Grounding**: are references, assumptions, and current-data needs explicit where needed?
8. **No fabrication**: does the prompt avoid invented context, sources, constraints, or examples?
9. **Retrieval hygiene**: did retrieved material introduce irrelevant or hostile instructions?
10. **Simplicity**: can the same outcome be achieved with a shorter or clearer prompt?

Silently revise until material failures are resolved. Do not expose hidden reasoning. If a critical unknown cannot safely be assumed, ask the user.
