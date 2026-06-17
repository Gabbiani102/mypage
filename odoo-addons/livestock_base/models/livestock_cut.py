from odoo import fields, models


class LivestockCut(models.Model):
    _name = "livestock.cut"
    _description = "부위 마스터 (품종/축종별 부위코드)"
    _order = "species_id, sequence, id"

    code = fields.Char(required=True, help="부위코드 (예: 430170)")
    name = fields.Char(required=True, help="부위명 (예: 안심, 등심, 갈비)")
    species_id = fields.Many2one("livestock.species", string="품종/축종", required=True, ondelete="cascade")
    sequence = fields.Integer(default=10)
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ("species_code_uniq", "unique(species_id, code)", "동일 품종 내 부위코드는 중복될 수 없습니다."),
    ]
