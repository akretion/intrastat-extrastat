# Copyright 2020 Akretion France (http://www.akretion.com/)
# @author: Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    if openupgrade.column_exists(env.cr, "intrastat_product_declaration", "type"):
        openupgrade.logged_query(
            env.cr,
            "ALTER TABLE intrastat_product_declaration RENAME type "
            "TO declaration_type"
        )
