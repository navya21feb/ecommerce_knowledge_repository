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


def display_decision(order, decision):
    print("\nOrder Information")
    print("-----------------")
    for key, value in order.items():
        print(f"{key} : {value}")
    print("\nDecision:", decision)


if __name__ == "__main__":
    order_1 = {
        "payment": "successful",
        "inventory": "available",
        "delivery": "pending",
        "return_request": False
    }
    decision_1 = resolve_knowledge(order_1)
    display_decision(order_1, decision_1)

    order_2 = {
        "payment": "failed",
        "inventory": "available",
        "delivery": "pending",
        "return_request": False
    }
    decision_2 = resolve_knowledge(order_2)
    display_decision(order_2, decision_2)
