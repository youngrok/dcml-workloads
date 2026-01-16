namespace Commerce;

model User {
  id: string;
  tier: UserTier;
  point: Point;
}

enum UserTier {
  BRONZE,
  SILVER,
  GOLD,
}

model Point {
  balance: int32;
}

model Product {
  id: string;
  name: string;
  benefits: Benefit[];
  variants: ProductVariant[];
}

model ProductVariant {
  id: string;
  sku: string;
  price: int32;
  stock: int32;
}

model Benefit {
  id: string;
  type: BenefitType;
  rate?: float64;
  amount?: int32;
  startAt: string;
  endAt: string;
  combinableWithCoupons: boolean;
}

enum BenefitType {
  RATE,
  FIXED,
}

model Coupon {
  id: string;
  code: string;
  couponType: CouponType;
  discountType: DiscountType;
  rate?: float64;
  amount?: int32;
  combinable: boolean;
  targetVariantId?: string;
  minOrderAmount?: int32;
  active: boolean;
  startAt: string;
  endAt: string;
}

enum CouponType {
  FREE_SHIPPING,
  ITEM_DISCOUNT,
  ORDER_DISCOUNT,
}

enum DiscountType {
  FIXED,
  RATE,
}

model Order {
  id: string;
  userId: string;
  status: OrderStatus;
  items: OrderItem[];
  itemSubtotalBeforeDiscount: int32;
  benefitDiscount: int32;
  couponDiscount: int32;
  pointsUsed: int32;
  pointsAllocationBase: int32;
  shippingFee: int32;
  totalAmount: int32;
  appliedBenefit?: AppliedBenefit;
  benefitBlockedReason?: BenefitBlockedReason;
  appliedCoupons: AppliedCoupon[];
  createdAt: string;
}

enum OrderStatus {
  CREATED,
  PAID,
  SHIPPED,
  DELIVERED,
  CANCELLED,
}

enum BenefitBlockedReason {
  NON_COMBINABLE_COUPON_APPLIED,
}

model AppliedBenefit {
  benefitId: string;
  type: BenefitType;
  rate?: float64;
  amount?: int32;
  discountAmount: int32;
}

model AppliedCoupon {
  couponId: string;
  couponType: CouponType;
  discountAmount: int32;
}

model OrderItem {
  id: string;
  variantId: string;
  quantity: int32;
  cancelledQuantity: int32;
  unitPrice: int32;
  originalAmount: int32;
  benefitDiscount: int32;
  couponDiscount: int32;
  pointsAllocated: int32;
  netAmount: int32;
  finalAmount: int32;
}

model Shipping {
  id: string;
  orderId: string;
  status: ShippingStatus;
  freeShippingReason?: FreeShippingReason;
}

enum ShippingStatus {
  READY,
  SHIPPED,
  DELIVERED,
  RETURNED,
}

enum FreeShippingReason {
  THRESHOLD_MET,
  COUPON_APPLIED,
}

model Refund {
  id: string;
  orderId: string;
  status: RefundStatus;
  refundItems: RefundItem[];
  itemRefundAmount: int32;
  shippingAdjustment: int32;
  calculatedRefundAmount: int32;
  finalRefundAmount: int32;
  flooredToZero: boolean;
  remainingSubtotalBeforeDiscount: int32;
  newShippingFee: int32;
  freeShippingCouponRetained: boolean;
  createdAt: string;
}

model RefundItem {
  orderItemId: string;
  variantId: string;
  quantity: int32;
  originalAmount: int32;
  benefitRefund: int32;
  couponRefund: int32;
  pointsRefund: int32;
  leftoverAmount: int32;
  netRefundAmount: int32;
}

enum RefundStatus {
  REQUESTED,
  APPROVED,
  REJECTED,
  COMPLETED,
}
