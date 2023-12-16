from typing import List

from pydantic import BaseModel

from app.model.general import SuccessModel
from app.utils.as_form import as_form

class Coupon(BaseModel):
    shop_uuid: str
    discount: int
    coupon_code: str
    expire_time: str
    update_time: str

class ReturnCoupon(SuccessModel):
    data: List[Coupon]

@as_form
class CreateCouponForm(BaseModel):
    shop_uuid: str
    discount: int
    coupon_code: str
    expire_time: str

class ReturnCreateCoupon(SuccessModel):
    data: str