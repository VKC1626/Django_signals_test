By default, Django signals are executed synchronously.

This means when an event (like saving a model) happens, the connected signal runs immediately in the same thread before moving to the next operation.
