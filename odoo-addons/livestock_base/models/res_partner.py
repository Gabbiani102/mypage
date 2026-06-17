from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    sales_channel = fields.Selection(
        [
            ("b2b", "B2B"),
            ("b2c", "B2C"),
            ("direct_store", "직영매장"),
            ("franchise", "가맹매장"),
            ("foodservice", "외식사업장"),
        ],
        string="영업채널",
        help="이 거래처가 속한 영업 채널. 수주 등록 시 채널별 프로세스(배송준비, 거래명세서 등) 분기에 사용.",
    )
    business_reg_no = fields.Char(
        string="사업자등록번호",
        help="세금계산서 발행 및 거래처 식별에 사용되는 사업자등록번호.",
    )
