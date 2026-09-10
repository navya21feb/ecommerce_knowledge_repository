# Knowledge Resolution for E-Commerce Order Management System

knowledge_base = {

    "confirm_order": {
        "payment": "successful",
        "inventory": "available"
    },

    "retry_payment": {
        "payment": "failed"
    },

    "cancel_or_backorder": {
        "inventory": "out_of_stock"
    },

    "escalate_support": {
        "delivery": "delayed"
    },

    "allow_return": {
        "delivery": "delivered",
        "return_request": True
    }
}


def matches(rule, facts):
    """
    Checks whether all conditions of a rule
    are satisfied by the given facts.
    """

    for key, value in rule.items():

        if facts.get(key) != value:
            return False

    return True


def resolve_knowledge(facts):
    """
    Matches the given facts with the knowledge base
    and returns the appropriate decision.
    """

    # Return rule is checked first
    if matches(knowledge_base["allow_return"], facts):
        return "Allow Return"

    # Delivery issue
    if matches(knowledge_base["escalate_support"], facts):
        return "Escalate to Customer Support"

    # Inventory issue
    if matches(knowledge_base["cancel_or_backorder"], facts):
        return "Cancel or Backorder Order"

    # Payment issue
    if matches(knowledge_base["retry_payment"], facts):
        return "Retry Payment"

    # Normal successful order
    if matches(knowledge_base["confirm_order"], facts):
        return "Confirm Order"

    return "Manual Support Required"


def display_decision(order):
    print("\nOrder Information")
    print("-----------------")

    for key, value in order.items():
        print(key, ":", value)

    decision = resolve_knowledge(order)

    print("\nDecision:", decision)


# Example order
order = {
    "payment": "successful",
    "inventory": "available",
    "delivery": "pending",
    "return_request": False
}

display_decision(order)
