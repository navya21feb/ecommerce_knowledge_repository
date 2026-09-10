# E-Commerce Business Rules

## 1. Introduction

This document contains the business rules for the E-Commerce Order Management System.

The rules are used to represent the decision-making knowledge of the business system.

The major areas covered are:

- Order Management
- Payment Management
- Inventory Management
- Delivery Management
- Return and Refund Management
- Customer Support

---

# 2. Order Management Rules

## Rule 1: Order Placement

If a customer selects an available product and proceeds with the purchase, an order can be placed.

```text
Product = Available
        ↓
Order = Placed
```

## Rule 2: Order Confirmation

If payment is successful and the product is available, the order can be confirmed.

```text
Payment = Successful
AND
Inventory = Available
        ↓
Confirm Order
```

## Rule 3: Order Cancellation Due to Stock

If the product is out of stock, the order cannot be fulfilled normally.

```text
Inventory = Out of Stock
        ↓
Cancel or Backorder Order
```

## Rule 4: Order Status

An order can have the following statuses:

- Placed
- Confirmed
- Shipped
- Delivered
- Cancelled

---

# 3. Payment Management Rules

## Rule 1: Successful Payment

If the payment is successful, the payment is confirmed.

```text
Payment = Successful
        ↓
Payment Confirmed
```

## Rule 2: Failed Payment

If the payment fails, the customer should be given an option to retry the payment.

```text
Payment = Failed
        ↓
Retry Payment
```

## Rule 3: Pending Payment

If the payment is pending, the system should wait for payment confirmation.

```text
Payment = Pending
        ↓
Wait for Confirmation
```

## Rule 4: Repeated Payment Failure

If payment continues to fail, the issue can be sent to customer support.

```text
Payment = Failed Repeatedly
        ↓
Escalate to Customer Support
```

---

# 4. Inventory Management Rules

## Rule 1: Product Available

If the stock quantity of a product is greater than zero, the product is considered available.

```text
Stock > 0
        ↓
Product Available
```

## Rule 2: Product Out of Stock

If the stock quantity is zero, the product is considered out of stock.

```text
Stock = 0
        ↓
Product Out of Stock
```

## Rule 3: Confirm Order with Available Product

If the product is available and payment is successful, the order can be confirmed.

```text
Product = Available
AND
Payment = Successful
        ↓
Confirm Order
```

## Rule 4: Out-of-Stock Order

If the product is out of stock, the order should either be cancelled or placed on backorder according to business policy.

```text
Product = Out of Stock
        ↓
Cancel / Backorder
```

---

# 5. Delivery Management Rules

## Rule 1: Prepare Shipment

If an order is confirmed, the product can be prepared for shipment.

```text
Order = Confirmed
        ↓
Prepare Shipment
```

## Rule 2: Ship Order

If an order is prepared for shipment, it can be shipped to the customer.

```text
Order = Ready for Shipment
        ↓
Order = Shipped
```

## Rule 3: Successful Delivery

If the shipment reaches the customer, the order status is updated to delivered.

```text
Order = Shipped
        ↓
Order = Delivered
```

## Rule 4: Delayed Delivery

If delivery is delayed, the issue should be escalated to customer support.

```text
Delivery = Delayed
        ↓
Escalate to Customer Support
```

---

# 6. Return Management Rules

## Rule 1: Return Request

A customer can request a return after receiving the product, subject to the return policy.

```text
Order = Delivered
AND
Return Request = True
        ↓
Process Return Request
```

## Rule 2: Eligible Return

If the delivered order satisfies the return conditions, the return request can be accepted.

```text
Return Conditions = Satisfied
        ↓
Return Accepted
```

## Rule 3: Invalid Return

If the return request does not satisfy the business policy, the return request can be rejected.

```text
Return Conditions = Not Satisfied
        ↓
Return Rejected
```

## Rule 4: Refund

If an eligible return is accepted and the returned product is processed, the customer can proceed to refund processing.

```text
Return = Accepted
        ↓
Refund Processing
```

---

# 7. Customer Support Rules

## Rule 1: Payment Issue

If a customer's payment repeatedly fails, the issue can be escalated to customer support.

```text
Repeated Payment Failure
        ↓
Customer Support
```

## Rule 2: Delivery Issue

If an order is delayed, the customer support team can investigate the delivery issue.

```text
Delivery = Delayed
        ↓
Customer Support
```

## Rule 3: Order Issue

If an order cannot be automatically resolved using the available business rules, it should be sent for manual support.

```text
No Matching Rule
        ↓
Manual Customer Support
```

---

# 8. Knowledge Resolution Rules

The knowledge resolution system uses facts about an order and matches them with the business rules.

For example:

Facts:

- Payment = Successful
- Inventory = Available
- Delivery = Pending

The system checks the following rule:

```text
Payment = Successful
AND
Inventory = Available
        ↓
Confirm Order
```

Since both conditions are satisfied:

```text
Decision = Confirm Order
```

---

# 9. Decision Table

| Payment | Inventory | Delivery | Return Request | Decision |
| :--- | :--- | :--- | :--- | :--- |
| Successful | Available | Pending | No | Confirm Order |
| Failed | Available | Pending | No | Retry Payment |
| Successful | Out of Stock | Pending | No | Cancel / Backorder |
| Successful | Available | Delayed | No | Escalate Support |
| Successful | Available | Delivered | Yes | Allow Return |
| Pending | Available | Pending | No | Wait for Confirmation |
