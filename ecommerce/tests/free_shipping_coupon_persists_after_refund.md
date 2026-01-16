POST /user
{"id":"U1","tier":"BRONZE","point":{"balance":0}}

POST /product
{"id":"P1","name":"Prod","benefits":[],"variants":[{"id":"A","sku":"A","price":12000,"stock":10},{"id":"B","sku":"B","price":8000,"stock":10}]}

POST /coupon
{"id":"C_FREE","code":"FREE","couponType":"FREE_SHIPPING","discountType":"FIXED","amount":0,"combinable":false,"active":true,"startAt":"2025-01-01","endAt":"2025-12-31"}

POST /order
{"id":"O1","userId":"U1","items":[{"variantId":"A","quantity":1},{"variantId":"B","quantity":1}],"couponIds":["C_FREE"]}

GET /order/O1
>>> {"id":"O1","itemSubtotalBeforeDiscount":20000,"benefitDiscount":0,"couponDiscount":0,"pointsUsed":0,"shippingFee":0,"totalAmount":20000,"appliedCoupons":[{"couponType":"FREE_SHIPPING","discountAmount":0}]}

POST /refund
{"orderId":"O1","variantId":"B","quantity":1}

GET /refund?orderId=O1
>>> {"orderId":"O1","itemRefundAmount":8000,"shippingAdjustment":0,"calculatedRefundAmount":8000,"finalRefundAmount":8000,"flooredToZero":false,"remainingSubtotalBeforeDiscount":12000,"newShippingFee":0,"freeShippingCouponRetained":true}
