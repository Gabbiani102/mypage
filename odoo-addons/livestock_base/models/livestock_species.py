from odoo import fields, models


class LivestockSpecies(models.Model):
    _name = "livestock.species"
    _description = "축종 (소/돼지/닭/수입우/수입돈)"
    _order = "sequence, id"

    name = fields.Char(required=True)
    code = fields.Char(required=True, help="내부 코드 (예: CATTLE_KR, PIG_KR, CHICKEN_KR, CATTLE_IMP, PIG_IMP)")
    origin_type = fields.Selection(
        [("domestic", "국내"), ("import", "수입")],
        required=True,
        default="domestic",
    )
    sequence = fields.Integer(default=10)
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ("code_uniq", "unique(code)", "축종 코드는 중복될 수 없습니다."),
    ]
