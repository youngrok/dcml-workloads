POST /user
{"id":"U1","tier":"BRONZE","point":{"balance":0}}

POST /product
{"id":"P1","name":"Prod","benefits":[],"variants":[{"id":"A","sku":"A","price":25000,"stock":10},{"id":"B","sku":"B","price":10000,"stock":10}]}

POST /coupon
{"id":"C_ORDER","code":"ORDER","couponType":"ORDER_DISCOUNT","discountType":"FIXED","amount":5000,"combinable":true,"active":true,"startAt":"2025-01-01","endAt":"2025-12-31"}

POST /order
{"id":"O1","userId":"U1","items":[{"variantId":"A","quantity":1},{"variantId":"B","quantity":1}],"couponIds":["C_ORDER"]}

GET /order/O1
>>> {"id":"O1","itemSubtotalBeforeDiscount":35000,"benefitDiscount":0,"couponDiscount":5000,"pointsUsed":0,"shippingFee":0,"totalAmount":30000,"appliedCoupons":[{"couponType":"ORDER_DISCOUNT","discountAmount":5000}]}

POST /refund
{"orderId":"O1","variantId":"B","quantity":1}

GET /refund?orderId=O1
>>> {"orderId":"O1","itemRefundAmount":8571,"shippingAdjustment":5000,"calculatedRefundAmount":3571,"finalRefundAmount":3571,"flooredToZero":false,"remainingSubtotalBeforeDiscount":25000,"newShippingFee":5000}
