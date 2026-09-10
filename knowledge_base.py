knowledge_base = {

    "order_rules": {

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
    },

    "order_status": [
        "placed",
        "confirmed",
        "shipped",
        "delivered",
        "cancelled"
    ],

    "payment_status": [
        "successful",
        "failed",
        "pending"
    ],

    "inventory_status": [
        "available",
        "out_of_stock"
    ],

    "delivery_status": [
        "pending",
        "shipped",
        "delivered",
        "delayed"
    ]
}


def display_knowledge_base():

    print("E-Commerce Knowledge Base")
    print("--------------------------")

    for category, information in knowledge_base.items():

        print("\n", category)
        print(information)


if __name__ == "__main__":
    display_knowledge_base()
