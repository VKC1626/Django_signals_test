Question : By default are django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.


Answer:
By default, Django signals are executed synchronously.

This means when an event (like saving a model) happens, the connected signal runs immediately in the same thread before moving to the next operation.
