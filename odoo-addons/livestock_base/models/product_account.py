from odoo import fields, models


class LivestockProductAccount(models.Model):
    _name = "livestock.product.account"
    _description = "품목계정 (품목자산분류코드)"
    _order = "sequence, code"

    code = fields.Char(required=True, help="품목자산분류코드 (예: 01, 02 ...)")
    name = fields.Char(string="품목자산분류", required=True)
    asset_type = fields.Char(string="재고자산종류")
    inventory_managed = fields.Boolean(string="재고관리여부")
    inventory_value_managed = fields.Boolean(string="재고금액관리여부")
    usable_as_other_account = fields.Boolean(string="타계정으로계정사용")
    usable_from_other_account = fields.Boolean(string="타계정에서계정사용")
    asset_account_id = fields.Many2one("account.account", string="자산처리계정")
    domestic_sales_account_id = fields.Many2one("account.account", string="내수매출처리계정")
    local_sales_account_id = fields.Many2one("account.account", string="Local매출 처리계정")
    export_sales_account_id = fields.Many2one("account.account", string="수출매출처리계정")
    production_input_account_id = fields.Many2one("account.account", string="생산투입처리계정")
    cogs_account_id = fields.Many2one("account.account", string="매출원가처리계정")
    transfer_in_account_id = fields.Many2one("account.account", string="타계정에서 처리계정")
    transfer_out_account_id = fields.Many2one("account.account", string="타계정으로 처리계정")
    outsourcing_account_id = fields.Many2one("account.account", string="외주가공 처리계정")
    sequence = fields.Integer(default=10)
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ("code_uniq", "unique(code)", "품목자산분류코드는 중복될 수 없습니다."),
    ]
