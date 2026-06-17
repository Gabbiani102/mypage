from odoo import fields, models


class LivestockUom(models.Model):
    _name = "livestock.uom"
    _description = "단위 마스터 (포장/유통 단위, Odoo 기본 UoM과 별개로 운영)"
    _order = "sequence, code"

    code = fields.Char(string="단위", required=True)
    note = fields.Char(string="비고")
    measure_type = fields.Selection(
        [
            ("length", "길이"),
            ("weight", "무게"),
            ("volume", "부피"),
            ("area", "넓이"),
            ("head", "두수"),
            ("mass", "중량"),
            ("quantity", "수량"),
        ],
        string="단위종류",
    )
    rounding_mode = fields.Selection(
        [("floor", "버림"), ("round", "반올림"), ("ceil", "올림")],
        string="소수점 자릿수 처리",
    )
    sequence = fields.Integer(default=10)
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ("code_uniq", "unique(code)", "단위 코드는 중복될 수 없습니다."),
    ]


class LivestockUomConversion(models.Model):
    _name = "livestock.uom.conversion"
    _description = "환산단위관리 (부위별 단위 변환 규칙)"
    _order = "species_id, cut_code, sequence"

    species_id = fields.Many2one("livestock.species", string="품종/축종", required=True)
    cut_code = fields.Char(string="UOM코드")
    cut_name = fields.Char(string="부위명")
    sequence = fields.Integer(default=10)
    base_uom_id = fields.Many2one("livestock.uom", string="기준단위", required=True)
    base_qty = fields.Float(string="기준수량", default=1.0)
    target_uom_id = fields.Many2one("livestock.uom", string="변환단위", required=True)
    target_qty = fields.Float(string="변환수량", default=1.0)
    decimal_digits = fields.Integer(string="소수점자릿수", default=2)
    rounding_mode = fields.Selection(
        [("floor", "버림"), ("round", "반올림"), ("ceil", "올림")],
        string="소수점끝처리",
        default="round",
    )
    note = fields.Char(string="비고")
