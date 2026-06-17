from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    species_id = fields.Many2one("livestock.species", string="축종")
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
