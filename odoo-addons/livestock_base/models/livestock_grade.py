from odoo import fields, models


class LivestockGrade(models.Model):
    _name = "livestock.grade"
    _description = "축산물 등급 (축평원 등급 기준)"
    _order = "species_id, sequence, id"

    name = fields.Char(required=True, help="예: 1++, 1+, 1, 2, 3 / 등외")
    code = fields.Char(required=True)
    species_id = fields.Many2one("livestock.species", string="축종", required=True, ondelete="cascade")
    sequence = fields.Integer(default=10)
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ("species_code_uniq", "unique(species_id, code)", "동일 축종 내 등급 코드는 중복될 수 없습니다."),
    ]
