# Glossary with Programming Terms & Meanings
Glossary = {
    "Variable": "A Container that stores a Value.",
    "Function": "A Block of Reuseable Code that Performs a Set Task.",
    "Loop": "A Block of Code that Repeats Execution until a Specific Condition is True.",
    "List": "A Collection of Ordered Items. Can be Changed or Sorted",
    "Conditional Statement": "A Statement that Executes Different Actions based on a True or False Condition."
}

# Adding 5 More Terms & Meanings
Glossary.update({
    "Dictionary": "A Collection of Key-Value Pairs. Allows Efficient Lookup, Insertion, & Deletion.",
    "String": "A Sequence of Characters, Enclosed in Single or Double Quotes.",
    "Module": "A File containing Python Code. Defines Functions, Classes, Variables, Etc.",
    "Argument": "A Value given to a Function when it's Called. Allows the Function to Operate on said Value.",
    "Boolean": "A Data Type that has 1 of 2 Possible Values usually representing True or False"
})

# Print Term & Meaning in Neat Format
for Term, Meaning in Glossary.items():
    print(Term + ": " + Meaning + "\n")