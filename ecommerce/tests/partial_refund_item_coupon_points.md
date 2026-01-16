POST /user
{"id":"U1","tier":"BRONZE","point":{"balance":10000}}

POST /product
{"id":"P1","name":"Prod","benefits":[],"variants":[{"id":"A","sku":"A","price":22000,"stock":10},{"id":"B","sku":"B","price":12000,"stock":10}]}

POST /coupon
{"id":"C_ITEM","code":"ITEM","couponType":"ITEM_DISCOUNT","discountType":"FIXED","amount":2000,"combinable":true,"targetVariantId":"B","active":true,"startAt":"2025-01-01","endAt":"2025-12-31"}

POST /order
{"id":"O1","userId":"U1","items":[{"variantId":"A","quantity":1},{"variantId":"B","quantity":1}],"couponIds":["C_ITEM"],"pointAmount":4000}

GET /order/O1
>>> {"id":"O1","itemSubtotalBeforeDiscount":34000,"benefitDiscount":0,"couponDiscount":2000,"pointsUsed":4000,"shippingFee":0,"totalAmount":28000,"pointsAllocationBase":32000,"appliedCoupons":[{"couponType":"ITEM_DISCOUNT","discountAmount":2000}]}

POST /refund
{"orderId":"O1","variantId":"B","quantity":1}

GET /refund?orderId=O1
>>> {"orderId":"O1","itemRefundAmount":8750,"shippingAdjustment":5000,"calculatedRefundAmount":3750,"finalRefundAmount":3750,"flooredToZero":false,"remainingSubtotalBeforeDiscount":22000,"newShippingFee":5000}
