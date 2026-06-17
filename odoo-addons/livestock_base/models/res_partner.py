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

    # --- 거래처 등록 양식 (엑셀 분석 반영) ---
    distribution_structure_id = fields.Many2one(
        "livestock.code", string="유통구조",
        domain="[('group_id.code', '=', 'DISTRIBUTION_STRUCTURE')]",
    )
    partner_classification_id = fields.Many2one(
        "livestock.code", string="거래처분류값",
        domain="[('group_id.code', '=', 'PARTNER_CLASSIFICATION_VALUE')]",
    )
    credit_grade = fields.Selection(
        [("a", "A"), ("b", "B"), ("c", "C"), ("d", "D")],
        string="신용등급",
    )
    domestic_overseas = fields.Selection(
        [("domestic", "국내"), ("overseas", "해외")],
        string="국내외구분",
        default="domestic",
    )
    partner_status = fields.Selection(
        [("normal", "정상"), ("unused", "미사용"), ("closed", "폐업")],
        string="거래처상태",
        default="normal",
    )
    corporate_individual = fields.Selection(
        [("corporate", "법인"), ("individual", "개인")],
        string="법인/개인",
    )
    corporate_no = fields.Char(string="법인번호")
    representative_name = fields.Char(string="대표자성명")
    resident_reg_no = fields.Char(string="주민등록번호")
    sub_business_place_no = fields.Char(string="종사업장번호")
    business_type = fields.Char(string="업태")
    business_item = fields.Char(string="종목")
    partner_type_ids = fields.Many2many(
        "livestock.code", string="거래처종류",
        domain="[('group_id.code', '=', 'PARTNER_TYPE')]",
        relation="livestock_partner_partner_type_rel",
    )
    einvoice_issue_exception = fields.Selection(
        [("forward", "정발행"), ("reverse", "역발행")],
        string="전자세금계산서정발행예외",
    )
    einvoice_consolidated_issue = fields.Selection(
        [("yes", "대상"), ("no", "미대상")],
        string="전자세금계산서집계발행",
    )
    sales_report_type_id = fields.Many2one(
        "livestock.code", string="매출처유형(신고용)",
        domain="[('group_id.code', '=', 'SALES_REPORT_TYPE')]",
    )
    farm_flag = fields.Boolean(string="목장여부")
    slaughterhouse_flag = fields.Boolean(string="도축장여부")
    processing_plant_flag = fields.Boolean(string="가공장여부")
    slaughterhouse_code = fields.Char(string="도축장코드")
    meatwatch_partner_no = fields.Char(string="미트와치교부번호")
    bank_name = fields.Char(string="은행")
    bank_account_no = fields.Char(string="계좌번호")
    account_holder_name = fields.Char(string="예금주명")
    business_start_date = fields.Date(string="영업개시일")
