from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    species_id = fields.Many2one("livestock.species", string="품종")
    grade_id = fields.Many2one(
        "livestock.grade",
        string="등급",
        domain="[('species_id', '=', species_id)]",
    )
    origin_type = fields.Selection(
        [("domestic", "국내"), ("import", "수입")],
        string="원산지 구분",
        related="species_id.origin_type",
        store=True,
        readonly=True,
    )
    traceability_required = fields.Boolean(
        string="이력추적 대상",
        default=True,
        help="축평원 축산물 이력번호 연동이 필요한 품목인지 여부.",
    )
    packaging_unit_id = fields.Many2one(
        "livestock.code",
        string="포장단위",
        domain="[('group_id.code', '=', 'PACKAGING_UNIT')]",
        help="공통코드 마스터의 '포장단위' 그룹에서 선택 (예: 박스, kg, 마리).",
    )
    shelf_life_days = fields.Integer(
        string="유통기한(일)",
        help="입고/생산일로부터 유통기한까지의 일수.",
    )

    # --- 품목 등록 양식 (엑셀 분석 반영) ---
    product_account_id = fields.Many2one("livestock.product.account", string="품목계정")
    item_status = fields.Selection(
        [("active", "사용"), ("stopped", "중지")], string="품목상태", default="active",
    )
    domestic_overseas = fields.Selection(
        [("domestic", "국내"), ("overseas", "해외")], string="내외자구분", default="domestic",
    )
    importance = fields.Selection(
        [("a", "A"), ("b", "B"), ("c", "C"), ("d", "D")], string="중요도",
    )
    department_id = fields.Many2one("hr.department", string="담당부서")
    responsible_user_id = fields.Many2one("res.users", string="담당자")
    category_large_id = fields.Many2one(
        "livestock.code", string="품목대분류",
        domain="[('group_id.code', '=', 'PRODUCT_CATEGORY_LARGE')]",
    )
    category_mid_id = fields.Many2one(
        "livestock.code", string="품목중분류",
        domain="[('group_id.code', '=', 'PRODUCT_CATEGORY_MID')]",
    )
    category_small_id = fields.Many2one(
        "livestock.code", string="품목소분류",
        domain="[('group_id.code', '=', 'PRODUCT_CATEGORY_SMALL')]",
    )
    set_product_type = fields.Selection(
        [("normal", "일반"), ("combo", "결합"), ("gift_set", "선물세트")],
        string="세트상품유형", default="normal",
    )
    lot_management = fields.Boolean(string="Lot 관리 대상")
    expiry_unit = fields.Selection(
        [("year", "연"), ("month", "월"), ("day", "일")], string="소비기한구분",
    )
    shelf_life_period = fields.Integer(string="유통기간")
    main_supplier_id = fields.Many2one("res.partner", string="구매거래처")
    vat_type = fields.Selection(
        [("exempt", "면세"), ("taxable", "과세")], string="부가세구분",
    )
    vat_rate = fields.Float(string="부가세율(%)")
    sale_price_vat_included = fields.Boolean(string="판매단가에부가세포함")
    purchase_price_vat_included = fields.Boolean(string="구매단가에부가세포함")
    manufacturer = fields.Char(string="제조사")
    purchase_min_qty = fields.Float(string="구매최소수량")
    purchase_interval_qty = fields.Float(string="구매간격수량")
    customs_duty_rate = fields.Float(string="관세율")
    avg_lead_time_days = fields.Integer(string="평균조달일수")
    reorder_qty = fields.Float(string="적정발주수량")
    production_type = fields.Selection(
        [("none", "미대상"), ("make_to_order", "수주생산"), ("make_to_stock", "계획생산")],
        string="생산유형구분", default="none",
    )
    daily_production_qty = fields.Float(string="1일적정생산량")
    production_lead_time_days = fields.Integer(string="LeadTime")
    weight_kg = fields.Float(string="중량")
    gender_id = fields.Many2one(
        "livestock.code", string="성별", domain="[('group_id.code', '=', 'GENDER')]",
    )
    eco_type_id = fields.Many2one(
        "livestock.code", string="친환경구분", domain="[('group_id.code', '=', 'ECO_TYPE')]",
    )
    cut_id = fields.Many2one(
        "livestock.cut", string="부위",
        domain="[('species_id', '=', species_id)]",
    )
    storage_type_id = fields.Many2one(
        "livestock.code", string="보관", domain="[('group_id.code', '=', 'STORAGE_TYPE')]",
    )
    use_type_id = fields.Many2one(
        "livestock.code", string="용도", domain="[('group_id.code', '=', 'USE_TYPE')]",
    )
    livestock_type_id = fields.Many2one(
        "livestock.code", string="축산물유형", domain="[('group_id.code', '=', 'LIVESTOCK_PRODUCT_TYPE')]",
    )
    box_type_id = fields.Many2one(
        "livestock.code", string="박스종류", domain="[('group_id.code', '=', 'BOX_TYPE')]",
    )
    box_qty = fields.Integer(string="박스입수량")
    origin_country_id = fields.Many2one("res.country", string="원산지")
    storage_period = fields.Char(string="보관기한")
    traceability_report_required = fields.Boolean(string="이력정보신고대상여부")
    graded_flag = fields.Boolean(string="지정등급여부")
    pallet_box_qty = fields.Integer(string="PLT적재량(박스)")
    auto_production_request = fields.Boolean(string="생산의뢰자동생성")
