step 1
Entities

Person      → Base class
Doctor      → Child class
Patient     → Child class
Hospital    → Manager class


             Person
            /      \
           /        \
      Doctor      Patient

                Hospital
                   │
         ┌─────────┴─────────┐
         │                   │
    List[Doctor]       List[Patient]


