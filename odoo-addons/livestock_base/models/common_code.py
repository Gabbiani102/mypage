from odoo import fields, models


class LivestockCodeGroup(models.Model):
    _name = "livestock.code.group"
    _description = "공통코드 그룹 (예: 포장단위, 배송구분, 출하구분)"
    _order = "name"

    name = fields.Char(required=True)
    code = fields.Char(required=True, help="시스템에서 이 그룹을 식별하는 영문 코드 (예: PACKAGING_UNIT)")
    note = fields.Text(string="설명")
    code_ids = fields.One2many("livestock.code", "group_id", string="코드 목록")

    _sql_constraints = [
        ("code_uniq", "unique(code)", "공통코드 그룹 코드는 중복될 수 없습니다."),
    ]


class LivestockCode(models.Model):
    _name = "livestock.code"
    _description = "공통코드 (그룹에 속한 개별 항목)"
    _order = "group_id, sequence, id"

    group_id = fields.Many2one("livestock.code.group", string="코드 그룹", required=True, ondelete="cascade")
    code = fields.Char(required=True)
    name = fields.Char(required=True)
    sequence = fields.Integer(default=10)
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ("group_code_uniq", "unique(group_id, code)", "같은 그룹 안에서 코드는 중복될 수 없습니다."),
    ]
