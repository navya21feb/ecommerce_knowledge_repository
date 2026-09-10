# Knowledge Resolution for E-Commerce Order Management


knowledge_base = {

    "confirm_order": {
        "payment": "successful",
        "inventory": "available"
    },

    "retry_payment": {
        "payment": "failed"
    },

    "cancel_order": {
        "inventory": "out_of_stock"
    },

    "allow_return": {
        "delivery": "delivered",
        "return_request": True
    },

    "escalate_support": {
        "delivery": "delayed"
    }
}


def matches(rule, facts):

    for key, value in rule.items():

        if facts.get(key) != value:
            return False

    return True


def resolve_knowledge(facts):

    for action, rule in knowledge_base.items():

        if matches(rule, facts):
            return action

    return "manual_support"


def display_decision(facts, decision):

    print("\nOrder Information")
    print("-----------------")

    for key, value in facts.items():
        print(key, ":", value)

    print("\nDecision:", decision)


# Example order facts

order = {
    "payment": "successful",
    "inventory": "available",
    "delivery": "pending",
    "return_request": False
}


decision = resolve_knowledge(order)

display_decision(order, decision)
