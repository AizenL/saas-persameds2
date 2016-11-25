{
    "name"          : "Sale Form",
    "version"       : "1.0",
    "depends"       : ["sale","report_webkit"],
    "author"        : "Databit",
    "description"   : """This module is aim to add some new fields to:
                        - Sale Order""",
    "website"       : "https://www.databit.co.id/",
    "category"      : "Sales",
    "init_xml"      : [],
    "demo_xml"      : [],
    'test'          : [],
    "update_xml"    : [
                       'company_inherit_view.xml',
                       'quot_sequence.xml',
                       "wizard/sale_propose_approval_view.xml",
                       "report/persamed_header_footer.xml",
                       "report/report_sale_order.xml",
                       "res_config_view.xml",
                       "sale_workflow.xml",
                       "sale_view.xml",
                       "res_users_view.xml",
                       'wizard/sale_make_invoice_advance.xml',
                       'report/sale_report_view.xml',
                       ],
    "active"        : False,
    "installable"   : True,
}